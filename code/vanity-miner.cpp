#include <bitcoin/system.hpp>

BC_USE_LIBBITCOIN_MAIN

int bc::main(int argc, char* argv[])
{
    const std::string search = "1kid";
    data_chunk entropy(ec_secret_size);

    while (true)
    {
        pseudo_random_fill(entropy);
        wallet::ec_private private_key(entropy);

        // Guard against entropy -> invalid secret (rare but possible).
        if (!private_key)
            continue;

        const auto address = private_key.to_payment_address().encoded();

        if (to_lower(address.substr(0, search.length())) == search)
        {
            cout << "Found vanity address! " << address << std::endl;
            cout << "Secret (WIF encoded): " << private_key.encoded()
                << std::endl;

            return 0;
        }

        cout << address << address << std::endl;
    }

    return 0;
}
