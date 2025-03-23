package model;

public class Account {
    private String userName;
    private String password;
    private boolean active;

    public String getUserName() {
        return userName;
    }
    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getPassword() {
        return password;
    }
    public void setPassword(String password) {
        this.password = password;
    }

    public boolean isActive() {
        return active;
    }
    public void setActive(boolean active) {
        this.active = active;
    }

    public Account() {
    }

   public Account(String userName, String password) {
        this.userName = userName;
        this.password = password;
        active = true;
   }
}
