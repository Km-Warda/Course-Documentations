package service.Impl;

import model.Account;
import service.ApplicationService;

import java.util.Scanner;

public class ApplicationServiceImpl implements ApplicationService {
    public void start(){
        int counter = 0;
        while (true) {
            System.out.println("1.login   2. create account   3. exit");
            Scanner scanner = new Scanner(System.in);
            int choose = scanner.nextInt();
            boolean exit = false;
            switch (choose) {
                case 1:
                    login();
                    break;
                case 2:
                    createAccount();
                    break;
                case 3:
                    System.out.println("Done, Goodbye");
                    exit = true;
                    break;
                default:
                    counter ++;
                    System.out.println("Invalid Entry, try again");
            }
            if (exit) {
                break;
            }
            if (counter == 4) {
                System.out.println("Timeout, try later");
                break;
            }
        }
    };

    private void login() {
        System.out.println("login Process");
    }
    private SystemAccountServiceImpl systemAccountService = new SystemAccountServiceImpl();
    private void createAccount() {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your account");
        String userName = scanner.nextLine();
        System.out.println("Enter your password");
        String password = scanner.nextLine();

        Account account = new Account(userName, password);
        boolean result = systemAccountService.AccountAcceptance(account);
        if (result) {
            System.out.println("Account Created Successfully");
        }
        else {
            System.out.println("Error on creation, username already exists");
        }
    }
}
