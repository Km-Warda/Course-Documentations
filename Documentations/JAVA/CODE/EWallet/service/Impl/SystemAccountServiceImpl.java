package service.Impl;

import model.Account;
import model.WalletSystem;
import service.SystemAccountService;

import java.util.List;

public class SystemAccountServiceImpl  implements SystemAccountService {
    private WalletSystem walletSystem = new WalletSystem();
    @Override
    public boolean AccountAcceptance(Account account) {
        List<Account> accounts = walletSystem.getAccounts();
        for (int i=0; i<accounts.size();i++){
            if (accounts.get(i).getUserName().equals(account.getUserName())) {
                return false;
            }
        }
        walletSystem.getAccounts().add(account);
        return true;
    }
}
