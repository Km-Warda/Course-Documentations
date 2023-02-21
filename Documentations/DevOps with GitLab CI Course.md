# Part1: Running Pipelines on Gitlab

### Gitlab Architecture 
- Gitlab runners retrieve setup instructions stored in the Gitlab server.
- Then it downloads & starts the docker image specified.
- Then files are retrieved form a get repository.
- Then runs all the commands specified in the job.
- Then report back the execution result to the Gitlab server. 
- After the job is finished the docker container will be destroyed "Meaning that each time Gitlab runner starts the job, it creates a new Docker container".
![Pasted image 20230127035318](https://user-images.githubusercontent.com/109697567/220482787-eb50e3bb-9e25-4999-bbb9-14a1b483725e.png)
These steps can be seen in the pipeline results (Blue & white):
![Pasted image 20230127040434](https://user-images.githubusercontent.com/109697567/220482807-e635bda9-c464-47c4-b05d-803258c2b8fd.png)
### Building a Pipeline
Pipeline is a set of jobs that gets done in stages.
![Pasted image 20230119163003](https://user-images.githubusercontent.com/109697567/220482836-2513c643-b348-4102-8eb3-55a480b52e47.png)
### Yml Files
Simply by using spaces & tabs, it's able to create nesting behavior in the yml files:
![Pasted image 20230127034641](https://user-images.githubusercontent.com/109697567/220482893-d65a2687-fa1c-42e8-bc73-c5fc3c10a06b.png)
*Notice:* The image represents a one job, the job is "person"

### Create a file named as *.gitlab-ci.yml*
- Notice that the .yml is case sensitive & spaces matter.
- The default working image chosen by git-lab is "Ruby-Docker image", remember to change it to the desired image, simply by specifying a key word "image" as following
```
Main job:
	image: alpine
```
- Write a simple code line, under a job at the top
```
Main job:
	script: echo "Hello World"
```
- Write a multiple-line Code, to do this, use "-" to create a list.
```
Main job:
	script:
		- mkdir folder
		- touch folder/file.txt
		- echo "Main Text" >> folder/file.txt
```

### Gitlab Runners
By default, Gitlab will have the option to use online shared runners to pick up the jobs, this can be turned off & set to a specific runner.
![[Pasted image 20230208180815.png]]

- To use a runner, it must have Gitlab Runner installed on it.
	[Install GitLab Runner | GitLab](https://docs.gitlab.com/runner/install/)
- Link the runner to your Gitlab Project using the command:
```
sudo gitlab-runner register
```
- Register the runner with this URL:  
	`https://gitlab.com/`       
- Enter the registration token of the project
![[Pasted image 20230208181357.png]]
- Important note: Create a tag for the Runner as it will be needed for picking up a job.

### Assigning a job to a Gitlab Runner "tags"
If you are using a project runner, then you must assign the tag to the job that will run using this runner
- For the Runner in the previous image with the tags "local, vm" we will assign the job to it as follows:
```
Main job:
	tags:
		- local
		- vm
	script:
		- mkdir folder
		- touch folder/file.txt
		- echo "Main Text" >> folder/file.txt
```
- Otherwise you will get an indication that the job is stuck because there is no runner assigned to it.

### Pipeline Status
If there is any conflicts making the pipeline stuck, it can be indicated as a cross sign, in this case it's working:
![[Pasted image 20230127032711.png]]

### Pipeline Stages:
When you put multiple Jobs in one file, they will run simultaneously without a specific order.
- Use the job "stages" to specify stages & order of the jobs.
- Specify the stage in each job.
This way job2 won't start until job1 is finished:
![[Pasted image 20230127045603.png]]
**However you'll still see here that job2 is still failing.**
	This is because job1 destroys the container after the job is executed as discussed before, & job2 creates a new container, so the test command has false response.

#### Predefined Stages:
Gitlab already has built in Predefined Stages, coming in order as:
- .pre
- build
- test
- deploy
- .post
These stages doesn't need defining in the .yml file.

### Parallel Staging
If more than one job have the same stage, they will run in parallel & failure of one won't stop the other one from running by default.

- To make a job dependent on another job in thew same stage we can use the keyword `needs` followed by the list of required jobs
```
	needs:
		- job1
```

### Pipelines Failing
Pipelines uses exit codes to indicate if the pipeline was executed successfully or not.
- "exit code 0" indicates that the pipeline was executed successfully.
- Any other number indicates an error.
- the numbers can go from 0 to 255.
![[Pasted image 20230127050827.png]]

### Job Artifacts
In the example mentioned, each job had its own different container, which defeats the purpose of using stages.
- Job Artifacts are items that are set to be kept after the job is done & doesn't get lost when the container gets destroyed
![[Pasted image 20230127051550.png]]
This can be seen from the pipeline logs for both stages as well either in the logs or as files to browse through
![[Pasted image 20230127052000.png]]
![[Pasted image 20230127053411.png]]
- The key word `path` made the artifacts browsable, there are other keywords, for example `reports` can be used to show us the test reports in Gitlab pipeline test tab
![[Pasted image 20230214192408.png]]

### Setting Variables
It's able to set a variable either specifically for each job, or globally for all jobs.
- For setting a variable name globally:
```
variables:
	VAR_NAME: file.txt
job1:
	script: echo "Text Inside" >> $VAR_NAME
job2:
	script: echo "New Text" >> $VAR_NAME
```
- For setting a variable name for a job:
```
Main job:
	variables:
		VAR_NAME: file.txt
	script: echo "New Text" >> $VAR_NAME
```
- Setting a variable name for a job also can be determined inside the script:
```
Main job:
	script:
		- VAR_NAME: file.txt
		- echo "New Text" >> $VAR_NAME
```
*Note:* Variable name can be either in lower case or upper case or both, but it's case sensitive, **& it's known to be set as upper case in a working environment.**

### Global Variables
You can add variables in the CI/CD tab in the project settings instead of inputting them in jobs.
- "Protect Variables" option makes the variable available only for the protected branches, as the main branch, so disable it unless needed.
- "Mask Variables" option masks the variable in printed pages for security.
- Here I created a variable for an S3 bucket on AWS:
![[Pasted image 20230208184444.png]]

### Predefined Variables
Gitlab comes with some predefined variables that can be used in the project. Can be found at  `https://docs.gitlab.com/ee/ci/variables/predefined_variables.html`

### Disabling A Job
Placing a dot before the job name will disable it in the next pipeline run.
- Job1 is now disabled:
```
.Job1:
	image:
	script:
	
```

### Job Timeouts
If a job cannot end/succeed or fail, it doesn't run forever, but it has a specific max timeout to be terminated.
![[Pasted image 20230206224817.png]]

### Testing Stage
Instead of the test command, serve command can be more useful as it starts a server for the specified path not only checks it.
```
test job:
	image: node:16-alpine
	script:
		- serve -s build_folder
```
*Note:* serve command is not defined in the default image, so a specified supporting image should be used.

- Notice: if we used "curl | grip" to test the server connection, the command "curl" is a dependency on alpine image, so make sure to use the alpine package manager if not using the alpine image:
```
test job:
	image: node:16-alpine
	script:
		- yarn global add serve
		- apk add curl
		- serve -s build_folder
		- curl http://localhost:3000 | grep "text in source"
```

- The serve command starts a server, & it's supposed to be running forever until termination, so it stops the job from finishing & the job will reach timeout.
You can create the server in the background of the job using "&" sign at the end, this will not stop the job from completing.
```
test job:
	image: node:16-alpine
	script:
		- yarn global add serve
		- apk add curl
		- serve -s build_folder &
		- curl http://localhost:3000 | grep "text in source"
```

- Use the command "sleep" so that the job gives time to the server to run, it takes a parameter in seconds.
```
test job:
	image: node:16-alpine
	script:
		- yarn global add serve
		- apk add curl
		- serve -s build_folder &
		- sleep 20
		- curl http://localhost:3000 | grep "text in source"
```

### Gitlab Repositories
Gitlab has 3 types of repositories:
![[Pasted image 20230214193815.png]]
- In order to push/pull an image to a private docker repository you must have the credentials required.
- The repository location is included in the image name
![[Pasted image 20230214193904.png]]

### Linter
"lint" is a command used to checks C and C++ language programs for potential problems., so it's used mostly as a .pre stage.

```
linter job:
	image: node:16-alpine
	stage: .pre
	script:
		- yarn install
		- yarn lint
```

### Executing Shell Scripts
The code can get bigger inside the .yml file & may result in less readable scripts & lose of overview of it.
- The script can be written in a separate `.sh` file, & executed given its path.
- Remember to add the execution permission to it.
```
	script:
		- chmod +x script.sh
		- ./script.sh
```

### Protecting Branches & Merge Requests
- To Protect a branch from directly pushing into it, go to `"Settings > Repository > Protected Branches"`.
- You can see all the merge requests to be created, merged or cancelled directly from the `"Merge Requests"`.
- You can view all the branches from `"Repository > Branches"`.

# Part2: Pipelines deployment to AWS 

## Deploy stage
After the testing's succeed, the deployment stage starts, and will be deployed to an S3 Bucket.

### AWS CLI
Make sure to add the "AWS CLI" docker image to the stage, & it can be found & copied from the docker hub "amazon/aws-cli".
![[Pasted image 20230208172419.png]]
Notice that the image has an entry point, an application that runs with the image. This conflicts with how Gitlab run images, so in order to overwrite this, use the property **"entrypoint"**
```
deploy to s3:
	stage: deploy
	image:
		name: amazon/aws-cli:2.9.21
		entrypoint: [""]
	script:
		- aws --version
```

### Storing on an S3 Bucket
Let the following code be desired for storing a file on an S3 bucket, with the bucket name assigned toa custom variable: `$AWS_S3_BUCKET`
```
deploy to s3:
    stage: deploy
    image:
        name: amazon/aws-cli:2.9.21
        entrypoint: [""]
    script:
        - aws --version
        - echo "Hello s3" > text.txt
        - aws s3 cp text.txt s3://$AWS_S3_BUCKET/text.txt
```
- The pipeline will fail because of missing credentials
	- Create an IAM user with S3 access permissions.
	- Assign an access key to it and add it as a variable.
	- ***NOTE:*** upon adding the variable it must be under the name of `AWS_ACCESS_KEY_ID` & you will see that it will be autocompleted, AWS CLI will look for the variable with the same name
	![[Pasted image 20230208191528.png]]
	- Do the same for `AWS_SECRET_ACCESS_KEY`
	- Use the variable `AWS_DEFAULT_REGION` to avoid specifying a region "Because S3 buckets are region specific services".
	![[Pasted image 20230208192357.png]]
- Now retry running the pipeline with the same job, it will succeed, this is because AWS CLI automatically reaches for the credentials given.
- You can find the text.txt file now in the S3 bucket.
![[Pasted image 20230208193208.png]]

### Branches & Controlling When Jobs Run "Job Rules"
If we committed on a different branch from the main branch, we can then merge the branch into the main if the pipeline succeeded.
- We desire that only the build & the test stage gets committed on a feature branch, & only if it's merged then the deployment job gets initiated, otherwise on every small edit or a feature the whole pipeline will start, meaning that the S3 bucket will get the deployed objects from the feature branch even if it's not merged.
	- we can use the keyword rule to control when a job starts.
	- To make a job only running if the current branch is the main branch:
```
	rules:
		- if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
```
*Notice:* `CI_COMMIT_REF_NAME`: A predefined variable for the branch or tag name for which project is built, `CI_DEFAULT_BRANCH`: A predefined variable for the name of the project’s default branch.

- Another better +way of doing this is using the keywords `only` & `except` 
	* `only` defines when a job runs.
	- `except` defines when a job doesn't run.
```
	only:
		- main
	except:
		- branch2
```

### Workflow
Workflow controls whether the whole pipeline is to be created or not, using rules.
- It's written at the start of the pipeline code not inside a job.
- The following workflow runs the pipeline only in the main branch & merge requests.
```
workflow:
	rules:
		- if: $CI_COMMIT_REF_NAME != $CI_DEFAULT_BRANCH && $CI_PIPELINE_SOURCE != "merge_request_event"
			when: never
		when: always
```

### Deploy Staging Concept
Often pipelines have a staging environment before the deployment stage, which basically is a simulation of the deployment stage, but not a production environment.
It's main purpose is to prevent flows into the deployment stage if any adjustments was done to it or the buckets.
- Staging uses a bucket different from the production/deployment buckets, but usually the promotion is done automatically.

### Continuous Delivery
In Continuous Deployment, the staging triggers the deployment stage on success, while on Continuous Delivery, the promotion from staging to deployment is done manually.

- In order to do this, use a condition `when: manual` inside the deployment job, & you will see that it has to be started manually with a button.
![[Pasted image 20230209194149.png]]

### Environments
Introducing staging subjected us to using many variables as we now have two URLs, two S3 buckets, etc.

Gitlab Environments basically describe where this code is deployed, so the staging, production, deployment for example all can be treated as different environments.

- To add a new environment, go to `"Deployments > Environments"` and create a new environment.
- You can use the S3 bucket web hosting link as the External link.

Now we can see that we can define the same variable for the same value, each with a different environment scope
![[Pasted image 20230209190141.png]]
- You can find in the global variables page a variable for current environment URL `$CI_ENVIRONMENT_URL`
- Use the keyword `environment:` in the job to specify its environment.
```
staging:
	image:
	environment: staging
	script:
```

### Reusing Configuration
As seen before, we reused identical configurations for both staging & deploying stages, only the stage & the environment was set to be different.
- We can create an disabled job & recall it inside other jobs with the key word `extends:`

- In the following code we set a disabled recall job syncing the folder `build` to the S3 bucket assigned to the variable, & then also testing in the same job. Notice that it doesn't have neither a stage nor an environment.
- We recalled it at the staging & deployment jobs, each with its own stage & environment.
```
.recall:
	image:
		name: amazon/aws-cli:2.4.11
		entrypoint: [""]
	rules:
		- if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
	script:
		- aws s3 sync build s3://$AWS_S3_BUCKET --delete
		- curl $CI_ENVIRONMENT_URL| grep "React App"

staging:
	stage: staging
	environment: staging
	extends: .recall

deploy:
	stage: deploy
	environment: deploy
	extends: .recall
```
*Notice:* when recalling the job with the keyword extends, we used a dot before the disabled job.


