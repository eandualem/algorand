from algosdk import account, mnemonic


def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))


generate_algorand_keypair()
''' First set of keypair
    My address: EJUTBX26SG2MWRFXB2PPB3TLME4Z5DIAT56JFUXXFGMFHR6E6EQBAVHNBI
    My private key: iYG8RLbgVtEQ82iEuYzzDJ1Ti7655osE5ersOny6wv8iaTDfXpG0y0S3Dp7w7mthOZ6NAJ98ktL3KZhTx8TxIA==
    My passphrase: couple velvet car arena punch crowd obtain happy correct cream keep speak poet people social trade multiply neglect install put wear purse wrap abstract program
'''

''' Second set of keypair
    My address: WJQTSZX3BLNHU4RPJIC3TCVH4C5JRCZ3I4S3DPIUBP2KWB47W64OB3YIEI
    My private key: /uFqnV/O93GrtwVpsK5sNg1j2Y+BCXVBaEQmpKZnEtuyYTlm+wraenIvSgW5iqfgupiLO0clsb0UC/SrB5+3uA==
    My passphrase: divert process solid tourist usage symbol run aisle artwork river curve square ship wagon arrest another concert patient captain draw essence okay sudden absorb dove
'''
