# cloud-resume-challenge

<<<<<<< HEAD
resume.cloudyrob.com

I'm a self-led student currently focusing on AWS, Linux, IaC, and security fundamentals. I recently passed my AWS Cloud Practitioner and Solutions Architect Associate certifications in mid-2022. I found the 'Cloud Resume Challenge' and admittedly hit a road block with creating a working API. I let the project sit for several months now as I got sidetracked with some cybersecurity courses. But I want to document what I learned with this project and my struggles.

=======
**resume.cloudyrob.com**

I'm a self-led student currently focusing on AWS, Linux, IaC, and security fundamentals. I recently passed my AWS Cloud Practitioner and Solutions Architect Associate certifications in mid-2022. I found the 'Cloud Resume Challenge' and admittedly hit a road block with creating a working API. I let the project sit for several months now as I got sidetracked with some cybersecurity courses. But I want to document what I learned with this project and my struggles.

**AWS Certifications:**

> > > > > > > 1e7560ae9f8092dac123200a4780f458eef0908b
> > > > > > > I used various resources to study for the Certified Cloud Practitioner exam. I am very new to tech and find the concepts and reading documentation to be a bit over my head the first time through. As much as possible, I tried to utilize free resources to study.

AWS Cloud Quest - https://rzts78g6yj.execute-api.us-east-1.amazonaws.com/prod
FreeCodeCamp - Cloud Practitioner Course - https://www.youtube.com/watch?v=SOTamWNgDKc&t=3764s

<<<<<<< HEAD
Pre-project step:
=======
Adrian Cantrill - Solutions Architect Associate
Tutorial Dojo - Solutions Architect Associate - Study guides and practice exams

**Pre-project step:**

> > > > > > > 1e7560ae9f8092dac123200a4780f458eef0908b

I already had a free-tier AWS account set up that I used for other basic projects. I created a separate user from the root account and gave that user limited permissions for the projects that I work on. I did not give the user programmatic access, although I might come back and change that when I work on the CRC project add-ons. I also enabled MFA for increased security.

Next, I set up budget alerts for this account to avoid any surprises while working in AWS. Budgets are pretty easy to set up and a great way to track spending if you venture out of the free-tier.

Chunk 1:
Working with HTML and CSS can be a bit frustrating. I have some experience with front-end development so I was able to put together a simple graphic resume. I didn't spend a whole lot of time trying to make this look like my actual resume, but I might come back to this part with some React in the future.

Setting up an S3 bucket is fairly straight-forward. Since I didn't set up programmatic access, I just drag and dropped the front-end files to the bucket. Because this S3 bucket will be hosting a static website, I had to change the bucket permissions to all public access.
https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html

The next step is requiring our S3 website endpoint to use HTTPS. HTTPS is just HTTP with Transport Layer Security encryption. This ensures safety, security, and overall trustworthiness for websites and users today.

I ensured HTTPS is utilized when I set up a CloudFront distribution for the S3 endpoint. CloudFront is a Content Delivery Network that caches content at locations closer to the end user for better access/optimization.

Next, I utilized AWS' Route53, which is a Domain Name System, where one can purchase a web domain. For this project, it is useful to make a more readable and memorable domain name and then point it to the CloudFront endpoint. So I created the CNAME record of 'resume.cloudyrob.com' for this project.

Because I have purchased a web domain that will host this project, it is import to create a digital (SSL) certificate that authenticates a website's identity and enables encrypted connections. Most major web browser require the certificates. So I used AWS' Certificate Manager that handles the request for a new certificate. This step can take a while and I also learned that I needed to verify the authenticity of the request both via email and in R53.
