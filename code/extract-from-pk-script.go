package main

import (
	"encoding/hex"
	"fmt"
	"os"

	"github.com/conformal/btcnet"
	"github.com/conformal/btcscript"
)

// go run extract-from-pk-script.go

// This example demonstrates extracting information from a standard public key
// script.

func main() {
	scriptHex := "76a914128004ff2fcaf13b2b91eb654b1dc2b674f7ec6188ac"

	ExtractPkScriptAddrs(scriptHex)
	// Output:
	// Script Class: pubkeyhash
	// Addresses: [12gpXQVcCL2qhTNQgyLVdCFG2Qs2px98nV]
	// Required Signatures: 1
}

func ExtractPkScriptAddrs(scriptHex string) {
	script, err := hex.DecodeString(scriptHex)
	handle(err)

	// Extract and print details from the script.
	scriptClass, addresses, reqSigs, err := btcscript.ExtractPkScriptAddrs(script, &btcnet.MainNetParams)
	handle(err)

	fmt.Println("Script Class:", scriptClass)
	fmt.Println("Addresses:", addresses)
	fmt.Println("Required Signatures:", reqSigs)
}

func handle(err error) {
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
