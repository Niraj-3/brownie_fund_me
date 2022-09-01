from brownie import accounts,network,config,MockV3Aggregator

FORKED_LOCAL_ENVIRONMENT = ['mainnet-fork-dev']
LOCAL_BLOCKCHAIN_ENVIRONMENT = ['development', 'ganache-local']

DECIMALS = 8
STARTING_VALUE = 200000000

def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in FORKED_LOCAL_ENVIRONMENT):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks....")
    if len(MockV3Aggregator)<=0:
        MockV3Aggregator.deploy(DECIMALS,STARTING_VALUE,{"from":get_account()})
    print("Mock Deployed")
