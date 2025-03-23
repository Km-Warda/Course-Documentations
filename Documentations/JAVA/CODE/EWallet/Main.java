import service.ApplicationService;
import service.Impl.ApplicationServiceImpl;

public class Main {

    public static void main(String[] args) {
        ApplicationService applicationService = new ApplicationServiceImpl();
        applicationService.start();
    }
}