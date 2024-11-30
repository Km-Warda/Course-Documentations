# Terraform Starting Configuration 
## Logging into the Provider
- In the CLI:
	- `aws configure`  To give access keys credentials.
	- `export AWS_ACCESS_KEY="example123"` To use environmental variables in the terraform code.
- In the Providers Block
	- `shared_credential_file = /users/kmwarda/.aws/creds` To give access to a local file with the credentials. If there are multiple profiles you can add `profile = "kmwarda-us-east1"`

# Terraform Blocks
Terraform blocks are the basic units of configuration in Terraform. They define the infrastructure that Terraform manages and can be categorized into several types. Below are the main types of Terraform blocks with simple examples and explanations for each:

### 1. **Provider Block**
   - **Purpose:** Defines the provider, which is the plugin used to interact with the cloud or service API (e.g., AWS, Azure, GCP).
   - **Example:**
     ```hcl
     provider "aws" {
       region = "us-west-2"
     }
     ```
   - **Explanation:** The `provider` block specifies that Terraform should use the AWS provider and set the region to `us-west-2`.

### 2. **Resource Block**
   - **Purpose:** Defines a specific piece of infrastructure, such as an EC2 instance or an S3 bucket.
   - **Example:**
     ```hcl
     resource "aws_instance" "example" {
       ami           = "ami-12345678"
       instance_type = "t2.micro"
     }
     ```
   - **Explanation:** The `resource` block creates an EC2 instance using the specified AMI and instance type.

### 3. **Variable Block**
   - **Purpose:** Declares input variables that can be used to customize configurations without hard-coding values.
   - **Example:**
     ```hcl
     variable "instance_type" {
       default = "t2.micro"
     }
     ```
   - **Explanation:** The `variable` block defines an input variable named `instance_type` with a default value of `t2.micro`.

### 4. **Output Block**
   - **Purpose:** Outputs values from the Terraform state, often to be used by other systems or to view key attributes after deployment.
   - **Example:**
     ```hcl
     output "instance_ip" {
       value = aws_instance.example.public_ip
     }
     ```
   - **Explanation:** The `output` block prints the public IP address of the EC2 instance created in the `resource` block.

### 5. **Module Block**
   - **Purpose:** Groups multiple resources together, often reused across different configurations.
   - **Example:**
     ```hcl
     module "network" {
       source = "./modules/network"
     }
     ```
   - **Explanation:** The `module` block includes a predefined set of resources from the `./modules/network` directory.

### 6. **Data Block**
   - **Purpose:** Retrieves information from existing infrastructure, often used to reference resources not managed by Terraform.
   - **Example:**
     ```hcl
     data "aws_ami" "ubuntu" {
       most_recent = true
       owners      = ["099720109477"]
       filter {
         name   = "name"
         values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
       }
     }
     ```
   - **Explanation:** The `data` block fetches the most recent Ubuntu AMI that matches the specified filter criteria.

### 7. **Locals Block**
   - **Purpose:** Defines local variables to simplify and reduce duplication in the configuration.
   - **Example:**
     ```hcl
     locals {
       instance_count = 3
     }
     ```
   - **Explanation:** The `locals` block defines a local variable `instance_count` that can be used elsewhere in the configuration.

### 8. **Terraform Block**
   - **Purpose:** Configures settings that are global to the entire Terraform configuration, such as required providers or backend configuration.
   - **Example:**
     ```hcl
     terraform {
       required_version = ">= 1.0.0"
       backend "s3" {
         bucket = "my-terraform-state"
         key    = "global/s3/terraform.tfstate"
         region = "us-west-2"
       }
     }
     ```
   - **Explanation:** The `terraform` block sets the required Terraform version and configures the backend to store state in an S3 bucket.

### 9. **Provisioner Block**
   - **Purpose:** Executes scripts or commands on the local machine or on a remote resource as part of the resource creation or destruction process.
   - **Example:**
     ```hcl
     resource "aws_instance" "example" {
       ami           = "ami-12345678"
       instance_type = "t2.micro"

       provisioner "local-exec" {
         command = "echo Hello, World!"
       }
     }
     ```
   - **Explanation:** The `provisioner` block runs the `local-exec` command to print "Hello, World!" after the instance is created.

These blocks work together to define and manage infrastructure in a modular, reusable way.

# Commands Dashboard
- `aws configure`
- `terraform help` Shows help menu for terraform commands
- `terraform -h COMMAND` Shows help menu for a specific terraform command, such as {terraform -h plan}
- `terraform fmt` Formats the code inside all file, the files must be saved to latest updated code.
- `terrafrom init` Initializes the backend & installs all required providers.
- `terrafrom init -upgrade` For updating providers versions.
- `terraform apply`
- `terraform destroy`
- `terraform apply -auto-approve`
- `terraform destroy -auto-approve`
--------------------------------------------------------------------------
![Pasted image 20240818225337](https://github.com/user-attachments/assets/7ea0071e-f05a-461c-ac18-6090262592b1)
![Pasted image 20240818224622](https://github.com/user-attachments/assets/738ed53d-0ae3-4319-ac60-a315b11aa285)

- `terraform console`

![Pasted image 20240818224653](https://github.com/user-attachments/assets/901071bb-2354-40db-a76e-7352f8cf8a96)
![Pasted image 20240818224715](https://github.com/user-attachments/assets/6f3926fc-1de4-40ea-bf55-a83129c91cec)
![Pasted image 20240818225426](https://github.com/user-attachments/assets/41d4f476-bba4-4709-a1d8-803f1a4b5402)
![Pasted image 20240818225457](https://github.com/user-attachments/assets/452a5f3e-ec18-41c0-a513-e73db1de9723)
![Pasted image 20240818225514](https://github.com/user-attachments/assets/9e81bd8e-6ca0-47f2-bfff-4525b67a636b)
![Pasted image 20240818225858](https://github.com/user-attachments/assets/8021a78b-d6a7-4898-a7b8-b31a18272f4b)
![Pasted image 20240818233302](https://github.com/user-attachments/assets/ef02d060-55b5-4de3-b258-8370d0d98aac)

Filtering traffic 
![Pasted image 20240818233457](https://github.com/user-attachments/assets/dd53ecca-2add-49d9-8dfe-43124cb05857)
![Pasted image 20240819073455](https://github.com/user-attachments/assets/e84858b6-9417-4ec5-8def-ef3b099551e3)
![Pasted image 20240819080148](https://github.com/user-attachments/assets/23af6d31-2e84-4944-8503-f610012541eb)
![Pasted image 20240819080739](https://github.com/user-attachments/assets/4aaf117b-ab6d-4cd4-9ed0-d4d3fb2fba80)

------------------------------------------------------
# **Lecture: Introduction to Terraform Modules**

## **1. Overview**
Terraform modules are essential tools for creating reusable and maintainable infrastructure as code. They enable you to encapsulate and organize Terraform configurations, making your deployments more modular and scalable.

### **Key Takeaways:**
- Understand what Terraform modules are and why they are important.
- Learn how to create and use modules in your Terraform configurations.
- Explore best practices for module design and management.

## **2. What is a Terraform Module?**
A **Terraform module** is a container for multiple resources that are used together. Every Terraform configuration file can be considered a module. The primary module is the root module, which can call other modules to encapsulate and reuse configurations.

### **Why Use Modules?**
- **Reusability:** Write your code once and use it in multiple environments.
- **Organization:** Break down complex configurations into manageable components.
- **Consistency:** Ensure uniformity across environments by using the same module for similar resources.

## **3. Structure of a Terraform Module**
A typical Terraform module is organized in a directory structure like this:

```
my-module/
├── main.tf         # The main configuration file for resources
├── variables.tf    # Input variable definitions
├── outputs.tf      # Output values
└── README.md       # Documentation (optional but recommended)
```

### **Core Files:**
- **`main.tf`:** Defines the resources that the module will manage.
- **`variables.tf`:** Declares variables that can be passed to the module.
- **`outputs.tf`:** Exposes values from the module for use in the root module or other modules.

## **4. Creating a Terraform Module**
### **Step 1: Define Resources in `main.tf`**
   Example: Creating an AWS S3 bucket
   ```hcl
   resource "aws_s3_bucket" "example" {
     bucket = var.bucket_name
   }
   ```

### **Step 2: Define Variables in `variables.tf`**
   Example: Defining input variables for the module
   ```hcl
   variable "bucket_name" {
     type = string
     description = "The name of the S3 bucket"
   }
   ```

### **Step 3: Define Outputs in `outputs.tf`**
   Example: Exposing the S3 bucket name
   ```hcl
   output "bucket_name" {
     value = aws_s3_bucket.example.bucket
   }
   ```

## **5. Using a Module in Your Configuration**
To use a module, you reference it from your root module or another module.

### **Example:**
```hcl
module "s3_bucket" {
  source      = "./modules/my-module"
  bucket_name = "my-unique-bucket-name"
}
```
- **`source`:** Specifies the path or location of the module.
- **`bucket_name`:** Passes the input variable `bucket_name` to the module.

## **6. Best Practices for Terraform Modules**
- **Encapsulation:** Limit the exposure of internal details; only expose what is necessary via outputs.
- **Versioning:** Use version control for modules, especially when sharing with teams.
- **Documentation:** Always include a `README.md` in your module directories to explain usage, inputs, and outputs.
- **Validation:** Test modules independently to ensure they work as expected before integrating them into larger configurations.

## **7. Examples of Common Terraform Modules**
### **Network Module**
   - Manages VPCs, subnets, route tables, and gateways.

### **Compute Module**
   - Manages EC2 instances, autoscaling groups, and security groups.

### **Storage Module**
   - Manages S3 buckets, EBS volumes, and RDS instances.

## **8. Conclusion**
Terraform modules are powerful tools that promote reuse, consistency, and organization in your infrastructure code. By structuring your Terraform configurations into modules, you can manage complex infrastructure with greater ease and confidence.

### **Further Reading:**
- [Terraform Module Registry](https://registry.terraform.io/)
- [Official Terraform Documentation](https://www.terraform.io/docs/language/modules/index.html)

### **Q&A and Discussion**
- Open the floor for any questions or discussions on how to implement and manage Terraform modules in real-world scenarios.

---

This lecture outline should help students grasp the importance of Terraform modules and provide them with the foundational knowledge needed to start creating and using their own modules.
