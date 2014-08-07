package main

import (
	"io/ioutil"
	"log"
	"path/filepath"
	"time"

	"github.com/conformal/btcrpcclient"
	"github.com/conformal/btcutil"
	"github.com/conformal/btcwire"
)

// This example demonstrates a connection to the bitcoin network
// by using websockets via btcd, use of notifications and an rpc
// call to getblockcount.
//
// Install and run btcd:
// 		$ go get github.com/conformal/btcd/...
//		$ btcd -u rpcuser -P rpcpass
//
// Install btcrpcclient:
// 		$ go get github.com/conformal/btcrpcclient
//
// Run this example:
// 		$ go run websocket-example.go
//
func main() {
	// Only override the handlers for notifications you care about.
	// Also note most of these handlers will only be called if you register
	// for notifications. See the documentation of the btcrpcclient
	// NotificationHandlers type for more details about each handler.
	ntfnHandlers := btcrpcclient.NotificationHandlers{
		OnBlockConnected: func(hash *btcwire.ShaHash, height int32) {
			log.Printf("Block connected: %v (%d)", hash, height)
		},
		OnBlockDisconnected: func(hash *btcwire.ShaHash, height int32) {
			log.Printf("Block disconnected: %v (%d)", hash, height)
		},
	}

	// Connect to local btcd RPC server using websockets.
	btcdHomeDir := btcutil.AppDataDir("btcd", false)
	certs, err := ioutil.ReadFile(filepath.Join(btcdHomeDir, "rpc.cert"))
	if err != nil {
		log.Fatal(err)
	}
	connCfg := &btcrpcclient.ConnConfig{
		Host:         "localhost:8334",
		Endpoint:     "ws",
		User:         "rpcuser",
		Pass:         "rpcpass",
		Certificates: certs,
	}
	client, err := btcrpcclient.New(connCfg, &ntfnHandlers)
	if err != nil {
		log.Fatal(err)
	}

	// Register for block connect and disconnect notifications.
	if err := client.NotifyBlocks(); err != nil {
		log.Fatal(err)
	}
	log.Println("NotifyBlocks: Registration Complete")

	// Get the current block count.
	blockCount, err := client.GetBlockCount()
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Block count: %d", blockCount)

	// For this example gracefully shutdown the client after 10 seconds.
	// Ordinarily when to shutdown the client is highly application
	// specific.
	log.Println("Client shutdown in 10 seconds...")
	time.AfterFunc(time.Second*10, func() {
		log.Println("Client shutting down...")
		client.Shutdown()
		log.Println("Client shutdown complete.")
	})

	// Wait until the client either shuts down gracefully (or the user
	// terminates the process with Ctrl+C).
	client.WaitForShutdown()
}
