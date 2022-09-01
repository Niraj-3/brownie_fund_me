from brownie import accounts,network,exceptions
from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account,LOCAL_BLOCKCHAIN_ENVIRONMENT
import pytest

def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()+100
    txn = fund_me.fund({"from":account,"value":entrance_fee})
    txn.wait(1);
    assert fund_me.addressToAmountFunded(account.address)==entrance_fee
    txn = fund_me.withdraw({"from":account})
    txn.wait(1)
    assert fund_me.addressToAmountFunded(account.address)==0

def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from":bad_actor})