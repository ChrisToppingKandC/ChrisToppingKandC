
```
Git
├─ api-management-policy-snippets
│  ├─ examples
│  │  ├─ Add correlation id to inbound request.policy.xml
│  │  ├─ Authenticate using Managed Identity to access Event Hub.xml
│  │  ├─ Authenticate using Managed Identity to access Service Bus.xml
│  │  ├─ Authenticate using Managed Identity to access Storage Account.xml
│  │  ├─ Authorize requests using external authorizer.policy.xml
│  │  ├─ Back-end API redundancy.policy.xml
│  │  ├─ Backend OAuth2 Authentication With Cache.policy.xml
│  │  ├─ Call out to an HTTP endpoint and cache the response.policy.xml
│  │  ├─ Create HMAC SHA256-Signed JWT.policy.xml
│  │  ├─ Decrypt AES Data using policy expressions.xml
│  │  ├─ DELETE a from to blobStorage account.xml
│  │  ├─ Encrypt data using expressions.policy.xml
│  │  ├─ Extract value from XML.xml
│  │  ├─ Extracting multiple values from xml documents.policy.xml
│  │  ├─ Filter on IP Address when using Application Gateway.policy.xml
│  │  ├─ Filter response content based on product name.policy.xml
│  │  ├─ Forward Azure Event Grid Event.xml
│  │  ├─ Forward gateway hostname to backend for generating correct urls in responses.policy.xml
│  │  ├─ Generate Azure Relay Token.policy.xml
│  │  ├─ Generate Shared Access Signature and forward request to Azure storage.policy.xml
│  │  ├─ GET a file from blobStorage account.xml
│  │  ├─ Get OAuth2 access token from AAD and forward it to the backend.policy.xml
│  │  ├─ Get OAuth2 access token from AAD using client id and certificate using key vault manage identity.xml
│  │  ├─ Get X-CSRF token from SAP gateway using send request.policy.xml
│  │  ├─ Handle Power Query access request to custom API.policy.xml
│  │  ├─ List all inbound headers.policy.xml
│  │  ├─ Log errors to Stackify.policy.xml
│  │  ├─ Look up Key Vault certificate using Managed Service Identity and call backend.policy.xml
│  │  ├─ Look up Key Vault secret using Managed Service Identity.policy.xml
│  │  ├─ Loopback request for service at same API Management service.xml
│  │  ├─ Mask async calls as synchronous.policy.xml
│  │  ├─ Parse a JWT token using expressions.xml
│  │  ├─ Perform basic authentication.policy.xml
│  │  ├─ Pre-authorize requests based on HTTP method with validate-jwt.policy.xml
│  │  ├─ PUT a file to blobStorage account.xml
│  │  ├─ Query CosmosDB.policy.xml
│  │  ├─ Random load balancer simpler.policy.xml
│  │  ├─ Random load balancer.policy.xml
│  │  ├─ README.md
│  │  ├─ Request OAuth2 access token from SAP using AAD JWT token.xml
│  │  ├─ Return a blob URL signed with a user delegation SAS token.xml
│  │  ├─ Return HTTP 405 if the HTTP Method of the request is not defined.xml
│  │  ├─ Route requests based on size.policy.xml
│  │  ├─ Route requests to regional backend instances.xml
│  │  ├─ Send request context information to the backend service.policy.xml
│  │  ├─ Set cache duration using response cache control header.policy.xml
│  │  ├─ Trigger Azure Data Factory Pipeline With Parameters.policy.xml
│  │  ├─ Trigger Azure Data Factory Pipeline.policy.xml
│  │  └─ Use custom error messages for jwt-validate policy with on-error handler.policy.xml
│  ├─ LICENSE
│  ├─ media
│  │  └─ vscode-snippets
│  │     ├─ apim-vscode-snippets-1.png
│  │     ├─ apim-vscode-snippets-2.png
│  │     └─ apim-vscode-snippets-3.png
│  ├─ policy-expressions
│  │  └─ README.md
│  ├─ README.md
│  ├─ SECURITY.md
│  └─ vscode-snippets
│     └─ xml.json
├─ apim-api-tests.ipynb
├─ azure-functions-sql-extension
│  ├─ .editorconfig
│  ├─ .gdn
│  │  └─ global.gdnsuppress
│  ├─ .vscode
│  │  ├─ extensions.json
│  │  ├─ launch.json
│  │  ├─ settings.json
│  │  └─ tasks.json
│  ├─ builds
│  │  ├─ azure-pipelines
│  │  │  ├─ build-pr.yml
│  │  │  ├─ build-release-java.yml
│  │  │  ├─ build-release.yml
│  │  │  ├─ performance.yml
│  │  │  ├─ template-steps-build-test.yml
│  │  │  ├─ template-steps-performance.yml
│  │  │  └─ template-steps-publish.yml
│  │  ├─ scripts
│  │  │  └─ UpdateLogLevel.ps1
│  │  └─ TSAConfig.gdntsa
│  ├─ CODE_OF_CONDUCT.md
│  ├─ CONTRIBUTING.md
│  ├─ Directory.Build.props
│  ├─ Directory.Packages.props
│  ├─ docs
│  │  ├─ BindingsOverview.md
│  │  ├─ GeneralSetup.md
│  │  ├─ SetupGuide_Dotnet.md
│  │  ├─ SetupGuide_DotnetCSharpScript.md
│  │  ├─ SetupGuide_DotnetOutOfProc.md
│  │  ├─ SetupGuide_Java.md
│  │  ├─ SetupGuide_Javascript.md
│  │  ├─ SetupGuide_PowerShell.md
│  │  ├─ SetupGuide_Python.md
│  │  └─ SqlBindingRelatedRepos.md
│  ├─ global.json
│  ├─ Images
│  │  ├─ dbSetup.png
│  │  └─ pkgicon.png
│  ├─ java-library
│  │  ├─ checkstyle.xml
│  │  ├─ pom.xml
│  │  └─ src
│  │     └─ main
│  │        └─ java
│  │           └─ com
│  │              └─ microsoft
│  │                 └─ azure
│  │                    └─ functions
│  │                       └─ sql
│  │                          └─ annotation
│  │                             ├─ SQLInput.java
│  │                             └─ SQLOutput.java
│  ├─ LICENSE
│  ├─ NOTICE.txt
│  ├─ nuget.config
│  ├─ performance
│  │  ├─ .editorconfig
│  │  ├─ Microsoft.Azure.WebJobs.Extensions.Sql.Performance.csproj
│  │  ├─ packages.lock.json
│  │  ├─ README.md
│  │  ├─ SqlBindingBenchmarks.cs
│  │  ├─ SqlInputBindingPerformance.cs
│  │  └─ SqlOutputBindingPerformance.cs
│  ├─ README.md
│  ├─ samples
│  │  ├─ Database
│  │  │  ├─ StoredProcedures
│  │  │  │  └─ SelectProductsCost.sql
│  │  │  ├─ Tables
│  │  │  │  ├─ Products.sql
│  │  │  │  ├─ ProductsCostNotNull.sql
│  │  │  │  ├─ ProductsNameNotNull.sql
│  │  │  │  ├─ ProductsWithDefaultPK.sql
│  │  │  │  ├─ ProductsWithIdentity.sql
│  │  │  │  └─ ProductsWithMultiplePrimaryColumnsAndIdentity.sql
│  │  │  └─ Views
│  │  │     └─ ProductsNamesView.sql
│  │  ├─ samples-csharp
│  │  │  ├─ .editorconfig
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ Common
│  │  │  │  ├─ Product.cs
│  │  │  │  └─ ProductUtilities.cs
│  │  │  ├─ GlobalSuppressions.cs
│  │  │  ├─ host.json
│  │  │  ├─ InputBindingSamples
│  │  │  │  ├─ GetProductNamesView.cs
│  │  │  │  ├─ GetProducts.cs
│  │  │  │  ├─ GetProductsAsyncEnumerable.cs
│  │  │  │  ├─ GetProductsNameEmpty.cs
│  │  │  │  ├─ GetProductsNameNull.cs
│  │  │  │  ├─ GetProductsSqlCommand.cs
│  │  │  │  ├─ GetProductsStoredProcedure.cs
│  │  │  │  ├─ GetProductsStoreProcedureFromAppSetting.cs
│  │  │  │  ├─ GetProductsString.cs
│  │  │  │  └─ GetProductsTopN.cs
│  │  │  ├─ local.settings.json
│  │  │  ├─ Microsoft.Azure.WebJobs.Extensions.Sql.Samples.csproj
│  │  │  ├─ MultipleBindingsSamples
│  │  │  │  └─ GetAndAddProducts.cs
│  │  │  ├─ OutputBindingSamples
│  │  │  │  ├─ AddProduct.cs
│  │  │  │  ├─ AddProductParams.cs
│  │  │  │  ├─ AddProductsArray.cs
│  │  │  │  ├─ AddProductsAsyncCollector.cs
│  │  │  │  ├─ AddProductsCollector.cs
│  │  │  │  ├─ AddProductsWithIdentityColumnArray.cs
│  │  │  │  ├─ AddProductWithDefaultPK.cs
│  │  │  │  ├─ AddProductWithIdentityColumn.cs
│  │  │  │  ├─ AddProductWithIdentityColumnIncluded.cs
│  │  │  │  ├─ AddProductWithMultiplePrimaryColumnsAndIdentity.cs
│  │  │  │  ├─ QueueTriggerProducts.cs
│  │  │  │  └─ TimerTriggerProducts.cs
│  │  │  ├─ packages.lock.json
│  │  │  └─ Properties
│  │  │     ├─ serviceDependencies.json
│  │  │     └─ serviceDependencies.local.json
│  │  ├─ samples-csx
│  │  │  ├─ .editorconfig
│  │  │  ├─ .vscode
│  │  │  │  └─ extensions.json
│  │  │  ├─ AddProduct
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductParams
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductsArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductsCollector
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductsWithIdentityColumnArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductWithDefaultPK
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductWithIdentityColumn
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductWithIdentityColumnIncluded
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductWithMultiplePrimaryColumnsAndIdentity
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ Common
│  │  │  │  └─ product.csx
│  │  │  ├─ GetAndAddProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProductNamesView
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProductsAsyncEnumerable
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProductsNameEmpty
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProductsNameNull
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProductsStoredProcedure
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProductsStoredProcedureFromAppSetting
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ host.json
│  │  │  ├─ local.settings.json
│  │  │  ├─ packages.lock.json
│  │  │  ├─ QueueTriggerProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  └─ TimerTriggerProducts
│  │  │     ├─ function.json
│  │  │     └─ run.csx
│  │  ├─ samples-java
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ checkstyle.xml
│  │  │  ├─ host.json
│  │  │  ├─ local.settings.json
│  │  │  ├─ pom.xml
│  │  │  └─ src
│  │  │     └─ main
│  │  │        └─ java
│  │  │           └─ com
│  │  │              └─ function
│  │  │                 ├─ AddProduct.java
│  │  │                 ├─ AddProductParams.java
│  │  │                 ├─ AddProductReturnValue.java
│  │  │                 ├─ AddProductsArray.java
│  │  │                 ├─ AddProductsWithIdentityColumnArray.java
│  │  │                 ├─ AddProductToTwoTables.java
│  │  │                 ├─ AddProductWithDefaultPK.java
│  │  │                 ├─ AddProductWithIdentityColumn.java
│  │  │                 ├─ AddProductWithIdentityColumnIncluded.java
│  │  │                 ├─ AddProductWithMultiplePrimaryColumnsAndIdentity.java
│  │  │                 ├─ Common
│  │  │                 │  ├─ MultiplePrimaryKeyProductWithoutId.java
│  │  │                 │  ├─ Product.java
│  │  │                 │  ├─ ProductName.java
│  │  │                 │  ├─ ProductWithDefaultPK.java
│  │  │                 │  ├─ ProductWithOptionalId.java
│  │  │                 │  └─ ProductWithoutId.java
│  │  │                 ├─ GetAndAddProducts.java
│  │  │                 ├─ GetProductNamesView.java
│  │  │                 ├─ GetProducts.java
│  │  │                 ├─ GetProductsFromTwoTables.java
│  │  │                 ├─ GetProductsNameEmpty.java
│  │  │                 ├─ GetProductsStoredProcedure.java
│  │  │                 ├─ GetProductsStoredProcedureFromAppSetting.java
│  │  │                 ├─ QueueTriggerProducts.java
│  │  │                 └─ TimerTriggerProducts.java
│  │  ├─ samples-js
│  │  │  ├─ .eslintrc.json
│  │  │  ├─ .funcignore
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ AddProduct
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductParams
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductsArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductsWithIdentityColumnArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductWithDefaultPK
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductWithIdentityColumn
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductWithIdentityColumnIncluded
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductWithMultiplePrimaryColumnsAndIdentity
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetAndAddProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetProductNamesView
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetProductsNameEmpty
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetProductsNameNull
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetProductsStoredProcedure
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetProductsStoredProcedureFromAppSetting
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ host.json
│  │  │  ├─ local.settings.json
│  │  │  ├─ package-lock.json
│  │  │  ├─ package.json
│  │  │  ├─ QueueTriggerProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  └─ TimerTriggerProducts
│  │  │     ├─ function.json
│  │  │     └─ index.js
│  │  ├─ samples-js-v4
│  │  │  ├─ .funcignore
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ host.json
│  │  │  ├─ local.settings.json
│  │  │  ├─ package-lock.json
│  │  │  ├─ package.json
│  │  │  └─ src
│  │  │     └─ functions
│  │  │        ├─ AddProduct.js
│  │  │        └─ GetProducts.js
│  │  ├─ samples-outofproc
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ GlobalSuppressions.cs
│  │  │  ├─ host.json
│  │  │  ├─ InputBindingSamples
│  │  │  │  ├─ GetProductNamesView.cs
│  │  │  │  ├─ GetProducts.cs
│  │  │  │  ├─ GetProductsAsyncEnumerable.cs
│  │  │  │  ├─ GetProductsNameEmpty.cs
│  │  │  │  ├─ GetProductsNameNull.cs
│  │  │  │  ├─ GetProductsStoredProcedure.cs
│  │  │  │  ├─ GetProductsStoreProcedureFromAppSetting.cs
│  │  │  │  ├─ GetProductsString.cs
│  │  │  │  └─ GetProductsTopN.cs
│  │  │  ├─ local.settings.json
│  │  │  ├─ Microsoft.Azure.WebJobs.Extensions.Sql.SamplesOutOfProc.csproj
│  │  │  ├─ MultipleBindingsSamples
│  │  │  │  └─ GetAndAddProducts.cs
│  │  │  ├─ OutputBindingSamples
│  │  │  │  ├─ AddProduct.cs
│  │  │  │  ├─ AddProductParams.cs
│  │  │  │  ├─ AddProductsArray.cs
│  │  │  │  ├─ AddProductsWithIdentityColumnArray.cs
│  │  │  │  ├─ AddProductWithDefaultPK.cs
│  │  │  │  ├─ AddProductWithIdentityColumn.cs
│  │  │  │  ├─ AddProductWithIdentityColumnIncluded.cs
│  │  │  │  ├─ AddProductWithMultiplePrimaryColumnsAndIdentity.cs
│  │  │  │  ├─ QueueTriggerProducts.cs
│  │  │  │  └─ TimerTriggerProducts.cs
│  │  │  ├─ packages.lock.json
│  │  │  ├─ Product.cs
│  │  │  ├─ Program.cs
│  │  │  └─ Properties
│  │  │     └─ launchSettings.json
│  │  ├─ samples-powershell
│  │  │  ├─ .funcignore
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ AddProduct
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductParams
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductsArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductsWithIdentityColumnArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductWithDefaultPK
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductWithIdentityColumn
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductWithIdentityColumnIncluded
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductWithMultiplePrimaryColumnsAndIdentity
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetAndAddProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetProductNamesView
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetProductsNameEmpty
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetProductsNameNull
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetProductsStoredProcedure
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetProductsStoredProcedureFromAppSetting
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ host.json
│  │  │  ├─ local.settings.json
│  │  │  ├─ profile.ps1
│  │  │  ├─ QueueTriggerProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ requirements.psd1
│  │  │  └─ TimerTriggerProducts
│  │  │     ├─ function.json
│  │  │     └─ run.ps1
│  │  ├─ samples-python
│  │  │  ├─ .devcontainer
│  │  │  │  ├─ devcontainer.json
│  │  │  │  ├─ Dockerfile
│  │  │  │  ├─ patch-core-tools.sh
│  │  │  │  └─ README.md
│  │  │  ├─ .funcignore
│  │  │  ├─ .pylintrc
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ AddProduct
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductParams
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductsArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductsWithIdentityColumnArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductWithDefaultPK
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductWithIdentityColumn
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductWithIdentityColumnIncluded
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductWithMultiplePrimaryColumnsAndIdentity
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ Common
│  │  │  │  ├─ multiplePrimaryKeyProductWithoutId.py
│  │  │  │  ├─ product.py
│  │  │  │  └─ productWithoutId.py
│  │  │  ├─ GetAndAddProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProductNamesView
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProductsColumnTypesSerialization
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProductsNameEmpty
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProductsNameNull
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProductsStoredProcedure
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProductsStoredProcedureFromAppSetting
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ host.json
│  │  │  ├─ local.settings.json
│  │  │  ├─ QueueTriggerProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ requirements.txt
│  │  │  └─ TimerTriggerProducts
│  │  │     ├─ function.json
│  │  │     └─ __init__.py
│  │  └─ samples-python-v2
│  │     ├─ .funcignore
│  │     ├─ .pylintrc
│  │     ├─ .vscode
│  │     │  ├─ extensions.json
│  │     │  ├─ launch.json
│  │     │  ├─ settings.json
│  │     │  └─ tasks.json
│  │     ├─ function_app.py
│  │     ├─ host.json
│  │     ├─ local.settings.json
│  │     └─ requirements.txt
│  ├─ scripts
│  │  ├─ BuildJavaProjectsAndRunIntegrationTests.ps1
│  │  └─ CopySqlDllToExtensionBundle.ps1
│  ├─ SECURITY.md
│  ├─ SQL2003.snk
│  ├─ src
│  │  ├─ Microsoft.Azure.WebJobs.Extensions.Sql.csproj
│  │  ├─ packages.lock.json
│  │  ├─ SqlAsyncCollector.cs
│  │  ├─ SqlAsyncCollectorBuilder.cs
│  │  ├─ SqlAsyncEnumerable.cs
│  │  ├─ SqlAttribute.cs
│  │  ├─ SqlBindingConfigProvider.cs
│  │  ├─ SqlBindingConstants.cs
│  │  ├─ SqlBindingExtension.cs
│  │  ├─ SqlBindingStartup.cs
│  │  ├─ SqlBindingUtilities.cs
│  │  ├─ SqlConverters.cs
│  │  ├─ SqlObject.cs
│  │  ├─ Telemetry
│  │  │  ├─ Telemetry.cs
│  │  │  ├─ TelemetryCommonProperties.cs
│  │  │  ├─ TelemetryUtils.cs
│  │  │  └─ UserLevelCacheWriter.cs
│  │  └─ Utils.cs
│  ├─ test
│  │  ├─ .editorconfig
│  │  ├─ Common
│  │  │  ├─ LogTestNameAttribute.cs
│  │  │  ├─ ProductColumnTypes.cs
│  │  │  ├─ ProductDefaultPKAndDifferentColumnOrder.cs
│  │  │  ├─ ProductExtraColumns.cs
│  │  │  ├─ ProductIncorrectCasing.cs
│  │  │  ├─ ProductMissingColumns.cs
│  │  │  ├─ ProductUnsupportedTypes.cs
│  │  │  ├─ SupportedLanguagesTestAttribute.cs
│  │  │  ├─ TestConfiguration.cs
│  │  │  ├─ TestConfigurationSection.cs
│  │  │  ├─ TestData.cs
│  │  │  └─ TestUtils.cs
│  │  ├─ coverage.runsettings
│  │  ├─ Database
│  │  │  └─ Tables
│  │  │     ├─ ProductsColumnTypes.sql
│  │  │     ├─ ProductsUnsupportedTypes.sql
│  │  │     ├─ ProductsWithoutPrimaryKey.sql
│  │  │     ├─ ProductsWithReservedPrimaryKeyColumnNames.sql
│  │  │     └─ ProductsWithUnsupportedColumnTypes.sql
│  │  ├─ GlobalSuppressions.cs
│  │  ├─ Integration
│  │  │  ├─ IntegrationTestBase.cs
│  │  │  ├─ IntegrationTestFixture.cs
│  │  │  ├─ IntegrationTestsCollection.cs
│  │  │  ├─ MultipleSqlBindingsIntegrationTests.cs
│  │  │  ├─ SqlInputBindingIntegrationTests.cs
│  │  │  ├─ SqlOutputBindingIntegrationTests.cs
│  │  │  ├─ test-csharp
│  │  │  │  ├─ AddProductColumnTypes.cs
│  │  │  │  ├─ AddProductDefaultPKAndDifferentColumnOrder.cs
│  │  │  │  ├─ AddProductExtraColumns.cs
│  │  │  │  ├─ AddProductIncorrectCasing.cs
│  │  │  │  ├─ AddProductMissingColumns.cs
│  │  │  │  ├─ AddProductMissingColumnsException.cs
│  │  │  │  ├─ AddProductsNoPartialUpsert.cs
│  │  │  │  ├─ AddProductUnsupportedTypes.cs
│  │  │  │  ├─ GetProductColumnTypesSerialization.cs
│  │  │  │  ├─ GetProductColumnTypesSerializationAsyncEnumerable.cs
│  │  │  │  └─ Startup.cs
│  │  │  ├─ test-csx
│  │  │  │  ├─ .vscode
│  │  │  │  │  └─ extensions.json
│  │  │  │  ├─ AddProductColumnTypes
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductDefaultPKAndDifferentColumnOrder
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductExtraColumns
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductIncorrectCasing
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductMissingColumns
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductMissingColumnsExceptionFunction
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductsNoPartialUpsert
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductUnsupportedTypes
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ Common
│  │  │  │  │  └─ Product.csx
│  │  │  │  ├─ GetProductsColumnTypesSerialization
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ GetProductsColumnTypesSerializationAsyncEnumerable
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  └─ host.json
│  │  │  ├─ test-java
│  │  │  │  ├─ .vscode
│  │  │  │  │  ├─ extensions.json
│  │  │  │  │  ├─ launch.json
│  │  │  │  │  ├─ settings.json
│  │  │  │  │  └─ tasks.json
│  │  │  │  ├─ checkstyle.xml
│  │  │  │  ├─ host.json
│  │  │  │  ├─ local.settings.json
│  │  │  │  ├─ pom.xml
│  │  │  │  └─ src
│  │  │  │     └─ main
│  │  │  │        └─ java
│  │  │  │           └─ com
│  │  │  │              └─ function
│  │  │  │                 ├─ AddProductColumnTypes.java
│  │  │  │                 ├─ AddProductDefaultPKAndDifferentColumnOrder.java
│  │  │  │                 ├─ AddProductExtraColumns.java
│  │  │  │                 ├─ AddProductIncorrectCasing.java
│  │  │  │                 ├─ AddProductMissingColumns.java
│  │  │  │                 ├─ AddProductMissingColumnsExceptionFunction.java
│  │  │  │                 ├─ AddProductsNoPartialUpsert.java
│  │  │  │                 ├─ AddProductUnsupportedTypes.java
│  │  │  │                 ├─ Common
│  │  │  │                 │  ├─ Product.java
│  │  │  │                 │  ├─ ProductColumnTypes.java
│  │  │  │                 │  ├─ ProductDefaultPKAndDifferentColumnOrder.java
│  │  │  │                 │  ├─ ProductExtraColumns.java
│  │  │  │                 │  ├─ ProductIncorrectCasing.java
│  │  │  │                 │  ├─ ProductMissingColumns.java
│  │  │  │                 │  └─ ProductUnsupportedTypes.java
│  │  │  │                 └─ GetProductsColumnTypesSerialization.java
│  │  │  ├─ test-js
│  │  │  │  ├─ .eslintrc.json
│  │  │  │  ├─ AddProductColumnTypes
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductDefaultPKAndDifferentColumnOrder
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductExtraColumns
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductIncorrectCasing
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductMissingColumns
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductMissingColumnsExceptionFunction
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductsNoPartialUpsert
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductUnsupportedTypes
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ GetProductsColumnTypesSerialization
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ package-lock.json
│  │  │  │  └─ package.json
│  │  │  ├─ test-powershell
│  │  │  │  ├─ AddProductColumnTypes
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductDefaultPKAndDifferentColumnOrder
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductExtraColumns
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductIncorrectCasing
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductMissingColumns
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductMissingColumnsExceptionFunction
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductsNoPartialUpsert
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductUnsupportedTypes
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  └─ GetProductsColumnTypesSerialization
│  │  │  │     ├─ function.json
│  │  │  │     └─ run.ps1
│  │  │  └─ test-python
│  │  │     ├─ AddProductColumnTypes
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ AddProductDefaultPKAndDifferentColumnOrder
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ AddProductExtraColumns
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ AddProductMissingColumns
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ AddProductMissingColumnsException
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ AddProductsNoPartialUpsert
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ AddProductUnsupportedTypes
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ Common
│  │  │     │  ├─ product.py
│  │  │     │  ├─ productcolumntypes.py
│  │  │     │  ├─ productdefaultpkanddifferentcolumnorder.py
│  │  │     │  ├─ productextracolumns.py
│  │  │     │  ├─ productmissingcolumns.py
│  │  │     │  └─ productunsupportedtypes.py
│  │  │     └─ GetProductsColumnTypesSerialization
│  │  │        ├─ function.json
│  │  │        └─ __init__.py
│  │  ├─ Microsoft.Azure.WebJobs.Extensions.Sql.Tests.csproj
│  │  ├─ packages.lock.json
│  │  ├─ README.md
│  │  └─ Unit
│  │     ├─ SqlInputBindingTests.cs
│  │     ├─ SqlOutputBindingTests.cs
│  │     └─ UtilsTests.cs
│  ├─ test-outofproc
│  │  ├─ .editorconfig
│  │  ├─ .vscode
│  │  │  └─ extensions.json
│  │  ├─ AddProductColumnTypes.cs
│  │  ├─ AddProductDefaultPKAndDifferentColumnOrder.cs
│  │  ├─ AddProductExtraColumns.cs
│  │  ├─ AddProductIncorrectCasing.cs
│  │  ├─ AddProductMissingColumns.cs
│  │  ├─ AddProductMissingColumnsException.cs
│  │  ├─ AddProductsNoPartialUpsert.cs
│  │  ├─ AddProductUnsupportedTypes.cs
│  │  ├─ GetProductColumnTypesSerialization.cs
│  │  ├─ GetProductColumnTypesSerializationAsyncEnumerable.cs
│  │  ├─ GlobalSuppressions.cs
│  │  ├─ host.json
│  │  ├─ local.settings.json
│  │  ├─ packages.lock.json
│  │  ├─ Product.cs
│  │  ├─ Program.cs
│  │  ├─ Properties
│  │  │  └─ launchSettings.json
│  │  ├─ test-outofproc.csproj
│  │  └─ Unit
│  │     └─ WorkerUnitTests.cs
│  ├─ WebJobs.Extensions.Sql.sln
│  └─ Worker.Extensions.Sql
│     └─ src
│        ├─ Microsoft.Azure.Functions.Worker.Extensions.Sql.csproj
│        ├─ packages.lock.json
│        ├─ README.md
│        ├─ SqlInputAttribute.cs
│        └─ SqlOutputAttribute.cs
├─ azure.ipynb
├─ CODEOWNERS
├─ config.yaml
├─ custom_fields.json
├─ diagram.drawio
├─ diagram.png
├─ diagrams
│  ├─ logicapp-architecture.ipynb
│  ├─ README.md
│  └─ requirements-diagrams.txt
├─ exercism.py
├─ Functions.code-workspace
├─ github-testing.ipynb
├─ github-testing.py
├─ gpt-engineer
│  ├─ archive
│  │  ├─ 20231009_142526
│  │  │  ├─ memory
│  │  │  │  └─ logs
│  │  │  └─ workspace
│  │  ├─ 20231009_142840
│  │  │  ├─ memory
│  │  │  │  └─ logs
│  │  │  │     └─ clarify
│  │  │  └─ workspace
│  │  └─ 20231009_143456
│  │     ├─ memory
│  │     │  └─ logs
│  │     │     └─ clarify
│  │     └─ workspace
│  ├─ gpt-engineer
│  │  ├─ archive
│  │  │  └─ 20231010_125320
│  │  │     ├─ memory
│  │  │     │  └─ logs
│  │  │     └─ workspace
│  │  └─ prompt
│  ├─ memory
│  │  └─ logs
│  │     └─ clarify
│  └─ prompt
├─ gpt-engineerclear
│  └─ archive
│     └─ 20231009_142823
│        ├─ memory
│        │  └─ logs
│        └─ workspace
├─ IMS-API.py
├─ ims-request-body.json
├─ ims_notebook.ipynb
├─ jsonToYaml.ipynb
├─ kwargs.ipynb
├─ lasagna.py
├─ markdown-test.md
├─ mermaid.md
├─ mslearn-ai-challenge
│  └─ ml-services
│     ├─ deployment.json
│     ├─ deployment_operations.json
│     ├─ parameters.json
│     └─ template.json
├─ ODW-Service
│  ├─ .checkov.yaml
│  ├─ .pre-commit-config.yaml
│  ├─ .terraform
│  │  └─ modules
│  │     └─ modules.json
│  ├─ .tflint.hcl
│  ├─ docs
│  │  ├─ architecture
│  │  │  └─ apim-and-function-apps.md
│  │  ├─ layers
│  │  │  ├─ 0_layers_overview.md
│  │  │  ├─ 1_raw.md
│  │  │  ├─ 2_standardised.md
│  │  │  ├─ 3_harmonised.md
│  │  │  ├─ 4_curated.md
│  │  │  └─ 5_publish.md
│  │  ├─ pull_request_template.md
│  │  └─ standards
│  │     ├─ brach_standards.md
│  │     ├─ data-standards.md
│  │     ├─ get-data-from-external-api.md
│  │     ├─ infrastructure_standards.md
│  │     ├─ naming_standards.md
│  │     ├─ notebooks_standards.md
│  │     └─ pipeline_standards.md
│  ├─ functions
│  │  ├─ .funcignore
│  │  ├─ .venv
│  │  │  ├─ Include
│  │  │  ├─ Lib
│  │  │  │  └─ site-packages
│  │  │  │     ├─ adodbapi
│  │  │  │     │  ├─ adodbapi.py
│  │  │  │     │  ├─ ado_consts.py
│  │  │  │     │  ├─ apibase.py
│  │  │  │     │  ├─ examples
│  │  │  │     │  │  ├─ db_print.py
│  │  │  │     │  │  ├─ db_table_names.py
│  │  │  │     │  │  ├─ xls_read.py
│  │  │  │     │  │  ├─ xls_write.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ db_print.cpython-310.pyc
│  │  │  │     │  │     ├─ db_table_names.cpython-310.pyc
│  │  │  │     │  │     ├─ xls_read.cpython-310.pyc
│  │  │  │     │  │     └─ xls_write.cpython-310.pyc
│  │  │  │     │  ├─ is64bit.py
│  │  │  │     │  ├─ license.txt
│  │  │  │     │  ├─ process_connect_string.py
│  │  │  │     │  ├─ readme.txt
│  │  │  │     │  ├─ remote.py
│  │  │  │     │  ├─ schema_table.py
│  │  │  │     │  ├─ setup.py
│  │  │  │     │  ├─ test
│  │  │  │     │  │  ├─ adodbapitest.py
│  │  │  │     │  │  ├─ adodbapitestconfig.py
│  │  │  │     │  │  ├─ dbapi20.py
│  │  │  │     │  │  ├─ is64bit.py
│  │  │  │     │  │  ├─ setuptestframework.py
│  │  │  │     │  │  ├─ test_adodbapi_dbapi20.py
│  │  │  │     │  │  ├─ tryconnection.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ adodbapitest.cpython-310.pyc
│  │  │  │     │  │     ├─ adodbapitestconfig.cpython-310.pyc
│  │  │  │     │  │     ├─ dbapi20.cpython-310.pyc
│  │  │  │     │  │     ├─ is64bit.cpython-310.pyc
│  │  │  │     │  │     ├─ setuptestframework.cpython-310.pyc
│  │  │  │     │  │     ├─ test_adodbapi_dbapi20.cpython-310.pyc
│  │  │  │     │  │     └─ tryconnection.cpython-310.pyc
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ adodbapi.cpython-310.pyc
│  │  │  │     │     ├─ ado_consts.cpython-310.pyc
│  │  │  │     │     ├─ apibase.cpython-310.pyc
│  │  │  │     │     ├─ is64bit.cpython-310.pyc
│  │  │  │     │     ├─ process_connect_string.cpython-310.pyc
│  │  │  │     │     ├─ remote.cpython-310.pyc
│  │  │  │     │     ├─ schema_table.cpython-310.pyc
│  │  │  │     │     ├─ setup.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ azure
│  │  │  │     │  ├─ core
│  │  │  │     │  │  ├─ async_paging.py
│  │  │  │     │  │  ├─ configuration.py
│  │  │  │     │  │  ├─ credentials.py
│  │  │  │     │  │  ├─ credentials_async.py
│  │  │  │     │  │  ├─ exceptions.py
│  │  │  │     │  │  ├─ messaging.py
│  │  │  │     │  │  ├─ paging.py
│  │  │  │     │  │  ├─ pipeline
│  │  │  │     │  │  │  ├─ policies
│  │  │  │     │  │  │  │  ├─ _authentication.py
│  │  │  │     │  │  │  │  ├─ _authentication_async.py
│  │  │  │     │  │  │  │  ├─ _base.py
│  │  │  │     │  │  │  │  ├─ _base_async.py
│  │  │  │     │  │  │  │  ├─ _custom_hook.py
│  │  │  │     │  │  │  │  ├─ _distributed_tracing.py
│  │  │  │     │  │  │  │  ├─ _redirect.py
│  │  │  │     │  │  │  │  ├─ _redirect_async.py
│  │  │  │     │  │  │  │  ├─ _retry.py
│  │  │  │     │  │  │  │  ├─ _retry_async.py
│  │  │  │     │  │  │  │  ├─ _sensitive_header_cleanup_policy.py
│  │  │  │     │  │  │  │  ├─ _universal.py
│  │  │  │     │  │  │  │  ├─ _utils.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ _authentication.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _authentication_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _base.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _base_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _custom_hook.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _distributed_tracing.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _redirect.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _redirect_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _retry.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _retry_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _sensitive_header_cleanup_policy.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _universal.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _utils.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ transport
│  │  │  │     │  │  │  │  ├─ _aiohttp.py
│  │  │  │     │  │  │  │  ├─ _base.py
│  │  │  │     │  │  │  │  ├─ _base_async.py
│  │  │  │     │  │  │  │  ├─ _base_requests_async.py
│  │  │  │     │  │  │  │  ├─ _bigger_block_size_http_adapters.py
│  │  │  │     │  │  │  │  ├─ _requests_asyncio.py
│  │  │  │     │  │  │  │  ├─ _requests_basic.py
│  │  │  │     │  │  │  │  ├─ _requests_trio.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ _aiohttp.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _base.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _base_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _base_requests_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _bigger_block_size_http_adapters.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _requests_asyncio.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _requests_basic.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _requests_trio.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _base.py
│  │  │  │     │  │  │  ├─ _base_async.py
│  │  │  │     │  │  │  ├─ _tools.py
│  │  │  │     │  │  │  ├─ _tools_async.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _base_async.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _tools.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _tools_async.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ polling
│  │  │  │     │  │  │  ├─ async_base_polling.py
│  │  │  │     │  │  │  ├─ base_polling.py
│  │  │  │     │  │  │  ├─ _async_poller.py
│  │  │  │     │  │  │  ├─ _poller.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ async_base_polling.cpython-310.pyc
│  │  │  │     │  │  │     ├─ base_polling.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _async_poller.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _poller.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ py.typed
│  │  │  │     │  │  ├─ rest
│  │  │  │     │  │  │  ├─ _aiohttp.py
│  │  │  │     │  │  │  ├─ _helpers.py
│  │  │  │     │  │  │  ├─ _http_response_impl.py
│  │  │  │     │  │  │  ├─ _http_response_impl_async.py
│  │  │  │     │  │  │  ├─ _requests_asyncio.py
│  │  │  │     │  │  │  ├─ _requests_basic.py
│  │  │  │     │  │  │  ├─ _requests_trio.py
│  │  │  │     │  │  │  ├─ _rest_py3.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _aiohttp.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _helpers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _http_response_impl.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _http_response_impl_async.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _requests_asyncio.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _requests_basic.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _requests_trio.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _rest_py3.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ serialization.py
│  │  │  │     │  │  ├─ settings.py
│  │  │  │     │  │  ├─ tracing
│  │  │  │     │  │  │  ├─ common.py
│  │  │  │     │  │  │  ├─ decorator.py
│  │  │  │     │  │  │  ├─ decorator_async.py
│  │  │  │     │  │  │  ├─ ext
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _abstract_span.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ common.cpython-310.pyc
│  │  │  │     │  │  │     ├─ decorator.cpython-310.pyc
│  │  │  │     │  │  │     ├─ decorator_async.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _abstract_span.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ utils
│  │  │  │     │  │  │  ├─ _connection_string_parser.py
│  │  │  │     │  │  │  ├─ _messaging_shared.py
│  │  │  │     │  │  │  ├─ _pipeline_transport_rest_shared.py
│  │  │  │     │  │  │  ├─ _pipeline_transport_rest_shared_async.py
│  │  │  │     │  │  │  ├─ _utils.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _connection_string_parser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _messaging_shared.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _pipeline_transport_rest_shared.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _pipeline_transport_rest_shared_async.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _utils.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ _enum_meta.py
│  │  │  │     │  │  ├─ _match_conditions.py
│  │  │  │     │  │  ├─ _pipeline_client.py
│  │  │  │     │  │  ├─ _pipeline_client_async.py
│  │  │  │     │  │  ├─ _version.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ async_paging.cpython-310.pyc
│  │  │  │     │  │     ├─ configuration.cpython-310.pyc
│  │  │  │     │  │     ├─ credentials.cpython-310.pyc
│  │  │  │     │  │     ├─ credentials_async.cpython-310.pyc
│  │  │  │     │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │     ├─ messaging.cpython-310.pyc
│  │  │  │     │  │     ├─ paging.cpython-310.pyc
│  │  │  │     │  │     ├─ serialization.cpython-310.pyc
│  │  │  │     │  │     ├─ settings.cpython-310.pyc
│  │  │  │     │  │     ├─ _enum_meta.cpython-310.pyc
│  │  │  │     │  │     ├─ _match_conditions.cpython-310.pyc
│  │  │  │     │  │     ├─ _pipeline_client.cpython-310.pyc
│  │  │  │     │  │     ├─ _pipeline_client_async.cpython-310.pyc
│  │  │  │     │  │     ├─ _version.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ functions
│  │  │  │     │  │  ├─ blob.py
│  │  │  │     │  │  ├─ cosmosdb.py
│  │  │  │     │  │  ├─ decorators
│  │  │  │     │  │  │  ├─ blob.py
│  │  │  │     │  │  │  ├─ constants.py
│  │  │  │     │  │  │  ├─ core.py
│  │  │  │     │  │  │  ├─ cosmosdb.py
│  │  │  │     │  │  │  ├─ eventgrid.py
│  │  │  │     │  │  │  ├─ eventhub.py
│  │  │  │     │  │  │  ├─ function_app.py
│  │  │  │     │  │  │  ├─ generic.py
│  │  │  │     │  │  │  ├─ http.py
│  │  │  │     │  │  │  ├─ queue.py
│  │  │  │     │  │  │  ├─ servicebus.py
│  │  │  │     │  │  │  ├─ table.py
│  │  │  │     │  │  │  ├─ timer.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ warmup.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ blob.cpython-310.pyc
│  │  │  │     │  │  │     ├─ constants.cpython-310.pyc
│  │  │  │     │  │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cosmosdb.cpython-310.pyc
│  │  │  │     │  │  │     ├─ eventgrid.cpython-310.pyc
│  │  │  │     │  │  │     ├─ eventhub.cpython-310.pyc
│  │  │  │     │  │  │     ├─ function_app.cpython-310.pyc
│  │  │  │     │  │  │     ├─ generic.cpython-310.pyc
│  │  │  │     │  │  │     ├─ http.cpython-310.pyc
│  │  │  │     │  │  │     ├─ queue.cpython-310.pyc
│  │  │  │     │  │  │     ├─ servicebus.cpython-310.pyc
│  │  │  │     │  │  │     ├─ table.cpython-310.pyc
│  │  │  │     │  │  │     ├─ timer.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ warmup.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ durable_functions.py
│  │  │  │     │  │  ├─ eventgrid.py
│  │  │  │     │  │  ├─ eventhub.py
│  │  │  │     │  │  ├─ extension
│  │  │  │     │  │  │  ├─ app_extension_base.py
│  │  │  │     │  │  │  ├─ extension_hook_meta.py
│  │  │  │     │  │  │  ├─ extension_meta.py
│  │  │  │     │  │  │  ├─ extension_scope.py
│  │  │  │     │  │  │  ├─ function_extension_exception.py
│  │  │  │     │  │  │  ├─ func_extension_base.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ app_extension_base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ extension_hook_meta.cpython-310.pyc
│  │  │  │     │  │  │     ├─ extension_meta.cpython-310.pyc
│  │  │  │     │  │  │     ├─ extension_scope.cpython-310.pyc
│  │  │  │     │  │  │     ├─ function_extension_exception.cpython-310.pyc
│  │  │  │     │  │  │     ├─ func_extension_base.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ http.py
│  │  │  │     │  │  ├─ kafka.py
│  │  │  │     │  │  ├─ meta.py
│  │  │  │     │  │  ├─ py.typed
│  │  │  │     │  │  ├─ queue.py
│  │  │  │     │  │  ├─ servicebus.py
│  │  │  │     │  │  ├─ sql.py
│  │  │  │     │  │  ├─ timer.py
│  │  │  │     │  │  ├─ warmup.py
│  │  │  │     │  │  ├─ _abc.py
│  │  │  │     │  │  ├─ _cosmosdb.py
│  │  │  │     │  │  ├─ _durable_functions.py
│  │  │  │     │  │  ├─ _eventgrid.py
│  │  │  │     │  │  ├─ _eventhub.py
│  │  │  │     │  │  ├─ _http.py
│  │  │  │     │  │  ├─ _http_asgi.py
│  │  │  │     │  │  ├─ _http_wsgi.py
│  │  │  │     │  │  ├─ _kafka.py
│  │  │  │     │  │  ├─ _queue.py
│  │  │  │     │  │  ├─ _servicebus.py
│  │  │  │     │  │  ├─ _sql.py
│  │  │  │     │  │  ├─ _thirdparty
│  │  │  │     │  │  │  ├─ typing_inspect.py
│  │  │  │     │  │  │  ├─ werkzeug
│  │  │  │     │  │  │  │  ├─ datastructures.py
│  │  │  │     │  │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  │  ├─ formparser.py
│  │  │  │     │  │  │  │  ├─ http.py
│  │  │  │     │  │  │  │  ├─ urls.py
│  │  │  │     │  │  │  │  ├─ utils.py
│  │  │  │     │  │  │  │  ├─ wsgi.py
│  │  │  │     │  │  │  │  ├─ _compat.py
│  │  │  │     │  │  │  │  ├─ _internal.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ datastructures.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ formparser.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ http.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ urls.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ wsgi.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _compat.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _internal.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ typing_inspect.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ _utils.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ blob.cpython-310.pyc
│  │  │  │     │  │     ├─ cosmosdb.cpython-310.pyc
│  │  │  │     │  │     ├─ durable_functions.cpython-310.pyc
│  │  │  │     │  │     ├─ eventgrid.cpython-310.pyc
│  │  │  │     │  │     ├─ eventhub.cpython-310.pyc
│  │  │  │     │  │     ├─ http.cpython-310.pyc
│  │  │  │     │  │     ├─ kafka.cpython-310.pyc
│  │  │  │     │  │     ├─ meta.cpython-310.pyc
│  │  │  │     │  │     ├─ queue.cpython-310.pyc
│  │  │  │     │  │     ├─ servicebus.cpython-310.pyc
│  │  │  │     │  │     ├─ sql.cpython-310.pyc
│  │  │  │     │  │     ├─ timer.cpython-310.pyc
│  │  │  │     │  │     ├─ warmup.cpython-310.pyc
│  │  │  │     │  │     ├─ _abc.cpython-310.pyc
│  │  │  │     │  │     ├─ _cosmosdb.cpython-310.pyc
│  │  │  │     │  │     ├─ _durable_functions.cpython-310.pyc
│  │  │  │     │  │     ├─ _eventgrid.cpython-310.pyc
│  │  │  │     │  │     ├─ _eventhub.cpython-310.pyc
│  │  │  │     │  │     ├─ _http.cpython-310.pyc
│  │  │  │     │  │     ├─ _http_asgi.cpython-310.pyc
│  │  │  │     │  │     ├─ _http_wsgi.cpython-310.pyc
│  │  │  │     │  │     ├─ _kafka.cpython-310.pyc
│  │  │  │     │  │     ├─ _queue.cpython-310.pyc
│  │  │  │     │  │     ├─ _servicebus.cpython-310.pyc
│  │  │  │     │  │     ├─ _sql.cpython-310.pyc
│  │  │  │     │  │     ├─ _utils.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  └─ identity
│  │  │  │     │     ├─ aio
│  │  │  │     │     │  ├─ _credentials
│  │  │  │     │     │  │  ├─ application.py
│  │  │  │     │     │  │  ├─ app_service.py
│  │  │  │     │     │  │  ├─ authorization_code.py
│  │  │  │     │     │  │  ├─ azd_cli.py
│  │  │  │     │     │  │  ├─ azure_arc.py
│  │  │  │     │     │  │  ├─ azure_cli.py
│  │  │  │     │     │  │  ├─ azure_ml.py
│  │  │  │     │     │  │  ├─ azure_powershell.py
│  │  │  │     │     │  │  ├─ certificate.py
│  │  │  │     │     │  │  ├─ chained.py
│  │  │  │     │     │  │  ├─ client_assertion.py
│  │  │  │     │     │  │  ├─ client_secret.py
│  │  │  │     │     │  │  ├─ cloud_shell.py
│  │  │  │     │     │  │  ├─ default.py
│  │  │  │     │     │  │  ├─ environment.py
│  │  │  │     │     │  │  ├─ imds.py
│  │  │  │     │     │  │  ├─ managed_identity.py
│  │  │  │     │     │  │  ├─ on_behalf_of.py
│  │  │  │     │     │  │  ├─ service_fabric.py
│  │  │  │     │     │  │  ├─ shared_cache.py
│  │  │  │     │     │  │  ├─ vscode.py
│  │  │  │     │     │  │  ├─ workload_identity.py
│  │  │  │     │     │  │  ├─ __init__.py
│  │  │  │     │     │  │  └─ __pycache__
│  │  │  │     │     │  │     ├─ application.cpython-310.pyc
│  │  │  │     │     │  │     ├─ app_service.cpython-310.pyc
│  │  │  │     │     │  │     ├─ authorization_code.cpython-310.pyc
│  │  │  │     │     │  │     ├─ azd_cli.cpython-310.pyc
│  │  │  │     │     │  │     ├─ azure_arc.cpython-310.pyc
│  │  │  │     │     │  │     ├─ azure_cli.cpython-310.pyc
│  │  │  │     │     │  │     ├─ azure_ml.cpython-310.pyc
│  │  │  │     │     │  │     ├─ azure_powershell.cpython-310.pyc
│  │  │  │     │     │  │     ├─ certificate.cpython-310.pyc
│  │  │  │     │     │  │     ├─ chained.cpython-310.pyc
│  │  │  │     │     │  │     ├─ client_assertion.cpython-310.pyc
│  │  │  │     │     │  │     ├─ client_secret.cpython-310.pyc
│  │  │  │     │     │  │     ├─ cloud_shell.cpython-310.pyc
│  │  │  │     │     │  │     ├─ default.cpython-310.pyc
│  │  │  │     │     │  │     ├─ environment.cpython-310.pyc
│  │  │  │     │     │  │     ├─ imds.cpython-310.pyc
│  │  │  │     │     │  │     ├─ managed_identity.cpython-310.pyc
│  │  │  │     │     │  │     ├─ on_behalf_of.cpython-310.pyc
│  │  │  │     │     │  │     ├─ service_fabric.cpython-310.pyc
│  │  │  │     │     │  │     ├─ shared_cache.cpython-310.pyc
│  │  │  │     │     │  │     ├─ vscode.cpython-310.pyc
│  │  │  │     │     │  │     ├─ workload_identity.cpython-310.pyc
│  │  │  │     │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │     │  ├─ _internal
│  │  │  │     │     │  │  ├─ aad_client.py
│  │  │  │     │     │  │  ├─ decorators.py
│  │  │  │     │     │  │  ├─ get_token_mixin.py
│  │  │  │     │     │  │  ├─ managed_identity_base.py
│  │  │  │     │     │  │  ├─ managed_identity_client.py
│  │  │  │     │     │  │  ├─ __init__.py
│  │  │  │     │     │  │  └─ __pycache__
│  │  │  │     │     │  │     ├─ aad_client.cpython-310.pyc
│  │  │  │     │     │  │     ├─ decorators.cpython-310.pyc
│  │  │  │     │     │  │     ├─ get_token_mixin.cpython-310.pyc
│  │  │  │     │     │  │     ├─ managed_identity_base.cpython-310.pyc
│  │  │  │     │     │  │     ├─ managed_identity_client.cpython-310.pyc
│  │  │  │     │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │     │  ├─ __init__.py
│  │  │  │     │     │  └─ __pycache__
│  │  │  │     │     │     └─ __init__.cpython-310.pyc
│  │  │  │     │     ├─ py.typed
│  │  │  │     │     ├─ _auth_record.py
│  │  │  │     │     ├─ _constants.py
│  │  │  │     │     ├─ _credentials
│  │  │  │     │     │  ├─ application.py
│  │  │  │     │     │  ├─ app_service.py
│  │  │  │     │     │  ├─ authorization_code.py
│  │  │  │     │     │  ├─ azd_cli.py
│  │  │  │     │     │  ├─ azure_arc.py
│  │  │  │     │     │  ├─ azure_cli.py
│  │  │  │     │     │  ├─ azure_ml.py
│  │  │  │     │     │  ├─ azure_powershell.py
│  │  │  │     │     │  ├─ browser.py
│  │  │  │     │     │  ├─ certificate.py
│  │  │  │     │     │  ├─ chained.py
│  │  │  │     │     │  ├─ client_assertion.py
│  │  │  │     │     │  ├─ client_secret.py
│  │  │  │     │     │  ├─ cloud_shell.py
│  │  │  │     │     │  ├─ default.py
│  │  │  │     │     │  ├─ device_code.py
│  │  │  │     │     │  ├─ environment.py
│  │  │  │     │     │  ├─ imds.py
│  │  │  │     │     │  ├─ managed_identity.py
│  │  │  │     │     │  ├─ on_behalf_of.py
│  │  │  │     │     │  ├─ service_fabric.py
│  │  │  │     │     │  ├─ shared_cache.py
│  │  │  │     │     │  ├─ silent.py
│  │  │  │     │     │  ├─ user_password.py
│  │  │  │     │     │  ├─ vscode.py
│  │  │  │     │     │  ├─ workload_identity.py
│  │  │  │     │     │  ├─ __init__.py
│  │  │  │     │     │  └─ __pycache__
│  │  │  │     │     │     ├─ application.cpython-310.pyc
│  │  │  │     │     │     ├─ app_service.cpython-310.pyc
│  │  │  │     │     │     ├─ authorization_code.cpython-310.pyc
│  │  │  │     │     │     ├─ azd_cli.cpython-310.pyc
│  │  │  │     │     │     ├─ azure_arc.cpython-310.pyc
│  │  │  │     │     │     ├─ azure_cli.cpython-310.pyc
│  │  │  │     │     │     ├─ azure_ml.cpython-310.pyc
│  │  │  │     │     │     ├─ azure_powershell.cpython-310.pyc
│  │  │  │     │     │     ├─ browser.cpython-310.pyc
│  │  │  │     │     │     ├─ certificate.cpython-310.pyc
│  │  │  │     │     │     ├─ chained.cpython-310.pyc
│  │  │  │     │     │     ├─ client_assertion.cpython-310.pyc
│  │  │  │     │     │     ├─ client_secret.cpython-310.pyc
│  │  │  │     │     │     ├─ cloud_shell.cpython-310.pyc
│  │  │  │     │     │     ├─ default.cpython-310.pyc
│  │  │  │     │     │     ├─ device_code.cpython-310.pyc
│  │  │  │     │     │     ├─ environment.cpython-310.pyc
│  │  │  │     │     │     ├─ imds.cpython-310.pyc
│  │  │  │     │     │     ├─ managed_identity.cpython-310.pyc
│  │  │  │     │     │     ├─ on_behalf_of.cpython-310.pyc
│  │  │  │     │     │     ├─ service_fabric.cpython-310.pyc
│  │  │  │     │     │     ├─ shared_cache.cpython-310.pyc
│  │  │  │     │     │     ├─ silent.cpython-310.pyc
│  │  │  │     │     │     ├─ user_password.cpython-310.pyc
│  │  │  │     │     │     ├─ vscode.cpython-310.pyc
│  │  │  │     │     │     ├─ workload_identity.cpython-310.pyc
│  │  │  │     │     │     └─ __init__.cpython-310.pyc
│  │  │  │     │     ├─ _enums.py
│  │  │  │     │     ├─ _exceptions.py
│  │  │  │     │     ├─ _internal
│  │  │  │     │     │  ├─ aadclient_certificate.py
│  │  │  │     │     │  ├─ aad_client.py
│  │  │  │     │     │  ├─ aad_client_base.py
│  │  │  │     │     │  ├─ auth_code_redirect_handler.py
│  │  │  │     │     │  ├─ client_credential_base.py
│  │  │  │     │     │  ├─ decorators.py
│  │  │  │     │     │  ├─ get_token_mixin.py
│  │  │  │     │     │  ├─ interactive.py
│  │  │  │     │     │  ├─ linux_vscode_adapter.py
│  │  │  │     │     │  ├─ macos_vscode_adapter.py
│  │  │  │     │     │  ├─ managed_identity_base.py
│  │  │  │     │     │  ├─ managed_identity_client.py
│  │  │  │     │     │  ├─ msal_client.py
│  │  │  │     │     │  ├─ msal_credentials.py
│  │  │  │     │     │  ├─ pipeline.py
│  │  │  │     │     │  ├─ shared_token_cache.py
│  │  │  │     │     │  ├─ user_agent.py
│  │  │  │     │     │  ├─ utils.py
│  │  │  │     │     │  ├─ win_vscode_adapter.py
│  │  │  │     │     │  ├─ __init__.py
│  │  │  │     │     │  └─ __pycache__
│  │  │  │     │     │     ├─ aadclient_certificate.cpython-310.pyc
│  │  │  │     │     │     ├─ aad_client.cpython-310.pyc
│  │  │  │     │     │     ├─ aad_client_base.cpython-310.pyc
│  │  │  │     │     │     ├─ auth_code_redirect_handler.cpython-310.pyc
│  │  │  │     │     │     ├─ client_credential_base.cpython-310.pyc
│  │  │  │     │     │     ├─ decorators.cpython-310.pyc
│  │  │  │     │     │     ├─ get_token_mixin.cpython-310.pyc
│  │  │  │     │     │     ├─ interactive.cpython-310.pyc
│  │  │  │     │     │     ├─ linux_vscode_adapter.cpython-310.pyc
│  │  │  │     │     │     ├─ macos_vscode_adapter.cpython-310.pyc
│  │  │  │     │     │     ├─ managed_identity_base.cpython-310.pyc
│  │  │  │     │     │     ├─ managed_identity_client.cpython-310.pyc
│  │  │  │     │     │     ├─ msal_client.cpython-310.pyc
│  │  │  │     │     │     ├─ msal_credentials.cpython-310.pyc
│  │  │  │     │     │     ├─ pipeline.cpython-310.pyc
│  │  │  │     │     │     ├─ shared_token_cache.cpython-310.pyc
│  │  │  │     │     │     ├─ user_agent.cpython-310.pyc
│  │  │  │     │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     │     ├─ win_vscode_adapter.cpython-310.pyc
│  │  │  │     │     │     └─ __init__.cpython-310.pyc
│  │  │  │     │     ├─ _persistent_cache.py
│  │  │  │     │     ├─ _version.py
│  │  │  │     │     ├─ __init__.py
│  │  │  │     │     └─ __pycache__
│  │  │  │     │        ├─ _auth_record.cpython-310.pyc
│  │  │  │     │        ├─ _constants.cpython-310.pyc
│  │  │  │     │        ├─ _enums.cpython-310.pyc
│  │  │  │     │        ├─ _exceptions.cpython-310.pyc
│  │  │  │     │        ├─ _persistent_cache.cpython-310.pyc
│  │  │  │     │        ├─ _version.cpython-310.pyc
│  │  │  │     │        └─ __init__.cpython-310.pyc
│  │  │  │     ├─ azure_core-1.29.4.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ azure_functions-1.17.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ azure_identity-1.14.1.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ certifi
│  │  │  │     │  ├─ cacert.pem
│  │  │  │     │  ├─ core.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ core.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ certifi-2023.7.22.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ cffi
│  │  │  │     │  ├─ api.py
│  │  │  │     │  ├─ backend_ctypes.py
│  │  │  │     │  ├─ cffi_opcode.py
│  │  │  │     │  ├─ commontypes.py
│  │  │  │     │  ├─ cparser.py
│  │  │  │     │  ├─ error.py
│  │  │  │     │  ├─ ffiplatform.py
│  │  │  │     │  ├─ lock.py
│  │  │  │     │  ├─ model.py
│  │  │  │     │  ├─ parse_c_type.h
│  │  │  │     │  ├─ pkgconfig.py
│  │  │  │     │  ├─ recompiler.py
│  │  │  │     │  ├─ setuptools_ext.py
│  │  │  │     │  ├─ vengine_cpy.py
│  │  │  │     │  ├─ vengine_gen.py
│  │  │  │     │  ├─ verifier.py
│  │  │  │     │  ├─ _cffi_errors.h
│  │  │  │     │  ├─ _cffi_include.h
│  │  │  │     │  ├─ _embedding.h
│  │  │  │     │  ├─ _imp_emulation.py
│  │  │  │     │  ├─ _shimmed_dist_utils.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ api.cpython-310.pyc
│  │  │  │     │     ├─ backend_ctypes.cpython-310.pyc
│  │  │  │     │     ├─ cffi_opcode.cpython-310.pyc
│  │  │  │     │     ├─ commontypes.cpython-310.pyc
│  │  │  │     │     ├─ cparser.cpython-310.pyc
│  │  │  │     │     ├─ error.cpython-310.pyc
│  │  │  │     │     ├─ ffiplatform.cpython-310.pyc
│  │  │  │     │     ├─ lock.cpython-310.pyc
│  │  │  │     │     ├─ model.cpython-310.pyc
│  │  │  │     │     ├─ pkgconfig.cpython-310.pyc
│  │  │  │     │     ├─ recompiler.cpython-310.pyc
│  │  │  │     │     ├─ setuptools_ext.cpython-310.pyc
│  │  │  │     │     ├─ vengine_cpy.cpython-310.pyc
│  │  │  │     │     ├─ vengine_gen.cpython-310.pyc
│  │  │  │     │     ├─ verifier.cpython-310.pyc
│  │  │  │     │     ├─ _imp_emulation.cpython-310.pyc
│  │  │  │     │     ├─ _shimmed_dist_utils.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ cffi-1.16.0.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ charset_normalizer
│  │  │  │     │  ├─ api.py
│  │  │  │     │  ├─ cd.py
│  │  │  │     │  ├─ cli
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  ├─ __main__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ __init__.cpython-310.pyc
│  │  │  │     │  │     └─ __main__.cpython-310.pyc
│  │  │  │     │  ├─ constant.py
│  │  │  │     │  ├─ legacy.py
│  │  │  │     │  ├─ md.cp310-win_amd64.pyd
│  │  │  │     │  ├─ md.py
│  │  │  │     │  ├─ md__mypyc.cp310-win_amd64.pyd
│  │  │  │     │  ├─ models.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ version.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ api.cpython-310.pyc
│  │  │  │     │     ├─ cd.cpython-310.pyc
│  │  │  │     │     ├─ constant.cpython-310.pyc
│  │  │  │     │     ├─ legacy.cpython-310.pyc
│  │  │  │     │     ├─ md.cpython-310.pyc
│  │  │  │     │     ├─ models.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ version.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ charset_normalizer-3.3.0.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ cryptography
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ fernet.py
│  │  │  │     │  ├─ hazmat
│  │  │  │     │  │  ├─ backends
│  │  │  │     │  │  │  ├─ openssl
│  │  │  │     │  │  │  │  ├─ aead.py
│  │  │  │     │  │  │  │  ├─ backend.py
│  │  │  │     │  │  │  │  ├─ ciphers.py
│  │  │  │     │  │  │  │  ├─ cmac.py
│  │  │  │     │  │  │  │  ├─ decode_asn1.py
│  │  │  │     │  │  │  │  ├─ ec.py
│  │  │  │     │  │  │  │  ├─ rsa.py
│  │  │  │     │  │  │  │  ├─ utils.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ aead.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ backend.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ciphers.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ cmac.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ decode_asn1.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ec.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ rsa.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ bindings
│  │  │  │     │  │  │  ├─ openssl
│  │  │  │     │  │  │  │  ├─ binding.py
│  │  │  │     │  │  │  │  ├─ _conditional.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ binding.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _conditional.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _rust
│  │  │  │     │  │  │  │  ├─ asn1.pyi
│  │  │  │     │  │  │  │  ├─ exceptions.pyi
│  │  │  │     │  │  │  │  ├─ ocsp.pyi
│  │  │  │     │  │  │  │  ├─ openssl
│  │  │  │     │  │  │  │  │  ├─ dh.pyi
│  │  │  │     │  │  │  │  │  ├─ dsa.pyi
│  │  │  │     │  │  │  │  │  ├─ ed25519.pyi
│  │  │  │     │  │  │  │  │  ├─ ed448.pyi
│  │  │  │     │  │  │  │  │  ├─ hashes.pyi
│  │  │  │     │  │  │  │  │  ├─ hmac.pyi
│  │  │  │     │  │  │  │  │  ├─ kdf.pyi
│  │  │  │     │  │  │  │  │  ├─ poly1305.pyi
│  │  │  │     │  │  │  │  │  ├─ x25519.pyi
│  │  │  │     │  │  │  │  │  ├─ x448.pyi
│  │  │  │     │  │  │  │  │  └─ __init__.pyi
│  │  │  │     │  │  │  │  ├─ pkcs7.pyi
│  │  │  │     │  │  │  │  ├─ x509.pyi
│  │  │  │     │  │  │  │  ├─ _openssl.pyi
│  │  │  │     │  │  │  │  └─ __init__.pyi
│  │  │  │     │  │  │  ├─ _rust.pyd
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ primitives
│  │  │  │     │  │  │  ├─ asymmetric
│  │  │  │     │  │  │  │  ├─ dh.py
│  │  │  │     │  │  │  │  ├─ dsa.py
│  │  │  │     │  │  │  │  ├─ ec.py
│  │  │  │     │  │  │  │  ├─ ed25519.py
│  │  │  │     │  │  │  │  ├─ ed448.py
│  │  │  │     │  │  │  │  ├─ padding.py
│  │  │  │     │  │  │  │  ├─ rsa.py
│  │  │  │     │  │  │  │  ├─ types.py
│  │  │  │     │  │  │  │  ├─ utils.py
│  │  │  │     │  │  │  │  ├─ x25519.py
│  │  │  │     │  │  │  │  ├─ x448.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ dh.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ dsa.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ec.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ed25519.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ed448.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ padding.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ rsa.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ types.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ x25519.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ x448.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ ciphers
│  │  │  │     │  │  │  │  ├─ aead.py
│  │  │  │     │  │  │  │  ├─ algorithms.py
│  │  │  │     │  │  │  │  ├─ base.py
│  │  │  │     │  │  │  │  ├─ modes.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ aead.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ algorithms.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ modes.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ cmac.py
│  │  │  │     │  │  │  ├─ constant_time.py
│  │  │  │     │  │  │  ├─ hashes.py
│  │  │  │     │  │  │  ├─ hmac.py
│  │  │  │     │  │  │  ├─ kdf
│  │  │  │     │  │  │  │  ├─ concatkdf.py
│  │  │  │     │  │  │  │  ├─ hkdf.py
│  │  │  │     │  │  │  │  ├─ kbkdf.py
│  │  │  │     │  │  │  │  ├─ pbkdf2.py
│  │  │  │     │  │  │  │  ├─ scrypt.py
│  │  │  │     │  │  │  │  ├─ x963kdf.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ concatkdf.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ hkdf.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ kbkdf.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ pbkdf2.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ scrypt.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ x963kdf.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ keywrap.py
│  │  │  │     │  │  │  ├─ padding.py
│  │  │  │     │  │  │  ├─ poly1305.py
│  │  │  │     │  │  │  ├─ serialization
│  │  │  │     │  │  │  │  ├─ base.py
│  │  │  │     │  │  │  │  ├─ pkcs12.py
│  │  │  │     │  │  │  │  ├─ pkcs7.py
│  │  │  │     │  │  │  │  ├─ ssh.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ pkcs12.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ pkcs7.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ssh.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ twofactor
│  │  │  │     │  │  │  │  ├─ hotp.py
│  │  │  │     │  │  │  │  ├─ totp.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ hotp.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ totp.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _asymmetric.py
│  │  │  │     │  │  │  ├─ _cipheralgorithm.py
│  │  │  │     │  │  │  ├─ _serialization.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ cmac.cpython-310.pyc
│  │  │  │     │  │  │     ├─ constant_time.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hashes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hmac.cpython-310.pyc
│  │  │  │     │  │  │     ├─ keywrap.cpython-310.pyc
│  │  │  │     │  │  │     ├─ padding.cpython-310.pyc
│  │  │  │     │  │  │     ├─ poly1305.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _asymmetric.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _cipheralgorithm.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _serialization.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ _oid.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ _oid.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ x509
│  │  │  │     │  │  ├─ base.py
│  │  │  │     │  │  ├─ certificate_transparency.py
│  │  │  │     │  │  ├─ extensions.py
│  │  │  │     │  │  ├─ general_name.py
│  │  │  │     │  │  ├─ name.py
│  │  │  │     │  │  ├─ ocsp.py
│  │  │  │     │  │  ├─ oid.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │     ├─ certificate_transparency.cpython-310.pyc
│  │  │  │     │  │     ├─ extensions.cpython-310.pyc
│  │  │  │     │  │     ├─ general_name.cpython-310.pyc
│  │  │  │     │  │     ├─ name.cpython-310.pyc
│  │  │  │     │  │     ├─ ocsp.cpython-310.pyc
│  │  │  │     │  │     ├─ oid.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ __about__.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ fernet.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ __about__.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ cryptography-41.0.4.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ LICENSE.APACHE
│  │  │  │     │  ├─ LICENSE.BSD
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ distutils-precedence.pth
│  │  │  │     ├─ idna
│  │  │  │     │  ├─ codec.py
│  │  │  │     │  ├─ compat.py
│  │  │  │     │  ├─ core.py
│  │  │  │     │  ├─ idnadata.py
│  │  │  │     │  ├─ intranges.py
│  │  │  │     │  ├─ package_data.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ uts46data.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ codec.cpython-310.pyc
│  │  │  │     │     ├─ compat.cpython-310.pyc
│  │  │  │     │     ├─ core.cpython-310.pyc
│  │  │  │     │     ├─ idnadata.cpython-310.pyc
│  │  │  │     │     ├─ intranges.cpython-310.pyc
│  │  │  │     │     ├─ package_data.cpython-310.pyc
│  │  │  │     │     ├─ uts46data.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ idna-3.4.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE.md
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ isapi
│  │  │  │     │  ├─ doc
│  │  │  │     │  │  └─ isapi.html
│  │  │  │     │  ├─ install.py
│  │  │  │     │  ├─ isapicon.py
│  │  │  │     │  ├─ PyISAPI_loader.dll
│  │  │  │     │  ├─ README.txt
│  │  │  │     │  ├─ samples
│  │  │  │     │  │  ├─ advanced.py
│  │  │  │     │  │  ├─ README.txt
│  │  │  │     │  │  ├─ redirector.py
│  │  │  │     │  │  ├─ redirector_asynch.py
│  │  │  │     │  │  ├─ redirector_with_filter.py
│  │  │  │     │  │  ├─ test.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ advanced.cpython-310.pyc
│  │  │  │     │  │     ├─ redirector.cpython-310.pyc
│  │  │  │     │  │     ├─ redirector_asynch.cpython-310.pyc
│  │  │  │     │  │     ├─ redirector_with_filter.cpython-310.pyc
│  │  │  │     │  │     └─ test.cpython-310.pyc
│  │  │  │     │  ├─ simple.py
│  │  │  │     │  ├─ test
│  │  │  │     │  │  ├─ extension_simple.py
│  │  │  │     │  │  ├─ README.txt
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ extension_simple.cpython-310.pyc
│  │  │  │     │  ├─ threaded_extension.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ install.cpython-310.pyc
│  │  │  │     │     ├─ isapicon.cpython-310.pyc
│  │  │  │     │     ├─ simple.cpython-310.pyc
│  │  │  │     │     ├─ threaded_extension.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ jwt
│  │  │  │     │  ├─ algorithms.py
│  │  │  │     │  ├─ api_jwk.py
│  │  │  │     │  ├─ api_jws.py
│  │  │  │     │  ├─ api_jwt.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ help.py
│  │  │  │     │  ├─ jwks_client.py
│  │  │  │     │  ├─ jwk_set_cache.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ types.py
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ warnings.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ algorithms.cpython-310.pyc
│  │  │  │     │     ├─ api_jwk.cpython-310.pyc
│  │  │  │     │     ├─ api_jws.cpython-310.pyc
│  │  │  │     │     ├─ api_jwt.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ help.cpython-310.pyc
│  │  │  │     │     ├─ jwks_client.cpython-310.pyc
│  │  │  │     │     ├─ jwk_set_cache.cpython-310.pyc
│  │  │  │     │     ├─ types.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ warnings.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ msal
│  │  │  │     │  ├─ application.py
│  │  │  │     │  ├─ authority.py
│  │  │  │     │  ├─ broker.py
│  │  │  │     │  ├─ cloudshell.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ individual_cache.py
│  │  │  │     │  ├─ mex.py
│  │  │  │     │  ├─ oauth2cli
│  │  │  │     │  │  ├─ assertion.py
│  │  │  │     │  │  ├─ authcode.py
│  │  │  │     │  │  ├─ http.py
│  │  │  │     │  │  ├─ oauth2.py
│  │  │  │     │  │  ├─ oidc.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ assertion.cpython-310.pyc
│  │  │  │     │  │     ├─ authcode.cpython-310.pyc
│  │  │  │     │  │     ├─ http.cpython-310.pyc
│  │  │  │     │  │     ├─ oauth2.cpython-310.pyc
│  │  │  │     │  │     ├─ oidc.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ region.py
│  │  │  │     │  ├─ telemetry.py
│  │  │  │     │  ├─ throttled_http_client.py
│  │  │  │     │  ├─ token_cache.py
│  │  │  │     │  ├─ wstrust_request.py
│  │  │  │     │  ├─ wstrust_response.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ application.cpython-310.pyc
│  │  │  │     │     ├─ authority.cpython-310.pyc
│  │  │  │     │     ├─ broker.cpython-310.pyc
│  │  │  │     │     ├─ cloudshell.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ individual_cache.cpython-310.pyc
│  │  │  │     │     ├─ mex.cpython-310.pyc
│  │  │  │     │     ├─ region.cpython-310.pyc
│  │  │  │     │     ├─ telemetry.cpython-310.pyc
│  │  │  │     │     ├─ throttled_http_client.cpython-310.pyc
│  │  │  │     │     ├─ token_cache.cpython-310.pyc
│  │  │  │     │     ├─ wstrust_request.cpython-310.pyc
│  │  │  │     │     ├─ wstrust_response.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ msal-1.24.1.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ msal_extensions
│  │  │  │     │  ├─ cache_lock.py
│  │  │  │     │  ├─ libsecret.py
│  │  │  │     │  ├─ osx.py
│  │  │  │     │  ├─ persistence.py
│  │  │  │     │  ├─ token_cache.py
│  │  │  │     │  ├─ windows.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ cache_lock.cpython-310.pyc
│  │  │  │     │     ├─ libsecret.cpython-310.pyc
│  │  │  │     │     ├─ osx.cpython-310.pyc
│  │  │  │     │     ├─ persistence.cpython-310.pyc
│  │  │  │     │     ├─ token_cache.cpython-310.pyc
│  │  │  │     │     ├─ windows.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ msal_extensions-1.0.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pip
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ _internal
│  │  │  │     │  │  ├─ build_env.py
│  │  │  │     │  │  ├─ cache.py
│  │  │  │     │  │  ├─ cli
│  │  │  │     │  │  │  ├─ autocompletion.py
│  │  │  │     │  │  │  ├─ base_command.py
│  │  │  │     │  │  │  ├─ cmdoptions.py
│  │  │  │     │  │  │  ├─ command_context.py
│  │  │  │     │  │  │  ├─ main.py
│  │  │  │     │  │  │  ├─ main_parser.py
│  │  │  │     │  │  │  ├─ parser.py
│  │  │  │     │  │  │  ├─ progress_bars.py
│  │  │  │     │  │  │  ├─ req_command.py
│  │  │  │     │  │  │  ├─ spinners.py
│  │  │  │     │  │  │  ├─ status_codes.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ autocompletion.cpython-310.pyc
│  │  │  │     │  │  │     ├─ base_command.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cmdoptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ command_context.cpython-310.pyc
│  │  │  │     │  │  │     ├─ main.cpython-310.pyc
│  │  │  │     │  │  │     ├─ main_parser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ parser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ progress_bars.cpython-310.pyc
│  │  │  │     │  │  │     ├─ req_command.cpython-310.pyc
│  │  │  │     │  │  │     ├─ spinners.cpython-310.pyc
│  │  │  │     │  │  │     ├─ status_codes.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ commands
│  │  │  │     │  │  │  ├─ cache.py
│  │  │  │     │  │  │  ├─ check.py
│  │  │  │     │  │  │  ├─ completion.py
│  │  │  │     │  │  │  ├─ configuration.py
│  │  │  │     │  │  │  ├─ debug.py
│  │  │  │     │  │  │  ├─ download.py
│  │  │  │     │  │  │  ├─ freeze.py
│  │  │  │     │  │  │  ├─ hash.py
│  │  │  │     │  │  │  ├─ help.py
│  │  │  │     │  │  │  ├─ index.py
│  │  │  │     │  │  │  ├─ inspect.py
│  │  │  │     │  │  │  ├─ install.py
│  │  │  │     │  │  │  ├─ list.py
│  │  │  │     │  │  │  ├─ search.py
│  │  │  │     │  │  │  ├─ show.py
│  │  │  │     │  │  │  ├─ uninstall.py
│  │  │  │     │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ cache.cpython-310.pyc
│  │  │  │     │  │  │     ├─ check.cpython-310.pyc
│  │  │  │     │  │  │     ├─ completion.cpython-310.pyc
│  │  │  │     │  │  │     ├─ configuration.cpython-310.pyc
│  │  │  │     │  │  │     ├─ debug.cpython-310.pyc
│  │  │  │     │  │  │     ├─ download.cpython-310.pyc
│  │  │  │     │  │  │     ├─ freeze.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hash.cpython-310.pyc
│  │  │  │     │  │  │     ├─ help.cpython-310.pyc
│  │  │  │     │  │  │     ├─ index.cpython-310.pyc
│  │  │  │     │  │  │     ├─ inspect.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install.cpython-310.pyc
│  │  │  │     │  │  │     ├─ list.cpython-310.pyc
│  │  │  │     │  │  │     ├─ search.cpython-310.pyc
│  │  │  │     │  │  │     ├─ show.cpython-310.pyc
│  │  │  │     │  │  │     ├─ uninstall.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ configuration.py
│  │  │  │     │  │  ├─ distributions
│  │  │  │     │  │  │  ├─ base.py
│  │  │  │     │  │  │  ├─ installed.py
│  │  │  │     │  │  │  ├─ sdist.py
│  │  │  │     │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ installed.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sdist.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ exceptions.py
│  │  │  │     │  │  ├─ index
│  │  │  │     │  │  │  ├─ collector.py
│  │  │  │     │  │  │  ├─ package_finder.py
│  │  │  │     │  │  │  ├─ sources.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ collector.cpython-310.pyc
│  │  │  │     │  │  │     ├─ package_finder.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sources.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ locations
│  │  │  │     │  │  │  ├─ base.py
│  │  │  │     │  │  │  ├─ _distutils.py
│  │  │  │     │  │  │  ├─ _sysconfig.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _distutils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _sysconfig.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ main.py
│  │  │  │     │  │  ├─ metadata
│  │  │  │     │  │  │  ├─ base.py
│  │  │  │     │  │  │  ├─ importlib
│  │  │  │     │  │  │  │  ├─ _compat.py
│  │  │  │     │  │  │  │  ├─ _dists.py
│  │  │  │     │  │  │  │  ├─ _envs.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ _compat.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _dists.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _envs.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ pkg_resources.py
│  │  │  │     │  │  │  ├─ _json.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pkg_resources.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _json.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ models
│  │  │  │     │  │  │  ├─ candidate.py
│  │  │  │     │  │  │  ├─ direct_url.py
│  │  │  │     │  │  │  ├─ format_control.py
│  │  │  │     │  │  │  ├─ index.py
│  │  │  │     │  │  │  ├─ installation_report.py
│  │  │  │     │  │  │  ├─ link.py
│  │  │  │     │  │  │  ├─ scheme.py
│  │  │  │     │  │  │  ├─ search_scope.py
│  │  │  │     │  │  │  ├─ selection_prefs.py
│  │  │  │     │  │  │  ├─ target_python.py
│  │  │  │     │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ candidate.cpython-310.pyc
│  │  │  │     │  │  │     ├─ direct_url.cpython-310.pyc
│  │  │  │     │  │  │     ├─ format_control.cpython-310.pyc
│  │  │  │     │  │  │     ├─ index.cpython-310.pyc
│  │  │  │     │  │  │     ├─ installation_report.cpython-310.pyc
│  │  │  │     │  │  │     ├─ link.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scheme.cpython-310.pyc
│  │  │  │     │  │  │     ├─ search_scope.cpython-310.pyc
│  │  │  │     │  │  │     ├─ selection_prefs.cpython-310.pyc
│  │  │  │     │  │  │     ├─ target_python.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ network
│  │  │  │     │  │  │  ├─ auth.py
│  │  │  │     │  │  │  ├─ cache.py
│  │  │  │     │  │  │  ├─ download.py
│  │  │  │     │  │  │  ├─ lazy_wheel.py
│  │  │  │     │  │  │  ├─ session.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ xmlrpc.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ auth.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cache.cpython-310.pyc
│  │  │  │     │  │  │     ├─ download.cpython-310.pyc
│  │  │  │     │  │  │     ├─ lazy_wheel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ session.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ xmlrpc.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ operations
│  │  │  │     │  │  │  ├─ build
│  │  │  │     │  │  │  │  ├─ build_tracker.py
│  │  │  │     │  │  │  │  ├─ metadata.py
│  │  │  │     │  │  │  │  ├─ metadata_editable.py
│  │  │  │     │  │  │  │  ├─ metadata_legacy.py
│  │  │  │     │  │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  │  ├─ wheel_editable.py
│  │  │  │     │  │  │  │  ├─ wheel_legacy.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ build_tracker.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ metadata.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ metadata_editable.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ metadata_legacy.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ wheel_editable.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ wheel_legacy.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ check.py
│  │  │  │     │  │  │  ├─ freeze.py
│  │  │  │     │  │  │  ├─ install
│  │  │  │     │  │  │  │  ├─ editable_legacy.py
│  │  │  │     │  │  │  │  ├─ legacy.py
│  │  │  │     │  │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ editable_legacy.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ legacy.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ prepare.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ check.cpython-310.pyc
│  │  │  │     │  │  │     ├─ freeze.cpython-310.pyc
│  │  │  │     │  │  │     ├─ prepare.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ pyproject.py
│  │  │  │     │  │  ├─ req
│  │  │  │     │  │  │  ├─ constructors.py
│  │  │  │     │  │  │  ├─ req_file.py
│  │  │  │     │  │  │  ├─ req_install.py
│  │  │  │     │  │  │  ├─ req_set.py
│  │  │  │     │  │  │  ├─ req_uninstall.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ constructors.cpython-310.pyc
│  │  │  │     │  │  │     ├─ req_file.cpython-310.pyc
│  │  │  │     │  │  │     ├─ req_install.cpython-310.pyc
│  │  │  │     │  │  │     ├─ req_set.cpython-310.pyc
│  │  │  │     │  │  │     ├─ req_uninstall.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ resolution
│  │  │  │     │  │  │  ├─ base.py
│  │  │  │     │  │  │  ├─ legacy
│  │  │  │     │  │  │  │  ├─ resolver.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ resolver.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ resolvelib
│  │  │  │     │  │  │  │  ├─ base.py
│  │  │  │     │  │  │  │  ├─ candidates.py
│  │  │  │     │  │  │  │  ├─ factory.py
│  │  │  │     │  │  │  │  ├─ found_candidates.py
│  │  │  │     │  │  │  │  ├─ provider.py
│  │  │  │     │  │  │  │  ├─ reporter.py
│  │  │  │     │  │  │  │  ├─ requirements.py
│  │  │  │     │  │  │  │  ├─ resolver.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ candidates.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ factory.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ found_candidates.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ provider.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ reporter.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ requirements.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ resolver.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ self_outdated_check.py
│  │  │  │     │  │  ├─ utils
│  │  │  │     │  │  │  ├─ appdirs.py
│  │  │  │     │  │  │  ├─ compat.py
│  │  │  │     │  │  │  ├─ compatibility_tags.py
│  │  │  │     │  │  │  ├─ datetime.py
│  │  │  │     │  │  │  ├─ deprecation.py
│  │  │  │     │  │  │  ├─ direct_url_helpers.py
│  │  │  │     │  │  │  ├─ distutils_args.py
│  │  │  │     │  │  │  ├─ egg_link.py
│  │  │  │     │  │  │  ├─ encoding.py
│  │  │  │     │  │  │  ├─ entrypoints.py
│  │  │  │     │  │  │  ├─ filesystem.py
│  │  │  │     │  │  │  ├─ filetypes.py
│  │  │  │     │  │  │  ├─ glibc.py
│  │  │  │     │  │  │  ├─ hashes.py
│  │  │  │     │  │  │  ├─ inject_securetransport.py
│  │  │  │     │  │  │  ├─ logging.py
│  │  │  │     │  │  │  ├─ misc.py
│  │  │  │     │  │  │  ├─ models.py
│  │  │  │     │  │  │  ├─ packaging.py
│  │  │  │     │  │  │  ├─ setuptools_build.py
│  │  │  │     │  │  │  ├─ subprocess.py
│  │  │  │     │  │  │  ├─ temp_dir.py
│  │  │  │     │  │  │  ├─ unpacking.py
│  │  │  │     │  │  │  ├─ urls.py
│  │  │  │     │  │  │  ├─ virtualenv.py
│  │  │  │     │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  ├─ _log.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ appdirs.cpython-310.pyc
│  │  │  │     │  │  │     ├─ compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ compatibility_tags.cpython-310.pyc
│  │  │  │     │  │  │     ├─ datetime.cpython-310.pyc
│  │  │  │     │  │  │     ├─ deprecation.cpython-310.pyc
│  │  │  │     │  │  │     ├─ direct_url_helpers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ distutils_args.cpython-310.pyc
│  │  │  │     │  │  │     ├─ egg_link.cpython-310.pyc
│  │  │  │     │  │  │     ├─ encoding.cpython-310.pyc
│  │  │  │     │  │  │     ├─ entrypoints.cpython-310.pyc
│  │  │  │     │  │  │     ├─ filesystem.cpython-310.pyc
│  │  │  │     │  │  │     ├─ filetypes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ glibc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hashes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ inject_securetransport.cpython-310.pyc
│  │  │  │     │  │  │     ├─ logging.cpython-310.pyc
│  │  │  │     │  │  │     ├─ misc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ models.cpython-310.pyc
│  │  │  │     │  │  │     ├─ packaging.cpython-310.pyc
│  │  │  │     │  │  │     ├─ setuptools_build.cpython-310.pyc
│  │  │  │     │  │  │     ├─ subprocess.cpython-310.pyc
│  │  │  │     │  │  │     ├─ temp_dir.cpython-310.pyc
│  │  │  │     │  │  │     ├─ unpacking.cpython-310.pyc
│  │  │  │     │  │  │     ├─ urls.cpython-310.pyc
│  │  │  │     │  │  │     ├─ virtualenv.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _log.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ vcs
│  │  │  │     │  │  │  ├─ bazaar.py
│  │  │  │     │  │  │  ├─ git.py
│  │  │  │     │  │  │  ├─ mercurial.py
│  │  │  │     │  │  │  ├─ subversion.py
│  │  │  │     │  │  │  ├─ versioncontrol.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ bazaar.cpython-310.pyc
│  │  │  │     │  │  │     ├─ git.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mercurial.cpython-310.pyc
│  │  │  │     │  │  │     ├─ subversion.cpython-310.pyc
│  │  │  │     │  │  │     ├─ versioncontrol.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ wheel_builder.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ build_env.cpython-310.pyc
│  │  │  │     │  │     ├─ cache.cpython-310.pyc
│  │  │  │     │  │     ├─ configuration.cpython-310.pyc
│  │  │  │     │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │     ├─ main.cpython-310.pyc
│  │  │  │     │  │     ├─ pyproject.cpython-310.pyc
│  │  │  │     │  │     ├─ self_outdated_check.cpython-310.pyc
│  │  │  │     │  │     ├─ wheel_builder.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _vendor
│  │  │  │     │  │  ├─ cachecontrol
│  │  │  │     │  │  │  ├─ adapter.py
│  │  │  │     │  │  │  ├─ cache.py
│  │  │  │     │  │  │  ├─ caches
│  │  │  │     │  │  │  │  ├─ file_cache.py
│  │  │  │     │  │  │  │  ├─ redis_cache.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ file_cache.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ redis_cache.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ compat.py
│  │  │  │     │  │  │  ├─ controller.py
│  │  │  │     │  │  │  ├─ filewrapper.py
│  │  │  │     │  │  │  ├─ heuristics.py
│  │  │  │     │  │  │  ├─ serialize.py
│  │  │  │     │  │  │  ├─ wrapper.py
│  │  │  │     │  │  │  ├─ _cmd.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ adapter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cache.cpython-310.pyc
│  │  │  │     │  │  │     ├─ compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ controller.cpython-310.pyc
│  │  │  │     │  │  │     ├─ filewrapper.cpython-310.pyc
│  │  │  │     │  │  │     ├─ heuristics.cpython-310.pyc
│  │  │  │     │  │  │     ├─ serialize.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wrapper.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _cmd.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ certifi
│  │  │  │     │  │  │  ├─ cacert.pem
│  │  │  │     │  │  │  ├─ core.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  ├─ __main__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __main__.cpython-310.pyc
│  │  │  │     │  │  ├─ chardet
│  │  │  │     │  │  │  ├─ big5freq.py
│  │  │  │     │  │  │  ├─ big5prober.py
│  │  │  │     │  │  │  ├─ chardistribution.py
│  │  │  │     │  │  │  ├─ charsetgroupprober.py
│  │  │  │     │  │  │  ├─ charsetprober.py
│  │  │  │     │  │  │  ├─ cli
│  │  │  │     │  │  │  │  ├─ chardetect.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ chardetect.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ codingstatemachine.py
│  │  │  │     │  │  │  ├─ cp949prober.py
│  │  │  │     │  │  │  ├─ enums.py
│  │  │  │     │  │  │  ├─ escprober.py
│  │  │  │     │  │  │  ├─ escsm.py
│  │  │  │     │  │  │  ├─ eucjpprober.py
│  │  │  │     │  │  │  ├─ euckrfreq.py
│  │  │  │     │  │  │  ├─ euckrprober.py
│  │  │  │     │  │  │  ├─ euctwfreq.py
│  │  │  │     │  │  │  ├─ euctwprober.py
│  │  │  │     │  │  │  ├─ gb2312freq.py
│  │  │  │     │  │  │  ├─ gb2312prober.py
│  │  │  │     │  │  │  ├─ hebrewprober.py
│  │  │  │     │  │  │  ├─ jisfreq.py
│  │  │  │     │  │  │  ├─ johabfreq.py
│  │  │  │     │  │  │  ├─ johabprober.py
│  │  │  │     │  │  │  ├─ jpcntx.py
│  │  │  │     │  │  │  ├─ langbulgarianmodel.py
│  │  │  │     │  │  │  ├─ langgreekmodel.py
│  │  │  │     │  │  │  ├─ langhebrewmodel.py
│  │  │  │     │  │  │  ├─ langhungarianmodel.py
│  │  │  │     │  │  │  ├─ langrussianmodel.py
│  │  │  │     │  │  │  ├─ langthaimodel.py
│  │  │  │     │  │  │  ├─ langturkishmodel.py
│  │  │  │     │  │  │  ├─ latin1prober.py
│  │  │  │     │  │  │  ├─ mbcharsetprober.py
│  │  │  │     │  │  │  ├─ mbcsgroupprober.py
│  │  │  │     │  │  │  ├─ mbcssm.py
│  │  │  │     │  │  │  ├─ metadata
│  │  │  │     │  │  │  │  ├─ languages.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ languages.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ sbcharsetprober.py
│  │  │  │     │  │  │  ├─ sbcsgroupprober.py
│  │  │  │     │  │  │  ├─ sjisprober.py
│  │  │  │     │  │  │  ├─ universaldetector.py
│  │  │  │     │  │  │  ├─ utf1632prober.py
│  │  │  │     │  │  │  ├─ utf8prober.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ big5freq.cpython-310.pyc
│  │  │  │     │  │  │     ├─ big5prober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ chardistribution.cpython-310.pyc
│  │  │  │     │  │  │     ├─ charsetgroupprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ charsetprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ codingstatemachine.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cp949prober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ enums.cpython-310.pyc
│  │  │  │     │  │  │     ├─ escprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ escsm.cpython-310.pyc
│  │  │  │     │  │  │     ├─ eucjpprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ euckrfreq.cpython-310.pyc
│  │  │  │     │  │  │     ├─ euckrprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ euctwfreq.cpython-310.pyc
│  │  │  │     │  │  │     ├─ euctwprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ gb2312freq.cpython-310.pyc
│  │  │  │     │  │  │     ├─ gb2312prober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hebrewprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ jisfreq.cpython-310.pyc
│  │  │  │     │  │  │     ├─ johabfreq.cpython-310.pyc
│  │  │  │     │  │  │     ├─ johabprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ jpcntx.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langbulgarianmodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langgreekmodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langhebrewmodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langhungarianmodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langrussianmodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langthaimodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langturkishmodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ latin1prober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mbcharsetprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mbcsgroupprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mbcssm.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sbcharsetprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sbcsgroupprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sjisprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ universaldetector.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utf1632prober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utf8prober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ colorama
│  │  │  │     │  │  │  ├─ ansi.py
│  │  │  │     │  │  │  ├─ ansitowin32.py
│  │  │  │     │  │  │  ├─ initialise.py
│  │  │  │     │  │  │  ├─ win32.py
│  │  │  │     │  │  │  ├─ winterm.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ ansi.cpython-310.pyc
│  │  │  │     │  │  │     ├─ ansitowin32.cpython-310.pyc
│  │  │  │     │  │  │     ├─ initialise.cpython-310.pyc
│  │  │  │     │  │  │     ├─ win32.cpython-310.pyc
│  │  │  │     │  │  │     ├─ winterm.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ distlib
│  │  │  │     │  │  │  ├─ compat.py
│  │  │  │     │  │  │  ├─ database.py
│  │  │  │     │  │  │  ├─ index.py
│  │  │  │     │  │  │  ├─ locators.py
│  │  │  │     │  │  │  ├─ manifest.py
│  │  │  │     │  │  │  ├─ markers.py
│  │  │  │     │  │  │  ├─ metadata.py
│  │  │  │     │  │  │  ├─ resources.py
│  │  │  │     │  │  │  ├─ scripts.py
│  │  │  │     │  │  │  ├─ t32.exe
│  │  │  │     │  │  │  ├─ t64-arm.exe
│  │  │  │     │  │  │  ├─ t64.exe
│  │  │  │     │  │  │  ├─ util.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ w32.exe
│  │  │  │     │  │  │  ├─ w64-arm.exe
│  │  │  │     │  │  │  ├─ w64.exe
│  │  │  │     │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ database.cpython-310.pyc
│  │  │  │     │  │  │     ├─ index.cpython-310.pyc
│  │  │  │     │  │  │     ├─ locators.cpython-310.pyc
│  │  │  │     │  │  │     ├─ manifest.cpython-310.pyc
│  │  │  │     │  │  │     ├─ markers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ metadata.cpython-310.pyc
│  │  │  │     │  │  │     ├─ resources.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scripts.cpython-310.pyc
│  │  │  │     │  │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ distro
│  │  │  │     │  │  │  ├─ distro.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  ├─ __main__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ distro.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __main__.cpython-310.pyc
│  │  │  │     │  │  ├─ idna
│  │  │  │     │  │  │  ├─ codec.py
│  │  │  │     │  │  │  ├─ compat.py
│  │  │  │     │  │  │  ├─ core.py
│  │  │  │     │  │  │  ├─ idnadata.py
│  │  │  │     │  │  │  ├─ intranges.py
│  │  │  │     │  │  │  ├─ package_data.py
│  │  │  │     │  │  │  ├─ uts46data.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ codec.cpython-310.pyc
│  │  │  │     │  │  │     ├─ compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │  │     ├─ idnadata.cpython-310.pyc
│  │  │  │     │  │  │     ├─ intranges.cpython-310.pyc
│  │  │  │     │  │  │     ├─ package_data.cpython-310.pyc
│  │  │  │     │  │  │     ├─ uts46data.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ msgpack
│  │  │  │     │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  ├─ ext.py
│  │  │  │     │  │  │  ├─ fallback.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ ext.cpython-310.pyc
│  │  │  │     │  │  │     ├─ fallback.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ packaging
│  │  │  │     │  │  │  ├─ markers.py
│  │  │  │     │  │  │  ├─ requirements.py
│  │  │  │     │  │  │  ├─ specifiers.py
│  │  │  │     │  │  │  ├─ tags.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ _manylinux.py
│  │  │  │     │  │  │  ├─ _musllinux.py
│  │  │  │     │  │  │  ├─ _structures.py
│  │  │  │     │  │  │  ├─ __about__.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ markers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ requirements.cpython-310.pyc
│  │  │  │     │  │  │     ├─ specifiers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tags.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _manylinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _musllinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _structures.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __about__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ pep517
│  │  │  │     │  │  │  ├─ build.py
│  │  │  │     │  │  │  ├─ check.py
│  │  │  │     │  │  │  ├─ colorlog.py
│  │  │  │     │  │  │  ├─ dirtools.py
│  │  │  │     │  │  │  ├─ envbuild.py
│  │  │  │     │  │  │  ├─ in_process
│  │  │  │     │  │  │  │  ├─ _in_process.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ _in_process.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ meta.py
│  │  │  │     │  │  │  ├─ wrappers.py
│  │  │  │     │  │  │  ├─ _compat.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ build.cpython-310.pyc
│  │  │  │     │  │  │     ├─ check.cpython-310.pyc
│  │  │  │     │  │  │     ├─ colorlog.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dirtools.cpython-310.pyc
│  │  │  │     │  │  │     ├─ envbuild.cpython-310.pyc
│  │  │  │     │  │  │     ├─ meta.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wrappers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _compat.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ pkg_resources
│  │  │  │     │  │  │  ├─ py31compat.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ py31compat.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ platformdirs
│  │  │  │     │  │  │  ├─ android.py
│  │  │  │     │  │  │  ├─ api.py
│  │  │  │     │  │  │  ├─ macos.py
│  │  │  │     │  │  │  ├─ unix.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ windows.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  ├─ __main__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ android.cpython-310.pyc
│  │  │  │     │  │  │     ├─ api.cpython-310.pyc
│  │  │  │     │  │  │     ├─ macos.cpython-310.pyc
│  │  │  │     │  │  │     ├─ unix.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     ├─ windows.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __main__.cpython-310.pyc
│  │  │  │     │  │  ├─ pygments
│  │  │  │     │  │  │  ├─ cmdline.py
│  │  │  │     │  │  │  ├─ console.py
│  │  │  │     │  │  │  ├─ filter.py
│  │  │  │     │  │  │  ├─ filters
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ formatter.py
│  │  │  │     │  │  │  ├─ formatters
│  │  │  │     │  │  │  │  ├─ bbcode.py
│  │  │  │     │  │  │  │  ├─ groff.py
│  │  │  │     │  │  │  │  ├─ html.py
│  │  │  │     │  │  │  │  ├─ img.py
│  │  │  │     │  │  │  │  ├─ irc.py
│  │  │  │     │  │  │  │  ├─ latex.py
│  │  │  │     │  │  │  │  ├─ other.py
│  │  │  │     │  │  │  │  ├─ pangomarkup.py
│  │  │  │     │  │  │  │  ├─ rtf.py
│  │  │  │     │  │  │  │  ├─ svg.py
│  │  │  │     │  │  │  │  ├─ terminal.py
│  │  │  │     │  │  │  │  ├─ terminal256.py
│  │  │  │     │  │  │  │  ├─ _mapping.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ bbcode.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ groff.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ html.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ img.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ irc.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ latex.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ other.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ pangomarkup.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ rtf.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ svg.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ terminal.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ terminal256.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _mapping.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ lexer.py
│  │  │  │     │  │  │  ├─ lexers
│  │  │  │     │  │  │  │  ├─ python.py
│  │  │  │     │  │  │  │  ├─ _mapping.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ python.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _mapping.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ modeline.py
│  │  │  │     │  │  │  ├─ plugin.py
│  │  │  │     │  │  │  ├─ regexopt.py
│  │  │  │     │  │  │  ├─ scanner.py
│  │  │  │     │  │  │  ├─ sphinxext.py
│  │  │  │     │  │  │  ├─ style.py
│  │  │  │     │  │  │  ├─ styles
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ token.py
│  │  │  │     │  │  │  ├─ unistring.py
│  │  │  │     │  │  │  ├─ util.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  ├─ __main__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ cmdline.cpython-310.pyc
│  │  │  │     │  │  │     ├─ console.cpython-310.pyc
│  │  │  │     │  │  │     ├─ filter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ formatter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ lexer.cpython-310.pyc
│  │  │  │     │  │  │     ├─ modeline.cpython-310.pyc
│  │  │  │     │  │  │     ├─ plugin.cpython-310.pyc
│  │  │  │     │  │  │     ├─ regexopt.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scanner.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sphinxext.cpython-310.pyc
│  │  │  │     │  │  │     ├─ style.cpython-310.pyc
│  │  │  │     │  │  │     ├─ token.cpython-310.pyc
│  │  │  │     │  │  │     ├─ unistring.cpython-310.pyc
│  │  │  │     │  │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __main__.cpython-310.pyc
│  │  │  │     │  │  ├─ pyparsing
│  │  │  │     │  │  │  ├─ actions.py
│  │  │  │     │  │  │  ├─ common.py
│  │  │  │     │  │  │  ├─ core.py
│  │  │  │     │  │  │  ├─ diagram
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  ├─ helpers.py
│  │  │  │     │  │  │  ├─ results.py
│  │  │  │     │  │  │  ├─ testing.py
│  │  │  │     │  │  │  ├─ unicode.py
│  │  │  │     │  │  │  ├─ util.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ actions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ common.cpython-310.pyc
│  │  │  │     │  │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ helpers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ results.cpython-310.pyc
│  │  │  │     │  │  │     ├─ testing.cpython-310.pyc
│  │  │  │     │  │  │     ├─ unicode.cpython-310.pyc
│  │  │  │     │  │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ requests
│  │  │  │     │  │  │  ├─ adapters.py
│  │  │  │     │  │  │  ├─ api.py
│  │  │  │     │  │  │  ├─ auth.py
│  │  │  │     │  │  │  ├─ certs.py
│  │  │  │     │  │  │  ├─ compat.py
│  │  │  │     │  │  │  ├─ cookies.py
│  │  │  │     │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  ├─ help.py
│  │  │  │     │  │  │  ├─ models.py
│  │  │  │     │  │  │  ├─ packages.py
│  │  │  │     │  │  │  ├─ sessions.py
│  │  │  │     │  │  │  ├─ status_codes.py
│  │  │  │     │  │  │  ├─ structures.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ _internal_utils.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  ├─ __pycache__
│  │  │  │     │  │  │  │  ├─ adapters.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ api.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ auth.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ certs.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ compat.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ cookies.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ help.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ models.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ packages.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ sessions.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ status_codes.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ structures.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ _internal_utils.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  │  └─ __version__.cpython-310.pyc
│  │  │  │     │  │  │  └─ __version__.py
│  │  │  │     │  │  ├─ resolvelib
│  │  │  │     │  │  │  ├─ compat
│  │  │  │     │  │  │  │  ├─ collections_abc.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ collections_abc.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ providers.py
│  │  │  │     │  │  │  ├─ reporters.py
│  │  │  │     │  │  │  ├─ resolvers.py
│  │  │  │     │  │  │  ├─ structs.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ providers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ reporters.cpython-310.pyc
│  │  │  │     │  │  │     ├─ resolvers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ structs.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ rich
│  │  │  │     │  │  │  ├─ abc.py
│  │  │  │     │  │  │  ├─ align.py
│  │  │  │     │  │  │  ├─ ansi.py
│  │  │  │     │  │  │  ├─ bar.py
│  │  │  │     │  │  │  ├─ box.py
│  │  │  │     │  │  │  ├─ cells.py
│  │  │  │     │  │  │  ├─ color.py
│  │  │  │     │  │  │  ├─ color_triplet.py
│  │  │  │     │  │  │  ├─ columns.py
│  │  │  │     │  │  │  ├─ console.py
│  │  │  │     │  │  │  ├─ constrain.py
│  │  │  │     │  │  │  ├─ containers.py
│  │  │  │     │  │  │  ├─ control.py
│  │  │  │     │  │  │  ├─ default_styles.py
│  │  │  │     │  │  │  ├─ diagnose.py
│  │  │  │     │  │  │  ├─ emoji.py
│  │  │  │     │  │  │  ├─ errors.py
│  │  │  │     │  │  │  ├─ filesize.py
│  │  │  │     │  │  │  ├─ file_proxy.py
│  │  │  │     │  │  │  ├─ highlighter.py
│  │  │  │     │  │  │  ├─ json.py
│  │  │  │     │  │  │  ├─ jupyter.py
│  │  │  │     │  │  │  ├─ layout.py
│  │  │  │     │  │  │  ├─ live.py
│  │  │  │     │  │  │  ├─ live_render.py
│  │  │  │     │  │  │  ├─ logging.py
│  │  │  │     │  │  │  ├─ markup.py
│  │  │  │     │  │  │  ├─ measure.py
│  │  │  │     │  │  │  ├─ padding.py
│  │  │  │     │  │  │  ├─ pager.py
│  │  │  │     │  │  │  ├─ palette.py
│  │  │  │     │  │  │  ├─ panel.py
│  │  │  │     │  │  │  ├─ pretty.py
│  │  │  │     │  │  │  ├─ progress.py
│  │  │  │     │  │  │  ├─ progress_bar.py
│  │  │  │     │  │  │  ├─ prompt.py
│  │  │  │     │  │  │  ├─ protocol.py
│  │  │  │     │  │  │  ├─ region.py
│  │  │  │     │  │  │  ├─ repr.py
│  │  │  │     │  │  │  ├─ rule.py
│  │  │  │     │  │  │  ├─ scope.py
│  │  │  │     │  │  │  ├─ screen.py
│  │  │  │     │  │  │  ├─ segment.py
│  │  │  │     │  │  │  ├─ spinner.py
│  │  │  │     │  │  │  ├─ status.py
│  │  │  │     │  │  │  ├─ style.py
│  │  │  │     │  │  │  ├─ styled.py
│  │  │  │     │  │  │  ├─ syntax.py
│  │  │  │     │  │  │  ├─ table.py
│  │  │  │     │  │  │  ├─ terminal_theme.py
│  │  │  │     │  │  │  ├─ text.py
│  │  │  │     │  │  │  ├─ theme.py
│  │  │  │     │  │  │  ├─ themes.py
│  │  │  │     │  │  │  ├─ traceback.py
│  │  │  │     │  │  │  ├─ tree.py
│  │  │  │     │  │  │  ├─ _cell_widths.py
│  │  │  │     │  │  │  ├─ _emoji_codes.py
│  │  │  │     │  │  │  ├─ _emoji_replace.py
│  │  │  │     │  │  │  ├─ _export_format.py
│  │  │  │     │  │  │  ├─ _extension.py
│  │  │  │     │  │  │  ├─ _inspect.py
│  │  │  │     │  │  │  ├─ _log_render.py
│  │  │  │     │  │  │  ├─ _loop.py
│  │  │  │     │  │  │  ├─ _palettes.py
│  │  │  │     │  │  │  ├─ _pick.py
│  │  │  │     │  │  │  ├─ _ratio.py
│  │  │  │     │  │  │  ├─ _spinners.py
│  │  │  │     │  │  │  ├─ _stack.py
│  │  │  │     │  │  │  ├─ _timer.py
│  │  │  │     │  │  │  ├─ _win32_console.py
│  │  │  │     │  │  │  ├─ _windows.py
│  │  │  │     │  │  │  ├─ _windows_renderer.py
│  │  │  │     │  │  │  ├─ _wrap.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  ├─ __main__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ abc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ align.cpython-310.pyc
│  │  │  │     │  │  │     ├─ ansi.cpython-310.pyc
│  │  │  │     │  │  │     ├─ bar.cpython-310.pyc
│  │  │  │     │  │  │     ├─ box.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cells.cpython-310.pyc
│  │  │  │     │  │  │     ├─ color.cpython-310.pyc
│  │  │  │     │  │  │     ├─ color_triplet.cpython-310.pyc
│  │  │  │     │  │  │     ├─ columns.cpython-310.pyc
│  │  │  │     │  │  │     ├─ console.cpython-310.pyc
│  │  │  │     │  │  │     ├─ constrain.cpython-310.pyc
│  │  │  │     │  │  │     ├─ containers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ control.cpython-310.pyc
│  │  │  │     │  │  │     ├─ default_styles.cpython-310.pyc
│  │  │  │     │  │  │     ├─ diagnose.cpython-310.pyc
│  │  │  │     │  │  │     ├─ emoji.cpython-310.pyc
│  │  │  │     │  │  │     ├─ errors.cpython-310.pyc
│  │  │  │     │  │  │     ├─ filesize.cpython-310.pyc
│  │  │  │     │  │  │     ├─ file_proxy.cpython-310.pyc
│  │  │  │     │  │  │     ├─ highlighter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ json.cpython-310.pyc
│  │  │  │     │  │  │     ├─ jupyter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ layout.cpython-310.pyc
│  │  │  │     │  │  │     ├─ live.cpython-310.pyc
│  │  │  │     │  │  │     ├─ live_render.cpython-310.pyc
│  │  │  │     │  │  │     ├─ logging.cpython-310.pyc
│  │  │  │     │  │  │     ├─ markup.cpython-310.pyc
│  │  │  │     │  │  │     ├─ measure.cpython-310.pyc
│  │  │  │     │  │  │     ├─ padding.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pager.cpython-310.pyc
│  │  │  │     │  │  │     ├─ palette.cpython-310.pyc
│  │  │  │     │  │  │     ├─ panel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pretty.cpython-310.pyc
│  │  │  │     │  │  │     ├─ progress.cpython-310.pyc
│  │  │  │     │  │  │     ├─ progress_bar.cpython-310.pyc
│  │  │  │     │  │  │     ├─ prompt.cpython-310.pyc
│  │  │  │     │  │  │     ├─ protocol.cpython-310.pyc
│  │  │  │     │  │  │     ├─ region.cpython-310.pyc
│  │  │  │     │  │  │     ├─ repr.cpython-310.pyc
│  │  │  │     │  │  │     ├─ rule.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scope.cpython-310.pyc
│  │  │  │     │  │  │     ├─ screen.cpython-310.pyc
│  │  │  │     │  │  │     ├─ segment.cpython-310.pyc
│  │  │  │     │  │  │     ├─ spinner.cpython-310.pyc
│  │  │  │     │  │  │     ├─ status.cpython-310.pyc
│  │  │  │     │  │  │     ├─ style.cpython-310.pyc
│  │  │  │     │  │  │     ├─ styled.cpython-310.pyc
│  │  │  │     │  │  │     ├─ syntax.cpython-310.pyc
│  │  │  │     │  │  │     ├─ table.cpython-310.pyc
│  │  │  │     │  │  │     ├─ terminal_theme.cpython-310.pyc
│  │  │  │     │  │  │     ├─ text.cpython-310.pyc
│  │  │  │     │  │  │     ├─ theme.cpython-310.pyc
│  │  │  │     │  │  │     ├─ themes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ traceback.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tree.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _cell_widths.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _emoji_codes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _emoji_replace.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _export_format.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _extension.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _inspect.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _log_render.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _loop.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _palettes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _pick.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _ratio.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _spinners.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _stack.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _timer.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _win32_console.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _windows.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _windows_renderer.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _wrap.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __main__.cpython-310.pyc
│  │  │  │     │  │  ├─ six.py
│  │  │  │     │  │  ├─ tenacity
│  │  │  │     │  │  │  ├─ after.py
│  │  │  │     │  │  │  ├─ before.py
│  │  │  │     │  │  │  ├─ before_sleep.py
│  │  │  │     │  │  │  ├─ nap.py
│  │  │  │     │  │  │  ├─ retry.py
│  │  │  │     │  │  │  ├─ stop.py
│  │  │  │     │  │  │  ├─ tornadoweb.py
│  │  │  │     │  │  │  ├─ wait.py
│  │  │  │     │  │  │  ├─ _asyncio.py
│  │  │  │     │  │  │  ├─ _utils.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ after.cpython-310.pyc
│  │  │  │     │  │  │     ├─ before.cpython-310.pyc
│  │  │  │     │  │  │     ├─ before_sleep.cpython-310.pyc
│  │  │  │     │  │  │     ├─ nap.cpython-310.pyc
│  │  │  │     │  │  │     ├─ retry.cpython-310.pyc
│  │  │  │     │  │  │     ├─ stop.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tornadoweb.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wait.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _asyncio.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _utils.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ tomli
│  │  │  │     │  │  │  ├─ _parser.py
│  │  │  │     │  │  │  ├─ _re.py
│  │  │  │     │  │  │  ├─ _types.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _parser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _re.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _types.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ typing_extensions.py
│  │  │  │     │  │  ├─ urllib3
│  │  │  │     │  │  │  ├─ connection.py
│  │  │  │     │  │  │  ├─ connectionpool.py
│  │  │  │     │  │  │  ├─ contrib
│  │  │  │     │  │  │  │  ├─ appengine.py
│  │  │  │     │  │  │  │  ├─ ntlmpool.py
│  │  │  │     │  │  │  │  ├─ pyopenssl.py
│  │  │  │     │  │  │  │  ├─ securetransport.py
│  │  │  │     │  │  │  │  ├─ socks.py
│  │  │  │     │  │  │  │  ├─ _appengine_environ.py
│  │  │  │     │  │  │  │  ├─ _securetransport
│  │  │  │     │  │  │  │  │  ├─ bindings.py
│  │  │  │     │  │  │  │  │  ├─ low_level.py
│  │  │  │     │  │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │  │     ├─ bindings.cpython-310.pyc
│  │  │  │     │  │  │  │  │     ├─ low_level.cpython-310.pyc
│  │  │  │     │  │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ appengine.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ntlmpool.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ pyopenssl.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ securetransport.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ socks.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _appengine_environ.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  ├─ fields.py
│  │  │  │     │  │  │  ├─ filepost.py
│  │  │  │     │  │  │  ├─ packages
│  │  │  │     │  │  │  │  ├─ backports
│  │  │  │     │  │  │  │  │  ├─ makefile.py
│  │  │  │     │  │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │  │     ├─ makefile.cpython-310.pyc
│  │  │  │     │  │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ six.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ six.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ poolmanager.py
│  │  │  │     │  │  │  ├─ request.py
│  │  │  │     │  │  │  ├─ response.py
│  │  │  │     │  │  │  ├─ util
│  │  │  │     │  │  │  │  ├─ connection.py
│  │  │  │     │  │  │  │  ├─ proxy.py
│  │  │  │     │  │  │  │  ├─ queue.py
│  │  │  │     │  │  │  │  ├─ request.py
│  │  │  │     │  │  │  │  ├─ response.py
│  │  │  │     │  │  │  │  ├─ retry.py
│  │  │  │     │  │  │  │  ├─ ssltransport.py
│  │  │  │     │  │  │  │  ├─ ssl_.py
│  │  │  │     │  │  │  │  ├─ ssl_match_hostname.py
│  │  │  │     │  │  │  │  ├─ timeout.py
│  │  │  │     │  │  │  │  ├─ url.py
│  │  │  │     │  │  │  │  ├─ wait.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ connection.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ proxy.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ queue.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ request.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ response.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ retry.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ssltransport.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ssl_.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ssl_match_hostname.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ timeout.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ url.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ wait.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _collections.py
│  │  │  │     │  │  │  ├─ _version.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ connection.cpython-310.pyc
│  │  │  │     │  │  │     ├─ connectionpool.cpython-310.pyc
│  │  │  │     │  │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ fields.cpython-310.pyc
│  │  │  │     │  │  │     ├─ filepost.cpython-310.pyc
│  │  │  │     │  │  │     ├─ poolmanager.cpython-310.pyc
│  │  │  │     │  │  │     ├─ request.cpython-310.pyc
│  │  │  │     │  │  │     ├─ response.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _collections.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _version.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ vendor.txt
│  │  │  │     │  │  ├─ webencodings
│  │  │  │     │  │  │  ├─ labels.py
│  │  │  │     │  │  │  ├─ mklabels.py
│  │  │  │     │  │  │  ├─ tests.py
│  │  │  │     │  │  │  ├─ x_user_defined.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ labels.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mklabels.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tests.cpython-310.pyc
│  │  │  │     │  │  │     ├─ x_user_defined.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ six.cpython-310.pyc
│  │  │  │     │  │     ├─ typing_extensions.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  ├─ __pip-runner__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     ├─ __main__.cpython-310.pyc
│  │  │  │     │     └─ __pip-runner__.cpython-310.pyc
│  │  │  │     ├─ pip-22.3.1.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE.txt
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pkg_resources
│  │  │  │     │  ├─ extern
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _vendor
│  │  │  │     │  │  ├─ appdirs.py
│  │  │  │     │  │  ├─ importlib_resources
│  │  │  │     │  │  │  ├─ abc.py
│  │  │  │     │  │  │  ├─ readers.py
│  │  │  │     │  │  │  ├─ simple.py
│  │  │  │     │  │  │  ├─ _adapters.py
│  │  │  │     │  │  │  ├─ _common.py
│  │  │  │     │  │  │  ├─ _compat.py
│  │  │  │     │  │  │  ├─ _itertools.py
│  │  │  │     │  │  │  ├─ _legacy.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ abc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ readers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ simple.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _adapters.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _common.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _itertools.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _legacy.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ jaraco
│  │  │  │     │  │  │  ├─ context.py
│  │  │  │     │  │  │  ├─ functools.py
│  │  │  │     │  │  │  ├─ text
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ context.cpython-310.pyc
│  │  │  │     │  │  │     ├─ functools.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ more_itertools
│  │  │  │     │  │  │  ├─ more.py
│  │  │  │     │  │  │  ├─ recipes.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ more.cpython-310.pyc
│  │  │  │     │  │  │     ├─ recipes.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ packaging
│  │  │  │     │  │  │  ├─ markers.py
│  │  │  │     │  │  │  ├─ requirements.py
│  │  │  │     │  │  │  ├─ specifiers.py
│  │  │  │     │  │  │  ├─ tags.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ _manylinux.py
│  │  │  │     │  │  │  ├─ _musllinux.py
│  │  │  │     │  │  │  ├─ _structures.py
│  │  │  │     │  │  │  ├─ __about__.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ markers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ requirements.cpython-310.pyc
│  │  │  │     │  │  │     ├─ specifiers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tags.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _manylinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _musllinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _structures.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __about__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ pyparsing
│  │  │  │     │  │  │  ├─ actions.py
│  │  │  │     │  │  │  ├─ common.py
│  │  │  │     │  │  │  ├─ core.py
│  │  │  │     │  │  │  ├─ diagram
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  ├─ helpers.py
│  │  │  │     │  │  │  ├─ results.py
│  │  │  │     │  │  │  ├─ testing.py
│  │  │  │     │  │  │  ├─ unicode.py
│  │  │  │     │  │  │  ├─ util.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ actions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ common.cpython-310.pyc
│  │  │  │     │  │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ helpers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ results.cpython-310.pyc
│  │  │  │     │  │  │     ├─ testing.cpython-310.pyc
│  │  │  │     │  │  │     ├─ unicode.cpython-310.pyc
│  │  │  │     │  │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ zipp.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ appdirs.cpython-310.pyc
│  │  │  │     │  │     ├─ zipp.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ portalocker
│  │  │  │     │  ├─ constants.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ portalocker.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ redis.py
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ __about__.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ constants.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ portalocker.cpython-310.pyc
│  │  │  │     │     ├─ redis.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ __about__.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ portalocker-2.8.2.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pycparser
│  │  │  │     │  ├─ ast_transforms.py
│  │  │  │     │  ├─ c_ast.py
│  │  │  │     │  ├─ c_generator.py
│  │  │  │     │  ├─ c_lexer.py
│  │  │  │     │  ├─ c_parser.py
│  │  │  │     │  ├─ lextab.py
│  │  │  │     │  ├─ ply
│  │  │  │     │  │  ├─ cpp.py
│  │  │  │     │  │  ├─ ctokens.py
│  │  │  │     │  │  ├─ lex.py
│  │  │  │     │  │  ├─ yacc.py
│  │  │  │     │  │  ├─ ygen.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ cpp.cpython-310.pyc
│  │  │  │     │  │     ├─ ctokens.cpython-310.pyc
│  │  │  │     │  │     ├─ lex.cpython-310.pyc
│  │  │  │     │  │     ├─ yacc.cpython-310.pyc
│  │  │  │     │  │     ├─ ygen.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ plyparser.py
│  │  │  │     │  ├─ yacctab.py
│  │  │  │     │  ├─ _ast_gen.py
│  │  │  │     │  ├─ _build_tables.py
│  │  │  │     │  ├─ _c_ast.cfg
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ ast_transforms.cpython-310.pyc
│  │  │  │     │     ├─ c_ast.cpython-310.pyc
│  │  │  │     │     ├─ c_generator.cpython-310.pyc
│  │  │  │     │     ├─ c_lexer.cpython-310.pyc
│  │  │  │     │     ├─ c_parser.cpython-310.pyc
│  │  │  │     │     ├─ lextab.cpython-310.pyc
│  │  │  │     │     ├─ plyparser.cpython-310.pyc
│  │  │  │     │     ├─ yacctab.cpython-310.pyc
│  │  │  │     │     ├─ _ast_gen.cpython-310.pyc
│  │  │  │     │     ├─ _build_tables.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ pycparser-2.21.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ PyJWT-2.8.0.dist-info
│  │  │  │     │  ├─ AUTHORS.rst
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pythoncom.py
│  │  │  │     ├─ pythonwin
│  │  │  │     │  ├─ dde.pyd
│  │  │  │     │  ├─ license.txt
│  │  │  │     │  ├─ mfc140u.dll
│  │  │  │     │  ├─ Pythonwin.exe
│  │  │  │     │  ├─ pywin
│  │  │  │     │  │  ├─ debugger
│  │  │  │     │  │  │  ├─ configui.py
│  │  │  │     │  │  │  ├─ dbgcon.py
│  │  │  │     │  │  │  ├─ dbgpyapp.py
│  │  │  │     │  │  │  ├─ debugger.py
│  │  │  │     │  │  │  ├─ fail.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ configui.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dbgcon.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dbgpyapp.cpython-310.pyc
│  │  │  │     │  │  │     ├─ debugger.cpython-310.pyc
│  │  │  │     │  │  │     ├─ fail.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ default.cfg
│  │  │  │     │  │  ├─ Demos
│  │  │  │     │  │  │  ├─ app
│  │  │  │     │  │  │  │  ├─ basictimerapp.py
│  │  │  │     │  │  │  │  ├─ customprint.py
│  │  │  │     │  │  │  │  ├─ demoutils.py
│  │  │  │     │  │  │  │  ├─ dlgappdemo.py
│  │  │  │     │  │  │  │  ├─ dojobapp.py
│  │  │  │     │  │  │  │  ├─ helloapp.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ basictimerapp.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ customprint.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ demoutils.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ dlgappdemo.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ dojobapp.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ helloapp.cpython-310.pyc
│  │  │  │     │  │  │  ├─ cmdserver.py
│  │  │  │     │  │  │  ├─ createwin.py
│  │  │  │     │  │  │  ├─ demoutils.py
│  │  │  │     │  │  │  ├─ dibdemo.py
│  │  │  │     │  │  │  ├─ dlgtest.py
│  │  │  │     │  │  │  ├─ dyndlg.py
│  │  │  │     │  │  │  ├─ fontdemo.py
│  │  │  │     │  │  │  ├─ guidemo.py
│  │  │  │     │  │  │  ├─ hiertest.py
│  │  │  │     │  │  │  ├─ menutest.py
│  │  │  │     │  │  │  ├─ objdoc.py
│  │  │  │     │  │  │  ├─ ocx
│  │  │  │     │  │  │  │  ├─ demoutils.py
│  │  │  │     │  │  │  │  ├─ flash.py
│  │  │  │     │  │  │  │  ├─ msoffice.py
│  │  │  │     │  │  │  │  ├─ ocxserialtest.py
│  │  │  │     │  │  │  │  ├─ ocxtest.py
│  │  │  │     │  │  │  │  ├─ webbrowser.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ demoutils.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ flash.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ msoffice.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ocxserialtest.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ocxtest.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ webbrowser.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ openGLDemo.py
│  │  │  │     │  │  │  ├─ progressbar.py
│  │  │  │     │  │  │  ├─ sliderdemo.py
│  │  │  │     │  │  │  ├─ splittst.py
│  │  │  │     │  │  │  ├─ threadedgui.py
│  │  │  │     │  │  │  ├─ toolbar.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ cmdserver.cpython-310.pyc
│  │  │  │     │  │  │     ├─ createwin.cpython-310.pyc
│  │  │  │     │  │  │     ├─ demoutils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dibdemo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dlgtest.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dyndlg.cpython-310.pyc
│  │  │  │     │  │  │     ├─ fontdemo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ guidemo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hiertest.cpython-310.pyc
│  │  │  │     │  │  │     ├─ menutest.cpython-310.pyc
│  │  │  │     │  │  │     ├─ objdoc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ openGLDemo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ progressbar.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sliderdemo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ splittst.cpython-310.pyc
│  │  │  │     │  │  │     ├─ threadedgui.cpython-310.pyc
│  │  │  │     │  │  │     └─ toolbar.cpython-310.pyc
│  │  │  │     │  │  ├─ dialogs
│  │  │  │     │  │  │  ├─ ideoptions.py
│  │  │  │     │  │  │  ├─ list.py
│  │  │  │     │  │  │  ├─ login.py
│  │  │  │     │  │  │  ├─ status.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ ideoptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ list.cpython-310.pyc
│  │  │  │     │  │  │     ├─ login.cpython-310.pyc
│  │  │  │     │  │  │     ├─ status.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ docking
│  │  │  │     │  │  │  ├─ DockingBar.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ DockingBar.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ framework
│  │  │  │     │  │  │  ├─ app.py
│  │  │  │     │  │  │  ├─ bitmap.py
│  │  │  │     │  │  │  ├─ cmdline.py
│  │  │  │     │  │  │  ├─ dbgcommands.py
│  │  │  │     │  │  │  ├─ dlgappcore.py
│  │  │  │     │  │  │  ├─ editor
│  │  │  │     │  │  │  │  ├─ color
│  │  │  │     │  │  │  │  │  ├─ coloreditor.py
│  │  │  │     │  │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │  │     ├─ coloreditor.cpython-310.pyc
│  │  │  │     │  │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ configui.py
│  │  │  │     │  │  │  │  ├─ document.py
│  │  │  │     │  │  │  │  ├─ editor.py
│  │  │  │     │  │  │  │  ├─ frame.py
│  │  │  │     │  │  │  │  ├─ ModuleBrowser.py
│  │  │  │     │  │  │  │  ├─ template.py
│  │  │  │     │  │  │  │  ├─ vss.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ configui.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ document.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ editor.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ frame.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ModuleBrowser.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ template.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ vss.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ help.py
│  │  │  │     │  │  │  ├─ interact.py
│  │  │  │     │  │  │  ├─ intpyapp.py
│  │  │  │     │  │  │  ├─ intpydde.py
│  │  │  │     │  │  │  ├─ mdi_pychecker.py
│  │  │  │     │  │  │  ├─ scriptutils.py
│  │  │  │     │  │  │  ├─ sgrepmdi.py
│  │  │  │     │  │  │  ├─ startup.py
│  │  │  │     │  │  │  ├─ stdin.py
│  │  │  │     │  │  │  ├─ toolmenu.py
│  │  │  │     │  │  │  ├─ window.py
│  │  │  │     │  │  │  ├─ winout.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ app.cpython-310.pyc
│  │  │  │     │  │  │     ├─ bitmap.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cmdline.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dbgcommands.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dlgappcore.cpython-310.pyc
│  │  │  │     │  │  │     ├─ help.cpython-310.pyc
│  │  │  │     │  │  │     ├─ interact.cpython-310.pyc
│  │  │  │     │  │  │     ├─ intpyapp.cpython-310.pyc
│  │  │  │     │  │  │     ├─ intpydde.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mdi_pychecker.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scriptutils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sgrepmdi.cpython-310.pyc
│  │  │  │     │  │  │     ├─ startup.cpython-310.pyc
│  │  │  │     │  │  │     ├─ stdin.cpython-310.pyc
│  │  │  │     │  │  │     ├─ toolmenu.cpython-310.pyc
│  │  │  │     │  │  │     ├─ window.cpython-310.pyc
│  │  │  │     │  │  │     ├─ winout.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ idle
│  │  │  │     │  │  │  ├─ AutoExpand.py
│  │  │  │     │  │  │  ├─ AutoIndent.py
│  │  │  │     │  │  │  ├─ CallTips.py
│  │  │  │     │  │  │  ├─ FormatParagraph.py
│  │  │  │     │  │  │  ├─ IdleHistory.py
│  │  │  │     │  │  │  ├─ PyParse.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ AutoExpand.cpython-310.pyc
│  │  │  │     │  │  │     ├─ AutoIndent.cpython-310.pyc
│  │  │  │     │  │  │     ├─ CallTips.cpython-310.pyc
│  │  │  │     │  │  │     ├─ FormatParagraph.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IdleHistory.cpython-310.pyc
│  │  │  │     │  │  │     ├─ PyParse.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ IDLE.cfg
│  │  │  │     │  │  ├─ mfc
│  │  │  │     │  │  │  ├─ activex.py
│  │  │  │     │  │  │  ├─ afxres.py
│  │  │  │     │  │  │  ├─ dialog.py
│  │  │  │     │  │  │  ├─ docview.py
│  │  │  │     │  │  │  ├─ object.py
│  │  │  │     │  │  │  ├─ thread.py
│  │  │  │     │  │  │  ├─ window.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ activex.cpython-310.pyc
│  │  │  │     │  │  │     ├─ afxres.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dialog.cpython-310.pyc
│  │  │  │     │  │  │     ├─ docview.cpython-310.pyc
│  │  │  │     │  │  │     ├─ object.cpython-310.pyc
│  │  │  │     │  │  │     ├─ thread.cpython-310.pyc
│  │  │  │     │  │  │     ├─ window.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ scintilla
│  │  │  │     │  │  │  ├─ bindings.py
│  │  │  │     │  │  │  ├─ config.py
│  │  │  │     │  │  │  ├─ configui.py
│  │  │  │     │  │  │  ├─ control.py
│  │  │  │     │  │  │  ├─ document.py
│  │  │  │     │  │  │  ├─ find.py
│  │  │  │     │  │  │  ├─ formatter.py
│  │  │  │     │  │  │  ├─ IDLEenvironment.py
│  │  │  │     │  │  │  ├─ keycodes.py
│  │  │  │     │  │  │  ├─ scintillacon.py
│  │  │  │     │  │  │  ├─ view.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ bindings.cpython-310.pyc
│  │  │  │     │  │  │     ├─ config.cpython-310.pyc
│  │  │  │     │  │  │     ├─ configui.cpython-310.pyc
│  │  │  │     │  │  │     ├─ control.cpython-310.pyc
│  │  │  │     │  │  │     ├─ document.cpython-310.pyc
│  │  │  │     │  │  │     ├─ find.cpython-310.pyc
│  │  │  │     │  │  │     ├─ formatter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IDLEenvironment.cpython-310.pyc
│  │  │  │     │  │  │     ├─ keycodes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scintillacon.cpython-310.pyc
│  │  │  │     │  │  │     ├─ view.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ tools
│  │  │  │     │  │  │  ├─ browseProjects.py
│  │  │  │     │  │  │  ├─ browser.py
│  │  │  │     │  │  │  ├─ hierlist.py
│  │  │  │     │  │  │  ├─ regedit.py
│  │  │  │     │  │  │  ├─ regpy.py
│  │  │  │     │  │  │  ├─ TraceCollector.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ browseProjects.cpython-310.pyc
│  │  │  │     │  │  │     ├─ browser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hierlist.cpython-310.pyc
│  │  │  │     │  │  │     ├─ regedit.cpython-310.pyc
│  │  │  │     │  │  │     ├─ regpy.cpython-310.pyc
│  │  │  │     │  │  │     ├─ TraceCollector.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ scintilla.dll
│  │  │  │     │  ├─ start_pythonwin.pyw
│  │  │  │     │  ├─ win32ui.pyd
│  │  │  │     │  └─ win32uiole.pyd
│  │  │  │     ├─ pywin32-306.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ PyWin32.chm
│  │  │  │     ├─ pywin32.pth
│  │  │  │     ├─ pywin32.version.txt
│  │  │  │     ├─ pywin32_system32
│  │  │  │     │  ├─ pythoncom310.dll
│  │  │  │     │  └─ pywintypes310.dll
│  │  │  │     ├─ requests
│  │  │  │     │  ├─ adapters.py
│  │  │  │     │  ├─ api.py
│  │  │  │     │  ├─ auth.py
│  │  │  │     │  ├─ certs.py
│  │  │  │     │  ├─ compat.py
│  │  │  │     │  ├─ cookies.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ help.py
│  │  │  │     │  ├─ models.py
│  │  │  │     │  ├─ packages.py
│  │  │  │     │  ├─ sessions.py
│  │  │  │     │  ├─ status_codes.py
│  │  │  │     │  ├─ structures.py
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ _internal_utils.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __pycache__
│  │  │  │     │  │  ├─ adapters.cpython-310.pyc
│  │  │  │     │  │  ├─ api.cpython-310.pyc
│  │  │  │     │  │  ├─ auth.cpython-310.pyc
│  │  │  │     │  │  ├─ certs.cpython-310.pyc
│  │  │  │     │  │  ├─ compat.cpython-310.pyc
│  │  │  │     │  │  ├─ cookies.cpython-310.pyc
│  │  │  │     │  │  ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  ├─ help.cpython-310.pyc
│  │  │  │     │  │  ├─ models.cpython-310.pyc
│  │  │  │     │  │  ├─ packages.cpython-310.pyc
│  │  │  │     │  │  ├─ sessions.cpython-310.pyc
│  │  │  │     │  │  ├─ status_codes.cpython-310.pyc
│  │  │  │     │  │  ├─ structures.cpython-310.pyc
│  │  │  │     │  │  ├─ utils.cpython-310.pyc
│  │  │  │     │  │  ├─ _internal_utils.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  └─ __version__.cpython-310.pyc
│  │  │  │     │  └─ __version__.py
│  │  │  │     ├─ requests-2.31.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ setuptools
│  │  │  │     │  ├─ archive_util.py
│  │  │  │     │  ├─ build_meta.py
│  │  │  │     │  ├─ cli-32.exe
│  │  │  │     │  ├─ cli-64.exe
│  │  │  │     │  ├─ cli-arm64.exe
│  │  │  │     │  ├─ cli.exe
│  │  │  │     │  ├─ command
│  │  │  │     │  │  ├─ alias.py
│  │  │  │     │  │  ├─ bdist_egg.py
│  │  │  │     │  │  ├─ bdist_rpm.py
│  │  │  │     │  │  ├─ build.py
│  │  │  │     │  │  ├─ build_clib.py
│  │  │  │     │  │  ├─ build_ext.py
│  │  │  │     │  │  ├─ build_py.py
│  │  │  │     │  │  ├─ develop.py
│  │  │  │     │  │  ├─ dist_info.py
│  │  │  │     │  │  ├─ easy_install.py
│  │  │  │     │  │  ├─ editable_wheel.py
│  │  │  │     │  │  ├─ egg_info.py
│  │  │  │     │  │  ├─ install.py
│  │  │  │     │  │  ├─ install_egg_info.py
│  │  │  │     │  │  ├─ install_lib.py
│  │  │  │     │  │  ├─ install_scripts.py
│  │  │  │     │  │  ├─ launcher manifest.xml
│  │  │  │     │  │  ├─ py36compat.py
│  │  │  │     │  │  ├─ register.py
│  │  │  │     │  │  ├─ rotate.py
│  │  │  │     │  │  ├─ saveopts.py
│  │  │  │     │  │  ├─ sdist.py
│  │  │  │     │  │  ├─ setopt.py
│  │  │  │     │  │  ├─ test.py
│  │  │  │     │  │  ├─ upload.py
│  │  │  │     │  │  ├─ upload_docs.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ alias.cpython-310.pyc
│  │  │  │     │  │     ├─ bdist_egg.cpython-310.pyc
│  │  │  │     │  │     ├─ bdist_rpm.cpython-310.pyc
│  │  │  │     │  │     ├─ build.cpython-310.pyc
│  │  │  │     │  │     ├─ build_clib.cpython-310.pyc
│  │  │  │     │  │     ├─ build_ext.cpython-310.pyc
│  │  │  │     │  │     ├─ build_py.cpython-310.pyc
│  │  │  │     │  │     ├─ develop.cpython-310.pyc
│  │  │  │     │  │     ├─ dist_info.cpython-310.pyc
│  │  │  │     │  │     ├─ easy_install.cpython-310.pyc
│  │  │  │     │  │     ├─ editable_wheel.cpython-310.pyc
│  │  │  │     │  │     ├─ egg_info.cpython-310.pyc
│  │  │  │     │  │     ├─ install.cpython-310.pyc
│  │  │  │     │  │     ├─ install_egg_info.cpython-310.pyc
│  │  │  │     │  │     ├─ install_lib.cpython-310.pyc
│  │  │  │     │  │     ├─ install_scripts.cpython-310.pyc
│  │  │  │     │  │     ├─ py36compat.cpython-310.pyc
│  │  │  │     │  │     ├─ register.cpython-310.pyc
│  │  │  │     │  │     ├─ rotate.cpython-310.pyc
│  │  │  │     │  │     ├─ saveopts.cpython-310.pyc
│  │  │  │     │  │     ├─ sdist.cpython-310.pyc
│  │  │  │     │  │     ├─ setopt.cpython-310.pyc
│  │  │  │     │  │     ├─ test.cpython-310.pyc
│  │  │  │     │  │     ├─ upload.cpython-310.pyc
│  │  │  │     │  │     ├─ upload_docs.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ config
│  │  │  │     │  │  ├─ expand.py
│  │  │  │     │  │  ├─ pyprojecttoml.py
│  │  │  │     │  │  ├─ setupcfg.py
│  │  │  │     │  │  ├─ _apply_pyprojecttoml.py
│  │  │  │     │  │  ├─ _validate_pyproject
│  │  │  │     │  │  │  ├─ error_reporting.py
│  │  │  │     │  │  │  ├─ extra_validations.py
│  │  │  │     │  │  │  ├─ fastjsonschema_exceptions.py
│  │  │  │     │  │  │  ├─ fastjsonschema_validations.py
│  │  │  │     │  │  │  ├─ formats.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ error_reporting.cpython-310.pyc
│  │  │  │     │  │  │     ├─ extra_validations.cpython-310.pyc
│  │  │  │     │  │  │     ├─ fastjsonschema_exceptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ fastjsonschema_validations.cpython-310.pyc
│  │  │  │     │  │  │     ├─ formats.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ expand.cpython-310.pyc
│  │  │  │     │  │     ├─ pyprojecttoml.cpython-310.pyc
│  │  │  │     │  │     ├─ setupcfg.cpython-310.pyc
│  │  │  │     │  │     ├─ _apply_pyprojecttoml.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ depends.py
│  │  │  │     │  ├─ dep_util.py
│  │  │  │     │  ├─ discovery.py
│  │  │  │     │  ├─ dist.py
│  │  │  │     │  ├─ errors.py
│  │  │  │     │  ├─ extension.py
│  │  │  │     │  ├─ extern
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ glob.py
│  │  │  │     │  ├─ gui-32.exe
│  │  │  │     │  ├─ gui-64.exe
│  │  │  │     │  ├─ gui-arm64.exe
│  │  │  │     │  ├─ gui.exe
│  │  │  │     │  ├─ installer.py
│  │  │  │     │  ├─ launch.py
│  │  │  │     │  ├─ logging.py
│  │  │  │     │  ├─ monkey.py
│  │  │  │     │  ├─ msvc.py
│  │  │  │     │  ├─ namespaces.py
│  │  │  │     │  ├─ package_index.py
│  │  │  │     │  ├─ py34compat.py
│  │  │  │     │  ├─ sandbox.py
│  │  │  │     │  ├─ script (dev).tmpl
│  │  │  │     │  ├─ script.tmpl
│  │  │  │     │  ├─ unicode_utils.py
│  │  │  │     │  ├─ version.py
│  │  │  │     │  ├─ wheel.py
│  │  │  │     │  ├─ windows_support.py
│  │  │  │     │  ├─ _deprecation_warning.py
│  │  │  │     │  ├─ _distutils
│  │  │  │     │  │  ├─ archive_util.py
│  │  │  │     │  │  ├─ bcppcompiler.py
│  │  │  │     │  │  ├─ ccompiler.py
│  │  │  │     │  │  ├─ cmd.py
│  │  │  │     │  │  ├─ command
│  │  │  │     │  │  │  ├─ bdist.py
│  │  │  │     │  │  │  ├─ bdist_dumb.py
│  │  │  │     │  │  │  ├─ bdist_rpm.py
│  │  │  │     │  │  │  ├─ build.py
│  │  │  │     │  │  │  ├─ build_clib.py
│  │  │  │     │  │  │  ├─ build_ext.py
│  │  │  │     │  │  │  ├─ build_py.py
│  │  │  │     │  │  │  ├─ build_scripts.py
│  │  │  │     │  │  │  ├─ check.py
│  │  │  │     │  │  │  ├─ clean.py
│  │  │  │     │  │  │  ├─ config.py
│  │  │  │     │  │  │  ├─ install.py
│  │  │  │     │  │  │  ├─ install_data.py
│  │  │  │     │  │  │  ├─ install_egg_info.py
│  │  │  │     │  │  │  ├─ install_headers.py
│  │  │  │     │  │  │  ├─ install_lib.py
│  │  │  │     │  │  │  ├─ install_scripts.py
│  │  │  │     │  │  │  ├─ py37compat.py
│  │  │  │     │  │  │  ├─ register.py
│  │  │  │     │  │  │  ├─ sdist.py
│  │  │  │     │  │  │  ├─ upload.py
│  │  │  │     │  │  │  ├─ _framework_compat.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ bdist.cpython-310.pyc
│  │  │  │     │  │  │     ├─ bdist_dumb.cpython-310.pyc
│  │  │  │     │  │  │     ├─ bdist_rpm.cpython-310.pyc
│  │  │  │     │  │  │     ├─ build.cpython-310.pyc
│  │  │  │     │  │  │     ├─ build_clib.cpython-310.pyc
│  │  │  │     │  │  │     ├─ build_ext.cpython-310.pyc
│  │  │  │     │  │  │     ├─ build_py.cpython-310.pyc
│  │  │  │     │  │  │     ├─ build_scripts.cpython-310.pyc
│  │  │  │     │  │  │     ├─ check.cpython-310.pyc
│  │  │  │     │  │  │     ├─ clean.cpython-310.pyc
│  │  │  │     │  │  │     ├─ config.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install_data.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install_egg_info.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install_headers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install_lib.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install_scripts.cpython-310.pyc
│  │  │  │     │  │  │     ├─ py37compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ register.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sdist.cpython-310.pyc
│  │  │  │     │  │  │     ├─ upload.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _framework_compat.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ config.py
│  │  │  │     │  │  ├─ core.py
│  │  │  │     │  │  ├─ cygwinccompiler.py
│  │  │  │     │  │  ├─ debug.py
│  │  │  │     │  │  ├─ dep_util.py
│  │  │  │     │  │  ├─ dir_util.py
│  │  │  │     │  │  ├─ dist.py
│  │  │  │     │  │  ├─ errors.py
│  │  │  │     │  │  ├─ extension.py
│  │  │  │     │  │  ├─ fancy_getopt.py
│  │  │  │     │  │  ├─ filelist.py
│  │  │  │     │  │  ├─ file_util.py
│  │  │  │     │  │  ├─ log.py
│  │  │  │     │  │  ├─ msvc9compiler.py
│  │  │  │     │  │  ├─ msvccompiler.py
│  │  │  │     │  │  ├─ py38compat.py
│  │  │  │     │  │  ├─ py39compat.py
│  │  │  │     │  │  ├─ spawn.py
│  │  │  │     │  │  ├─ sysconfig.py
│  │  │  │     │  │  ├─ text_file.py
│  │  │  │     │  │  ├─ unixccompiler.py
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ version.py
│  │  │  │     │  │  ├─ versionpredicate.py
│  │  │  │     │  │  ├─ _collections.py
│  │  │  │     │  │  ├─ _functools.py
│  │  │  │     │  │  ├─ _macos_compat.py
│  │  │  │     │  │  ├─ _msvccompiler.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ archive_util.cpython-310.pyc
│  │  │  │     │  │     ├─ bcppcompiler.cpython-310.pyc
│  │  │  │     │  │     ├─ ccompiler.cpython-310.pyc
│  │  │  │     │  │     ├─ cmd.cpython-310.pyc
│  │  │  │     │  │     ├─ config.cpython-310.pyc
│  │  │  │     │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │     ├─ cygwinccompiler.cpython-310.pyc
│  │  │  │     │  │     ├─ debug.cpython-310.pyc
│  │  │  │     │  │     ├─ dep_util.cpython-310.pyc
│  │  │  │     │  │     ├─ dir_util.cpython-310.pyc
│  │  │  │     │  │     ├─ dist.cpython-310.pyc
│  │  │  │     │  │     ├─ errors.cpython-310.pyc
│  │  │  │     │  │     ├─ extension.cpython-310.pyc
│  │  │  │     │  │     ├─ fancy_getopt.cpython-310.pyc
│  │  │  │     │  │     ├─ filelist.cpython-310.pyc
│  │  │  │     │  │     ├─ file_util.cpython-310.pyc
│  │  │  │     │  │     ├─ log.cpython-310.pyc
│  │  │  │     │  │     ├─ msvc9compiler.cpython-310.pyc
│  │  │  │     │  │     ├─ msvccompiler.cpython-310.pyc
│  │  │  │     │  │     ├─ py38compat.cpython-310.pyc
│  │  │  │     │  │     ├─ py39compat.cpython-310.pyc
│  │  │  │     │  │     ├─ spawn.cpython-310.pyc
│  │  │  │     │  │     ├─ sysconfig.cpython-310.pyc
│  │  │  │     │  │     ├─ text_file.cpython-310.pyc
│  │  │  │     │  │     ├─ unixccompiler.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │     ├─ versionpredicate.cpython-310.pyc
│  │  │  │     │  │     ├─ _collections.cpython-310.pyc
│  │  │  │     │  │     ├─ _functools.cpython-310.pyc
│  │  │  │     │  │     ├─ _macos_compat.cpython-310.pyc
│  │  │  │     │  │     ├─ _msvccompiler.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _entry_points.py
│  │  │  │     │  ├─ _imp.py
│  │  │  │     │  ├─ _importlib.py
│  │  │  │     │  ├─ _itertools.py
│  │  │  │     │  ├─ _path.py
│  │  │  │     │  ├─ _reqs.py
│  │  │  │     │  ├─ _vendor
│  │  │  │     │  │  ├─ importlib_metadata
│  │  │  │     │  │  │  ├─ _adapters.py
│  │  │  │     │  │  │  ├─ _collections.py
│  │  │  │     │  │  │  ├─ _compat.py
│  │  │  │     │  │  │  ├─ _functools.py
│  │  │  │     │  │  │  ├─ _itertools.py
│  │  │  │     │  │  │  ├─ _meta.py
│  │  │  │     │  │  │  ├─ _text.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _adapters.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _collections.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _functools.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _itertools.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _meta.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _text.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ importlib_resources
│  │  │  │     │  │  │  ├─ abc.py
│  │  │  │     │  │  │  ├─ readers.py
│  │  │  │     │  │  │  ├─ simple.py
│  │  │  │     │  │  │  ├─ _adapters.py
│  │  │  │     │  │  │  ├─ _common.py
│  │  │  │     │  │  │  ├─ _compat.py
│  │  │  │     │  │  │  ├─ _itertools.py
│  │  │  │     │  │  │  ├─ _legacy.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ abc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ readers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ simple.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _adapters.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _common.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _itertools.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _legacy.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ jaraco
│  │  │  │     │  │  │  ├─ context.py
│  │  │  │     │  │  │  ├─ functools.py
│  │  │  │     │  │  │  ├─ text
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ context.cpython-310.pyc
│  │  │  │     │  │  │     ├─ functools.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ more_itertools
│  │  │  │     │  │  │  ├─ more.py
│  │  │  │     │  │  │  ├─ recipes.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ more.cpython-310.pyc
│  │  │  │     │  │  │     ├─ recipes.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ ordered_set.py
│  │  │  │     │  │  ├─ packaging
│  │  │  │     │  │  │  ├─ markers.py
│  │  │  │     │  │  │  ├─ requirements.py
│  │  │  │     │  │  │  ├─ specifiers.py
│  │  │  │     │  │  │  ├─ tags.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ _manylinux.py
│  │  │  │     │  │  │  ├─ _musllinux.py
│  │  │  │     │  │  │  ├─ _structures.py
│  │  │  │     │  │  │  ├─ __about__.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ markers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ requirements.cpython-310.pyc
│  │  │  │     │  │  │     ├─ specifiers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tags.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _manylinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _musllinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _structures.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __about__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ pyparsing
│  │  │  │     │  │  │  ├─ actions.py
│  │  │  │     │  │  │  ├─ common.py
│  │  │  │     │  │  │  ├─ core.py
│  │  │  │     │  │  │  ├─ diagram
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  ├─ helpers.py
│  │  │  │     │  │  │  ├─ results.py
│  │  │  │     │  │  │  ├─ testing.py
│  │  │  │     │  │  │  ├─ unicode.py
│  │  │  │     │  │  │  ├─ util.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ actions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ common.cpython-310.pyc
│  │  │  │     │  │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ helpers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ results.cpython-310.pyc
│  │  │  │     │  │  │     ├─ testing.cpython-310.pyc
│  │  │  │     │  │  │     ├─ unicode.cpython-310.pyc
│  │  │  │     │  │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ tomli
│  │  │  │     │  │  │  ├─ _parser.py
│  │  │  │     │  │  │  ├─ _re.py
│  │  │  │     │  │  │  ├─ _types.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _parser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _re.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _types.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ typing_extensions.py
│  │  │  │     │  │  ├─ zipp.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ ordered_set.cpython-310.pyc
│  │  │  │     │  │     ├─ typing_extensions.cpython-310.pyc
│  │  │  │     │  │     ├─ zipp.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ archive_util.cpython-310.pyc
│  │  │  │     │     ├─ build_meta.cpython-310.pyc
│  │  │  │     │     ├─ depends.cpython-310.pyc
│  │  │  │     │     ├─ dep_util.cpython-310.pyc
│  │  │  │     │     ├─ discovery.cpython-310.pyc
│  │  │  │     │     ├─ dist.cpython-310.pyc
│  │  │  │     │     ├─ errors.cpython-310.pyc
│  │  │  │     │     ├─ extension.cpython-310.pyc
│  │  │  │     │     ├─ glob.cpython-310.pyc
│  │  │  │     │     ├─ installer.cpython-310.pyc
│  │  │  │     │     ├─ launch.cpython-310.pyc
│  │  │  │     │     ├─ logging.cpython-310.pyc
│  │  │  │     │     ├─ monkey.cpython-310.pyc
│  │  │  │     │     ├─ msvc.cpython-310.pyc
│  │  │  │     │     ├─ namespaces.cpython-310.pyc
│  │  │  │     │     ├─ package_index.cpython-310.pyc
│  │  │  │     │     ├─ py34compat.cpython-310.pyc
│  │  │  │     │     ├─ sandbox.cpython-310.pyc
│  │  │  │     │     ├─ unicode_utils.cpython-310.pyc
│  │  │  │     │     ├─ version.cpython-310.pyc
│  │  │  │     │     ├─ wheel.cpython-310.pyc
│  │  │  │     │     ├─ windows_support.cpython-310.pyc
│  │  │  │     │     ├─ _deprecation_warning.cpython-310.pyc
│  │  │  │     │     ├─ _entry_points.cpython-310.pyc
│  │  │  │     │     ├─ _imp.cpython-310.pyc
│  │  │  │     │     ├─ _importlib.cpython-310.pyc
│  │  │  │     │     ├─ _itertools.cpython-310.pyc
│  │  │  │     │     ├─ _path.cpython-310.pyc
│  │  │  │     │     ├─ _reqs.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ setuptools-65.5.0.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ six-1.16.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ six.py
│  │  │  │     ├─ typing_extensions-4.8.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ typing_extensions.py
│  │  │  │     ├─ urllib3
│  │  │  │     │  ├─ connection.py
│  │  │  │     │  ├─ connectionpool.py
│  │  │  │     │  ├─ contrib
│  │  │  │     │  │  ├─ pyopenssl.py
│  │  │  │     │  │  ├─ securetransport.py
│  │  │  │     │  │  ├─ socks.py
│  │  │  │     │  │  ├─ _securetransport
│  │  │  │     │  │  │  ├─ bindings.py
│  │  │  │     │  │  │  ├─ low_level.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ bindings.cpython-310.pyc
│  │  │  │     │  │  │     ├─ low_level.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ pyopenssl.cpython-310.pyc
│  │  │  │     │  │     ├─ securetransport.cpython-310.pyc
│  │  │  │     │  │     ├─ socks.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ fields.py
│  │  │  │     │  ├─ filepost.py
│  │  │  │     │  ├─ poolmanager.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ response.py
│  │  │  │     │  ├─ util
│  │  │  │     │  │  ├─ connection.py
│  │  │  │     │  │  ├─ proxy.py
│  │  │  │     │  │  ├─ request.py
│  │  │  │     │  │  ├─ response.py
│  │  │  │     │  │  ├─ retry.py
│  │  │  │     │  │  ├─ ssltransport.py
│  │  │  │     │  │  ├─ ssl_.py
│  │  │  │     │  │  ├─ ssl_match_hostname.py
│  │  │  │     │  │  ├─ timeout.py
│  │  │  │     │  │  ├─ url.py
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ wait.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ connection.cpython-310.pyc
│  │  │  │     │  │     ├─ proxy.cpython-310.pyc
│  │  │  │     │  │     ├─ request.cpython-310.pyc
│  │  │  │     │  │     ├─ response.cpython-310.pyc
│  │  │  │     │  │     ├─ retry.cpython-310.pyc
│  │  │  │     │  │     ├─ ssltransport.cpython-310.pyc
│  │  │  │     │  │     ├─ ssl_.cpython-310.pyc
│  │  │  │     │  │     ├─ ssl_match_hostname.cpython-310.pyc
│  │  │  │     │  │     ├─ timeout.cpython-310.pyc
│  │  │  │     │  │     ├─ url.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     ├─ wait.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _base_connection.py
│  │  │  │     │  ├─ _collections.py
│  │  │  │     │  ├─ _request_methods.py
│  │  │  │     │  ├─ _version.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ connection.cpython-310.pyc
│  │  │  │     │     ├─ connectionpool.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ fields.cpython-310.pyc
│  │  │  │     │     ├─ filepost.cpython-310.pyc
│  │  │  │     │     ├─ poolmanager.cpython-310.pyc
│  │  │  │     │     ├─ response.cpython-310.pyc
│  │  │  │     │     ├─ _base_connection.cpython-310.pyc
│  │  │  │     │     ├─ _collections.cpython-310.pyc
│  │  │  │     │     ├─ _request_methods.cpython-310.pyc
│  │  │  │     │     ├─ _version.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ urllib3-2.0.6.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  └─ LICENSE.txt
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ win32
│  │  │  │     │  ├─ Demos
│  │  │  │     │  │  ├─ BackupRead_BackupWrite.py
│  │  │  │     │  │  ├─ BackupSeek_streamheaders.py
│  │  │  │     │  │  ├─ cerapi.py
│  │  │  │     │  │  ├─ CopyFileEx.py
│  │  │  │     │  │  ├─ CreateFileTransacted_MiniVersion.py
│  │  │  │     │  │  ├─ c_extension
│  │  │  │     │  │  │  ├─ setup.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ setup.cpython-310.pyc
│  │  │  │     │  │  ├─ dde
│  │  │  │     │  │  │  ├─ ddeclient.py
│  │  │  │     │  │  │  ├─ ddeserver.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ ddeclient.cpython-310.pyc
│  │  │  │     │  │  │     └─ ddeserver.cpython-310.pyc
│  │  │  │     │  │  ├─ desktopmanager.py
│  │  │  │     │  │  ├─ eventLogDemo.py
│  │  │  │     │  │  ├─ EvtFormatMessage.py
│  │  │  │     │  │  ├─ EvtSubscribe_pull.py
│  │  │  │     │  │  ├─ EvtSubscribe_push.py
│  │  │  │     │  │  ├─ FileSecurityTest.py
│  │  │  │     │  │  ├─ getfilever.py
│  │  │  │     │  │  ├─ GetSaveFileName.py
│  │  │  │     │  │  ├─ images
│  │  │  │     │  │  │  ├─ frowny.bmp
│  │  │  │     │  │  │  └─ smiley.bmp
│  │  │  │     │  │  ├─ mmapfile_demo.py
│  │  │  │     │  │  ├─ NetValidatePasswordPolicy.py
│  │  │  │     │  │  ├─ OpenEncryptedFileRaw.py
│  │  │  │     │  │  ├─ pipes
│  │  │  │     │  │  │  ├─ cat.py
│  │  │  │     │  │  │  ├─ runproc.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ cat.cpython-310.pyc
│  │  │  │     │  │  │     └─ runproc.cpython-310.pyc
│  │  │  │     │  │  ├─ print_desktop.py
│  │  │  │     │  │  ├─ rastest.py
│  │  │  │     │  │  ├─ RegCreateKeyTransacted.py
│  │  │  │     │  │  ├─ RegRestoreKey.py
│  │  │  │     │  │  ├─ security
│  │  │  │     │  │  │  ├─ account_rights.py
│  │  │  │     │  │  │  ├─ explicit_entries.py
│  │  │  │     │  │  │  ├─ GetTokenInformation.py
│  │  │  │     │  │  │  ├─ get_policy_info.py
│  │  │  │     │  │  │  ├─ list_rights.py
│  │  │  │     │  │  │  ├─ localized_names.py
│  │  │  │     │  │  │  ├─ lsaregevent.py
│  │  │  │     │  │  │  ├─ lsastore.py
│  │  │  │     │  │  │  ├─ query_information.py
│  │  │  │     │  │  │  ├─ regsave_sa.py
│  │  │  │     │  │  │  ├─ regsecurity.py
│  │  │  │     │  │  │  ├─ sa_inherit.py
│  │  │  │     │  │  │  ├─ security_enums.py
│  │  │  │     │  │  │  ├─ setkernelobjectsecurity.py
│  │  │  │     │  │  │  ├─ setnamedsecurityinfo.py
│  │  │  │     │  │  │  ├─ setsecurityinfo.py
│  │  │  │     │  │  │  ├─ setuserobjectsecurity.py
│  │  │  │     │  │  │  ├─ set_file_audit.py
│  │  │  │     │  │  │  ├─ set_file_owner.py
│  │  │  │     │  │  │  ├─ set_policy_info.py
│  │  │  │     │  │  │  ├─ sspi
│  │  │  │     │  │  │  │  ├─ fetch_url.py
│  │  │  │     │  │  │  │  ├─ simple_auth.py
│  │  │  │     │  │  │  │  ├─ socket_server.py
│  │  │  │     │  │  │  │  ├─ validate_password.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ fetch_url.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ simple_auth.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ socket_server.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ validate_password.cpython-310.pyc
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ account_rights.cpython-310.pyc
│  │  │  │     │  │  │     ├─ explicit_entries.cpython-310.pyc
│  │  │  │     │  │  │     ├─ GetTokenInformation.cpython-310.pyc
│  │  │  │     │  │  │     ├─ get_policy_info.cpython-310.pyc
│  │  │  │     │  │  │     ├─ list_rights.cpython-310.pyc
│  │  │  │     │  │  │     ├─ localized_names.cpython-310.pyc
│  │  │  │     │  │  │     ├─ lsaregevent.cpython-310.pyc
│  │  │  │     │  │  │     ├─ lsastore.cpython-310.pyc
│  │  │  │     │  │  │     ├─ query_information.cpython-310.pyc
│  │  │  │     │  │  │     ├─ regsave_sa.cpython-310.pyc
│  │  │  │     │  │  │     ├─ regsecurity.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sa_inherit.cpython-310.pyc
│  │  │  │     │  │  │     ├─ security_enums.cpython-310.pyc
│  │  │  │     │  │  │     ├─ setkernelobjectsecurity.cpython-310.pyc
│  │  │  │     │  │  │     ├─ setnamedsecurityinfo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ setsecurityinfo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ setuserobjectsecurity.cpython-310.pyc
│  │  │  │     │  │  │     ├─ set_file_audit.cpython-310.pyc
│  │  │  │     │  │  │     ├─ set_file_owner.cpython-310.pyc
│  │  │  │     │  │  │     └─ set_policy_info.cpython-310.pyc
│  │  │  │     │  │  ├─ service
│  │  │  │     │  │  │  ├─ nativePipeTestService.py
│  │  │  │     │  │  │  ├─ pipeTestService.py
│  │  │  │     │  │  │  ├─ pipeTestServiceClient.py
│  │  │  │     │  │  │  ├─ serviceEvents.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ nativePipeTestService.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pipeTestService.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pipeTestServiceClient.cpython-310.pyc
│  │  │  │     │  │  │     └─ serviceEvents.cpython-310.pyc
│  │  │  │     │  │  ├─ SystemParametersInfo.py
│  │  │  │     │  │  ├─ timer_demo.py
│  │  │  │     │  │  ├─ win32clipboardDemo.py
│  │  │  │     │  │  ├─ win32clipboard_bitmapdemo.py
│  │  │  │     │  │  ├─ win32comport_demo.py
│  │  │  │     │  │  ├─ win32console_demo.py
│  │  │  │     │  │  ├─ win32cred_demo.py
│  │  │  │     │  │  ├─ win32fileDemo.py
│  │  │  │     │  │  ├─ win32gui_demo.py
│  │  │  │     │  │  ├─ win32gui_devicenotify.py
│  │  │  │     │  │  ├─ win32gui_dialog.py
│  │  │  │     │  │  ├─ win32gui_menu.py
│  │  │  │     │  │  ├─ win32gui_taskbar.py
│  │  │  │     │  │  ├─ win32netdemo.py
│  │  │  │     │  │  ├─ win32rcparser_demo.py
│  │  │  │     │  │  ├─ win32servicedemo.py
│  │  │  │     │  │  ├─ win32ts_logoff_disconnected.py
│  │  │  │     │  │  ├─ win32wnet
│  │  │  │     │  │  │  ├─ testwnet.py
│  │  │  │     │  │  │  ├─ winnetwk.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ testwnet.cpython-310.pyc
│  │  │  │     │  │  │     └─ winnetwk.cpython-310.pyc
│  │  │  │     │  │  ├─ winprocess.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ BackupRead_BackupWrite.cpython-310.pyc
│  │  │  │     │  │     ├─ BackupSeek_streamheaders.cpython-310.pyc
│  │  │  │     │  │     ├─ cerapi.cpython-310.pyc
│  │  │  │     │  │     ├─ CopyFileEx.cpython-310.pyc
│  │  │  │     │  │     ├─ CreateFileTransacted_MiniVersion.cpython-310.pyc
│  │  │  │     │  │     ├─ desktopmanager.cpython-310.pyc
│  │  │  │     │  │     ├─ eventLogDemo.cpython-310.pyc
│  │  │  │     │  │     ├─ EvtFormatMessage.cpython-310.pyc
│  │  │  │     │  │     ├─ EvtSubscribe_pull.cpython-310.pyc
│  │  │  │     │  │     ├─ EvtSubscribe_push.cpython-310.pyc
│  │  │  │     │  │     ├─ FileSecurityTest.cpython-310.pyc
│  │  │  │     │  │     ├─ getfilever.cpython-310.pyc
│  │  │  │     │  │     ├─ GetSaveFileName.cpython-310.pyc
│  │  │  │     │  │     ├─ mmapfile_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ NetValidatePasswordPolicy.cpython-310.pyc
│  │  │  │     │  │     ├─ OpenEncryptedFileRaw.cpython-310.pyc
│  │  │  │     │  │     ├─ print_desktop.cpython-310.pyc
│  │  │  │     │  │     ├─ rastest.cpython-310.pyc
│  │  │  │     │  │     ├─ RegCreateKeyTransacted.cpython-310.pyc
│  │  │  │     │  │     ├─ RegRestoreKey.cpython-310.pyc
│  │  │  │     │  │     ├─ SystemParametersInfo.cpython-310.pyc
│  │  │  │     │  │     ├─ timer_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32clipboardDemo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32clipboard_bitmapdemo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32comport_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32console_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32cred_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32fileDemo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32gui_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32gui_devicenotify.cpython-310.pyc
│  │  │  │     │  │     ├─ win32gui_dialog.cpython-310.pyc
│  │  │  │     │  │     ├─ win32gui_menu.cpython-310.pyc
│  │  │  │     │  │     ├─ win32gui_taskbar.cpython-310.pyc
│  │  │  │     │  │     ├─ win32netdemo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32rcparser_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32servicedemo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32ts_logoff_disconnected.cpython-310.pyc
│  │  │  │     │  │     └─ winprocess.cpython-310.pyc
│  │  │  │     │  ├─ include
│  │  │  │     │  │  └─ PyWinTypes.h
│  │  │  │     │  ├─ lib
│  │  │  │     │  │  ├─ afxres.py
│  │  │  │     │  │  ├─ commctrl.py
│  │  │  │     │  │  ├─ dbi.py
│  │  │  │     │  │  ├─ mmsystem.py
│  │  │  │     │  │  ├─ netbios.py
│  │  │  │     │  │  ├─ ntsecuritycon.py
│  │  │  │     │  │  ├─ pywin32_bootstrap.py
│  │  │  │     │  │  ├─ pywin32_testutil.py
│  │  │  │     │  │  ├─ pywintypes.py
│  │  │  │     │  │  ├─ rasutil.py
│  │  │  │     │  │  ├─ regcheck.py
│  │  │  │     │  │  ├─ regutil.py
│  │  │  │     │  │  ├─ sspi.py
│  │  │  │     │  │  ├─ sspicon.py
│  │  │  │     │  │  ├─ win2kras.py
│  │  │  │     │  │  ├─ win32con.py
│  │  │  │     │  │  ├─ win32cryptcon.py
│  │  │  │     │  │  ├─ win32evtlogutil.py
│  │  │  │     │  │  ├─ win32gui_struct.py
│  │  │  │     │  │  ├─ win32inetcon.py
│  │  │  │     │  │  ├─ win32netcon.py
│  │  │  │     │  │  ├─ win32pdhquery.py
│  │  │  │     │  │  ├─ win32pdhutil.py
│  │  │  │     │  │  ├─ win32rcparser.py
│  │  │  │     │  │  ├─ win32serviceutil.py
│  │  │  │     │  │  ├─ win32timezone.py
│  │  │  │     │  │  ├─ win32traceutil.py
│  │  │  │     │  │  ├─ win32verstamp.py
│  │  │  │     │  │  ├─ winerror.py
│  │  │  │     │  │  ├─ winioctlcon.py
│  │  │  │     │  │  ├─ winnt.py
│  │  │  │     │  │  ├─ winperf.py
│  │  │  │     │  │  ├─ winxptheme.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ afxres.cpython-310.pyc
│  │  │  │     │  │     ├─ commctrl.cpython-310.pyc
│  │  │  │     │  │     ├─ dbi.cpython-310.pyc
│  │  │  │     │  │     ├─ mmsystem.cpython-310.pyc
│  │  │  │     │  │     ├─ netbios.cpython-310.pyc
│  │  │  │     │  │     ├─ ntsecuritycon.cpython-310.pyc
│  │  │  │     │  │     ├─ pywin32_bootstrap.cpython-310.pyc
│  │  │  │     │  │     ├─ pywin32_testutil.cpython-310.pyc
│  │  │  │     │  │     ├─ pywintypes.cpython-310.pyc
│  │  │  │     │  │     ├─ rasutil.cpython-310.pyc
│  │  │  │     │  │     ├─ regcheck.cpython-310.pyc
│  │  │  │     │  │     ├─ regutil.cpython-310.pyc
│  │  │  │     │  │     ├─ sspi.cpython-310.pyc
│  │  │  │     │  │     ├─ sspicon.cpython-310.pyc
│  │  │  │     │  │     ├─ win2kras.cpython-310.pyc
│  │  │  │     │  │     ├─ win32con.cpython-310.pyc
│  │  │  │     │  │     ├─ win32cryptcon.cpython-310.pyc
│  │  │  │     │  │     ├─ win32evtlogutil.cpython-310.pyc
│  │  │  │     │  │     ├─ win32gui_struct.cpython-310.pyc
│  │  │  │     │  │     ├─ win32inetcon.cpython-310.pyc
│  │  │  │     │  │     ├─ win32netcon.cpython-310.pyc
│  │  │  │     │  │     ├─ win32pdhquery.cpython-310.pyc
│  │  │  │     │  │     ├─ win32pdhutil.cpython-310.pyc
│  │  │  │     │  │     ├─ win32rcparser.cpython-310.pyc
│  │  │  │     │  │     ├─ win32serviceutil.cpython-310.pyc
│  │  │  │     │  │     ├─ win32timezone.cpython-310.pyc
│  │  │  │     │  │     ├─ win32traceutil.cpython-310.pyc
│  │  │  │     │  │     ├─ win32verstamp.cpython-310.pyc
│  │  │  │     │  │     ├─ winerror.cpython-310.pyc
│  │  │  │     │  │     ├─ winioctlcon.cpython-310.pyc
│  │  │  │     │  │     ├─ winnt.cpython-310.pyc
│  │  │  │     │  │     ├─ winperf.cpython-310.pyc
│  │  │  │     │  │     └─ winxptheme.cpython-310.pyc
│  │  │  │     │  ├─ libs
│  │  │  │     │  │  └─ pywintypes.lib
│  │  │  │     │  ├─ license.txt
│  │  │  │     │  ├─ mmapfile.pyd
│  │  │  │     │  ├─ odbc.pyd
│  │  │  │     │  ├─ perfmon.pyd
│  │  │  │     │  ├─ perfmondata.dll
│  │  │  │     │  ├─ pythonservice.exe
│  │  │  │     │  ├─ scripts
│  │  │  │     │  │  ├─ backupEventLog.py
│  │  │  │     │  │  ├─ ce
│  │  │  │     │  │  │  ├─ pysynch.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ pysynch.cpython-310.pyc
│  │  │  │     │  │  ├─ ControlService.py
│  │  │  │     │  │  ├─ killProcName.py
│  │  │  │     │  │  ├─ rasutil.py
│  │  │  │     │  │  ├─ regsetup.py
│  │  │  │     │  │  ├─ setup_d.py
│  │  │  │     │  │  ├─ VersionStamp
│  │  │  │     │  │  │  ├─ BrandProject.py
│  │  │  │     │  │  │  ├─ bulkstamp.py
│  │  │  │     │  │  │  ├─ vssutil.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ BrandProject.cpython-310.pyc
│  │  │  │     │  │  │     ├─ bulkstamp.cpython-310.pyc
│  │  │  │     │  │  │     └─ vssutil.cpython-310.pyc
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ backupEventLog.cpython-310.pyc
│  │  │  │     │  │     ├─ ControlService.cpython-310.pyc
│  │  │  │     │  │     ├─ killProcName.cpython-310.pyc
│  │  │  │     │  │     ├─ rasutil.cpython-310.pyc
│  │  │  │     │  │     ├─ regsetup.cpython-310.pyc
│  │  │  │     │  │     └─ setup_d.cpython-310.pyc
│  │  │  │     │  ├─ servicemanager.pyd
│  │  │  │     │  ├─ test
│  │  │  │     │  │  ├─ handles.py
│  │  │  │     │  │  ├─ testall.py
│  │  │  │     │  │  ├─ test_clipboard.py
│  │  │  │     │  │  ├─ test_exceptions.py
│  │  │  │     │  │  ├─ test_odbc.py
│  │  │  │     │  │  ├─ test_pywintypes.py
│  │  │  │     │  │  ├─ test_security.py
│  │  │  │     │  │  ├─ test_sspi.py
│  │  │  │     │  │  ├─ test_win32api.py
│  │  │  │     │  │  ├─ test_win32crypt.py
│  │  │  │     │  │  ├─ test_win32event.py
│  │  │  │     │  │  ├─ test_win32file.py
│  │  │  │     │  │  ├─ test_win32gui.py
│  │  │  │     │  │  ├─ test_win32guistruct.py
│  │  │  │     │  │  ├─ test_win32inet.py
│  │  │  │     │  │  ├─ test_win32net.py
│  │  │  │     │  │  ├─ test_win32pipe.py
│  │  │  │     │  │  ├─ test_win32print.py
│  │  │  │     │  │  ├─ test_win32profile.py
│  │  │  │     │  │  ├─ test_win32rcparser.py
│  │  │  │     │  │  ├─ test_win32timezone.py
│  │  │  │     │  │  ├─ test_win32trace.py
│  │  │  │     │  │  ├─ test_win32wnet.py
│  │  │  │     │  │  ├─ win32rcparser
│  │  │  │     │  │  │  ├─ python.bmp
│  │  │  │     │  │  │  ├─ python.ico
│  │  │  │     │  │  │  ├─ test.h
│  │  │  │     │  │  │  └─ test.rc
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ handles.cpython-310.pyc
│  │  │  │     │  │     ├─ testall.cpython-310.pyc
│  │  │  │     │  │     ├─ test_clipboard.cpython-310.pyc
│  │  │  │     │  │     ├─ test_exceptions.cpython-310.pyc
│  │  │  │     │  │     ├─ test_odbc.cpython-310.pyc
│  │  │  │     │  │     ├─ test_pywintypes.cpython-310.pyc
│  │  │  │     │  │     ├─ test_security.cpython-310.pyc
│  │  │  │     │  │     ├─ test_sspi.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32api.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32crypt.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32event.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32file.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32gui.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32guistruct.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32inet.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32net.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32pipe.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32print.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32profile.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32rcparser.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32timezone.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32trace.cpython-310.pyc
│  │  │  │     │  │     └─ test_win32wnet.cpython-310.pyc
│  │  │  │     │  ├─ timer.pyd
│  │  │  │     │  ├─ win32api.pyd
│  │  │  │     │  ├─ win32clipboard.pyd
│  │  │  │     │  ├─ win32console.pyd
│  │  │  │     │  ├─ win32cred.pyd
│  │  │  │     │  ├─ win32crypt.pyd
│  │  │  │     │  ├─ win32event.pyd
│  │  │  │     │  ├─ win32evtlog.pyd
│  │  │  │     │  ├─ win32file.pyd
│  │  │  │     │  ├─ win32gui.pyd
│  │  │  │     │  ├─ win32help.pyd
│  │  │  │     │  ├─ win32inet.pyd
│  │  │  │     │  ├─ win32job.pyd
│  │  │  │     │  ├─ win32lz.pyd
│  │  │  │     │  ├─ win32net.pyd
│  │  │  │     │  ├─ win32pdh.pyd
│  │  │  │     │  ├─ win32pipe.pyd
│  │  │  │     │  ├─ win32print.pyd
│  │  │  │     │  ├─ win32process.pyd
│  │  │  │     │  ├─ win32profile.pyd
│  │  │  │     │  ├─ win32ras.pyd
│  │  │  │     │  ├─ win32security.pyd
│  │  │  │     │  ├─ win32service.pyd
│  │  │  │     │  ├─ win32trace.pyd
│  │  │  │     │  ├─ win32transaction.pyd
│  │  │  │     │  ├─ win32ts.pyd
│  │  │  │     │  ├─ win32wnet.pyd
│  │  │  │     │  ├─ winxpgui.pyd
│  │  │  │     │  ├─ _win32sysloader.pyd
│  │  │  │     │  └─ _winxptheme.pyd
│  │  │  │     ├─ win32com
│  │  │  │     │  ├─ client
│  │  │  │     │  │  ├─ build.py
│  │  │  │     │  │  ├─ CLSIDToClass.py
│  │  │  │     │  │  ├─ combrowse.py
│  │  │  │     │  │  ├─ connect.py
│  │  │  │     │  │  ├─ dynamic.py
│  │  │  │     │  │  ├─ gencache.py
│  │  │  │     │  │  ├─ genpy.py
│  │  │  │     │  │  ├─ makepy.py
│  │  │  │     │  │  ├─ selecttlb.py
│  │  │  │     │  │  ├─ tlbrowse.py
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ build.cpython-310.pyc
│  │  │  │     │  │     ├─ CLSIDToClass.cpython-310.pyc
│  │  │  │     │  │     ├─ combrowse.cpython-310.pyc
│  │  │  │     │  │     ├─ connect.cpython-310.pyc
│  │  │  │     │  │     ├─ dynamic.cpython-310.pyc
│  │  │  │     │  │     ├─ gencache.cpython-310.pyc
│  │  │  │     │  │     ├─ genpy.cpython-310.pyc
│  │  │  │     │  │     ├─ makepy.cpython-310.pyc
│  │  │  │     │  │     ├─ selecttlb.cpython-310.pyc
│  │  │  │     │  │     ├─ tlbrowse.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ demos
│  │  │  │     │  │  ├─ connect.py
│  │  │  │     │  │  ├─ dump_clipboard.py
│  │  │  │     │  │  ├─ eventsApartmentThreaded.py
│  │  │  │     │  │  ├─ eventsFreeThreaded.py
│  │  │  │     │  │  ├─ excelAddin.py
│  │  │  │     │  │  ├─ excelRTDServer.py
│  │  │  │     │  │  ├─ iebutton.py
│  │  │  │     │  │  ├─ ietoolbar.py
│  │  │  │     │  │  ├─ outlookAddin.py
│  │  │  │     │  │  ├─ trybag.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ connect.cpython-310.pyc
│  │  │  │     │  │     ├─ dump_clipboard.cpython-310.pyc
│  │  │  │     │  │     ├─ eventsApartmentThreaded.cpython-310.pyc
│  │  │  │     │  │     ├─ eventsFreeThreaded.cpython-310.pyc
│  │  │  │     │  │     ├─ excelAddin.cpython-310.pyc
│  │  │  │     │  │     ├─ excelRTDServer.cpython-310.pyc
│  │  │  │     │  │     ├─ iebutton.cpython-310.pyc
│  │  │  │     │  │     ├─ ietoolbar.cpython-310.pyc
│  │  │  │     │  │     ├─ outlookAddin.cpython-310.pyc
│  │  │  │     │  │     ├─ trybag.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ HTML
│  │  │  │     │  │  ├─ docindex.html
│  │  │  │     │  │  ├─ GeneratedSupport.html
│  │  │  │     │  │  ├─ image
│  │  │  │     │  │  │  ├─ blank.gif
│  │  │  │     │  │  │  ├─ BTN_HomePage.gif
│  │  │  │     │  │  │  ├─ BTN_ManualTop.gif
│  │  │  │     │  │  │  ├─ BTN_NextPage.gif
│  │  │  │     │  │  │  ├─ BTN_PrevPage.gif
│  │  │  │     │  │  │  ├─ pycom_blowing.gif
│  │  │  │     │  │  │  ├─ pythoncom.gif
│  │  │  │     │  │  │  └─ www_icon.gif
│  │  │  │     │  │  ├─ index.html
│  │  │  │     │  │  ├─ misc.html
│  │  │  │     │  │  ├─ package.html
│  │  │  │     │  │  ├─ PythonCOM.html
│  │  │  │     │  │  ├─ QuickStartClientCom.html
│  │  │  │     │  │  ├─ QuickStartServerCom.html
│  │  │  │     │  │  └─ variant.html
│  │  │  │     │  ├─ include
│  │  │  │     │  │  ├─ PythonCOM.h
│  │  │  │     │  │  ├─ PythonCOMRegister.h
│  │  │  │     │  │  └─ PythonCOMServer.h
│  │  │  │     │  ├─ libs
│  │  │  │     │  │  ├─ axscript.lib
│  │  │  │     │  │  └─ pythoncom.lib
│  │  │  │     │  ├─ License.txt
│  │  │  │     │  ├─ makegw
│  │  │  │     │  │  ├─ makegw.py
│  │  │  │     │  │  ├─ makegwenum.py
│  │  │  │     │  │  ├─ makegwparse.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ makegw.cpython-310.pyc
│  │  │  │     │  │     ├─ makegwenum.cpython-310.pyc
│  │  │  │     │  │     ├─ makegwparse.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ olectl.py
│  │  │  │     │  ├─ readme.html
│  │  │  │     │  ├─ server
│  │  │  │     │  │  ├─ connect.py
│  │  │  │     │  │  ├─ dispatcher.py
│  │  │  │     │  │  ├─ exception.py
│  │  │  │     │  │  ├─ factory.py
│  │  │  │     │  │  ├─ localserver.py
│  │  │  │     │  │  ├─ policy.py
│  │  │  │     │  │  ├─ register.py
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ connect.cpython-310.pyc
│  │  │  │     │  │     ├─ dispatcher.cpython-310.pyc
│  │  │  │     │  │     ├─ exception.cpython-310.pyc
│  │  │  │     │  │     ├─ factory.cpython-310.pyc
│  │  │  │     │  │     ├─ localserver.cpython-310.pyc
│  │  │  │     │  │     ├─ policy.cpython-310.pyc
│  │  │  │     │  │     ├─ register.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ servers
│  │  │  │     │  │  ├─ dictionary.py
│  │  │  │     │  │  ├─ interp.py
│  │  │  │     │  │  ├─ perfmon.py
│  │  │  │     │  │  ├─ PythonTools.py
│  │  │  │     │  │  ├─ test_pycomtest.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ dictionary.cpython-310.pyc
│  │  │  │     │  │     ├─ interp.cpython-310.pyc
│  │  │  │     │  │     ├─ perfmon.cpython-310.pyc
│  │  │  │     │  │     ├─ PythonTools.cpython-310.pyc
│  │  │  │     │  │     ├─ test_pycomtest.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ storagecon.py
│  │  │  │     │  ├─ test
│  │  │  │     │  │  ├─ daodump.py
│  │  │  │     │  │  ├─ errorSemantics.py
│  │  │  │     │  │  ├─ GenTestScripts.py
│  │  │  │     │  │  ├─ pippo.idl
│  │  │  │     │  │  ├─ pippo_server.py
│  │  │  │     │  │  ├─ policySemantics.py
│  │  │  │     │  │  ├─ readme.txt
│  │  │  │     │  │  ├─ testAccess.py
│  │  │  │     │  │  ├─ testADOEvents.py
│  │  │  │     │  │  ├─ testall.py
│  │  │  │     │  │  ├─ testArrays.py
│  │  │  │     │  │  ├─ testAXScript.py
│  │  │  │     │  │  ├─ testClipboard.py
│  │  │  │     │  │  ├─ testCollections.py
│  │  │  │     │  │  ├─ testConversionErrors.py
│  │  │  │     │  │  ├─ testDates.py
│  │  │  │     │  │  ├─ testDCOM.py
│  │  │  │     │  │  ├─ testDictionary.py
│  │  │  │     │  │  ├─ testDictionary.vbs
│  │  │  │     │  │  ├─ testDynamic.py
│  │  │  │     │  │  ├─ testExchange.py
│  │  │  │     │  │  ├─ testExplorer.py
│  │  │  │     │  │  ├─ testGatewayAddresses.py
│  │  │  │     │  │  ├─ testGIT.py
│  │  │  │     │  │  ├─ testInterp.vbs
│  │  │  │     │  │  ├─ testIterators.py
│  │  │  │     │  │  ├─ testmakepy.py
│  │  │  │     │  │  ├─ testMarshal.py
│  │  │  │     │  │  ├─ testMSOffice.py
│  │  │  │     │  │  ├─ testMSOfficeEvents.py
│  │  │  │     │  │  ├─ testNetscape.py
│  │  │  │     │  │  ├─ testPersist.py
│  │  │  │     │  │  ├─ testPippo.py
│  │  │  │     │  │  ├─ testPyComTest.py
│  │  │  │     │  │  ├─ Testpys.sct
│  │  │  │     │  │  ├─ testPyScriptlet.js
│  │  │  │     │  │  ├─ testROT.py
│  │  │  │     │  │  ├─ testServers.py
│  │  │  │     │  │  ├─ testShell.py
│  │  │  │     │  │  ├─ testStorage.py
│  │  │  │     │  │  ├─ testStreams.py
│  │  │  │     │  │  ├─ testvb.py
│  │  │  │     │  │  ├─ testvbscript_regexp.py
│  │  │  │     │  │  ├─ testWMI.py
│  │  │  │     │  │  ├─ testxslt.js
│  │  │  │     │  │  ├─ testxslt.py
│  │  │  │     │  │  ├─ testxslt.xsl
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ daodump.cpython-310.pyc
│  │  │  │     │  │     ├─ errorSemantics.cpython-310.pyc
│  │  │  │     │  │     ├─ GenTestScripts.cpython-310.pyc
│  │  │  │     │  │     ├─ pippo_server.cpython-310.pyc
│  │  │  │     │  │     ├─ policySemantics.cpython-310.pyc
│  │  │  │     │  │     ├─ testAccess.cpython-310.pyc
│  │  │  │     │  │     ├─ testADOEvents.cpython-310.pyc
│  │  │  │     │  │     ├─ testall.cpython-310.pyc
│  │  │  │     │  │     ├─ testArrays.cpython-310.pyc
│  │  │  │     │  │     ├─ testAXScript.cpython-310.pyc
│  │  │  │     │  │     ├─ testClipboard.cpython-310.pyc
│  │  │  │     │  │     ├─ testCollections.cpython-310.pyc
│  │  │  │     │  │     ├─ testConversionErrors.cpython-310.pyc
│  │  │  │     │  │     ├─ testDates.cpython-310.pyc
│  │  │  │     │  │     ├─ testDCOM.cpython-310.pyc
│  │  │  │     │  │     ├─ testDictionary.cpython-310.pyc
│  │  │  │     │  │     ├─ testDynamic.cpython-310.pyc
│  │  │  │     │  │     ├─ testExchange.cpython-310.pyc
│  │  │  │     │  │     ├─ testExplorer.cpython-310.pyc
│  │  │  │     │  │     ├─ testGatewayAddresses.cpython-310.pyc
│  │  │  │     │  │     ├─ testGIT.cpython-310.pyc
│  │  │  │     │  │     ├─ testIterators.cpython-310.pyc
│  │  │  │     │  │     ├─ testmakepy.cpython-310.pyc
│  │  │  │     │  │     ├─ testMarshal.cpython-310.pyc
│  │  │  │     │  │     ├─ testMSOffice.cpython-310.pyc
│  │  │  │     │  │     ├─ testMSOfficeEvents.cpython-310.pyc
│  │  │  │     │  │     ├─ testNetscape.cpython-310.pyc
│  │  │  │     │  │     ├─ testPersist.cpython-310.pyc
│  │  │  │     │  │     ├─ testPippo.cpython-310.pyc
│  │  │  │     │  │     ├─ testPyComTest.cpython-310.pyc
│  │  │  │     │  │     ├─ testROT.cpython-310.pyc
│  │  │  │     │  │     ├─ testServers.cpython-310.pyc
│  │  │  │     │  │     ├─ testShell.cpython-310.pyc
│  │  │  │     │  │     ├─ testStorage.cpython-310.pyc
│  │  │  │     │  │     ├─ testStreams.cpython-310.pyc
│  │  │  │     │  │     ├─ testvb.cpython-310.pyc
│  │  │  │     │  │     ├─ testvbscript_regexp.cpython-310.pyc
│  │  │  │     │  │     ├─ testWMI.cpython-310.pyc
│  │  │  │     │  │     ├─ testxslt.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ universal.py
│  │  │  │     │  ├─ util.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ olectl.cpython-310.pyc
│  │  │  │     │     ├─ storagecon.cpython-310.pyc
│  │  │  │     │     ├─ universal.cpython-310.pyc
│  │  │  │     │     ├─ util.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ win32comext
│  │  │  │     │  ├─ adsi
│  │  │  │     │  │  ├─ adsi.pyd
│  │  │  │     │  │  ├─ adsicon.py
│  │  │  │     │  │  ├─ demos
│  │  │  │     │  │  │  ├─ objectPicker.py
│  │  │  │     │  │  │  ├─ scp.py
│  │  │  │     │  │  │  ├─ search.py
│  │  │  │     │  │  │  ├─ test.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ objectPicker.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scp.cpython-310.pyc
│  │  │  │     │  │  │     ├─ search.cpython-310.pyc
│  │  │  │     │  │  │     └─ test.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ adsicon.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ authorization
│  │  │  │     │  │  ├─ authorization.pyd
│  │  │  │     │  │  ├─ demos
│  │  │  │     │  │  │  ├─ EditSecurity.py
│  │  │  │     │  │  │  ├─ EditServiceSecurity.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ EditSecurity.cpython-310.pyc
│  │  │  │     │  │  │     └─ EditServiceSecurity.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ axcontrol
│  │  │  │     │  │  ├─ axcontrol.pyd
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ axdebug
│  │  │  │     │  │  ├─ adb.py
│  │  │  │     │  │  ├─ codecontainer.py
│  │  │  │     │  │  ├─ contexts.py
│  │  │  │     │  │  ├─ debugger.py
│  │  │  │     │  │  ├─ documents.py
│  │  │  │     │  │  ├─ dump.py
│  │  │  │     │  │  ├─ expressions.py
│  │  │  │     │  │  ├─ gateways.py
│  │  │  │     │  │  ├─ stackframe.py
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ adb.cpython-310.pyc
│  │  │  │     │  │     ├─ codecontainer.cpython-310.pyc
│  │  │  │     │  │     ├─ contexts.cpython-310.pyc
│  │  │  │     │  │     ├─ debugger.cpython-310.pyc
│  │  │  │     │  │     ├─ documents.cpython-310.pyc
│  │  │  │     │  │     ├─ dump.cpython-310.pyc
│  │  │  │     │  │     ├─ expressions.cpython-310.pyc
│  │  │  │     │  │     ├─ gateways.cpython-310.pyc
│  │  │  │     │  │     ├─ stackframe.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ axscript
│  │  │  │     │  │  ├─ asputil.py
│  │  │  │     │  │  ├─ axscript.pyd
│  │  │  │     │  │  ├─ client
│  │  │  │     │  │  │  ├─ debug.py
│  │  │  │     │  │  │  ├─ error.py
│  │  │  │     │  │  │  ├─ framework.py
│  │  │  │     │  │  │  ├─ pydumper.py
│  │  │  │     │  │  │  ├─ pyscript.py
│  │  │  │     │  │  │  ├─ pyscript_rexec.py
│  │  │  │     │  │  │  ├─ scriptdispatch.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ debug.cpython-310.pyc
│  │  │  │     │  │  │     ├─ error.cpython-310.pyc
│  │  │  │     │  │  │     ├─ framework.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pydumper.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pyscript.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pyscript_rexec.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scriptdispatch.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ Demos
│  │  │  │     │  │  │  └─ client
│  │  │  │     │  │  │     ├─ asp
│  │  │  │     │  │  │     │  ├─ caps.asp
│  │  │  │     │  │  │     │  ├─ CreateObject.asp
│  │  │  │     │  │  │     │  ├─ interrupt
│  │  │  │     │  │  │     │  │  ├─ test.asp
│  │  │  │     │  │  │     │  │  ├─ test.html
│  │  │  │     │  │  │     │  │  ├─ test1.asp
│  │  │  │     │  │  │     │  │  └─ test1.html
│  │  │  │     │  │  │     │  └─ tut1.asp
│  │  │  │     │  │  │     ├─ ie
│  │  │  │     │  │  │     │  ├─ calc.htm
│  │  │  │     │  │  │     │  ├─ dbgtest.htm
│  │  │  │     │  │  │     │  ├─ demo.htm
│  │  │  │     │  │  │     │  ├─ demo_check.htm
│  │  │  │     │  │  │     │  ├─ demo_intro.htm
│  │  │  │     │  │  │     │  ├─ demo_menu.htm
│  │  │  │     │  │  │     │  ├─ docwrite.htm
│  │  │  │     │  │  │     │  ├─ foo2.htm
│  │  │  │     │  │  │     │  ├─ form.htm
│  │  │  │     │  │  │     │  ├─ marqueeDemo.htm
│  │  │  │     │  │  │     │  ├─ MarqueeText1.htm
│  │  │  │     │  │  │     │  ├─ mousetrack.htm
│  │  │  │     │  │  │     │  └─ pycom_blowing.gif
│  │  │  │     │  │  │     └─ wsh
│  │  │  │     │  │  │        ├─ blank.pys
│  │  │  │     │  │  │        ├─ excel.pys
│  │  │  │     │  │  │        ├─ registry.pys
│  │  │  │     │  │  │        └─ test.pys
│  │  │  │     │  │  ├─ server
│  │  │  │     │  │  │  ├─ axsite.py
│  │  │  │     │  │  │  ├─ error.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ axsite.cpython-310.pyc
│  │  │  │     │  │  │     ├─ error.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ test
│  │  │  │     │  │  │  ├─ debugTest.pys
│  │  │  │     │  │  │  ├─ debugTest.vbs
│  │  │  │     │  │  │  ├─ leakTest.py
│  │  │  │     │  │  │  ├─ testHost.py
│  │  │  │     │  │  │  ├─ testHost4Dbg.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ leakTest.cpython-310.pyc
│  │  │  │     │  │  │     ├─ testHost.cpython-310.pyc
│  │  │  │     │  │  │     └─ testHost4Dbg.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ asputil.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ bits
│  │  │  │     │  │  ├─ bits.pyd
│  │  │  │     │  │  ├─ test
│  │  │  │     │  │  │  ├─ show_all_jobs.py
│  │  │  │     │  │  │  ├─ test_bits.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ show_all_jobs.cpython-310.pyc
│  │  │  │     │  │  │     └─ test_bits.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ directsound
│  │  │  │     │  │  ├─ directsound.pyd
│  │  │  │     │  │  ├─ test
│  │  │  │     │  │  │  ├─ ds_record.py
│  │  │  │     │  │  │  ├─ ds_test.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ ds_record.cpython-310.pyc
│  │  │  │     │  │  │     ├─ ds_test.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ ifilter
│  │  │  │     │  │  ├─ demo
│  │  │  │     │  │  │  ├─ filterDemo.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ filterDemo.cpython-310.pyc
│  │  │  │     │  │  ├─ ifilter.pyd
│  │  │  │     │  │  ├─ ifiltercon.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ ifiltercon.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ internet
│  │  │  │     │  │  ├─ inetcon.py
│  │  │  │     │  │  ├─ internet.pyd
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ inetcon.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ mapi
│  │  │  │     │  │  ├─ demos
│  │  │  │     │  │  │  ├─ mapisend.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ mapisend.cpython-310.pyc
│  │  │  │     │  │  ├─ emsabtags.py
│  │  │  │     │  │  ├─ exchange.pyd
│  │  │  │     │  │  ├─ mapi.pyd
│  │  │  │     │  │  ├─ mapitags.py
│  │  │  │     │  │  ├─ mapiutil.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ emsabtags.cpython-310.pyc
│  │  │  │     │  │     ├─ mapitags.cpython-310.pyc
│  │  │  │     │  │     ├─ mapiutil.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ propsys
│  │  │  │     │  │  ├─ propsys.pyd
│  │  │  │     │  │  ├─ pscon.py
│  │  │  │     │  │  ├─ test
│  │  │  │     │  │  │  ├─ testpropsys.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ testpropsys.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ pscon.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ shell
│  │  │  │     │  │  ├─ demos
│  │  │  │     │  │  │  ├─ browse_for_folder.py
│  │  │  │     │  │  │  ├─ create_link.py
│  │  │  │     │  │  │  ├─ dump_link.py
│  │  │  │     │  │  │  ├─ explorer_browser.py
│  │  │  │     │  │  │  ├─ IActiveDesktop.py
│  │  │  │     │  │  │  ├─ IFileOperationProgressSink.py
│  │  │  │     │  │  │  ├─ IShellLinkDataList.py
│  │  │  │     │  │  │  ├─ ITransferAdviseSink.py
│  │  │  │     │  │  │  ├─ IUniformResourceLocator.py
│  │  │  │     │  │  │  ├─ servers
│  │  │  │     │  │  │  │  ├─ column_provider.py
│  │  │  │     │  │  │  │  ├─ context_menu.py
│  │  │  │     │  │  │  │  ├─ copy_hook.py
│  │  │  │     │  │  │  │  ├─ empty_volume_cache.py
│  │  │  │     │  │  │  │  ├─ folder_view.py
│  │  │  │     │  │  │  │  ├─ icon_handler.py
│  │  │  │     │  │  │  │  ├─ shell_view.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ column_provider.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ context_menu.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ copy_hook.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ empty_volume_cache.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ folder_view.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ icon_handler.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ shell_view.cpython-310.pyc
│  │  │  │     │  │  │  ├─ shellexecuteex.py
│  │  │  │     │  │  │  ├─ viewstate.py
│  │  │  │     │  │  │  ├─ walk_shell_folders.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ browse_for_folder.cpython-310.pyc
│  │  │  │     │  │  │     ├─ create_link.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dump_link.cpython-310.pyc
│  │  │  │     │  │  │     ├─ explorer_browser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IActiveDesktop.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IFileOperationProgressSink.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IShellLinkDataList.cpython-310.pyc
│  │  │  │     │  │  │     ├─ ITransferAdviseSink.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IUniformResourceLocator.cpython-310.pyc
│  │  │  │     │  │  │     ├─ shellexecuteex.cpython-310.pyc
│  │  │  │     │  │  │     ├─ viewstate.cpython-310.pyc
│  │  │  │     │  │  │     └─ walk_shell_folders.cpython-310.pyc
│  │  │  │     │  │  ├─ shell.pyd
│  │  │  │     │  │  ├─ shellcon.py
│  │  │  │     │  │  ├─ test
│  │  │  │     │  │  │  ├─ testShellFolder.py
│  │  │  │     │  │  │  ├─ testShellItem.py
│  │  │  │     │  │  │  ├─ testSHFileOperation.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ testShellFolder.cpython-310.pyc
│  │  │  │     │  │  │     ├─ testShellItem.cpython-310.pyc
│  │  │  │     │  │  │     └─ testSHFileOperation.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ shellcon.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  └─ taskscheduler
│  │  │  │     │     ├─ taskscheduler.pyd
│  │  │  │     │     ├─ test
│  │  │  │     │     │  ├─ test_addtask.py
│  │  │  │     │     │  ├─ test_addtask_1.py
│  │  │  │     │     │  ├─ test_addtask_2.py
│  │  │  │     │     │  ├─ test_localsystem.py
│  │  │  │     │     │  └─ __pycache__
│  │  │  │     │     │     ├─ test_addtask.cpython-310.pyc
│  │  │  │     │     │     ├─ test_addtask_1.cpython-310.pyc
│  │  │  │     │     │     ├─ test_addtask_2.cpython-310.pyc
│  │  │  │     │     │     └─ test_localsystem.cpython-310.pyc
│  │  │  │     │     ├─ __init__.py
│  │  │  │     │     └─ __pycache__
│  │  │  │     │        └─ __init__.cpython-310.pyc
│  │  │  │     ├─ _cffi_backend.cp310-win_amd64.pyd
│  │  │  │     ├─ _distutils_hack
│  │  │  │     │  ├─ override.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ override.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     └─ __pycache__
│  │  │  │        ├─ pythoncom.cpython-310.pyc
│  │  │  │        ├─ six.cpython-310.pyc
│  │  │  │        └─ typing_extensions.cpython-310.pyc
│  │  │  ├─ pyvenv.cfg
│  │  │  └─ Scripts
│  │  │     ├─ activate
│  │  │     ├─ activate.bat
│  │  │     ├─ Activate.ps1
│  │  │     ├─ deactivate.bat
│  │  │     ├─ normalizer.exe
│  │  │     ├─ pip.exe
│  │  │     ├─ pip3.10.exe
│  │  │     ├─ pip3.exe
│  │  │     ├─ python.exe
│  │  │     ├─ pythonw.exe
│  │  │     ├─ pywin32_postinstall.py
│  │  │     ├─ pywin32_testall.py
│  │  │     └─ __pycache__
│  │  │        ├─ pywin32_postinstall.cpython-310.pyc
│  │  │        └─ pywin32_testall.cpython-310.pyc
│  │  ├─ .vscode
│  │  │  ├─ extensions.json
│  │  │  ├─ launch.json
│  │  │  ├─ settings.json
│  │  │  └─ tasks.json
│  │  ├─ function_app.py
│  │  ├─ host.json
│  │  ├─ local.settings.json
│  │  ├─ requirements.txt
│  │  ├─ __azurite_db_blob_extent__.json
│  │  ├─ __azurite_db_blob__.json
│  │  └─ __blobstorage__
│  │     └─ 3eddb2ee-b8da-488a-b4ac-920c0ea8c25c
│  ├─ images
│  │  ├─ apim-function-apps.drawio.svg
│  │  ├─ copy_data_task.png
│  │  ├─ create_new_dataset.png
│  │  ├─ datalake_storage_gen2.png
│  │  ├─ edit-custom-connector.png
│  │  ├─ json_file_format.png
│  │  ├─ linkedService.png
│  │  ├─ logging_notebook.png
│  │  ├─ pagination.png
│  │  ├─ relative_url.png
│  │  ├─ service-user-architecture.drawio.svg
│  │  ├─ sink_dataset.png
│  │  ├─ source_dataset.png
│  │  ├─ swagger-inspector.png
│  │  ├─ swaggerhub.png
│  │  ├─ zendesk-built-in.jpg
│  │  ├─ zendesk-created-workflow.png
│  │  ├─ zendesk-custom.jpg
│  │  └─ zendesk-logo.png
│  ├─ infrastructure
│  │  ├─ .terraform
│  │  │  └─ modules
│  │  │     ├─ azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ bastion_host.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ bastion_host_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ devops_agent_pool.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ devops_agent_pool_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ logic_app.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ logic_app_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ modules.json
│  │  │     ├─ odt_pe_backoffice_sb.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ odt_pe_backoffice_sb_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_data_lake.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_data_lake_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_ingestion.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_ingestion_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_management.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_management_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_monitoring.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_monitoring_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_network.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_network.subnets
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ main.tf
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ test
│  │  │     │  │  ├─ null_name.tf
│  │  │     │  │  ├─ README.md
│  │  │     │  │  └─ simple.tf
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_network_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_network_failover.subnets
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ main.tf
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ test
│  │  │     │  │  ├─ null_name.tf
│  │  │     │  │  ├─ README.md
│  │  │     │  │  └─ simple.tf
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_shir.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_shir_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_sql_server.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_sql_server_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_workspace_private.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     └─ synapse_workspace_private_failover.azure_region
│  │  │        ├─ CHANGELOG.md
│  │  │        ├─ CONTRIBUTING.md
│  │  │        ├─ examples
│  │  │        │  └─ main
│  │  │        │     ├─ main.tf
│  │  │        │     └─ modules.tf
│  │  │        ├─ LICENSE
│  │  │        ├─ NOTICE
│  │  │        ├─ outputs.tf
│  │  │        ├─ README.md
│  │  │        ├─ REGIONS.md
│  │  │        ├─ regions.tf
│  │  │        ├─ terraform.tfvars.ci
│  │  │        ├─ variables.tf
│  │  │        └─ versions.tf
│  │  ├─ .terraform.lock.hcl
│  │  ├─ configuration
│  │  │  ├─ data-lake
│  │  │  │  ├─ .DS_Store
│  │  │  │  ├─ curated_table_definitions
│  │  │  │  │  ├─ employee.json
│  │  │  │  │  ├─ mipins_hr_measures.json
│  │  │  │  │  └─ nsip_relevant_reps.json
│  │  │  │  ├─ harmonised_table_definitions
│  │  │  │  │  ├─ casework_additional_fields_dim.json
│  │  │  │  │  ├─ casework_advert_details_dim.json
│  │  │  │  │  ├─ casework_all_appeals_additional_data_dim.json
│  │  │  │  │  ├─ casework_all_appeals_dim.json
│  │  │  │  │  ├─ casework_application_sub_type_case_name_dim.json
│  │  │  │  │  ├─ casework_case_dates_dim.json
│  │  │  │  │  ├─ casework_case_fact.json
│  │  │  │  │  ├─ casework_case_info_dim.json
│  │  │  │  │  ├─ casework_case_officer_additional_details_dim.json
│  │  │  │  │  ├─ casework_common_land_dim.json
│  │  │  │  │  ├─ casework_contacts_organisation_dim.json
│  │  │  │  │  ├─ casework_contact_information_dim.json
│  │  │  │  │  ├─ casework_decision_issue_dim.json
│  │  │  │  │  ├─ casework_enforcement_grounds_dim.json
│  │  │  │  │  ├─ casework_event_dim.json
│  │  │  │  │  ├─ casework_event_fact.json
│  │  │  │  │  ├─ casework_examination_timetable_dim.json
│  │  │  │  │  ├─ casework_hedgerow_dim.json
│  │  │  │  │  ├─ casework_high_hedges_dim.json
│  │  │  │  │  ├─ casework_inspector_cases_dim.json
│  │  │  │  │  ├─ casework_legacy_rights_of_way_dim.json
│  │  │  │  │  ├─ casework_local_planning_authority_dim.json
│  │  │  │  │  ├─ casework_local_planning_authority_fact.json
│  │  │  │  │  ├─ casework_local_plans_dim.json
│  │  │  │  │  ├─ casework_lpa_responsibility_dim.json
│  │  │  │  │  ├─ casework_nsip_advice_dim.json
│  │  │  │  │  ├─ casework_nsip_examination_timetable_dim.json
│  │  │  │  │  ├─ casework_nsip_project_info_internal_dim.json
│  │  │  │  │  ├─ casework_nsip_redactions_dim.json
│  │  │  │  │  ├─ casework_nsip_relevant_representation_dim.json
│  │  │  │  │  ├─ casework_picaso_dim.json
│  │  │  │  │  ├─ casework_picasso_dim.json
│  │  │  │  │  ├─ casework_specialism_dim.json
│  │  │  │  │  ├─ casework_specialist_case_dates_dim.json
│  │  │  │  │  ├─ casework_specialist_case_string_dim.json
│  │  │  │  │  ├─ casework_specialist_coastal_access_dim.json
│  │  │  │  │  ├─ casework_specialist_environment_dim.json
│  │  │  │  │  ├─ casework_specialist_high_court_dim.json
│  │  │  │  │  ├─ casework_specialist_modifications_dim.json
│  │  │  │  │  ├─ casework_specialist_purchase_notice_dim.json
│  │  │  │  │  ├─ casework_specialist_recharge_dim.json
│  │  │  │  │  ├─ casework_special_circumstance_dim.json
│  │  │  │  │  ├─ casework_tpo_dim.json
│  │  │  │  │  ├─ checkmark_casemarking_dim.json
│  │  │  │  │  ├─ checkmark_casemarking_fact.json
│  │  │  │  │  ├─ checkmark_case_casemarking_bridge.json
│  │  │  │  │  ├─ checkmark_case_fact.json
│  │  │  │  │  ├─ checkmark_case_reading_case_bridge.json
│  │  │  │  │  ├─ checkmark_comments_case_bridge.json
│  │  │  │  │  ├─ checkmark_comments_dim.json
│  │  │  │  │  ├─ checkmark_comments_fact.json
│  │  │  │  │  ├─ checkmark_comment_state_reference_dim.json
│  │  │  │  │  ├─ checkmark_comment_type_reference_dim.json
│  │  │  │  │  ├─ checkmark_complexity_reference_dim.json
│  │  │  │  │  ├─ checkmark_conditions_reference_dim.json
│  │  │  │  │  ├─ checkmark_coverage_reference_dim.json
│  │  │  │  │  ├─ checkmark_documents_dim.json
│  │  │  │  │  ├─ checkmark_grounds_reference_dim.json
│  │  │  │  │  ├─ checkmark_inspector_manager_dim.json
│  │  │  │  │  ├─ checkmark_inspector_manager_fact.json
│  │  │  │  │  ├─ checkmark_inspector_manager_reading_case_bridge.json
│  │  │  │  │  ├─ checkmark_invalid_nullity_reference_dim.json
│  │  │  │  │  ├─ checkmark_level_reference_dim.json
│  │  │  │  │  ├─ checkmark_manager_type_reference_dim.json
│  │  │  │  │  ├─ checkmark_nsi_dim.json
│  │  │  │  │  ├─ checkmark_outcome_reference_dim.json
│  │  │  │  │  ├─ checkmark_presentation_accuracy_detail_reference_dim.json
│  │  │  │  │  ├─ checkmark_procedure_reference_dim.json
│  │  │  │  │  ├─ checkmark_reading_case_dim.json
│  │  │  │  │  ├─ checkmark_reading_case_fact.json
│  │  │  │  │  ├─ checkmark_source_reference_dim.json
│  │  │  │  │  ├─ checkmark_structure_reasoning_detail_reference_dim.json
│  │  │  │  │  ├─ date_dim.json
│  │  │  │  │  ├─ high_court_dim.json
│  │  │  │  │  ├─ hr_absence_dim.json
│  │  │  │  │  ├─ hr_contract_dim.json
│  │  │  │  │  ├─ hr_costcenter_dim.json
│  │  │  │  │  ├─ hr_disability_dim.json
│  │  │  │  │  ├─ hr_diversity_dim.json
│  │  │  │  │  ├─ hr_employeegroup_dim.json
│  │  │  │  │  ├─ hr_employee_dim.json
│  │  │  │  │  ├─ hr_employee_fact.json
│  │  │  │  │  ├─ hr_employee_hr_hierarchy_dim.json
│  │  │  │  │  ├─ hr_employee_leavers_dim.json
│  │  │  │  │  ├─ hr_historic_sap_hr.json
│  │  │  │  │  ├─ hr_leave_entitlement_dim.json
│  │  │  │  │  ├─ hr_organisation_unit_dim.json
│  │  │  │  │  ├─ hr_payband_dim.json
│  │  │  │  │  ├─ hr_payroll_area_dim.json
│  │  │  │  │  ├─ hr_personnel_area_dim.json
│  │  │  │  │  ├─ hr_personnel_sub_area_dim.json
│  │  │  │  │  ├─ hr_pins_location_dim.json
│  │  │  │  │  ├─ hr_position_dim.json
│  │  │  │  │  ├─ hr_record_fact.json
│  │  │  │  │  ├─ hr_religion_dim.json
│  │  │  │  │  ├─ hr_secure_info_fact.json
│  │  │  │  │  ├─ hr_specialism_dim.json
│  │  │  │  │  ├─ hr_sxo_dim.json
│  │  │  │  │  ├─ hr_work_schedule_dim.json
│  │  │  │  │  ├─ IMS
│  │  │  │  │  │  ├─ ims_attribute_dim.json
│  │  │  │  │  │  ├─ ims_dataflow_dim.json
│  │  │  │  │  │  ├─ ims_dpia_dim.json
│  │  │  │  │  │  ├─ ims_dsa_dim.json
│  │  │  │  │  │  ├─ ims_entity_dim.json
│  │  │  │  │  │  ├─ ims_information_asset_dim.json
│  │  │  │  │  │  ├─ ims_integration_dim.json
│  │  │  │  │  │  ├─ ims_masterdata_map_dim.json
│  │  │  │  │  │  └─ ims_ropa_dim.json
│  │  │  │  │  ├─ legacy_mwr_inspector_join.json
│  │  │  │  │  ├─ legacy_mwr_lines_dim.json
│  │  │  │  │  ├─ legacy_mwr_record_fact.json
│  │  │  │  │  ├─ legacy_mwr_status_dim.json
│  │  │  │  │  ├─ legacy_mwr_submission_date_dim.json
│  │  │  │  │  ├─ main_sourcesystem_fact.json
│  │  │  │  │  ├─ service_user_dim.json
│  │  │  │  │  ├─ timesheets_minutes_dim.json
│  │  │  │  │  ├─ timesheets_record_fact.json
│  │  │  │  │  ├─ timesheets_segment_type_reference_dim.json
│  │  │  │  │  ├─ timesheets_work_segment_dim.json
│  │  │  │  │  └─ timesheets_work_segment_lock_dim.json
│  │  │  │  ├─ orchestration
│  │  │  │  │  ├─ orchestration.json
│  │  │  │  │  └─ scheduling_outstanding_files_table.json
│  │  │  │  ├─ pins-odw-HR-table-list.json
│  │  │  │  ├─ pins-odw-mipins-table-list.json
│  │  │  │  ├─ pins-odw-source-to-standardised-table-list.json
│  │  │  │  ├─ pins-odw-standardised-to-harmonised-notebook-list.json
│  │  │  │  ├─ raw_logs
│  │  │  │  │  └─ datalabs_log_json
│  │  │  │  │     └─ fileshare_log_schema.json
│  │  │  │  └─ standardised_table_definitions
│  │  │  │     ├─ addresses.JSON
│  │  │  │     ├─ bis_pension_ernic_rates.json
│  │  │  │     ├─ CaseComment.json
│  │  │  │     ├─ CaseMarking.json
│  │  │  │     ├─ Casework_Adhoc
│  │  │  │     │  ├─ Calendar.json
│  │  │  │     │  ├─ Employee.json
│  │  │  │     │  ├─ ExaminationTimetable.json
│  │  │  │     │  ├─ Local_Plans.json
│  │  │  │     │  ├─ PicasoDataUnicode.json
│  │  │  │     │  ├─ Segment_Type_Reference.json
│  │  │  │     │  ├─ Specialist_Hedgerow.json
│  │  │  │     │  ├─ Specialist_HH.json
│  │  │  │     │  ├─ Specialist_TPO.json
│  │  │  │     │  ├─ WorkScheduleRule.json
│  │  │  │     │  ├─ Work_Segment.json
│  │  │  │     │  └─ Work_Segment_Lock.json
│  │  │  │     ├─ CommentStateReference.json
│  │  │  │     ├─ CommentTypeReference.json
│  │  │  │     ├─ ComplexityReference.json
│  │  │  │     ├─ ConditionsReference.json
│  │  │  │     ├─ CoverageReference.json
│  │  │  │     ├─ Documents.json
│  │  │  │     ├─ Example
│  │  │  │     │  └─ MOCK_DATA.json
│  │  │  │     ├─ GroundsReference.json
│  │  │  │     ├─ HighCourt.json
│  │  │  │     ├─ hist_sap_hr.json
│  │  │  │     ├─ Horizon
│  │  │  │     │  ├─ AddAdditionalData.json
│  │  │  │     │  ├─ AdditionalFields.json
│  │  │  │     │  ├─ AdvertDetails.json
│  │  │  │     │  ├─ AllAppeals.json
│  │  │  │     │  ├─ AppealsAdditionalData.json
│  │  │  │     │  ├─ AppSubTypeCaseName.json
│  │  │  │     │  ├─ CaseDates.json
│  │  │  │     │  ├─ CaseInfo.json
│  │  │  │     │  ├─ CaseInvolvement.json
│  │  │  │     │  ├─ CaseOfficerAdditionalDetails.json
│  │  │  │     │  ├─ CommonLand.json
│  │  │  │     │  ├─ Contacts_Organisation.json
│  │  │  │     │  ├─ DecisionIssues.json
│  │  │  │     │  ├─ EnforcementGroundsForAppeal.json
│  │  │  │     │  ├─ Event.json
│  │  │  │     │  ├─ ExaminationTimetable.json
│  │  │  │     │  ├─ HorizonContactInformation.json
│  │  │  │     │  ├─ HZNRightOfWay.json
│  │  │  │     │  ├─ InspectorCases.json
│  │  │  │     │  ├─ Local_Planning_Authority.json
│  │  │  │     │  ├─ LPAResponsibility.json
│  │  │  │     │  ├─ NSIPAdvice.json
│  │  │  │     │  ├─ NSIPData.json
│  │  │  │     │  ├─ NSIPRedactions.json
│  │  │  │     │  ├─ NSIPReleventRepresentation.json
│  │  │  │     │  ├─ ProjectInfoInternal.json
│  │  │  │     │  ├─ ServiceUser.json
│  │  │  │     │  ├─ SpecialCircumstance.json
│  │  │  │     │  ├─ Specialism.json
│  │  │  │     │  ├─ SpecialistCaseDates.json
│  │  │  │     │  ├─ SpecialistCaseString.json
│  │  │  │     │  ├─ SpecialistCoastalAccess.json
│  │  │  │     │  ├─ SpecialistEnvironment.json
│  │  │  │     │  ├─ SpecialistHighCourt.json
│  │  │  │     │  ├─ SpecialistModifications.json
│  │  │  │     │  ├─ SpecialistPurchaseNotice.json
│  │  │  │     │  ├─ SpecialistRecharge.json
│  │  │  │     │  └─ VW_BIS_Inspector_Cases.json
│  │  │  │     ├─ HorizonVwBISEvent.json
│  │  │  │     ├─ HR_Absence_Data.json
│  │  │  │     ├─ HR_PC.json
│  │  │  │     ├─ IMS
│  │  │  │     │  ├─ IMS_bdc_attribute.json
│  │  │  │     │  ├─ IMS_bdc_entity.json
│  │  │  │     │  ├─ IMS_data_flow.json
│  │  │  │     │  ├─ IMS_data_sharing.json
│  │  │  │     │  ├─ IMS_dpia.json
│  │  │  │     │  ├─ IMS_information_assets.json
│  │  │  │     │  ├─ IMS_integration.json
│  │  │  │     │  ├─ IMS_master_data_map.json
│  │  │  │     │  └─ IMS_ropa.json
│  │  │  │     ├─ IMS_Attribute.json
│  │  │  │     ├─ IMS_DataFlow.json
│  │  │  │     ├─ IMS_DPIA.json
│  │  │  │     ├─ IMS_DSA.json
│  │  │  │     ├─ IMS_Entity.json
│  │  │  │     ├─ IMS_InformationAsset.json
│  │  │  │     ├─ IMS_Intergration.json
│  │  │  │     ├─ IMS_MasterDataMap.json
│  │  │  │     ├─ IMS_ROPA.json
│  │  │  │     ├─ InspectorManager.json
│  │  │  │     ├─ InvalidNullityReference.json
│  │  │  │     ├─ Leave_Entitlement.json
│  │  │  │     ├─ LegacyTimeSheets
│  │  │  │     │  ├─ MWR_Inspector_dim.json
│  │  │  │     │  ├─ MWR_Lines.json
│  │  │  │     │  ├─ MWR_Status.json
│  │  │  │     │  └─ MWR_Submisison_Date.json
│  │  │  │     ├─ LevelReference.json
│  │  │  │     ├─ ListedBuildings
│  │  │  │     │  ├─ listed_building.json
│  │  │  │     │  └─ listed_building_outline.json
│  │  │  │     ├─ Local_Planning_Authority.json
│  │  │  │     ├─ ManagerTypeReference.json
│  │  │  │     ├─ Nsi.json
│  │  │  │     ├─ NSIPAdvice.json
│  │  │  │     ├─ OutcomeReference.json
│  │  │  │     ├─ PresentationAccuracyDetailReference.json
│  │  │  │     ├─ ProcedureReference.json
│  │  │  │     ├─ ReadingCase.json
│  │  │  │     ├─ ReadingStatusReference.json
│  │  │  │     ├─ ReadingTypeReference.json
│  │  │  │     ├─ SAPHR.JSON
│  │  │  │     ├─ SAP_email.json
│  │  │  │     ├─ SAP_Leavers.json
│  │  │  │     ├─ SourceReference.json
│  │  │  │     ├─ Specialisms.JSON
│  │  │  │     ├─ StructureReasoningDetailReference.json
│  │  │  │     ├─ Timesheets
│  │  │  │     │  ├─ Calendar.json
│  │  │  │     │  ├─ Employee.json
│  │  │  │     │  ├─ Local_Plans.json
│  │  │  │     │  ├─ Segment_Type_Reference.json
│  │  │  │     │  ├─ Specialist_Hedgerow.json
│  │  │  │     │  ├─ Specialist_HH.json
│  │  │  │     │  ├─ Specialist_TPO.json
│  │  │  │     │  ├─ Work_Segment.json
│  │  │  │     │  └─ Work_Segment_Lock.json
│  │  │  │     └─ WorkScheduleRule.json
│  │  │  ├─ data-lifecycle
│  │  │  │  └─ policies.json
│  │  │  ├─ devops-agents
│  │  │  │  ├─ build.pkr.hcl
│  │  │  │  ├─ sources.pkr.hcl
│  │  │  │  ├─ tools.sh
│  │  │  │  └─ variables.pkr.hcl
│  │  │  ├─ firewall-rules
│  │  │  │  └─ allowed_ip_addresses.yaml
│  │  │  ├─ README.md
│  │  │  └─ spark-pool
│  │  │     ├─ environment.yml
│  │  │     ├─ requirements-preview.txt
│  │  │     └─ requirements.txt
│  │  ├─ environments
│  │  │  ├─ dev.tfvars
│  │  │  ├─ prod.tfvars
│  │  │  └─ test.tfvars
│  │  ├─ locals.tf
│  │  ├─ modules
│  │  │  ├─ api-management
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ Demo_Conference_API.openapi+json.json
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ main.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variable.tf
│  │  │  ├─ bastion-host
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ bastion-host-nsg.tf
│  │  │  │  ├─ bastion-host.tf
│  │  │  │  ├─ bastion-vm-nsg.tf
│  │  │  │  ├─ bastion-vm.tf
│  │  │  │  ├─ key-vault-secrets.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ devops-agent-pool
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ agent-vmss.tf
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ outputs.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  ├─ resource-group.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ logic-app
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ api-connections.tf
│  │  │  │  ├─ api-custom-connector.tf
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ provider.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ region.tf
│  │  │  │  ├─ variable.tf
│  │  │  │  ├─ zendesk-created-workflow.tf
│  │  │  │  ├─ zendesk-swagger.json
│  │  │  │  ├─ zendesk-template.json
│  │  │  │  └─ zendesk-updated-workflow.tf
│  │  │  ├─ odt-pe-backoffice-sb
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ main.tf
│  │  │  │  ├─ odt-backoffice-subscription.tf
│  │  │  │  ├─ outputs.tf
│  │  │  │  ├─ provider.tf
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-data-lake
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ data-lake-configuration.tf
│  │  │  │  ├─ data-lake-firewall.tf
│  │  │  │  ├─ data-lake-lifecycle-policy.tf
│  │  │  │  ├─ data-lake-private-endpoint.tf
│  │  │  │  ├─ data-lake-rbac.tf
│  │  │  │  ├─ data-lake.tf
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ key-vault-rbac.tf
│  │  │  │  ├─ key-vault-secrets.tf
│  │  │  │  ├─ key-vault.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ outputs.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-ingestion
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ outputs.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  ├─ service-bus-failover.tf
│  │  │  │  ├─ service-bus-namespace.tf
│  │  │  │  ├─ service-bus-rbac.tf
│  │  │  │  ├─ service-bus-subscriptions.tf
│  │  │  │  ├─ service-bus-topics.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-management
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ key-vault-private-endpoint.tf
│  │  │  │  ├─ key-vault-rbac.tf
│  │  │  │  ├─ key-vault.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ outputs.tf
│  │  │  │  ├─ purview.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-monitoring
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ alert-data-lake.tf
│  │  │  │  ├─ alert-groups.tf
│  │  │  │  ├─ alert-key-vault.tf
│  │  │  │  ├─ alert-service-health.tf
│  │  │  │  ├─ alert-synapse.tf
│  │  │  │  ├─ application-insights.tf
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ key-vault-secrets.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ log-analytics.tf
│  │  │  │  ├─ monitor-data-lake.tf
│  │  │  │  ├─ monitor-key-vault.tf
│  │  │  │  ├─ monitor-network.tf
│  │  │  │  ├─ monitor-service-bus.tf
│  │  │  │  ├─ monitor-synapse-spark-pool.tf
│  │  │  │  ├─ monitor-synapse-sql-pool.tf
│  │  │  │  ├─ monitor-synapse.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-network
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ network-security.tf
│  │  │  │  ├─ network-watcher.tf
│  │  │  │  ├─ network.tf
│  │  │  │  ├─ outputs.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-shir
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  ├─ scripts
│  │  │  │  │  ├─ Deploy-Requirements.ps1
│  │  │  │  │  ├─ Initialize-IntegrationRuntime.ps1
│  │  │  │  │  └─ Install-OpenJDK.ps1
│  │  │  │  ├─ shir-vm-setup.tf
│  │  │  │  ├─ shir-vm.tf
│  │  │  │  ├─ storage-rbac.tf
│  │  │  │  ├─ storage.tf
│  │  │  │  ├─ synapse-shir.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-sql-server
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ key-vault-secrets.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  ├─ sql-server-auditing.tf
│  │  │  │  ├─ sql-server-firewall.tf
│  │  │  │  ├─ sql-server.tf
│  │  │  │  ├─ storage-account-firewall.tf
│  │  │  │  ├─ storage-account-rbac.tf
│  │  │  │  ├─ storage-account.tf
│  │  │  │  ├─ synapse-private-endpoints.tf
│  │  │  │  └─ variables.tf
│  │  │  └─ synapse-workspace-private
│  │  │     ├─ .terraform.lock.hcl
│  │  │     ├─ data-lake-rbac.tf
│  │  │     ├─ key-vault-rbac.tf
│  │  │     ├─ key-vault-secrets.tf
│  │  │     ├─ locals.tf
│  │  │     ├─ outputs.tf
│  │  │     ├─ random.tf
│  │  │     ├─ README.md
│  │  │     ├─ region.tf
│  │  │     ├─ synapse-firewall.tf
│  │  │     ├─ synapse-private-endpoints.tf
│  │  │     ├─ synapse-rbac.tf
│  │  │     ├─ synapse-spark-pool.tf
│  │  │     ├─ synapse-sql-pool.tf
│  │  │     ├─ synapse-workspace.tf
│  │  │     └─ variables.tf
│  │  ├─ outputs.tf
│  │  ├─ provider.tf
│  │  ├─ README.md
│  │  ├─ region.tf
│  │  ├─ variables.tf
│  │  ├─ workload-agent-pool.tf
│  │  ├─ workload-api-manangement.tf
│  │  ├─ workload-data-lake.tf
│  │  ├─ workload-ingestion.tf
│  │  ├─ workload-logic-app.tf
│  │  ├─ workload-management.tf
│  │  ├─ workload-monitoring.tf
│  │  ├─ workload-network.tf
│  │  ├─ workload-odt-pe-backoffice-sb.tf
│  │  ├─ workload-shir.tf
│  │  ├─ workload-sql-server.tf
│  │  └─ workload-synapse.tf
│  ├─ LICENSE
│  ├─ logicapp
│  │  ├─ custom-connectors
│  │  │  ├─ pins-la-custom-connector-zendesk.json
│  │  │  └─ zendesk-custom-connector.yaml
│  │  ├─ documentation.md
│  │  ├─ esb-to-odt-queue
│  │  │  ├─ connections.json
│  │  │  ├─ employee-publish-odt-stateless
│  │  │  │  └─ workflow.json
│  │  │  ├─ host.json
│  │  │  └─ parameters.json
│  │  ├─ logicapp-architecture.ipynb
│  │  ├─ logic_app_architecture_for_zendesk.png
│  │  └─ zendesk-to-esb
│  │     ├─ connections.json
│  │     ├─ host.json
│  │     ├─ zendesk-created
│  │     │  └─ workflow.json
│  │     └─ zendesk-updated
│  │        └─ workflow.json
│  ├─ pipelines
│  │  ├─ devops-agent-deploy.yaml
│  │  ├─ steps
│  │  │  ├─ azure-image-cleanup.yaml
│  │  │  ├─ azure-login.yaml
│  │  │  ├─ azure-private-endpoint-approval.yaml
│  │  │  ├─ azure-resource-lock.yaml
│  │  │  ├─ azure-resource-unlock.yaml
│  │  │  ├─ branch-set-source.yaml
│  │  │  ├─ branch-switch.yaml
│  │  │  ├─ checkov-validate.yaml
│  │  │  ├─ devops-agent-build.yaml
│  │  │  ├─ devops-agent-plan.yaml
│  │  │  ├─ download-secure-file.yaml
│  │  │  ├─ install-checkov.yaml
│  │  │  ├─ install-tflint.yaml
│  │  │  ├─ pause.yaml
│  │  │  ├─ synapse-parameters-override.yaml
│  │  │  ├─ synapse-sql-pool-check.yaml
│  │  │  ├─ synapse-sql-pool-pause.yaml
│  │  │  ├─ synapse-sql-pool-resume.yaml
│  │  │  ├─ terraform-apply.yaml
│  │  │  ├─ terraform-format.yaml
│  │  │  ├─ terraform-init.yaml
│  │  │  ├─ terraform-outputs-to-variables.yaml
│  │  │  ├─ terraform-outputs.yaml
│  │  │  ├─ terraform-plan.yaml
│  │  │  ├─ terraform-validate.yaml
│  │  │  ├─ tflint-validate.yaml
│  │  │  └─ verify-artifact.yaml
│  │  ├─ synapse-release.yaml
│  │  ├─ terraform-cd.yaml
│  │  └─ terraform-ci.yaml
│  ├─ README.md
│  ├─ scripts
│  │  ├─ ims_notebook.ipynb
│  │  ├─ listed-building-api.ipynb
│  │  └─ zendesk-custom-fields.ipynb
│  ├─ servicebus
│  │  ├─ receivefromsubscription.js
│  │  └─ sendtotopic.js
│  ├─ tests
│  │  └─ mock-data-employee.py
│  └─ workspace
│     ├─ credential
│     │  └─ WorkspaceSystemIdentity.json
│     ├─ dataflow
│     │  └─ Zendesk_POC.json
│     ├─ dataset
│     │  ├─ .DS_Store
│     │  ├─ AzureSqlTable1.json
│     │  ├─ AzureSqlTable2.json
│     │  ├─ a_ds_saphr_excel_binary_source.json
│     │  ├─ BISHighCourtEventDates.json
│     │  ├─ BIS_AddAdditionalData.json
│     │  ├─ BIS_AppealsAdditionalData_Parquet.json
│     │  ├─ BIS_HZN_AppealsAddtionalData.json
│     │  ├─ bkp_dst_odw_config.json
│     │  ├─ bkp_dst_odw_curated.json
│     │  ├─ bkp_dst_odw_harmonised.json
│     │  ├─ bkp_dst_odw_raw.json
│     │  ├─ bkp_dst_odw_standardised.json
│     │  ├─ bkp_src_odw_config.json
│     │  ├─ bkp_src_odw_curated.json
│     │  ├─ bkp_src_odw_harmonised.json
│     │  ├─ bkp_src_odw_raw.json
│     │  ├─ bkp_src_odw_standardised.json
│     │  ├─ b_ds_saphr_excel_binary_sink.json
│     │  ├─ checkmark_case_marking.json
│     │  ├─ checkmark_comment_state_reference.json
│     │  ├─ checkmark_complexity_reference.json
│     │  ├─ checkmark_conditions_reference.json
│     │  ├─ checkmark_coverage_reference.json
│     │  ├─ checkmark_documents.json
│     │  ├─ checkmark_grounds_reference.json
│     │  ├─ checkmark_inspector_manager.json
│     │  ├─ checkmark_invalid_nullity_reference.json
│     │  ├─ checkmark_level_reference.json
│     │  ├─ checkmark_manager_type_reference.json
│     │  ├─ checkmark_nsi.json
│     │  ├─ Checkmark_outcome_reference.json
│     │  ├─ checkmark_presentation_accuracy_detail_reference.json
│     │  ├─ checkmark_procedure_reference.json
│     │  ├─ checkmark_reading_case.json
│     │  ├─ checkmark_reading_status_reference.json
│     │  ├─ checkmark_reading_type_reference.json
│     │  ├─ checkmark_source_reference.json
│     │  ├─ checkmark_structure_reasoning_detail_reference.json
│     │  ├─ Contacts_Organisation.json
│     │  ├─ Contacts_Organisation_LPA.json
│     │  ├─ CostCenter_Dim_NonPII.JSON
│     │  ├─ DestinationDataset_ahn.json
│     │  ├─ dim_Local_Planning_Authority.json
│     │  ├─ dst_miPINS_load_tables.json
│     │  ├─ dst_MiPINS_load_tables_raw_storage.json
│     │  ├─ dst_source_to_standardised_table_list.json
│     │  ├─ dst_standardised_to_harmonised_pipeline_list.json
│     │  ├─ dst_temp_employee_syn_curated.json
│     │  ├─ dst_temp_employee_syn_service_json_rest.json
│     │  ├─ dst_temp_employee_syn_service_json_storage.json
│     │  ├─ ds_hist_sap_hr.json
│     │  ├─ ds_hist_sap_hr_csv.json
│     │  ├─ ds_odw_mipins_config.json
│     │  ├─ ds_odw_mipins_curated.json
│     │  ├─ ds_odw_mipins_load_tables.json
│     │  ├─ ds_odw_mipins_tables.json
│     │  ├─ ds_odw_mipins_tables_csv.json
│     │  ├─ ds_SAP_HR.json
│     │  ├─ ExaminationTimeTable.json
│     │  ├─ HighCourt.json
│     │  ├─ HighCourtDataSource.json
│     │  ├─ HorizonContactInfo.json
│     │  ├─ HorizonContactInformation.json
│     │  ├─ HorizonData_BIS_AllAppeals.json
│     │  ├─ HorizonVwBISEvent.json
│     │  ├─ Horizon_BIS_AllAppeals_Parquet.json
│     │  ├─ Horizon_Case_Involvement.json
│     │  ├─ Horizon_Tables_Data.json
│     │  ├─ Horizon_vw_BIS_Event.json
│     │  ├─ Horizon_VW_BIS_Inspector_Cases.json
│     │  ├─ HZNSpecialCircumstance.json
│     │  ├─ HZNSpecialism.json
│     │  ├─ HZN_AddAdditionalData_Parquet.json
│     │  ├─ HZN_AdditionalFields.json
│     │  ├─ Hzn_AdvertDetails.json
│     │  ├─ HZN_AdvertDetails_Parquet.json
│     │  ├─ HZN_AppSubTypeCaseName.json
│     │  ├─ HZN_BIS_DecisionIssues.json
│     │  ├─ HZN_CaseDates.json
│     │  ├─ HZN_CaseInfo.json
│     │  ├─ HZN_CaseOfficerAddDetail.json
│     │  ├─ HZN_CommonLand.json
│     │  ├─ HZN_DecisionIssues_Parquet.json
│     │  ├─ HZN_EnforcementGroundsForAppeal.json
│     │  ├─ HZN_EnforcementGroundsForAppeal_Parquet.json
│     │  ├─ HZN_Event.json
│     │  ├─ HZN_InspectorCases.json
│     │  ├─ HZN_LPAResponsability_Parquet.json
│     │  ├─ HZN_LPARResponsability.json
│     │  ├─ HZN_NSIPRedactions.json
│     │  ├─ HZN_NSIP_Query.json
│     │  ├─ HZN_ProjInfoInternal.json
│     │  ├─ HZN_RightOfWay.json
│     │  ├─ HZN_Right_Of_Way.json
│     │  ├─ HZN_SpecCaseDates.json
│     │  ├─ HZN_SpecCaseString.json
│     │  ├─ HZN_SpecCoastalAccess.json
│     │  ├─ HZN_SpecEnvironment.json
│     │  ├─ HZN_SpecHighCourt.json
│     │  ├─ HZN_SpecMods.json
│     │  ├─ HZN_SpecPurchaseNotice.json
│     │  ├─ HZN_SpecRecharge.json
│     │  ├─ HZN_ViewData.json
│     │  ├─ IMSAttribute.json
│     │  ├─ IMSDataFlow.json
│     │  ├─ IMSDPIA.json
│     │  ├─ IMSDSA.json
│     │  ├─ IMSEntity.json
│     │  ├─ IMSInformationAsset.json
│     │  ├─ IMSIntergration.json
│     │  ├─ IMSMasterDataMap.json
│     │  ├─ IMSROPA.json
│     │  ├─ IMS_Attribute.json
│     │  ├─ IMS_DataFlow.json
│     │  ├─ IMS_DPIA.json
│     │  ├─ IMS_DSA.json
│     │  ├─ IMS_Entity.json
│     │  ├─ IMS_InformationAsset.json
│     │  ├─ IMS_Intergration.json
│     │  ├─ IMS_MasterDataMap.json
│     │  ├─ IMS_ROPA.json
│     │  ├─ Legacy_Timesheets_Data.json
│     │  ├─ ListedBuildingOutline.json
│     │  ├─ ListedBuildings.json
│     │  ├─ listed_building.json
│     │  ├─ listed_building_csv.json
│     │  ├─ listed_building_outline.json
│     │  ├─ listed_building_outline_csv.json
│     │  ├─ Live_InspectorDIM.json
│     │  ├─ Live_Inspector_dim.json
│     │  ├─ load_vw_horizon_event_dates.json
│     │  ├─ Local_Planning_Authority.json
│     │  ├─ mipins_checkmark_case_comment.json
│     │  ├─ mipins_checkmark_data.json
│     │  ├─ MiPINS_information_schema_columns.json
│     │  ├─ MWR_Lines.json
│     │  ├─ MWR_Status.json
│     │  ├─ MWR_Submission_Date.json
│     │  ├─ NSIPAdvice.json
│     │  ├─ NSIP_Advice.json
│     │  ├─ NSIP_Data.json
│     │  ├─ NSIP_ReleventRepresentation.json
│     │  ├─ SourceDataset_ahn.json
│     │  ├─ SpecialCircumstance_Parquet.json
│     │  ├─ Specialism_Parquet.json
│     │  ├─ Timesheets_Calendar.json
│     │  ├─ Timesheets_Data.json
│     │  ├─ Timesheets_Employee.json
│     │  ├─ Timesheets_Segment_Type_Reference.json
│     │  ├─ Timesheets_Work_Segment.json
│     │  ├─ Timesheets_Work_Segment_Lock.json
│     │  ├─ VW_Inspector_Cases.json
│     │  ├─ zendesk_api_created_24hours.json
│     │  ├─ zendesk_api_created_response_24hours.json
│     │  ├─ zendesk_api_historical_response.json
│     │  ├─ zendesk_api_historical_tickets.json
│     │  ├─ zendesk_api_updated_24hours.json
│     │  └─ zendesk_api_updated_response_24hours.json
│     ├─ integrationRuntime
│     │  ├─ AutoResolveIntegrationRuntime.json
│     │  ├─ PinsIntegrationRuntime.json
│     │  ├─ prdacpdb001shir.json
│     │  └─ preacpdb001shir.json
│     ├─ linkedService
│     │  ├─ AzureSqlDatabase1.json
│     │  ├─ HighCourtConnection.json
│     │  ├─ HighCourtLS.json
│     │  ├─ HighCourtRaw.json
│     │  ├─ ls_backup_destination.json
│     │  ├─ ls_backup_source.json
│     │  ├─ ls_datalab.json
│     │  ├─ ls_dsql.json
│     │  ├─ ls_ims_auth.json
│     │  ├─ ls_kv.json
│     │  ├─ ls_listed_building.json
│     │  ├─ ls_odw_sql_mipins.json
│     │  ├─ ls_servicebus.json
│     │  ├─ ls_shpt_mipins.json
│     │  ├─ ls_sql_hzn.json
│     │  ├─ ls_sql_mipins.json
│     │  ├─ ls_ssql_builtin.json
│     │  ├─ ls_storage.json
│     │  ├─ ls_storage_ar.json
│     │  ├─ ls_zendesk.json
│     │  ├─ ls_zendesk_2.json
│     │  ├─ ls_zendesk_custom.json
│     │  ├─ mipins_checkmark_data.json
│     │  ├─ pins-synw-odw-dev-uks-WorkspaceDefaultSqlServer.json
│     │  ├─ pins-synw-odw-dev-uks-WorkspaceDefaultStorage.json
│     │  ├─ pins-synw-odw-dev-ukw-WorkspaceDefaultSqlServer.json
│     │  ├─ pins-synw-odw-dev-ukw-WorkspaceDefaultStorage.json
│     │  ├─ SqlServer1.json
│     │  └─ sql_hzn_tables.json
│     ├─ managedVirtualNetwork
│     │  ├─ default
│     │  │  └─ managedPrivateEndpoint
│     │  │     ├─ AzureSqlDatabase639.json
│     │  │     ├─ synapse-sql-sqlServer--sql-odw-dev-uks.json
│     │  │     ├─ synapse-sql-sqlServer--sql-odw-dev-ukw.json
│     │  │     ├─ synapse-st-dfs--pinsstodwdevuks9h80mb.json
│     │  │     ├─ synapse-st-dfs--pinsstodwdevukwdvzrjm.json
│     │  │     ├─ synapse-ws-sql--pins-synw-odw-dev-uks.json
│     │  │     ├─ synapse-ws-sql--pins-synw-odw-dev-ukw.json
│     │  │     ├─ synapse-ws-sqlOnDemand--pins-synw-odw-dev-uks.json
│     │  │     └─ synapse-ws-sqlOnDemand--pins-synw-odw-dev-ukw.json
│     │  └─ default.json
│     ├─ notebook
│     │  ├─ adding_zendesk_to_service_user.json
│     │  ├─ Calendar.json
│     │  ├─ casework-views.json
│     │  ├─ casework_additional_fields_dim.json
│     │  ├─ casework_advert_details_dim.json
│     │  ├─ casework_all_appeals_additional_data_dim.json
│     │  ├─ casework_all_appeals_dim.json
│     │  ├─ casework_application_sub_type_case_name_dim.json
│     │  ├─ casework_case_dates_dim.json
│     │  ├─ casework_case_fact_legacy.json
│     │  ├─ casework_case_full_list.json
│     │  ├─ casework_case_info_dim.json
│     │  ├─ casework_case_officer_additional_details_dim.json
│     │  ├─ casework_common_land_dim.json
│     │  ├─ casework_contacts_organisation_dim.json
│     │  ├─ casework_contact_information_dim.json
│     │  ├─ casework_decision_issue_dim.json
│     │  ├─ casework_enforcement_grounds_dim.json
│     │  ├─ casework_event_dim.json
│     │  ├─ casework_event_fact.json
│     │  ├─ casework_hedgerow_dim.json
│     │  ├─ casework_high_hedges_dim.json
│     │  ├─ casework_inspector_cases_dim.json
│     │  ├─ casework_legacy_rights_of_way_dim.json
│     │  ├─ casework_local_planning_authority_dim.json
│     │  ├─ casework_local_planning_authority_fact.json
│     │  ├─ casework_local_plans_dim.json
│     │  ├─ casework_lpa_resposibility_dim.json
│     │  ├─ casework_master.json
│     │  ├─ casework_nsip_advice_dim.json
│     │  ├─ casework_nsip_examination_timetable_dim.json
│     │  ├─ casework_nsip_project_info_internal_dim.json
│     │  ├─ casework_nsip_redactions_dim.json
│     │  ├─ casework_nsip_relevant_representation_dim.json
│     │  ├─ casework_picaso_dim.json
│     │  ├─ casework_specialism_dim.json
│     │  ├─ casework_specialist_case_dates_dim.json
│     │  ├─ casework_specialist_case_string_dim.json
│     │  ├─ casework_specialist_coastal_access_dim.json
│     │  ├─ casework_specialist_environment_dim.json
│     │  ├─ casework_specialist_high_court_dim.json
│     │  ├─ casework_specialist_modifications_dim.json
│     │  ├─ casework_specialist_purchase_notice_dim.json
│     │  ├─ casework_specialist_recharge_dim.json
│     │  ├─ casework_special_circumstance_dim.json
│     │  ├─ casework_tpo_dim.json
│     │  ├─ checkmark_casemarking_dim.json
│     │  ├─ checkmark_casemarking_fact.json
│     │  ├─ checkmark_case_casemarking_bridge.json
│     │  ├─ checkmark_case_fact.json
│     │  ├─ checkmark_case_reading_case_bridge.json
│     │  ├─ checkmark_comments_case_bridge.json
│     │  ├─ checkmark_comments_dim.json
│     │  ├─ checkmark_comments_fact.json
│     │  ├─ checkmark_comment_state_reference_dim.json
│     │  ├─ checkmark_comment_type_reference_dim.json
│     │  ├─ checkmark_complexity_reference_dim.json
│     │  ├─ checkmark_conditions_reference_dim.json
│     │  ├─ checkmark_coverage_reference_dim.json
│     │  ├─ checkmark_documents_dim.json
│     │  ├─ checkmark_grounds_reference_dim.json
│     │  ├─ checkmark_inspector_manager_dim.json
│     │  ├─ checkmark_inspector_manager_fact.json
│     │  ├─ checkmark_inspector_manager_reading_case_bridge.json
│     │  ├─ checkmark_invalid_nullity_reference_dim.json
│     │  ├─ checkmark_level_reference_dim.json
│     │  ├─ checkmark_manager_type_reference_dim.json
│     │  ├─ checkmark_nsi_dim.json
│     │  ├─ checkmark_outcome_reference_dim.json
│     │  ├─ checkmark_presentation_accuracy_detail_reference_dim.json
│     │  ├─ checkmark_procedure_reference_dim.json
│     │  ├─ checkmark_reading_case.json
│     │  ├─ checkmark_reading_case_bridge.json
│     │  ├─ checkmark_reading_case_fact.json
│     │  ├─ checkmark_reading_status_reference_dim.json
│     │  ├─ checkmark_reading_type_reference_dim.json
│     │  ├─ checkmark_source_reference_dim.json
│     │  ├─ checkmark_structure_reasoning_detail_reference_dim.json
│     │  ├─ data-checks.json
│     │  ├─ data_validation_testing.json
│     │  ├─ data_validation_wip.json
│     │  ├─ delete-hr-harmonised.json
│     │  ├─ employee-publish.json
│     │  ├─ employee.json
│     │  ├─ gather_data_quality_reports.json
│     │  ├─ high_court_dim.json
│     │  ├─ HIST_contract_dim.json
│     │  ├─ HIST_costcentre_dim.json
│     │  ├─ HIST_employeegroup_dim.json
│     │  ├─ HIST_employee_dim.json
│     │  ├─ HIST_employee_fact.json
│     │  ├─ HIST_Employee_HR_Hierarchy_Dim.json
│     │  ├─ HIST_HR_record_fact.json
│     │  ├─ HIST_initial_run_views.json
│     │  ├─ HIST_OrganisationUnit_Dim.json
│     │  ├─ HIST_payband_dim.json
│     │  ├─ HIST_payrollarea_dim.json
│     │  ├─ HIST_personnelarea_dim.json
│     │  ├─ HIST_personnelsubarea_dim.json
│     │  ├─ HIST_PINS_location_dim.json
│     │  ├─ HIST_position_dim.json
│     │  ├─ HIST_sap_hr_master.json
│     │  ├─ hr_absence_dim.json
│     │  ├─ hr_contract_dim.json
│     │  ├─ hr_costcenter_dim.json
│     │  ├─ hr_disability_dim.json
│     │  ├─ hr_diversity_dim.json
│     │  ├─ hr_employeegroup_dim.json
│     │  ├─ hr_employee_dim.json
│     │  ├─ hr_employee_dim_for_leavers.json
│     │  ├─ hr_employee_fact.json
│     │  ├─ hr_employee_fact_for_leavers.json
│     │  ├─ hr_employee_hr_hierarchy_dim.json
│     │  ├─ hr_employee_leavers_dim.json
│     │  ├─ hr_leave_entitlement_dim.json
│     │  ├─ hr_organisation_unit_dim.json
│     │  ├─ hr_payband_dim.json
│     │  ├─ hr_payroll_area_dim.json
│     │  ├─ hr_personnel_area_dim.json
│     │  ├─ hr_personnel_sub_area_dim.json
│     │  ├─ hr_pins_location_dim.json
│     │  ├─ hr_position_dim.json
│     │  ├─ hr_record_fact.json
│     │  ├─ hr_record_fact_for_leavers.json
│     │  ├─ hr_religion_dim.json
│     │  ├─ hr_secure_info_fact.json
│     │  ├─ hr_specialism_dim.json
│     │  ├─ hr_sxo_dim.json
│     │  ├─ hr_work_schedule_dim.json
│     │  ├─ ims-master.json
│     │  ├─ ims-master_historic.json
│     │  ├─ ims_attribute_dim.json
│     │  ├─ ims_attribute_dim_historic.json
│     │  ├─ ims_dataflow_dim.json
│     │  ├─ ims_dataflow_dim_historic.json
│     │  ├─ ims_dpia_dim.json
│     │  ├─ ims_dpia_dim_historic.json
│     │  ├─ ims_dsa_dim.json
│     │  ├─ ims_dsa_dim_historic.json
│     │  ├─ ims_entity_dim.json
│     │  ├─ ims_entity_dim_historic.json
│     │  ├─ ims_information_asset_dim.json
│     │  ├─ ims_information_asset_dim_historic.json
│     │  ├─ ims_integration_dim.json
│     │  ├─ ims_integration_dim_historic.json
│     │  ├─ ims_masterdata_map_dim.json
│     │  ├─ ims_masterdata_map_dim_historic.json
│     │  ├─ ims_ropa_dim.json
│     │  ├─ ims_ropa_dim_historic.json
│     │  ├─ lake database query.json
│     │  ├─ leave.json
│     │  ├─ Leavers not in SAPHR.json
│     │  ├─ legacy_mrw_tables.json
│     │  ├─ legacy_service_user_dim.json
│     │  ├─ listed_building_dim.json
│     │  ├─ listed_building_outline_dim.json
│     │  ├─ main_sourcesystem_fact.json
│     │  ├─ master.json
│     │  ├─ mipins_high_court.json
│     │  ├─ mipins_hr_contract.json
│     │  ├─ mipins_hr_cost_centre.json
│     │  ├─ mipins_hr_employee_leavers.json
│     │  ├─ mipins_hr_fact_sickness.json
│     │  ├─ mipins_hr_measures.json
│     │  ├─ mipins_hr_measures_NEW.json
│     │  ├─ mipins_hr_measures_new_data_lookup.json
│     │  ├─ mipins_hr_measures_old_data_ingestion.json
│     │  ├─ mipins_hr_organisation_unit.json
│     │  ├─ mipins_hr_personnel_area.json
│     │  ├─ mipins_hr_personnel_sub_area.json
│     │  ├─ mipins_hr_protected_data.json
│     │  ├─ mipins_ims_masterdatamap.json
│     │  ├─ MiPINS_query.json
│     │  ├─ mipins_views.json
│     │  ├─ mipins_vw_fact_absence_all.json
│     │  ├─ Notebook 1.json
│     │  ├─ nsip-project-subscribe.json
│     │  ├─ nsip_relevant_reps.json
│     │  ├─ outstanding_files_add_entry.json
│     │  ├─ py_0_create_config_tables.json
│     │  ├─ py_0_log_copy_activity_output.json
│     │  ├─ py_0_log_notebook_output.json
│     │  ├─ py_0_source_to_raw_hr_functions.json
│     │  ├─ py_0_source_to_raw_hr_main.json
│     │  ├─ py_0_source_to_raw_hr_tests.json
│     │  ├─ py_1_copy_source_file_for_schema_creation.json
│     │  ├─ py_1_initial_run_raw_to_standardised_scheduling.json
│     │  ├─ py_1_raw_to_standardised_hr_functions.json
│     │  ├─ py_1_raw_to_standardised_hr_main.json
│     │  ├─ py_1_raw_to_standardised_hr_tests.json
│     │  ├─ py_1_raw_to_standardised_scheduling.json
│     │  ├─ py_4_curated_tables.json
│     │  ├─ py_amend_tables.json
│     │  ├─ py_casework_raw_to_std.json
│     │  ├─ py_change_table.json
│     │  ├─ py_convert_json_to_csv_ims.json
│     │  ├─ py_convert_json_to_csv_listed_buildings.json
│     │  ├─ py_create_lake_databases.json
│     │  ├─ py_create_tables.json
│     │  ├─ py_create_tables_new.json
│     │  ├─ py_create_views_SAP_HR.json
│     │  ├─ py_daily_files_into_date_folders.json
│     │  ├─ py_delete_outstanding_files_entry.json
│     │  ├─ py_delete_rows_raw_to_std_outstanding_files.json
│     │  ├─ py_delete_table.json
│     │  ├─ py_delete_table_contents.json
│     │  ├─ py_delete_view.json
│     │  ├─ py_delta_table_cleanup.json
│     │  ├─ py_employee_harmonised_layer2_transform.json
│     │  ├─ py_fail_activity_logging.json
│     │  ├─ py_generate_schema_script.json
│     │  ├─ py_get_orchestration_entry.json
│     │  ├─ py_harmonised_and_hr_measures_monthly.json
│     │  ├─ py_HIST_all_hist_dates.json
│     │  ├─ py_hr_monthly_raw_to_std.json
│     │  ├─ py_inspector_address_harmonised_layer1_transform.json
│     │  ├─ py_inspector_harmonised_to_curated_load.json
│     │  ├─ py_inspector_raw_harmonised_layer1_transform.json
│     │  ├─ py_load_standardised_to_harmonised.json
│     │  ├─ py_logging_decorator.json
│     │  ├─ py_odw_curated_table_creation.json
│     │  ├─ py_odw_harmonised_table_creation.json
│     │  ├─ py_populate_HR_dimension_tables.json
│     │  ├─ py_populate_HR_dimension_tables_protected_data.json
│     │  ├─ py_process_raw_to_curated_table_for_reports.json
│     │  ├─ py_process_raw_to_standardised_delta_table.json
│     │  ├─ py_process_raw_to_standardised_validate.json
│     │  ├─ py_raw_to_std.json
│     │  ├─ py_reload_hr_leavers.json
│     │  ├─ py_reload_hr_record_fact.json
│     │  ├─ py_sap_hr_harmonised_layer1_transform.json
│     │  ├─ py_standardised_to_harmonised_data_conversions.json
│     │  ├─ py_temp_syn_employee_to_curated.json
│     │  ├─ py_testing_change_table_schema.json
│     │  ├─ py_utils_data_validation_final.json
│     │  ├─ py_utils_data_validation_functions.json
│     │  ├─ py_utils_get_function_metadata.json
│     │  ├─ py_utils_get_standardised_column_names.json
│     │  ├─ py_utils_get_storage_account.json
│     │  ├─ py_versions.json
│     │  ├─ py_vw_SAP_HR_email_harmonised_layer1_transform.json
│     │  ├─ py_vw_SAP_HR_email_weekly_harmonised_layer1_transform.json
│     │  ├─ py_vw_SAP_PINS_email_harmonised_layer1_transform.json
│     │  ├─ sample_to_call_listed_buiding_API.json
│     │  ├─ sap-hr-master.json
│     │  ├─ sap-hr-master_full_reload.json
│     │  ├─ sap-hr-views-historic.json
│     │  ├─ sap-hr-views-leavers.json
│     │  ├─ sap-hr-views-saphr.json
│     │  ├─ sap-hr-views.json
│     │  ├─ service_user.json
│     │  ├─ service_user_dim.json
│     │  ├─ service_user_zendesk_dim.json
│     │  ├─ template_notebook.json
│     │  ├─ timesheets_master.json
│     │  ├─ timesheets_minutes_dim.json
│     │  ├─ timesheets_record_fact.json
│     │  ├─ timesheets_segment_type_reference_dim.json
│     │  ├─ timesheets_work_segment_dim.json
│     │  ├─ timesheets_work_segment_lock_dim.json
│     │  ├─ zendesk-subscribe.json
│     │  ├─ zendesk_get_created_tickets.json
│     │  ├─ zendesk_get_updated_tickets.json
│     │  ├─ zendesk_harmonised_export.json
│     │  ├─ zendesk_historical.json
│     │  ├─ zendesk_raw_inspect.json
│     │  ├─ zendesk_raw_to_standerdised.json
│     │  ├─ zendesk_read_me.json
│     │  ├─ zendesk_schema_validation.json
│     │  └─ zendesk_standardised_and_harmonised.json
│     ├─ pipeline
│     │  ├─ 0_Horizon_Data_Transfer_Raw.json
│     │  ├─ 0_Horizon_Service_User.json
│     │  ├─ 0_Horizon_SQL_Tables_Raw_part1.json
│     │  ├─ 0_Horizon_SQL_Tables_Raw_part2.json
│     │  ├─ 0_Legacy_Timesheet_Data_Copy_RAW.json
│     │  ├─ 0_Listed_Buildings_API_to_RAW.json
│     │  ├─ 0_ODT_Data_Transfer.json
│     │  ├─ 0_pln_source_to_raw_fileshare.json
│     │  ├─ 0_pln_source_to_raw_fileshare_copy_activity.json
│     │  ├─ 0_pln_source_to_raw_MiPINS.json
│     │  ├─ 0_Raw_Case_Reference_Tables.json
│     │  ├─ 0_Raw_Checkmark_Data_part1.json
│     │  ├─ 0_Raw_Checkmark_Data_part2.json
│     │  ├─ 0_Raw_High_Court_Data_Copy.json
│     │  ├─ 0_Raw_Horizon_BIS_Event.json
│     │  ├─ 0_Raw_Horizon_Main.json
│     │  ├─ 0_Raw_IMS.json
│     │  ├─ 0_Raw_IMS_Initial_load.json
│     │  ├─ 0_Timesheets_Data_Copy_RAW.json
│     │  ├─ 0_Zendesk_API_to_RAW.json
│     │  ├─ 0_Zendesk_API_to_RAW_historical_load.json
│     │  ├─ 0_ZenDesk_Data_Transfer.json
│     │  ├─ CopyPipeline_ahn.json
│     │  ├─ data_validation_test.json
│     │  ├─ pln_backup_odw_config.json
│     │  ├─ pln_backup_odw_curated.json
│     │  ├─ pln_backup_odw_harmonised.json
│     │  ├─ pln_backup_odw_raw.json
│     │  ├─ pln_backup_odw_standardised.json
│     │  ├─ pln_casework_deployment_clean_slate.json
│     │  ├─ pln_casework_harmonised_deployment.json
│     │  ├─ pln_casework_main.json
│     │  ├─ pln_casework_source_to_raw.json
│     │  ├─ pln_casework_source_to_raw_legacy.json
│     │  ├─ pln_copy_mipins.json
│     │  ├─ pln_copy_mipins_TEST.json
│     │  ├─ pln_fact_sickness.json
│     │  ├─ pln_high_court_main.json
│     │  ├─ pln_hr_cube_objects.json
│     │  ├─ pln_hr_deployment_clean_slate.json
│     │  ├─ pln_hr_ingestion_harmonised_and_measures.json
│     │  ├─ pln_hr_ingestion_initial.json
│     │  ├─ pln_hr_main.json
│     │  ├─ pln_hr_measures_schedule.json
│     │  ├─ pln_ims_main.json
│     │  ├─ pln_initial_high_court.json
│     │  ├─ pln_listed_buildings_main.json
│     │  ├─ pln_load_employee_standardised_to_harmonised.json
│     │  ├─ pln_load_harmonised_to_curated.json
│     │  ├─ pln_load_raw_to_standardised.json
│     │  ├─ pln_load_standardised_to_harmonised.json
│     │  ├─ pln_migration_test.json
│     │  ├─ pln_mipins_raw_to_curated.json
│     │  ├─ pln_mipins_raw_to_curated_new_1.json
│     │  ├─ pln_mipins_raw_to_curated_new_2.json
│     │  ├─ pln_odw_master.json
│     │  ├─ pln_post_deployment.json
│     │  ├─ pln_raw_to_standardised_e2e.json
│     │  ├─ pln_service_user_clean_slate.json
│     │  ├─ pln_service_user_main.json
│     │  ├─ pln_temp_employee_syn_raw_to_curated.json
│     │  ├─ pln_temp_eployee_syn_service_to_raw.json
│     │  ├─ pln_zendesk_main.json
│     │  └─ pl_copy_sap_load_tables_to_raw_storage.json
│     ├─ publish_config.json
│     ├─ sparkConfiguration
│     │  ├─ Kat.json
│     │  ├─ maxFields.json
│     │  └─ NewConfig.json
│     ├─ sqlscript
│     │  ├─ add_user.json
│     │  ├─ Duplicates_in_Employee_Dim.json
│     │  ├─ Duplicates_in_Employee_Fact.json
│     │  ├─ hist_sap_hr.json
│     │  ├─ hr_checking_duplicates.json
│     │  ├─ IMS InformationAsset.json
│     │  ├─ IMS_Attribute.json
│     │  ├─ IMS_Entity.json
│     │  ├─ IMS_Masterdata_Map.json
│     │  ├─ IMS_ROPA.json
│     │  ├─ mipins_high_court.json
│     │  ├─ mipins_hr_contract.json
│     │  ├─ mipins_hr_cost_centre.json
│     │  ├─ mipins_hr_employee_details.json
│     │  ├─ mipins_hr_employee_leavers.json
│     │  ├─ mipins_hr_fact_sickness.json
│     │  ├─ mipins_hr_organisational_unit.json
│     │  ├─ mipins_hr_personnel_area.json
│     │  ├─ mipins_hr_personnel_area_table.json
│     │  ├─ mipins_hr_personnel_sub_area.json
│     │  ├─ mipins_hr_protected_data.json
│     │  ├─ mipins_vw_fact_absence_all.json
│     │  ├─ miPINS_vw_mipins_high_court.json
│     │  ├─ miPINS_vw_mipins_listed_building.json
│     │  ├─ Table without duplicates.json
│     │  ├─ vw_mipins_hr_gender.json
│     │  └─ vw_service_user.json
│     ├─ template-parameters-definition.json
│     └─ trigger
│        ├─ odt-to-odw.json
│        ├─ src_to_standardised_trigger.json
│        ├─ tr_backup_daily.json
│        ├─ tr_daily.json
│        ├─ tr_odw_raw_service_user.json
│        └─ tr_weekly.json
├─ package-lock.json
├─ package.json
├─ PINS.code-workspace
├─ pins_azure_architecture.png
├─ planning-swagger.json
├─ python-snippets
│  ├─ create-function-reference-table.ipynb
│  ├─ create-function-reference-table.py
│  ├─ dynamically-populate-function-args.py
│  ├─ function-args-unittest.py
│  └─ README.md
├─ requirements.txt
├─ table_keys.json
├─ table_mapping.json
├─ test_results_dict.json
├─ zendesk-data.ipynb
├─ zendesk.py
├─ zendesk_sample.json
├─ __azurite_db_blob_extent__.json
├─ __azurite_db_blob__.json
├─ __azurite_db_queue_extent__.json
├─ __azurite_db_queue__.json
├─ __azurite_db_table__.json
├─ __blobstorage__
│  └─ 49c6c808-710e-4bd4-a82f-02e575ced10e
├─ __pycache__
│  └─ lasagna.cpython-310.pyc
└─ __queuestorage__

```
```
Git
├─ .pytest_cache
│  ├─ CACHEDIR.TAG
│  ├─ README.md
│  └─ v
│     └─ cache
│        └─ stepwise
├─ .vscode
│  ├─ extensions.json
│  ├─ launch.json
│  ├─ settings.json
│  └─ tasks.json
├─ api-management-policy-snippets
│  ├─ examples
│  │  ├─ Add correlation id to inbound request.policy.xml
│  │  ├─ Authenticate using Managed Identity to access Event Hub.xml
│  │  ├─ Authenticate using Managed Identity to access Service Bus.xml
│  │  ├─ Authenticate using Managed Identity to access Storage Account.xml
│  │  ├─ Authorize requests using external authorizer.policy.xml
│  │  ├─ Back-end API redundancy.policy.xml
│  │  ├─ Backend OAuth2 Authentication With Cache.policy.xml
│  │  ├─ Call out to an HTTP endpoint and cache the response.policy.xml
│  │  ├─ Create HMAC SHA256-Signed JWT.policy.xml
│  │  ├─ Decrypt AES Data using policy expressions.xml
│  │  ├─ DELETE a from to blobStorage account.xml
│  │  ├─ Encrypt data using expressions.policy.xml
│  │  ├─ Extract value from XML.xml
│  │  ├─ Extracting multiple values from xml documents.policy.xml
│  │  ├─ Filter on IP Address when using Application Gateway.policy.xml
│  │  ├─ Filter response content based on product name.policy.xml
│  │  ├─ Forward Azure Event Grid Event.xml
│  │  ├─ Forward gateway hostname to backend for generating correct urls in responses.policy.xml
│  │  ├─ Generate Azure Relay Token.policy.xml
│  │  ├─ Generate Shared Access Signature and forward request to Azure storage.policy.xml
│  │  ├─ GET a file from blobStorage account.xml
│  │  ├─ Get OAuth2 access token from AAD and forward it to the backend.policy.xml
│  │  ├─ Get OAuth2 access token from AAD using client id and certificate using key vault manage identity.xml
│  │  ├─ Get X-CSRF token from SAP gateway using send request.policy.xml
│  │  ├─ Handle Power Query access request to custom API.policy.xml
│  │  ├─ List all inbound headers.policy.xml
│  │  ├─ Log errors to Stackify.policy.xml
│  │  ├─ Look up Key Vault certificate using Managed Service Identity and call backend.policy.xml
│  │  ├─ Look up Key Vault secret using Managed Service Identity.policy.xml
│  │  ├─ Loopback request for service at same API Management service.xml
│  │  ├─ Mask async calls as synchronous.policy.xml
│  │  ├─ Parse a JWT token using expressions.xml
│  │  ├─ Perform basic authentication.policy.xml
│  │  ├─ Pre-authorize requests based on HTTP method with validate-jwt.policy.xml
│  │  ├─ PUT a file to blobStorage account.xml
│  │  ├─ Query CosmosDB.policy.xml
│  │  ├─ Random load balancer simpler.policy.xml
│  │  ├─ Random load balancer.policy.xml
│  │  ├─ README.md
│  │  ├─ Request OAuth2 access token from SAP using AAD JWT token.xml
│  │  ├─ Return a blob URL signed with a user delegation SAS token.xml
│  │  ├─ Return HTTP 405 if the HTTP Method of the request is not defined.xml
│  │  ├─ Route requests based on size.policy.xml
│  │  ├─ Route requests to regional backend instances.xml
│  │  ├─ Send request context information to the backend service.policy.xml
│  │  ├─ Set cache duration using response cache control header.policy.xml
│  │  ├─ Trigger Azure Data Factory Pipeline With Parameters.policy.xml
│  │  ├─ Trigger Azure Data Factory Pipeline.policy.xml
│  │  └─ Use custom error messages for jwt-validate policy with on-error handler.policy.xml
│  ├─ LICENSE
│  ├─ media
│  │  └─ vscode-snippets
│  │     ├─ apim-vscode-snippets-1.png
│  │     ├─ apim-vscode-snippets-2.png
│  │     └─ apim-vscode-snippets-3.png
│  ├─ policy-expressions
│  │  └─ README.md
│  ├─ README.md
│  ├─ SECURITY.md
│  └─ vscode-snippets
│     └─ xml.json
├─ apim-api-tests.ipynb
├─ asyncio_test.py
├─ asyncio_test_funcs.py
├─ azure-functions-sql-extension
│  ├─ .editorconfig
│  ├─ .gdn
│  │  └─ global.gdnsuppress
│  ├─ .vscode
│  │  ├─ extensions.json
│  │  ├─ launch.json
│  │  ├─ settings.json
│  │  └─ tasks.json
│  ├─ builds
│  │  ├─ azure-pipelines
│  │  │  ├─ build-pr.yml
│  │  │  ├─ build-release-java.yml
│  │  │  ├─ build-release.yml
│  │  │  ├─ performance.yml
│  │  │  ├─ template-steps-build-test.yml
│  │  │  ├─ template-steps-performance.yml
│  │  │  └─ template-steps-publish.yml
│  │  ├─ scripts
│  │  │  └─ UpdateLogLevel.ps1
│  │  └─ TSAConfig.gdntsa
│  ├─ CODE_OF_CONDUCT.md
│  ├─ CONTRIBUTING.md
│  ├─ Directory.Build.props
│  ├─ Directory.Packages.props
│  ├─ docs
│  │  ├─ BindingsOverview.md
│  │  ├─ GeneralSetup.md
│  │  ├─ SetupGuide_Dotnet.md
│  │  ├─ SetupGuide_DotnetCSharpScript.md
│  │  ├─ SetupGuide_DotnetOutOfProc.md
│  │  ├─ SetupGuide_Java.md
│  │  ├─ SetupGuide_Javascript.md
│  │  ├─ SetupGuide_PowerShell.md
│  │  ├─ SetupGuide_Python.md
│  │  └─ SqlBindingRelatedRepos.md
│  ├─ global.json
│  ├─ Images
│  │  ├─ dbSetup.png
│  │  └─ pkgicon.png
│  ├─ java-library
│  │  ├─ checkstyle.xml
│  │  ├─ pom.xml
│  │  └─ src
│  │     └─ main
│  │        └─ java
│  │           └─ com
│  │              └─ microsoft
│  │                 └─ azure
│  │                    └─ functions
│  │                       └─ sql
│  │                          └─ annotation
│  │                             ├─ SQLInput.java
│  │                             └─ SQLOutput.java
│  ├─ LICENSE
│  ├─ NOTICE.txt
│  ├─ nuget.config
│  ├─ performance
│  │  ├─ .editorconfig
│  │  ├─ Microsoft.Azure.WebJobs.Extensions.Sql.Performance.csproj
│  │  ├─ packages.lock.json
│  │  ├─ README.md
│  │  ├─ SqlBindingBenchmarks.cs
│  │  ├─ SqlInputBindingPerformance.cs
│  │  └─ SqlOutputBindingPerformance.cs
│  ├─ README.md
│  ├─ samples
│  │  ├─ Database
│  │  │  ├─ StoredProcedures
│  │  │  │  └─ SelectProductsCost.sql
│  │  │  ├─ Tables
│  │  │  │  ├─ Products.sql
│  │  │  │  ├─ ProductsCostNotNull.sql
│  │  │  │  ├─ ProductsNameNotNull.sql
│  │  │  │  ├─ ProductsWithDefaultPK.sql
│  │  │  │  ├─ ProductsWithIdentity.sql
│  │  │  │  └─ ProductsWithMultiplePrimaryColumnsAndIdentity.sql
│  │  │  └─ Views
│  │  │     └─ ProductsNamesView.sql
│  │  ├─ samples-csharp
│  │  │  ├─ .editorconfig
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ Common
│  │  │  │  ├─ Product.cs
│  │  │  │  └─ ProductUtilities.cs
│  │  │  ├─ GlobalSuppressions.cs
│  │  │  ├─ host.json
│  │  │  ├─ InputBindingSamples
│  │  │  │  ├─ GetProductNamesView.cs
│  │  │  │  ├─ GetProducts.cs
│  │  │  │  ├─ GetProductsAsyncEnumerable.cs
│  │  │  │  ├─ GetProductsNameEmpty.cs
│  │  │  │  ├─ GetProductsNameNull.cs
│  │  │  │  ├─ GetProductsSqlCommand.cs
│  │  │  │  ├─ GetProductsStoredProcedure.cs
│  │  │  │  ├─ GetProductsStoreProcedureFromAppSetting.cs
│  │  │  │  ├─ GetProductsString.cs
│  │  │  │  └─ GetProductsTopN.cs
│  │  │  ├─ local.settings.json
│  │  │  ├─ Microsoft.Azure.WebJobs.Extensions.Sql.Samples.csproj
│  │  │  ├─ MultipleBindingsSamples
│  │  │  │  └─ GetAndAddProducts.cs
│  │  │  ├─ OutputBindingSamples
│  │  │  │  ├─ AddProduct.cs
│  │  │  │  ├─ AddProductParams.cs
│  │  │  │  ├─ AddProductsArray.cs
│  │  │  │  ├─ AddProductsAsyncCollector.cs
│  │  │  │  ├─ AddProductsCollector.cs
│  │  │  │  ├─ AddProductsWithIdentityColumnArray.cs
│  │  │  │  ├─ AddProductWithDefaultPK.cs
│  │  │  │  ├─ AddProductWithIdentityColumn.cs
│  │  │  │  ├─ AddProductWithIdentityColumnIncluded.cs
│  │  │  │  ├─ AddProductWithMultiplePrimaryColumnsAndIdentity.cs
│  │  │  │  ├─ QueueTriggerProducts.cs
│  │  │  │  └─ TimerTriggerProducts.cs
│  │  │  ├─ packages.lock.json
│  │  │  └─ Properties
│  │  │     ├─ serviceDependencies.json
│  │  │     └─ serviceDependencies.local.json
│  │  ├─ samples-csx
│  │  │  ├─ .editorconfig
│  │  │  ├─ .vscode
│  │  │  │  └─ extensions.json
│  │  │  ├─ AddProduct
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductParams
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductsArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductsCollector
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductsWithIdentityColumnArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductWithDefaultPK
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductWithIdentityColumn
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductWithIdentityColumnIncluded
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ AddProductWithMultiplePrimaryColumnsAndIdentity
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ Common
│  │  │  │  └─ product.csx
│  │  │  ├─ GetAndAddProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProductNamesView
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProductsAsyncEnumerable
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProductsNameEmpty
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProductsNameNull
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProductsStoredProcedure
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ GetProductsStoredProcedureFromAppSetting
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  ├─ host.json
│  │  │  ├─ local.settings.json
│  │  │  ├─ packages.lock.json
│  │  │  ├─ QueueTriggerProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.csx
│  │  │  └─ TimerTriggerProducts
│  │  │     ├─ function.json
│  │  │     └─ run.csx
│  │  ├─ samples-java
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ checkstyle.xml
│  │  │  ├─ host.json
│  │  │  ├─ local.settings.json
│  │  │  ├─ pom.xml
│  │  │  └─ src
│  │  │     └─ main
│  │  │        └─ java
│  │  │           └─ com
│  │  │              └─ function
│  │  │                 ├─ AddProduct.java
│  │  │                 ├─ AddProductParams.java
│  │  │                 ├─ AddProductReturnValue.java
│  │  │                 ├─ AddProductsArray.java
│  │  │                 ├─ AddProductsWithIdentityColumnArray.java
│  │  │                 ├─ AddProductToTwoTables.java
│  │  │                 ├─ AddProductWithDefaultPK.java
│  │  │                 ├─ AddProductWithIdentityColumn.java
│  │  │                 ├─ AddProductWithIdentityColumnIncluded.java
│  │  │                 ├─ AddProductWithMultiplePrimaryColumnsAndIdentity.java
│  │  │                 ├─ Common
│  │  │                 │  ├─ MultiplePrimaryKeyProductWithoutId.java
│  │  │                 │  ├─ Product.java
│  │  │                 │  ├─ ProductName.java
│  │  │                 │  ├─ ProductWithDefaultPK.java
│  │  │                 │  ├─ ProductWithOptionalId.java
│  │  │                 │  └─ ProductWithoutId.java
│  │  │                 ├─ GetAndAddProducts.java
│  │  │                 ├─ GetProductNamesView.java
│  │  │                 ├─ GetProducts.java
│  │  │                 ├─ GetProductsFromTwoTables.java
│  │  │                 ├─ GetProductsNameEmpty.java
│  │  │                 ├─ GetProductsStoredProcedure.java
│  │  │                 ├─ GetProductsStoredProcedureFromAppSetting.java
│  │  │                 ├─ QueueTriggerProducts.java
│  │  │                 └─ TimerTriggerProducts.java
│  │  ├─ samples-js
│  │  │  ├─ .eslintrc.json
│  │  │  ├─ .funcignore
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ AddProduct
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductParams
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductsArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductsWithIdentityColumnArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductWithDefaultPK
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductWithIdentityColumn
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductWithIdentityColumnIncluded
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ AddProductWithMultiplePrimaryColumnsAndIdentity
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetAndAddProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetProductNamesView
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetProductsNameEmpty
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetProductsNameNull
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetProductsStoredProcedure
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ GetProductsStoredProcedureFromAppSetting
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  ├─ host.json
│  │  │  ├─ local.settings.json
│  │  │  ├─ package-lock.json
│  │  │  ├─ package.json
│  │  │  ├─ QueueTriggerProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ index.js
│  │  │  └─ TimerTriggerProducts
│  │  │     ├─ function.json
│  │  │     └─ index.js
│  │  ├─ samples-js-v4
│  │  │  ├─ .funcignore
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ host.json
│  │  │  ├─ local.settings.json
│  │  │  ├─ package-lock.json
│  │  │  ├─ package.json
│  │  │  └─ src
│  │  │     └─ functions
│  │  │        ├─ AddProduct.js
│  │  │        └─ GetProducts.js
│  │  ├─ samples-outofproc
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ GlobalSuppressions.cs
│  │  │  ├─ host.json
│  │  │  ├─ InputBindingSamples
│  │  │  │  ├─ GetProductNamesView.cs
│  │  │  │  ├─ GetProducts.cs
│  │  │  │  ├─ GetProductsAsyncEnumerable.cs
│  │  │  │  ├─ GetProductsNameEmpty.cs
│  │  │  │  ├─ GetProductsNameNull.cs
│  │  │  │  ├─ GetProductsStoredProcedure.cs
│  │  │  │  ├─ GetProductsStoreProcedureFromAppSetting.cs
│  │  │  │  ├─ GetProductsString.cs
│  │  │  │  └─ GetProductsTopN.cs
│  │  │  ├─ local.settings.json
│  │  │  ├─ Microsoft.Azure.WebJobs.Extensions.Sql.SamplesOutOfProc.csproj
│  │  │  ├─ MultipleBindingsSamples
│  │  │  │  └─ GetAndAddProducts.cs
│  │  │  ├─ OutputBindingSamples
│  │  │  │  ├─ AddProduct.cs
│  │  │  │  ├─ AddProductParams.cs
│  │  │  │  ├─ AddProductsArray.cs
│  │  │  │  ├─ AddProductsWithIdentityColumnArray.cs
│  │  │  │  ├─ AddProductWithDefaultPK.cs
│  │  │  │  ├─ AddProductWithIdentityColumn.cs
│  │  │  │  ├─ AddProductWithIdentityColumnIncluded.cs
│  │  │  │  ├─ AddProductWithMultiplePrimaryColumnsAndIdentity.cs
│  │  │  │  ├─ QueueTriggerProducts.cs
│  │  │  │  └─ TimerTriggerProducts.cs
│  │  │  ├─ packages.lock.json
│  │  │  ├─ Product.cs
│  │  │  ├─ Program.cs
│  │  │  └─ Properties
│  │  │     └─ launchSettings.json
│  │  ├─ samples-powershell
│  │  │  ├─ .funcignore
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ AddProduct
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductParams
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductsArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductsWithIdentityColumnArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductWithDefaultPK
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductWithIdentityColumn
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductWithIdentityColumnIncluded
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ AddProductWithMultiplePrimaryColumnsAndIdentity
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetAndAddProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetProductNamesView
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetProductsNameEmpty
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetProductsNameNull
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetProductsStoredProcedure
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ GetProductsStoredProcedureFromAppSetting
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ host.json
│  │  │  ├─ local.settings.json
│  │  │  ├─ profile.ps1
│  │  │  ├─ QueueTriggerProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ run.ps1
│  │  │  ├─ requirements.psd1
│  │  │  └─ TimerTriggerProducts
│  │  │     ├─ function.json
│  │  │     └─ run.ps1
│  │  ├─ samples-python
│  │  │  ├─ .devcontainer
│  │  │  │  ├─ devcontainer.json
│  │  │  │  ├─ Dockerfile
│  │  │  │  ├─ patch-core-tools.sh
│  │  │  │  └─ README.md
│  │  │  ├─ .funcignore
│  │  │  ├─ .pylintrc
│  │  │  ├─ .vscode
│  │  │  │  ├─ extensions.json
│  │  │  │  ├─ launch.json
│  │  │  │  ├─ settings.json
│  │  │  │  └─ tasks.json
│  │  │  ├─ AddProduct
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductParams
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductsArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductsWithIdentityColumnArray
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductWithDefaultPK
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductWithIdentityColumn
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductWithIdentityColumnIncluded
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ AddProductWithMultiplePrimaryColumnsAndIdentity
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ Common
│  │  │  │  ├─ multiplePrimaryKeyProductWithoutId.py
│  │  │  │  ├─ product.py
│  │  │  │  └─ productWithoutId.py
│  │  │  ├─ GetAndAddProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProductNamesView
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProductsColumnTypesSerialization
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProductsNameEmpty
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProductsNameNull
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProductsStoredProcedure
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ GetProductsStoredProcedureFromAppSetting
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ host.json
│  │  │  ├─ local.settings.json
│  │  │  ├─ QueueTriggerProducts
│  │  │  │  ├─ function.json
│  │  │  │  └─ __init__.py
│  │  │  ├─ requirements.txt
│  │  │  └─ TimerTriggerProducts
│  │  │     ├─ function.json
│  │  │     └─ __init__.py
│  │  └─ samples-python-v2
│  │     ├─ .funcignore
│  │     ├─ .pylintrc
│  │     ├─ .vscode
│  │     │  ├─ extensions.json
│  │     │  ├─ launch.json
│  │     │  ├─ settings.json
│  │     │  └─ tasks.json
│  │     ├─ function_app.py
│  │     ├─ host.json
│  │     ├─ local.settings.json
│  │     └─ requirements.txt
│  ├─ scripts
│  │  ├─ BuildJavaProjectsAndRunIntegrationTests.ps1
│  │  └─ CopySqlDllToExtensionBundle.ps1
│  ├─ SECURITY.md
│  ├─ SQL2003.snk
│  ├─ src
│  │  ├─ Microsoft.Azure.WebJobs.Extensions.Sql.csproj
│  │  ├─ packages.lock.json
│  │  ├─ SqlAsyncCollector.cs
│  │  ├─ SqlAsyncCollectorBuilder.cs
│  │  ├─ SqlAsyncEnumerable.cs
│  │  ├─ SqlAttribute.cs
│  │  ├─ SqlBindingConfigProvider.cs
│  │  ├─ SqlBindingConstants.cs
│  │  ├─ SqlBindingExtension.cs
│  │  ├─ SqlBindingStartup.cs
│  │  ├─ SqlBindingUtilities.cs
│  │  ├─ SqlConverters.cs
│  │  ├─ SqlObject.cs
│  │  ├─ Telemetry
│  │  │  ├─ Telemetry.cs
│  │  │  ├─ TelemetryCommonProperties.cs
│  │  │  ├─ TelemetryUtils.cs
│  │  │  └─ UserLevelCacheWriter.cs
│  │  └─ Utils.cs
│  ├─ test
│  │  ├─ .editorconfig
│  │  ├─ Common
│  │  │  ├─ LogTestNameAttribute.cs
│  │  │  ├─ ProductColumnTypes.cs
│  │  │  ├─ ProductDefaultPKAndDifferentColumnOrder.cs
│  │  │  ├─ ProductExtraColumns.cs
│  │  │  ├─ ProductIncorrectCasing.cs
│  │  │  ├─ ProductMissingColumns.cs
│  │  │  ├─ ProductUnsupportedTypes.cs
│  │  │  ├─ SupportedLanguagesTestAttribute.cs
│  │  │  ├─ TestConfiguration.cs
│  │  │  ├─ TestConfigurationSection.cs
│  │  │  ├─ TestData.cs
│  │  │  └─ TestUtils.cs
│  │  ├─ coverage.runsettings
│  │  ├─ Database
│  │  │  └─ Tables
│  │  │     ├─ ProductsColumnTypes.sql
│  │  │     ├─ ProductsUnsupportedTypes.sql
│  │  │     ├─ ProductsWithoutPrimaryKey.sql
│  │  │     ├─ ProductsWithReservedPrimaryKeyColumnNames.sql
│  │  │     └─ ProductsWithUnsupportedColumnTypes.sql
│  │  ├─ GlobalSuppressions.cs
│  │  ├─ Integration
│  │  │  ├─ IntegrationTestBase.cs
│  │  │  ├─ IntegrationTestFixture.cs
│  │  │  ├─ IntegrationTestsCollection.cs
│  │  │  ├─ MultipleSqlBindingsIntegrationTests.cs
│  │  │  ├─ SqlInputBindingIntegrationTests.cs
│  │  │  ├─ SqlOutputBindingIntegrationTests.cs
│  │  │  ├─ test-csharp
│  │  │  │  ├─ AddProductColumnTypes.cs
│  │  │  │  ├─ AddProductDefaultPKAndDifferentColumnOrder.cs
│  │  │  │  ├─ AddProductExtraColumns.cs
│  │  │  │  ├─ AddProductIncorrectCasing.cs
│  │  │  │  ├─ AddProductMissingColumns.cs
│  │  │  │  ├─ AddProductMissingColumnsException.cs
│  │  │  │  ├─ AddProductsNoPartialUpsert.cs
│  │  │  │  ├─ AddProductUnsupportedTypes.cs
│  │  │  │  ├─ GetProductColumnTypesSerialization.cs
│  │  │  │  ├─ GetProductColumnTypesSerializationAsyncEnumerable.cs
│  │  │  │  └─ Startup.cs
│  │  │  ├─ test-csx
│  │  │  │  ├─ .vscode
│  │  │  │  │  └─ extensions.json
│  │  │  │  ├─ AddProductColumnTypes
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductDefaultPKAndDifferentColumnOrder
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductExtraColumns
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductIncorrectCasing
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductMissingColumns
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductMissingColumnsExceptionFunction
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductsNoPartialUpsert
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ AddProductUnsupportedTypes
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ Common
│  │  │  │  │  └─ Product.csx
│  │  │  │  ├─ GetProductsColumnTypesSerialization
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  ├─ GetProductsColumnTypesSerializationAsyncEnumerable
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.csx
│  │  │  │  └─ host.json
│  │  │  ├─ test-java
│  │  │  │  ├─ .vscode
│  │  │  │  │  ├─ extensions.json
│  │  │  │  │  ├─ launch.json
│  │  │  │  │  ├─ settings.json
│  │  │  │  │  └─ tasks.json
│  │  │  │  ├─ checkstyle.xml
│  │  │  │  ├─ host.json
│  │  │  │  ├─ local.settings.json
│  │  │  │  ├─ pom.xml
│  │  │  │  └─ src
│  │  │  │     └─ main
│  │  │  │        └─ java
│  │  │  │           └─ com
│  │  │  │              └─ function
│  │  │  │                 ├─ AddProductColumnTypes.java
│  │  │  │                 ├─ AddProductDefaultPKAndDifferentColumnOrder.java
│  │  │  │                 ├─ AddProductExtraColumns.java
│  │  │  │                 ├─ AddProductIncorrectCasing.java
│  │  │  │                 ├─ AddProductMissingColumns.java
│  │  │  │                 ├─ AddProductMissingColumnsExceptionFunction.java
│  │  │  │                 ├─ AddProductsNoPartialUpsert.java
│  │  │  │                 ├─ AddProductUnsupportedTypes.java
│  │  │  │                 ├─ Common
│  │  │  │                 │  ├─ Product.java
│  │  │  │                 │  ├─ ProductColumnTypes.java
│  │  │  │                 │  ├─ ProductDefaultPKAndDifferentColumnOrder.java
│  │  │  │                 │  ├─ ProductExtraColumns.java
│  │  │  │                 │  ├─ ProductIncorrectCasing.java
│  │  │  │                 │  ├─ ProductMissingColumns.java
│  │  │  │                 │  └─ ProductUnsupportedTypes.java
│  │  │  │                 └─ GetProductsColumnTypesSerialization.java
│  │  │  ├─ test-js
│  │  │  │  ├─ .eslintrc.json
│  │  │  │  ├─ AddProductColumnTypes
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductDefaultPKAndDifferentColumnOrder
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductExtraColumns
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductIncorrectCasing
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductMissingColumns
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductMissingColumnsExceptionFunction
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductsNoPartialUpsert
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ AddProductUnsupportedTypes
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ GetProductsColumnTypesSerialization
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ package-lock.json
│  │  │  │  └─ package.json
│  │  │  ├─ test-powershell
│  │  │  │  ├─ AddProductColumnTypes
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductDefaultPKAndDifferentColumnOrder
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductExtraColumns
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductIncorrectCasing
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductMissingColumns
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductMissingColumnsExceptionFunction
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductsNoPartialUpsert
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  ├─ AddProductUnsupportedTypes
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ run.ps1
│  │  │  │  └─ GetProductsColumnTypesSerialization
│  │  │  │     ├─ function.json
│  │  │  │     └─ run.ps1
│  │  │  └─ test-python
│  │  │     ├─ AddProductColumnTypes
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ AddProductDefaultPKAndDifferentColumnOrder
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ AddProductExtraColumns
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ AddProductMissingColumns
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ AddProductMissingColumnsException
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ AddProductsNoPartialUpsert
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ AddProductUnsupportedTypes
│  │  │     │  ├─ function.json
│  │  │     │  └─ __init__.py
│  │  │     ├─ Common
│  │  │     │  ├─ product.py
│  │  │     │  ├─ productcolumntypes.py
│  │  │     │  ├─ productdefaultpkanddifferentcolumnorder.py
│  │  │     │  ├─ productextracolumns.py
│  │  │     │  ├─ productmissingcolumns.py
│  │  │     │  └─ productunsupportedtypes.py
│  │  │     └─ GetProductsColumnTypesSerialization
│  │  │        ├─ function.json
│  │  │        └─ __init__.py
│  │  ├─ Microsoft.Azure.WebJobs.Extensions.Sql.Tests.csproj
│  │  ├─ packages.lock.json
│  │  ├─ README.md
│  │  └─ Unit
│  │     ├─ SqlInputBindingTests.cs
│  │     ├─ SqlOutputBindingTests.cs
│  │     └─ UtilsTests.cs
│  ├─ test-outofproc
│  │  ├─ .editorconfig
│  │  ├─ .vscode
│  │  │  └─ extensions.json
│  │  ├─ AddProductColumnTypes.cs
│  │  ├─ AddProductDefaultPKAndDifferentColumnOrder.cs
│  │  ├─ AddProductExtraColumns.cs
│  │  ├─ AddProductIncorrectCasing.cs
│  │  ├─ AddProductMissingColumns.cs
│  │  ├─ AddProductMissingColumnsException.cs
│  │  ├─ AddProductsNoPartialUpsert.cs
│  │  ├─ AddProductUnsupportedTypes.cs
│  │  ├─ GetProductColumnTypesSerialization.cs
│  │  ├─ GetProductColumnTypesSerializationAsyncEnumerable.cs
│  │  ├─ GlobalSuppressions.cs
│  │  ├─ host.json
│  │  ├─ local.settings.json
│  │  ├─ packages.lock.json
│  │  ├─ Product.cs
│  │  ├─ Program.cs
│  │  ├─ Properties
│  │  │  └─ launchSettings.json
│  │  ├─ test-outofproc.csproj
│  │  └─ Unit
│  │     └─ WorkerUnitTests.cs
│  ├─ WebJobs.Extensions.Sql.sln
│  └─ Worker.Extensions.Sql
│     └─ src
│        ├─ Microsoft.Azure.Functions.Worker.Extensions.Sql.csproj
│        ├─ packages.lock.json
│        ├─ README.md
│        ├─ SqlInputAttribute.cs
│        └─ SqlOutputAttribute.cs
├─ azure.ipynb
├─ back-office
│  ├─ .dockerignore
│  ├─ .editorconfig
│  ├─ .eslintignore
│  ├─ .eslintrc.cjs
│  ├─ .husky
│  │  ├─ commit-msg
│  │  └─ pre-commit
│  ├─ .nvmrc
│  ├─ .prettierignore
│  ├─ .prettierrc
│  ├─ .vscode
│  │  ├─ extensions.json
│  │  ├─ launch.json
│  │  └─ settings.json
│  ├─ appeals
│  │  ├─ api
│  │  │  ├─ .dockerignore
│  │  │  ├─ .env.example
│  │  │  ├─ .env.test
│  │  │  ├─ Dockerfile
│  │  │  ├─ index.d.ts
│  │  │  ├─ jest.config.js
│  │  │  ├─ jsconfig.json
│  │  │  ├─ package.json
│  │  │  ├─ setup-tests.js
│  │  │  └─ src
│  │  │     ├─ database
│  │  │     │  ├─ migrations
│  │  │     │  │  ├─ 20230314111643_create_initial_migration
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230316153311_remove_unique_constraint_on_versionid
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230316160310_remove_version_id
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230328110224_rename_column_is_over18_to_under18
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230420095018_documentversion_documenttype_nullable
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230421140434_documentversion_publishedstatusprev
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230421141335_exam_timetable_type_reference_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230424123305_exam_timetable_type_name_unique
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230426150420_examtimetable_add_template_type_field
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230509134331_add_document_latest_version_column
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230510080111_default_appeal_status
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230518104003_move_coulmn_from_document_to_document_versions
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230518112455_add_appeal_timetable
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230519123437_representations_actions_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230522131308_add_examination_timetable_items_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230522131835_add_case_id_column_examination_items_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230523195409_add_start_end_time_columns_examination_items_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230526092956_update_lpa_questionnaire
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230526130756_represntauions_actions_table_notes
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230530093928_correct_schema_drift
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230530111714_add_linked_appeals
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230530142748_configure_latest_document_version_constraints
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230531134004_representations_actions_none_mandatory_fields
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230531185104_denormalise_case_to_document
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230531185105_make_document_non_nullable
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230601144617_remove_end_date_column_examination_items_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230601183730_latest_version_id_nullable
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230602140605_rename_examination_item_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230605140153_
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230608100202_add_address_country_column
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230609122204_add_published_column_examination_items_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230609152850_add_appellant_case
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230612174905_representation_attachment_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230615143104_representaion_received_is_optional
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230620101631_save_appellant_case_outcome
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230621205323_add_folder_id_to_examination_timetable_items
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230622105609_save_lpa_questionnaire_validation_outcome
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230628150520_document_folders
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230629073034_clear_application_objects
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230707131036_update_lpa_questionnaire
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230707180928_enforce_folder_appeal_constraint
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230713091434_update_site_visit
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230713134406_add_appeal_due_date
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230725195721_add_appeal_allocation_specialisms
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230817113739_other_not_valid_reasons_character_limit_4000
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230817140914_adjust_documents_and_folders
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230817154404_add_is_conservation_area
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230905113921_update_lpa_questionnaire
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230906083337_add_case_officer_and_inspector_assignment
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230914105124_update_incomplete_invalid_reason_text
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230918144210_update_address_schema
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230922142342_add_document_redaction_status_and_received_date
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230928104020_add_audit_trail
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231005112224_serviceusers_lpa_models
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231012155812_additional_appellantcase_fields
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231020085722_docs_audit_trail_extension
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231025153740_set_redaction_status
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231107145621_inspector_decision
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231127093218_agent_submission
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231128131711_optional_decision_letter_guid_in_inspector_decision
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231130170615_document_version_refactor
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231212091313_default_status_assign_case_officer
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  └─ migration_lock.toml
│  │  │     │  ├─ prisma.truncate.js
│  │  │     │  ├─ schema.d.ts
│  │  │     │  ├─ schema.prisma
│  │  │     │  └─ seed
│  │  │     │     ├─ data-samples.js
│  │  │     │     ├─ data-static.js
│  │  │     │     ├─ data-test.js
│  │  │     │     ├─ seed-clear.js
│  │  │     │     ├─ seed-development.js
│  │  │     │     └─ seed-production.js
│  │  │     ├─ message-schemas
│  │  │     │  ├─ pins-appeal.schema.json
│  │  │     │  ├─ pins-appellant-case.schema.json
│  │  │     │  ├─ pins-document.schema.json
│  │  │     │  ├─ pins-lpa-questionnaire.schema.json
│  │  │     │  └─ pins-root.schema.json
│  │  │     ├─ server
│  │  │     │  ├─ app-test.js
│  │  │     │  ├─ app.js
│  │  │     │  ├─ build-app.js
│  │  │     │  ├─ common
│  │  │     │  │  ├─ controllers
│  │  │     │  │  │  └─ lookup-data.controller.js
│  │  │     │  │  └─ validators
│  │  │     │  │     ├─ boolean-parameter.js
│  │  │     │  │     ├─ boolean-with-conditional-string-parameters.js
│  │  │     │  │     ├─ date-parameter.js
│  │  │     │  │     ├─ id-parameter.js
│  │  │     │  │     ├─ incomplete-invalid-reason-parameter.js
│  │  │     │  │     ├─ number-array-parameter.js
│  │  │     │  │     ├─ number-parameter.js
│  │  │     │  │     ├─ string-parameter.js
│  │  │     │  │     ├─ time-parameter.js
│  │  │     │  │     ├─ time-range-parameters.js
│  │  │     │  │     └─ uuid-parameter.js
│  │  │     │  ├─ config
│  │  │     │  │  ├─ config.js
│  │  │     │  │  └─ schema.js
│  │  │     │  ├─ endpoints
│  │  │     │  │  ├─ addresses
│  │  │     │  │  │  ├─ addresses.controller.js
│  │  │     │  │  │  ├─ addresses.formatter.js
│  │  │     │  │  │  ├─ addresses.routes.js
│  │  │     │  │  │  ├─ addresses.service.js
│  │  │     │  │  │  ├─ addresses.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ addresses.test.js
│  │  │     │  │  ├─ appeal-allocation
│  │  │     │  │  │  ├─ appeal-allocation-controller.js
│  │  │     │  │  │  ├─ appeal-allocation-routes.js
│  │  │     │  │  │  ├─ appeal-allocation-validator.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ appeal-allocation.test.js
│  │  │     │  │  ├─ appeal-decision
│  │  │     │  │  │  ├─ appeal-decision.controller.js
│  │  │     │  │  │  ├─ appeal-decision.middleware.js
│  │  │     │  │  │  ├─ appeal-decision.routes.js
│  │  │     │  │  │  ├─ appeal-decision.service.js
│  │  │     │  │  │  ├─ appeal-decision.validator.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ appeal-decision.test.js
│  │  │     │  │  ├─ appeal-timetables
│  │  │     │  │  │  ├─ appeal-timetables.controller.js
│  │  │     │  │  │  ├─ appeal-timetables.routes.js
│  │  │     │  │  │  ├─ appeal-timetables.service.js
│  │  │     │  │  │  ├─ appeal-timetables.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ appeal-timetables.test.js
│  │  │     │  │  ├─ appeals
│  │  │     │  │  │  ├─ appeals.controller.js
│  │  │     │  │  │  ├─ appeals.formatter.js
│  │  │     │  │  │  ├─ appeals.routes.js
│  │  │     │  │  │  ├─ appeals.service.js
│  │  │     │  │  │  ├─ appeals.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ appeals.test.js
│  │  │     │  │  ├─ appeals.d.ts
│  │  │     │  │  ├─ appeals.routes.js
│  │  │     │  │  ├─ appellant-case-incomplete-reasons
│  │  │     │  │  │  ├─ appellant-case-incomplete-reasons.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ appellant-case-incomplete-reasons.test.js
│  │  │     │  │  ├─ appellant-case-invalid-reasons
│  │  │     │  │  │  ├─ appellant-case-invalid-reasons.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ appellant-case-invalid-reasons.test.js
│  │  │     │  │  ├─ appellant-case-validation-outcomes
│  │  │     │  │  │  ├─ appellant-case-validation-outcomes.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ appellant-case-validation-outcomes.test.js
│  │  │     │  │  ├─ appellant-cases
│  │  │     │  │  │  ├─ appellant-cases.controller.js
│  │  │     │  │  │  ├─ appellant-cases.formatter.js
│  │  │     │  │  │  ├─ appellant-cases.routes.js
│  │  │     │  │  │  ├─ appellant-cases.service.js
│  │  │     │  │  │  ├─ appellant-cases.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ appellant-cases.test.js
│  │  │     │  │  ├─ appellants
│  │  │     │  │  │  ├─ appellants.controller.js
│  │  │     │  │  │  ├─ appellants.formatter.js
│  │  │     │  │  │  ├─ appellants.routes.js
│  │  │     │  │  │  ├─ appellants.service.js
│  │  │     │  │  │  ├─ appellants.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ appellants.test.js
│  │  │     │  │  ├─ audit-trails
│  │  │     │  │  │  ├─ audit-trails.controller.js
│  │  │     │  │  │  ├─ audit-trails.formatter.js
│  │  │     │  │  │  ├─ audit-trails.routes.js
│  │  │     │  │  │  ├─ audit-trails.service.js
│  │  │     │  │  │  ├─ audit-trails.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ audit-trails.test.js
│  │  │     │  │  ├─ constants.js
│  │  │     │  │  ├─ designated-sites
│  │  │     │  │  │  ├─ designated-sites.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ designated-sites.test.js
│  │  │     │  │  ├─ document-redaction-statuses
│  │  │     │  │  │  ├─ document-redaction-statuses.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ document-redaction-statuses.test.js
│  │  │     │  │  ├─ documents
│  │  │     │  │  │  ├─ documents.controller.js
│  │  │     │  │  │  ├─ documents.formatter.js
│  │  │     │  │  │  ├─ documents.mapper.js
│  │  │     │  │  │  ├─ documents.middleware.js
│  │  │     │  │  │  ├─ documents.routes.js
│  │  │     │  │  │  ├─ documents.service.js
│  │  │     │  │  │  ├─ documents.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ documents.test.js
│  │  │     │  │  ├─ integrations
│  │  │     │  │  │  ├─ integrations.controller.js
│  │  │     │  │  │  ├─ integrations.mappers
│  │  │     │  │  │  │  ├─ address.mapper.js
│  │  │     │  │  │  │  ├─ appeal-allocation.mapper.js
│  │  │     │  │  │  │  ├─ appeal-type.mapper.js
│  │  │     │  │  │  │  ├─ appellant-case.mapper.js
│  │  │     │  │  │  │  ├─ casedata.mapper.js
│  │  │     │  │  │  │  ├─ document.mapper.js
│  │  │     │  │  │  │  ├─ index.js
│  │  │     │  │  │  │  ├─ lpa.mapper.js
│  │  │     │  │  │  │  ├─ questionnaire.mapper.js
│  │  │     │  │  │  │  └─ service-user.mapper.js
│  │  │     │  │  │  ├─ integrations.middleware.js
│  │  │     │  │  │  ├─ integrations.routes.js
│  │  │     │  │  │  ├─ integrations.service.js
│  │  │     │  │  │  ├─ integrations.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ integration.test.js
│  │  │     │  │  ├─ invalid-appeal-decision
│  │  │     │  │  │  ├─ invalid-appeal-decision.controller.js
│  │  │     │  │  │  ├─ invalid-appeal-decision.middleware.js
│  │  │     │  │  │  ├─ invalid-appeal-decision.routes.js
│  │  │     │  │  │  ├─ invalid-appeal-decision.service.js
│  │  │     │  │  │  ├─ invalid-appeal-decision.validator.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ invalid-appeal-decision.test.js
│  │  │     │  │  ├─ knowledge-of-other-landowners
│  │  │     │  │  │  ├─ knowledge-of-other-landowners.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ knowledge-of-other-landowners.test.js
│  │  │     │  │  ├─ lpa-notification-methods
│  │  │     │  │  │  ├─ lpa-notification-methods.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ lpa-notification-methods.test.js
│  │  │     │  │  ├─ lpa-questionnaire-incomplete-reasons
│  │  │     │  │  │  ├─ lpa-questionnaire-incomplete-reasons.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ lpa-questionnaire-incomplete-reasons.test.js
│  │  │     │  │  ├─ lpa-questionnaire-validation-outcomes
│  │  │     │  │  │  ├─ lpa-questionnaire-validation-outcomes.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ lpa-questionnaire-validation-outcomes.test.js
│  │  │     │  │  ├─ lpa-questionnaires
│  │  │     │  │  │  ├─ lpa-questionnaires.controller.js
│  │  │     │  │  │  ├─ lpa-questionnaires.formatter.js
│  │  │     │  │  │  ├─ lpa-questionnaires.routes.js
│  │  │     │  │  │  ├─ lpa-questionnaires.service.js
│  │  │     │  │  │  ├─ lpa-questionnaires.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ lpa-questionnaires.test.js
│  │  │     │  │  ├─ planning-obligation-statuses
│  │  │     │  │  │  ├─ planning-obligation-statuses.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ planning-obligation-statuses.test.js
│  │  │     │  │  ├─ procedure-types
│  │  │     │  │  │  ├─ procedure-types.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ procedure-types.test.js
│  │  │     │  │  ├─ schedule-types
│  │  │     │  │  │  ├─ schedule-types.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ schedule-types.test.js
│  │  │     │  │  ├─ site-visit-types
│  │  │     │  │  │  ├─ site-visit-types.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ site-visit-types.test.js
│  │  │     │  │  └─ site-visits
│  │  │     │  │     ├─ site-visits.controller.js
│  │  │     │  │     ├─ site-visits.formatter.js
│  │  │     │  │     ├─ site-visits.routes.js
│  │  │     │  │     ├─ site-visits.service.js
│  │  │     │  │     ├─ site-visits.validators.js
│  │  │     │  │     └─ __tests__
│  │  │     │  │        └─ site-visits.test.js
│  │  │     │  ├─ gen-api-spec.js
│  │  │     │  ├─ infrastructure
│  │  │     │  │  ├─ event-client.js
│  │  │     │  │  └─ topics.js
│  │  │     │  ├─ middleware
│  │  │     │  │  ├─ async-handler.js
│  │  │     │  │  ├─ check-appeal-exists-and-add-to-request.js
│  │  │     │  │  ├─ check-azure-ad-user-id-header-exists.js
│  │  │     │  │  ├─ check-lookup-value-is-valid-and-add-to-request.js
│  │  │     │  │  ├─ check-lookup-values-are-valid.js
│  │  │     │  │  ├─ error-handler.js
│  │  │     │  │  ├─ handle-validation-error.js
│  │  │     │  │  ├─ init-notify-client-and-add-to-request.js
│  │  │     │  │  └─ version-routes.js
│  │  │     │  ├─ openapi-types.ts
│  │  │     │  ├─ openapi.json
│  │  │     │  ├─ repositories
│  │  │     │  │  ├─ address.repository.js
│  │  │     │  │  ├─ appeal-allocation.repository.js
│  │  │     │  │  ├─ appeal-status.repository.js
│  │  │     │  │  ├─ appeal-timetable.repository.js
│  │  │     │  │  ├─ appeal.repository.js
│  │  │     │  │  ├─ appellant-case.repository.js
│  │  │     │  │  ├─ appellant.repository.js
│  │  │     │  │  ├─ audit-trail.repository.js
│  │  │     │  │  ├─ common.repository.js
│  │  │     │  │  ├─ document-metadata.repository.js
│  │  │     │  │  ├─ document-redaction-status.repository.js
│  │  │     │  │  ├─ document.repository.js
│  │  │     │  │  ├─ folder.repository.js
│  │  │     │  │  ├─ integrations.repository.js
│  │  │     │  │  ├─ lpa-questionnaire.repository.js
│  │  │     │  │  ├─ raw_sql_queries
│  │  │     │  │  │  └─ update-application-reference.sql
│  │  │     │  │  ├─ service-customer.repository.js
│  │  │     │  │  ├─ site-visit.repository.js
│  │  │     │  │  └─ user.repository.js
│  │  │     │  ├─ state
│  │  │     │  │  ├─ create-state-machine.js
│  │  │     │  │  ├─ state-machines
│  │  │     │  │  │  ├─ fpa.js
│  │  │     │  │  │  └─ has.js
│  │  │     │  │  └─ transition-state.js
│  │  │     │  ├─ swagger.js
│  │  │     │  ├─ tests
│  │  │     │  │  ├─ appeals
│  │  │     │  │  │  ├─ expectation.js
│  │  │     │  │  │  └─ mocks.js
│  │  │     │  │  ├─ documents
│  │  │     │  │  │  └─ mocks.js
│  │  │     │  │  ├─ integrations
│  │  │     │  │  │  └─ mocks.js
│  │  │     │  │  └─ shared
│  │  │     │  │     └─ mocks.js
│  │  │     │  └─ utils
│  │  │     │     ├─ app-error.js
│  │  │     │     ├─ appeal-formatter.js
│  │  │     │     ├─ appeal-sorter.js
│  │  │     │     ├─ application-factory-for-tests.js
│  │  │     │     ├─ array-of-statuses-contains-string.js
│  │  │     │     ├─ break-up-compound-status.js
│  │  │     │     ├─ build-appeal-compound-status.js
│  │  │     │     ├─ business-days.js
│  │  │     │     ├─ cache-data.js
│  │  │     │     ├─ check-strings-match.js
│  │  │     │     ├─ check-validation-outcome.js
│  │  │     │     ├─ create-enums.js
│  │  │     │     ├─ create-many-to-many-relation-data.js
│  │  │     │     ├─ database-connector.js
│  │  │     │     ├─ database-pagination.js
│  │  │     │     ├─ date-comparison.js
│  │  │     │     ├─ date-formatter.js
│  │  │     │     ├─ days-between-dates.js
│  │  │     │     ├─ feature-flags.js
│  │  │     │     ├─ find-previous-version.js
│  │  │     │     ├─ format-address.js
│  │  │     │     ├─ format-documentation-status.js
│  │  │     │     ├─ format-linked-appeals.js
│  │  │     │     ├─ format-neighbouring-site-contacts.js
│  │  │     │     ├─ format-validation-outcome-response.js
│  │  │     │     ├─ is-fpa.js
│  │  │     │     ├─ join-date-and-time.js
│  │  │     │     ├─ logger.js
│  │  │     │     ├─ map-states-to-strings.js
│  │  │     │     ├─ mapping
│  │  │     │     │  ├─ map-application-with-search-criteria.js
│  │  │     │     │  ├─ map-application-with-sector-and-subsector.js
│  │  │     │     │  ├─ map-application.js
│  │  │     │     │  ├─ map-case-details.js
│  │  │     │     │  ├─ map-case-status-string.js
│  │  │     │     │  ├─ map-case-status.js
│  │  │     │     │  ├─ map-date-string-to-unix-timestamp.js
│  │  │     │     │  ├─ map-document-details.js
│  │  │     │     │  ├─ map-folder-details.js
│  │  │     │     │  ├─ map-grid-reference.js
│  │  │     │     │  ├─ map-keys-using-object.js
│  │  │     │     │  ├─ map-region.js
│  │  │     │     │  ├─ map-sector.js
│  │  │     │     │  ├─ map-service-customer.js
│  │  │     │     │  ├─ map-values-using-object.js
│  │  │     │     │  └─ map-zoom-level.js
│  │  │     │     ├─ notify-client.js
│  │  │     │     ├─ prisma-middleware
│  │  │     │     │  └─ index.js
│  │  │     │     ├─ prisma-middleware.js
│  │  │     │     ├─ schema-test-utils.js
│  │  │     │     ├─ string-token-replacement.js
│  │  │     │     ├─ transition-state.js
│  │  │     │     └─ __tests__
│  │  │     │        ├─ break-up-compound-status.test.js
│  │  │     │        ├─ build-appeal-compound-status.test.js
│  │  │     │        ├─ create-enums.test.js
│  │  │     │        ├─ date-comparison.test.js
│  │  │     │        ├─ days-between-dates.test.js
│  │  │     │        ├─ feature-flags.test.js
│  │  │     │        ├─ find-previous-version.test.js
│  │  │     │        ├─ prisma-middleware.test.js
│  │  │     │        └─ sort-appeals.test.js
│  │  │     └─ server.js
│  │  ├─ functions
│  │  │  ├─ casedata-import
│  │  │  │  ├─ appellant-case
│  │  │  │  │  ├─ back-office-api-client.js
│  │  │  │  │  ├─ config.js
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ host.json
│  │  │  │  ├─ local.settings.json
│  │  │  │  ├─ package.json
│  │  │  │  ├─ questionnaire
│  │  │  │  │  ├─ back-office-api-client.js
│  │  │  │  │  ├─ config.js
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  └─ README.md
│  │  │  ├─ document-processing
│  │  │  │  ├─ document-move
│  │  │  │  │  ├─ blob.js
│  │  │  │  │  ├─ config.js
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ host.json
│  │  │  │  ├─ local.settings.json
│  │  │  │  ├─ malware-detection
│  │  │  │  │  ├─ back-office-api-client.js
│  │  │  │  │  ├─ config.js
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ package.json
│  │  │  │  └─ README.md
│  │  │  └─ user-import
│  │  │     ├─ employee
│  │  │     │  ├─ back-office-api-client.js
│  │  │     │  ├─ config.js
│  │  │     │  ├─ function.json
│  │  │     │  └─ index.js
│  │  │     ├─ host.json
│  │  │     ├─ local.settings.json
│  │  │     ├─ package.json
│  │  │     ├─ README.md
│  │  │     └─ service-user
│  │  │        ├─ back-office-api-client.js
│  │  │        ├─ config.js
│  │  │        ├─ function.json
│  │  │        └─ index.js
│  │  └─ web
│  │     ├─ .browserslistrc
│  │     ├─ .dockerignore
│  │     ├─ .env.example
│  │     ├─ .env.test
│  │     ├─ babel.config.js
│  │     ├─ Dockerfile
│  │     ├─ environment
│  │     │  ├─ base-config.js
│  │     │  ├─ config.d.ts
│  │     │  ├─ config.js
│  │     │  └─ schema.js
│  │     ├─ jest.config.js
│  │     ├─ jsconfig.json
│  │     ├─ nodemon.json
│  │     ├─ package.json
│  │     ├─ scripts
│  │     │  └─ rollup
│  │     │     ├─ bundle-js.js
│  │     │     ├─ compile-css.js
│  │     │     ├─ get-logger.js
│  │     │     ├─ hash.js
│  │     │     ├─ minify-js.js
│  │     │     └─ rollup-plugin-virtual-json.js
│  │     ├─ setup-tests.js
│  │     ├─ src
│  │     │  ├─ client
│  │     │  │  ├─ app.js
│  │     │  │  ├─ components
│  │     │  │  │  ├─ accessible-autocomplete.js
│  │     │  │  │  ├─ add-another
│  │     │  │  │  │  └─ add-another.js
│  │     │  │  │  ├─ base.js
│  │     │  │  │  ├─ excerpts
│  │     │  │  │  │  ├─ excerpt.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     └─ excerpt.test.js
│  │     │  │  │  ├─ file-uploader
│  │     │  │  │  │  ├─ file-uploader.module.js
│  │     │  │  │  │  ├─ _client-actions.js
│  │     │  │  │  │  ├─ _errors.js
│  │     │  │  │  │  ├─ _html.js
│  │     │  │  │  │  ├─ _server-actions.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     └─ file-uploader.test.js
│  │     │  │  │  ├─ files-list
│  │     │  │  │  │  ├─ files-list.module.js
│  │     │  │  │  │  ├─ _html.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     └─ files-list.test.js
│  │     │  │  │  └─ select-all-checkbox
│  │     │  │  │     ├─ select-all-checkbox.js
│  │     │  │  │     └─ __tests__
│  │     │  │  │        └─ select-all-checkbox.test.js
│  │     │  │  └─ pages
│  │     │  │     └─ default.js
│  │     │  ├─ common
│  │     │  │  ├─ feature-flags.js
│  │     │  │  └─ __tests__
│  │     │  │     └─ feature-flags.test.js
│  │     │  ├─ server
│  │     │  │  ├─ app
│  │     │  │  │  ├─ app.controller.js
│  │     │  │  │  ├─ app.express.js
│  │     │  │  │  ├─ app.router.js
│  │     │  │  │  ├─ auth
│  │     │  │  │  │  ├─ auth-session.service.js
│  │     │  │  │  │  ├─ auth.controller.js
│  │     │  │  │  │  ├─ auth.guards.js
│  │     │  │  │  │  ├─ auth.pipes.js
│  │     │  │  │  │  ├─ auth.router.js
│  │     │  │  │  │  ├─ auth.service.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     ├─ auth.test.js
│  │     │  │  │  │     └─ __snapshots__
│  │     │  │  │  │        └─ auth.test.js.snap
│  │     │  │  │  ├─ components
│  │     │  │  │  │  ├─ file-downloader.component.js
│  │     │  │  │  │  └─ file-uploader.component.js
│  │     │  │  │  └─ config
│  │     │  │  │     ├─ locals.js
│  │     │  │  │     ├─ nunjucks.js
│  │     │  │  │     └─ session.js
│  │     │  │  ├─ appeals
│  │     │  │  │  ├─ appeal-details
│  │     │  │  │  │  ├─ allocation-details
│  │     │  │  │  │  │  ├─ allocation-details.controller.js
│  │     │  │  │  │  │  ├─ allocation-details.mapper.js
│  │     │  │  │  │  │  ├─ allocation-details.router.js
│  │     │  │  │  │  │  ├─ allocation-details.service.js
│  │     │  │  │  │  │  ├─ allocation-details.validators.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ allocation-details.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ allocation-details.test.js.snap
│  │     │  │  │  │  ├─ appeal-details.controller.js
│  │     │  │  │  │  ├─ appeal-details.mapper.js
│  │     │  │  │  │  ├─ appeal-details.middleware.js
│  │     │  │  │  │  ├─ appeal-details.router.js
│  │     │  │  │  │  ├─ appeal-details.service.js
│  │     │  │  │  │  ├─ appeal-details.types.d.ts
│  │     │  │  │  │  ├─ appeal-timetables
│  │     │  │  │  │  │  ├─ appeal-timetables.controller.js
│  │     │  │  │  │  │  ├─ appeal-timetables.mapper.js
│  │     │  │  │  │  │  ├─ appeal-timetables.router.js
│  │     │  │  │  │  │  ├─ appeal-timetables.service.js
│  │     │  │  │  │  │  ├─ appeal-timetables.validators.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ appeal-timetables.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ appeal-timetables.test.js.snap
│  │     │  │  │  │  ├─ appellant-case
│  │     │  │  │  │  │  ├─ appellant-case.controller.js
│  │     │  │  │  │  │  ├─ appellant-case.mapper.js
│  │     │  │  │  │  │  ├─ appellant-case.router.js
│  │     │  │  │  │  │  ├─ appellant-case.service.js
│  │     │  │  │  │  │  ├─ appellant-case.types.d.ts
│  │     │  │  │  │  │  ├─ appellant-case.validators.js
│  │     │  │  │  │  │  ├─ outcome-incomplete
│  │     │  │  │  │  │  │  ├─ outcome-incomplete.controller.js
│  │     │  │  │  │  │  │  ├─ outcome-incomplete.router.js
│  │     │  │  │  │  │  │  └─ outcome-incomplete.validators.js
│  │     │  │  │  │  │  ├─ outcome-invalid
│  │     │  │  │  │  │  │  ├─ outcome-invalid.controller.js
│  │     │  │  │  │  │  │  ├─ outcome-invalid.router.js
│  │     │  │  │  │  │  │  └─ outcome-invalid.validators.js
│  │     │  │  │  │  │  ├─ outcome-valid
│  │     │  │  │  │  │  │  ├─ outcome-valid.controller.js
│  │     │  │  │  │  │  │  └─ outcome-valid.router.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ appellant-case.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ appellant-case.test.js.snap
│  │     │  │  │  │  ├─ assign-user
│  │     │  │  │  │  │  ├─ assign-user.controller.js
│  │     │  │  │  │  │  ├─ assign-user.mapper.js
│  │     │  │  │  │  │  ├─ assign-user.router.js
│  │     │  │  │  │  │  ├─ assign-user.service.js
│  │     │  │  │  │  │  ├─ assign-user.validator.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ assign-user.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ assign-user.test.js.snap
│  │     │  │  │  │  ├─ lpa-questionnaire
│  │     │  │  │  │  │  ├─ lpa-questionnaire.controller.js
│  │     │  │  │  │  │  ├─ lpa-questionnaire.mapper.js
│  │     │  │  │  │  │  ├─ lpa-questionnaire.router.js
│  │     │  │  │  │  │  ├─ lpa-questionnaire.service.js
│  │     │  │  │  │  │  ├─ lpa-questionnaire.types.d.ts
│  │     │  │  │  │  │  ├─ lpa-questionnaire.validators.js
│  │     │  │  │  │  │  ├─ outcome-incomplete
│  │     │  │  │  │  │  │  ├─ outcome-incomplete.controller.js
│  │     │  │  │  │  │  │  ├─ outcome-incomplete.router.js
│  │     │  │  │  │  │  │  └─ outcome-incomplete.validators.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ lpa-questionnaire.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ lpa-questionnaire.test.js.snap
│  │     │  │  │  │  ├─ site-visit
│  │     │  │  │  │  │  ├─ site-visit.controller.js
│  │     │  │  │  │  │  ├─ site-visit.mapper.js
│  │     │  │  │  │  │  ├─ site-visit.router.js
│  │     │  │  │  │  │  ├─ site-visit.service.js
│  │     │  │  │  │  │  ├─ site-visit.validators.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ site-visit.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ site-visit.test.js.snap
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     ├─ appeal-details.test.js
│  │     │  │  │  │     └─ __snapshots__
│  │     │  │  │  │        └─ appeal-details.test.js.snap
│  │     │  │  │  ├─ appeal-documents
│  │     │  │  │  │  ├─ appeal-documents.controller.js
│  │     │  │  │  │  ├─ appeal-documents.mapper.js
│  │     │  │  │  │  ├─ appeal-documents.middleware.js
│  │     │  │  │  │  ├─ appeal-documents.router.js
│  │     │  │  │  │  ├─ appeal-documents.validators.js
│  │     │  │  │  │  ├─ appeal.documents.service.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     ├─ appeal-documents.test.js
│  │     │  │  │  │     └─ __snapshots__
│  │     │  │  │  │        └─ appeal-documents.test.js.snap
│  │     │  │  │  ├─ appeal-users
│  │     │  │  │  │  └─ users-service.js
│  │     │  │  │  ├─ appeal.constants.js
│  │     │  │  │  ├─ appeals.copy.js
│  │     │  │  │  ├─ appeals.router.js
│  │     │  │  │  ├─ appeals.types.d.ts
│  │     │  │  │  ├─ change-page
│  │     │  │  │  │  ├─ change-page.controller.js
│  │     │  │  │  │  ├─ change-page.mapper.js
│  │     │  │  │  │  └─ change-page.router.js
│  │     │  │  │  ├─ national-list
│  │     │  │  │  │  ├─ national-list.controller.js
│  │     │  │  │  │  ├─ national-list.router.js
│  │     │  │  │  │  ├─ national-list.service.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     ├─ national-list.test.js
│  │     │  │  │  │     └─ __snapshots__
│  │     │  │  │  │        └─ national-list.test.js.snap
│  │     │  │  │  └─ personal-list
│  │     │  │  │     ├─ personal-list.controller.js
│  │     │  │  │     ├─ personal-list.mapper.js
│  │     │  │  │     ├─ personal-list.router.js
│  │     │  │  │     ├─ personal-list.service.js
│  │     │  │  │     └─ __tests__
│  │     │  │  │        ├─ personal-list.test.js
│  │     │  │  │        └─ __snapshots__
│  │     │  │  │           └─ personal-list.test.js.snap
│  │     │  │  ├─ lib
│  │     │  │  │  ├─ accessibility.js
│  │     │  │  │  ├─ active-directory-token.js
│  │     │  │  │  ├─ address-formatter.js
│  │     │  │  │  ├─ appeals-formatter.js
│  │     │  │  │  ├─ async-route.js
│  │     │  │  │  ├─ body-formatter.js
│  │     │  │  │  ├─ boolean-formatter.js
│  │     │  │  │  ├─ cache-handler.js
│  │     │  │  │  ├─ dates.js
│  │     │  │  │  ├─ display-page-formatter.js
│  │     │  │  │  ├─ graph-request.js
│  │     │  │  │  ├─ id-name-pairs.js
│  │     │  │  │  ├─ logger.js
│  │     │  │  │  ├─ mappers
│  │     │  │  │  │  ├─ appeal.mapper.js
│  │     │  │  │  │  ├─ appellantCase.mapper.js
│  │     │  │  │  │  ├─ global-mapper-formatter.js
│  │     │  │  │  │  ├─ lpaQuestionnaire.mapper.js
│  │     │  │  │  │  ├─ mapper-types-jsdoc.js
│  │     │  │  │  │  ├─ mapper-utilities.js
│  │     │  │  │  │  ├─ notification-banners.mapper.js
│  │     │  │  │  │  ├─ validation-outcome-reasons.mapper.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     └─ mappers.test.js
│  │     │  │  │  ├─ middleware
│  │     │  │  │  │  ├─ add-apiclient-to-request.js
│  │     │  │  │  │  ├─ skip-middleware-if-errors-in-body.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     ├─ add-apiclient-to-request.test.js
│  │     │  │  │  │     └─ skip-middleware-if-errors-in-body.test.js
│  │     │  │  │  ├─ msal.js
│  │     │  │  │  ├─ nunjucks-filters
│  │     │  │  │  │  ├─ actions-parameter-for-document-status.js
│  │     │  │  │  │  ├─ add-conditional-html.js
│  │     │  │  │  │  ├─ appeals.js
│  │     │  │  │  │  ├─ boolean-answer.js
│  │     │  │  │  │  ├─ collapse.js
│  │     │  │  │  │  ├─ date.js
│  │     │  │  │  │  ├─ ends-with.js
│  │     │  │  │  │  ├─ error-message.js
│  │     │  │  │  │  ├─ error-summary.js
│  │     │  │  │  │  ├─ file-size.js
│  │     │  │  │  │  ├─ index.js
│  │     │  │  │  │  ├─ json.js
│  │     │  │  │  │  ├─ mime-type.js
│  │     │  │  │  │  ├─ object.js
│  │     │  │  │  │  ├─ select-items.js
│  │     │  │  │  │  ├─ set-attribute.js
│  │     │  │  │  │  ├─ status-tag.js
│  │     │  │  │  │  ├─ strip-query-parameters.js
│  │     │  │  │  │  ├─ url.js
│  │     │  │  │  │  └─ user-type-map.js
│  │     │  │  │  ├─ nunjucks-globals
│  │     │  │  │  │  ├─ index.js
│  │     │  │  │  │  └─ now.js
│  │     │  │  │  ├─ nunjucks-template-builders
│  │     │  │  │  │  ├─ gds-components-properties-jsdoc.js
│  │     │  │  │  │  ├─ page-component-rendering.js
│  │     │  │  │  │  └─ tag-builders.js
│  │     │  │  │  ├─ object-utilities.js
│  │     │  │  │  ├─ person-name-formatter.js
│  │     │  │  │  ├─ session-utilities.js
│  │     │  │  │  ├─ string-utilities.js
│  │     │  │  │  ├─ times.js
│  │     │  │  │  ├─ ts-utilities.js
│  │     │  │  │  ├─ validators
│  │     │  │  │  │  ├─ checkbox-text-items.validator.js
│  │     │  │  │  │  ├─ date-input.validator.js
│  │     │  │  │  │  ├─ textarea-validator.js
│  │     │  │  │  │  └─ time-input.validator.js
│  │     │  │  │  └─ __tests__
│  │     │  │  │     └─ libraries.test.js
│  │     │  │  ├─ server.js
│  │     │  │  ├─ static
│  │     │  │  │  └─ images
│  │     │  │  │     ├─ favicon.ico
│  │     │  │  │     ├─ govuk-apple-touch-icon-152x152.png
│  │     │  │  │     ├─ govuk-apple-touch-icon-167x167.png
│  │     │  │  │     ├─ govuk-apple-touch-icon-180x180.png
│  │     │  │  │     ├─ govuk-apple-touch-icon.png
│  │     │  │  │     ├─ govuk-crest-2x.png
│  │     │  │  │     ├─ govuk-crest.png
│  │     │  │  │     ├─ govuk-logotype-crown.png
│  │     │  │  │     ├─ govuk-mask-icon.svg
│  │     │  │  │     └─ govuk-opengraph-image.png
│  │     │  │  └─ views
│  │     │  │     ├─ app
│  │     │  │     │  ├─ 401.njk
│  │     │  │     │  ├─ 403.njk
│  │     │  │     │  ├─ 404.njk
│  │     │  │     │  ├─ 500.njk
│  │     │  │     │  ├─ components
│  │     │  │     │  │  ├─ add-another.njk
│  │     │  │     │  │  ├─ document-link.component.njk
│  │     │  │     │  │  ├─ document-list.component.njk
│  │     │  │     │  │  ├─ document-upload-info.njk
│  │     │  │     │  │  ├─ file-uploader.component.njk
│  │     │  │     │  │  ├─ file-uploader_legacy.njk
│  │     │  │     │  │  ├─ global-header.njk
│  │     │  │     │  │  ├─ govuk-date-input-extended.njk
│  │     │  │     │  │  ├─ info-box.njk
│  │     │  │     │  │  └─ time-input.njk
│  │     │  │     │  ├─ dashboard.njk
│  │     │  │     │  ├─ includes
│  │     │  │     │  │  └─ csrf.njk
│  │     │  │     │  └─ layouts
│  │     │  │     │     ├─ app-three-column.layout.njk
│  │     │  │     │     ├─ app-two-column.layout.njk
│  │     │  │     │     ├─ app.layout.njk
│  │     │  │     │     └─ README.md
│  │     │  │     ├─ appeals
│  │     │  │     │  ├─ all-appeals
│  │     │  │     │  │  └─ dashboard.njk
│  │     │  │     │  ├─ appeal
│  │     │  │     │  │  ├─ appellant-case-invalid-incomplete.njk
│  │     │  │     │  │  ├─ assign-new-user.njk
│  │     │  │     │  │  ├─ assign-user.njk
│  │     │  │     │  │  ├─ confirm-assign-unassign-user.njk
│  │     │  │     │  │  ├─ lpa-questionnaire-incomplete.njk
│  │     │  │     │  │  ├─ schedule-site-visit.njk
│  │     │  │     │  │  ├─ set-site-visit-type.njk
│  │     │  │     │  │  ├─ site-visit-booked.njk
│  │     │  │     │  │  └─ update-due-date.njk
│  │     │  │     │  ├─ components
│  │     │  │     │  │  ├─ add-another-reason.njk
│  │     │  │     │  │  ├─ appeals-table.njk
│  │     │  │     │  │  ├─ govuk-details.njk
│  │     │  │     │  │  ├─ page-component.njk
│  │     │  │     │  │  └─ status-tag.njk
│  │     │  │     │  ├─ confirmation.njk
│  │     │  │     │  └─ documents
│  │     │  │     │     ├─ add-document-details.njk
│  │     │  │     │     ├─ delete-document.njk
│  │     │  │     │     ├─ document-upload.njk
│  │     │  │     │     ├─ manage-document.njk
│  │     │  │     │     └─ manage-folder.njk
│  │     │  │     └─ patterns
│  │     │  │        ├─ change-page.pattern.njk
│  │     │  │        ├─ check-and-confirm-page.pattern.njk
│  │     │  │        └─ display-page.pattern.njk
│  │     │  └─ styles
│  │     │     ├─ .prettierrc
│  │     │     ├─ 1-settings
│  │     │     │  ├─ _settings.config.scss
│  │     │     │  └─ _settings.global.scss
│  │     │     ├─ 2-design-tokens
│  │     │     ├─ 3-tools
│  │     │     │  ├─ _index.scss
│  │     │     │  ├─ _tools.functions.scss
│  │     │     │  └─ _tools.z-index.scss
│  │     │     ├─ 4-generic
│  │     │     │  ├─ _generic.box-sizing.scss
│  │     │     │  ├─ _generic.colours.scss
│  │     │     │  ├─ _generic.display.scss
│  │     │     │  ├─ _generic.flex-grow.scss
│  │     │     │  ├─ _generic.font-weight.scss
│  │     │     │  ├─ _generic.reset.scss
│  │     │     │  ├─ _generic.text-align.scss
│  │     │     │  ├─ _generic.white-space.scss
│  │     │     │  └─ _generic.word-break.scss
│  │     │     ├─ 5-elements
│  │     │     │  ├─ _elements.form-group.scss
│  │     │     │  ├─ _elements.images.scss
│  │     │     │  └─ _elements.page.scss
│  │     │     ├─ 6-skeleton
│  │     │     │  └─ _container.scss
│  │     │     ├─ 7-components
│  │     │     │  ├─ add-another.scss
│  │     │     │  ├─ app-header.scss
│  │     │     │  ├─ DashboardBox
│  │     │     │  │  └─ DashboardBox.scss
│  │     │     │  ├─ file-upload.scss
│  │     │     │  ├─ files-list.scss
│  │     │     │  ├─ filter-box.scss
│  │     │     │  ├─ InfoBox
│  │     │     │  │  └─ InfoBox.scss
│  │     │     │  ├─ inline-definition-list.scss
│  │     │     │  ├─ ListMenu
│  │     │     │  │  └─ ListMenu.scss
│  │     │     │  ├─ results-per-page.scss
│  │     │     │  ├─ sort-table.scss
│  │     │     │  ├─ status-tag.scss
│  │     │     │  ├─ _autocomplete.scss
│  │     │     │  ├─ _button-group.scss
│  │     │     │  ├─ _header.scss
│  │     │     │  ├─ _masthead.scss
│  │     │     │  ├─ _related.scss
│  │     │     │  ├─ _summary-list.scss
│  │     │     │  └─ _table.scss
│  │     │     ├─ 8-utilities
│  │     │     │  └─ _layout.scss
│  │     │     ├─ 9-pages
│  │     │     ├─ dev
│  │     │     │  ├─ dev
│  │     │     │  │  └─ _dev.scss
│  │     │     │  └─ release
│  │     │     │     └─ _dev.scss
│  │     │     ├─ env
│  │     │     │  ├─ development
│  │     │     │  │  └─ _env-vars.scss
│  │     │     │  └─ production
│  │     │     │     └─ _env-vars.scss
│  │     │     ├─ main.scss
│  │     │     ├─ README.md
│  │     │     └─ _shame.scss
│  │     ├─ testing
│  │     │  ├─ app
│  │     │  │  ├─ app.js
│  │     │  │  ├─ factory
│  │     │  │  │  └─ account-info.js
│  │     │  │  ├─ fixtures
│  │     │  │  │  └─ referencedata.js
│  │     │  │  └─ mocks
│  │     │  │     ├─ auth.js
│  │     │  │     ├─ client-side.js
│  │     │  │     └─ msal.js
│  │     │  ├─ appeals
│  │     │  │  ├─ appeals.js
│  │     │  │  ├─ appeals.test.d.ts
│  │     │  │  └─ mocks
│  │     │  │     └─ api.js
│  │     │  ├─ index.js
│  │     │  ├─ lib
│  │     │  │  └─ testMappers.js
│  │     │  └─ util
│  │     │     └─ date.js
│  │     ├─ types-session.d.ts
│  │     └─ typings.d.ts
│  ├─ apps
│  │  ├─ api
│  │  │  ├─ .dockerignore
│  │  │  ├─ .env.example
│  │  │  ├─ .env.test
│  │  │  ├─ Dockerfile
│  │  │  ├─ index.d.ts
│  │  │  ├─ jest.config.js
│  │  │  ├─ jsconfig.json
│  │  │  ├─ package.json
│  │  │  ├─ setup-tests.js
│  │  │  └─ src
│  │  │     ├─ database
│  │  │     │  ├─ migrations
│  │  │     │  │  ├─ 20230314111643_create_initial_migration
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230316153311_remove_unique_constraint_on_versionid
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230316160310_remove_version_id
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230328110224_rename_column_is_over18_to_under18
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230420095018_documentversion_documenttype_nullable
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230421140434_documentversion_publishedstatusprev
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230421141335_exam_timetable_type_reference_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230424123305_exam_timetable_type_name_unique
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230426150420_examtimetable_add_template_type_field
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230509134331_add_document_latest_version_column
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230510080111_default_appeal_status
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230518104003_move_coulmn_from_document_to_document_versions
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230518112455_add_appeal_timetable
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230519123437_representations_actions_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230522131308_add_examination_timetable_items_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230522131835_add_case_id_column_examination_items_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230523195409_add_start_end_time_columns_examination_items_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230526092956_update_lpa_questionnaire
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230526130756_represntauions_actions_table_notes
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230530093928_correct_schema_drift
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230530111714_add_linked_appeals
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230530142748_configure_latest_document_version_constraints
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230531134004_representations_actions_none_mandatory_fields
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230531185104_denormalise_case_to_document
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230531185105_make_document_non_nullable
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230601144617_remove_end_date_column_examination_items_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230601183730_latest_version_id_nullable
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230602140605_rename_examination_item_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230605140153_
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230608100202_add_address_country_column
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230609122204_add_published_column_examination_items_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230609152850_add_appellant_case
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230612174905_representation_attachment_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230615143104_representaion_received_is_optional
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230620101631_save_appellant_case_outcome
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230621205323_add_folder_id_to_examination_timetable_items
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230622093219_subscriptions
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230627104159_add_examination_timetable_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230628085657_project_update
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230705010101_update_document_statuses
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230707173013_add_stage_to_folders
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230712105601_add_document_activity_log_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230712130206_remove_all_references_to_appeals_from_applications_db
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230717153600_add_document_reference
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230718132204_unique_document_reference
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230718135108_examination_timetable_date_not_null
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230719092654_non_unique_reference
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230724150821_create_s51_advice
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230728131711_add_name_columns_s51_advice
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230801133050_project_update_type
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230802092923_add_new_columns
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230802092924_remove_redundant_columns
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230802104058_add_status_reference_columns_s51_advice
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230802120606_s51_remove_default_redacted_status
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230810091400_project_update_notification_log
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230811104500_add_unpublished_updates_to_representations
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230811151812_add_from_front_office_document_column
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230814101918_s51_advice_document_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230824150019_s51_advice_add_published_status_prev_field
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230906132516_add_key_dates
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230915144719_migrated_id_project_updates
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230918102414_project_update_content_size_increase
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230918123521_subscriptions_migrated_id
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230918131201_s51_advice_add_column_published_date
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230919124820_s51_advice_add_column_isdeleted
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230921160146_exam_timetable_item_timestamp
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230925111802_unpublished_changes
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20230926155134_migrate_legacy_project_update_ids
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231002110212_case_published_state
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231012111536_service_user_applicant_migration
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231016115614_remove_service_user_id_from_case
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231016175637_remove_circular_dependency
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231019141316_add_transcript_relation
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231020074907_seed_service_user_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231110102118_representation_service_user_refactor
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231110102119_representation_service_user_refactor
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231117144113_add_project_team_table
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231208133850_add_document_type
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  ├─ 20231208134356_document_type_required
│  │  │     │  │  │  └─ migration.sql
│  │  │     │  │  └─ migration_lock.toml
│  │  │     │  ├─ prisma.truncate.js
│  │  │     │  ├─ schema.d.ts
│  │  │     │  ├─ schema.prisma
│  │  │     │  └─ seed
│  │  │     │     ├─ data-samples.js
│  │  │     │     ├─ data-static.js
│  │  │     │     ├─ data-test.js
│  │  │     │     ├─ seed-clear.js
│  │  │     │     ├─ seed-development.js
│  │  │     │     ├─ seed-production.js
│  │  │     │     └─ util.js
│  │  │     ├─ message-schemas
│  │  │     │  ├─ commands
│  │  │     │  │  ├─ new-deadline-submission.d.ts
│  │  │     │  │  ├─ new-deadline-submission.schema.json
│  │  │     │  │  ├─ register-nsip-subscription.d.ts
│  │  │     │  │  ├─ register-nsip-subscription.schema.json
│  │  │     │  │  ├─ register-representation.schema.json
│  │  │     │  │  └─ submit-timetable-item.schema.json
│  │  │     │  └─ events
│  │  │     │     ├─ case-schedule.schema.json
│  │  │     │     ├─ employee.schema.json
│  │  │     │     ├─ interested-party.schema.json
│  │  │     │     ├─ nsip-document.schema.json
│  │  │     │     ├─ nsip-exam-timetable-submission.d.ts
│  │  │     │     ├─ nsip-exam-timetable-submission.schema.json
│  │  │     │     ├─ nsip-exam-timetable.d.ts
│  │  │     │     ├─ nsip-exam-timetable.schema.json
│  │  │     │     ├─ nsip-project-update.d.ts
│  │  │     │     ├─ nsip-project-update.schema.json
│  │  │     │     ├─ nsip-project.d.ts
│  │  │     │     ├─ nsip-project.schema.json
│  │  │     │     ├─ nsip-representation.schema.json
│  │  │     │     ├─ nsip-subscription.d.ts
│  │  │     │     ├─ nsip-subscription.schema.json
│  │  │     │     ├─ s51-advice.schema.json
│  │  │     │     ├─ service-user.d.ts
│  │  │     │     └─ service-user.schema.json
│  │  │     ├─ server
│  │  │     │  ├─ app-test.js
│  │  │     │  ├─ app.js
│  │  │     │  ├─ applications
│  │  │     │  │  ├─ all-applications
│  │  │     │  │  │  ├─ get-all-applications.controller.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ get-applications.test.js
│  │  │     │  │  ├─ application
│  │  │     │  │  │  ├─ application.controller.js
│  │  │     │  │  │  ├─ application.mapper.js
│  │  │     │  │  │  ├─ application.routes.js
│  │  │     │  │  │  ├─ application.service.js
│  │  │     │  │  │  ├─ application.validators.js
│  │  │     │  │  │  ├─ documents
│  │  │     │  │  │  │  ├─ document.controller.js
│  │  │     │  │  │  │  ├─ document.js
│  │  │     │  │  │  │  ├─ document.routes.js
│  │  │     │  │  │  │  ├─ document.service.js
│  │  │     │  │  │  │  ├─ document.validators.js
│  │  │     │  │  │  │  └─ __tests__
│  │  │     │  │  │  │     ├─ delete-document.test.js
│  │  │     │  │  │  │     ├─ document-payload.test.js
│  │  │     │  │  │  │     ├─ document.service.test.js
│  │  │     │  │  │  │     ├─ get-document.test.js
│  │  │     │  │  │  │     ├─ mark-as-published.test.js
│  │  │     │  │  │  │     ├─ provide-document-upload-urls.test.js
│  │  │     │  │  │  │     ├─ publish-document.test.js
│  │  │     │  │  │  │     ├─ store-document-metadata.test.js
│  │  │     │  │  │  │     ├─ unpublish-document.test.js
│  │  │     │  │  │  │     └─ update-document-status.test.js
│  │  │     │  │  │  ├─ file-folders
│  │  │     │  │  │  │  ├─ folders.controller.js
│  │  │     │  │  │  │  ├─ folders.routes.js
│  │  │     │  │  │  │  ├─ folders.service.js
│  │  │     │  │  │  │  ├─ folders.validation.js
│  │  │     │  │  │  │  └─ __tests__
│  │  │     │  │  │  │     └─ get-folder-details.test.js
│  │  │     │  │  │  ├─ project-updates
│  │  │     │  │  │  │  ├─ notification-logs
│  │  │     │  │  │  │  │  ├─ notification-logs.controller.js
│  │  │     │  │  │  │  │  ├─ notification-logs.routes.js
│  │  │     │  │  │  │  │  ├─ notification-logs.validators.js
│  │  │     │  │  │  │  │  └─ __tests__
│  │  │     │  │  │  │  │     └─ notification-logs.test.js
│  │  │     │  │  │  │  ├─ project-updates.controller.js
│  │  │     │  │  │  │  ├─ project-updates.mapper.js
│  │  │     │  │  │  │  ├─ project-updates.routes.js
│  │  │     │  │  │  │  ├─ project-updates.service.js
│  │  │     │  │  │  │  ├─ project-updates.validators.js
│  │  │     │  │  │  │  └─ __tests__
│  │  │     │  │  │  │     └─ project-updates.test.js
│  │  │     │  │  │  ├─ representations
│  │  │     │  │  │  │  ├─ attachment
│  │  │     │  │  │  │  │  ├─ attachment.controller.js
│  │  │     │  │  │  │  │  ├─ attachment.route.js
│  │  │     │  │  │  │  │  ├─ attachment.service.js
│  │  │     │  │  │  │  │  ├─ attachment.validator.js
│  │  │     │  │  │  │  │  └─ __tests__
│  │  │     │  │  │  │  │     ├─ delete-attachment.test.js
│  │  │     │  │  │  │  │     └─ post-attachment.test.js
│  │  │     │  │  │  │  ├─ download
│  │  │     │  │  │  │  │  ├─ rep-download.controller.js
│  │  │     │  │  │  │  │  ├─ rep-download.router.js
│  │  │     │  │  │  │  │  ├─ rep-download.service.js
│  │  │     │  │  │  │  │  ├─ utils
│  │  │     │  │  │  │  │  │  ├─ map-rep-to-csv.js
│  │  │     │  │  │  │  │  │  └─ stream-transform-to-csv.js
│  │  │     │  │  │  │  │  ├─ __fixtures__
│  │  │     │  │  │  │  │  │  ├─ existing-representations.js
│  │  │     │  │  │  │  │  │  └─ expected-csv-string-120.js
│  │  │     │  │  │  │  │  └─ __tests__
│  │  │     │  │  │  │  │     ├─ get-representation-download.test.js
│  │  │     │  │  │  │  │     └─ map-rep-to-csv.test.js
│  │  │     │  │  │  │  ├─ publish
│  │  │     │  │  │  │  │  ├─ publish.controller.js
│  │  │     │  │  │  │  │  ├─ publish.route.js
│  │  │     │  │  │  │  │  ├─ publish.service.js
│  │  │     │  │  │  │  │  ├─ publish.validators.js
│  │  │     │  │  │  │  │  ├─ representation.js
│  │  │     │  │  │  │  │  └─ __tests__
│  │  │     │  │  │  │  │     └─ publish-representation.test.js
│  │  │     │  │  │  │  ├─ publishable
│  │  │     │  │  │  │  │  ├─ publishable.controller.js
│  │  │     │  │  │  │  │  ├─ publishable.route.js
│  │  │     │  │  │  │  │  ├─ publishable.service.js
│  │  │     │  │  │  │  │  └─ __tests__
│  │  │     │  │  │  │  │     └─ publishable-representations.test.js
│  │  │     │  │  │  │  ├─ redact
│  │  │     │  │  │  │  │  ├─ redact.controller.js
│  │  │     │  │  │  │  │  ├─ redact.mapper.js
│  │  │     │  │  │  │  │  ├─ redact.route.js
│  │  │     │  │  │  │  │  ├─ redact.service.js
│  │  │     │  │  │  │  │  ├─ redact.validators.js
│  │  │     │  │  │  │  │  └─ __tests__
│  │  │     │  │  │  │  │     └─ patch-redact.test.js
│  │  │     │  │  │  │  ├─ representaions.service.js
│  │  │     │  │  │  │  ├─ representation.mapper.js
│  │  │     │  │  │  │  ├─ representation.validators.js
│  │  │     │  │  │  │  ├─ representations.controller.js
│  │  │     │  │  │  │  ├─ representations.routes.js
│  │  │     │  │  │  │  ├─ status
│  │  │     │  │  │  │  │  ├─ status.controller.js
│  │  │     │  │  │  │  │  ├─ status.mapper.js
│  │  │     │  │  │  │  │  ├─ status.route.js
│  │  │     │  │  │  │  │  ├─ status.service.js
│  │  │     │  │  │  │  │  ├─ status.validator.js
│  │  │     │  │  │  │  │  └─ __tests__
│  │  │     │  │  │  │  │     └─ patch-status.test.js
│  │  │     │  │  │  │  └─ __tests__
│  │  │     │  │  │  │     ├─ create-representation.test.js
│  │  │     │  │  │  │     ├─ get-representation.test.js
│  │  │     │  │  │  │     ├─ get-representations.test.js
│  │  │     │  │  │  │     └─ patch-representation.test.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     ├─ application.test.js
│  │  │     │  │  │     ├─ create-application.test.js
│  │  │     │  │  │     ├─ get-application-details.test.js
│  │  │     │  │  │     ├─ publish-application.test.js
│  │  │     │  │  │     ├─ start-case.test.js
│  │  │     │  │  │     └─ update-application.test.js
│  │  │     │  │  ├─ applications.routes.js
│  │  │     │  │  ├─ case-stage
│  │  │     │  │  │  ├─ case-stage.controller.js
│  │  │     │  │  │  └─ case-stage.routes.js
│  │  │     │  │  ├─ constants.js
│  │  │     │  │  ├─ documents
│  │  │     │  │  │  ├─ documents.controller.js
│  │  │     │  │  │  ├─ documents.service.js
│  │  │     │  │  │  ├─ documents.validators.js
│  │  │     │  │  │  └─ youtube-html-template.js
│  │  │     │  │  ├─ examination-timetable-items
│  │  │     │  │  │  ├─ examination-timetable-items.controller.js
│  │  │     │  │  │  ├─ examination-timetable-items.routes.js
│  │  │     │  │  │  ├─ examination-timetable-items.service.js
│  │  │     │  │  │  ├─ examination-timetable-items.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ examination-timetable-items.test.js
│  │  │     │  │  ├─ examination-timetable-type
│  │  │     │  │  │  ├─ examination-timetable-type.controller.js
│  │  │     │  │  │  ├─ examination-timetable-type.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ get-examination-timetable-type.test.js
│  │  │     │  │  ├─ key-dates
│  │  │     │  │  │  ├─ key-dates.controller.js
│  │  │     │  │  │  ├─ key-dates.routes.js
│  │  │     │  │  │  ├─ key-dates.utils.js
│  │  │     │  │  │  ├─ key-dates.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     ├─ get-key-dates.test.js
│  │  │     │  │  │     └─ update-key-dates.test.js
│  │  │     │  │  ├─ project-team
│  │  │     │  │  │  ├─ project-team.controller.js
│  │  │     │  │  │  ├─ project-team.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ project-team.test.js
│  │  │     │  │  ├─ region
│  │  │     │  │  │  ├─ region.controller.js
│  │  │     │  │  │  ├─ region.routes.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ get-regions.test.js
│  │  │     │  │  ├─ s51advice
│  │  │     │  │  │  ├─ s51-advice.controller.js
│  │  │     │  │  │  ├─ s51-advice.js
│  │  │     │  │  │  ├─ s51-advice.routes.js
│  │  │     │  │  │  ├─ s51-advice.service.js
│  │  │     │  │  │  ├─ s51-advice.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     ├─ s51-advice-payload.test.js
│  │  │     │  │  │     ├─ s51-advice-update.test.js
│  │  │     │  │  │     └─ s51-advice.test.js
│  │  │     │  │  ├─ search
│  │  │     │  │  │  ├─ case-search.controller.js
│  │  │     │  │  │  ├─ case-search.routes.js
│  │  │     │  │  │  ├─ case-search.services.js
│  │  │     │  │  │  ├─ case-search.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ case-search.test.js
│  │  │     │  │  ├─ sector
│  │  │     │  │  │  ├─ sector.controller.js
│  │  │     │  │  │  ├─ sector.routes.js
│  │  │     │  │  │  ├─ sectors.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ get-sectors.test.js
│  │  │     │  │  ├─ state-machine
│  │  │     │  │  │  ├─ application.machine.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ application.machine.test.js
│  │  │     │  │  ├─ subscriptions
│  │  │     │  │  │  ├─ subscriptions.controller.js
│  │  │     │  │  │  ├─ subscriptions.js
│  │  │     │  │  │  ├─ subscriptions.md
│  │  │     │  │  │  ├─ subscriptions.routes.js
│  │  │     │  │  │  ├─ subscriptions.service.js
│  │  │     │  │  │  ├─ subscriptions.validators.js
│  │  │     │  │  │  └─ __tests__
│  │  │     │  │  │     └─ subscriptions.test.js
│  │  │     │  │  └─ zoom-level
│  │  │     │  │     ├─ zoom-level.controller.js
│  │  │     │  │     ├─ zoom-level.routes.js
│  │  │     │  │     └─ __tests__
│  │  │     │  │        └─ get-zoom-map.test.js
│  │  │     │  ├─ build-app.js
│  │  │     │  ├─ config
│  │  │     │  │  ├─ config.js
│  │  │     │  │  └─ schema.js
│  │  │     │  ├─ gen-api-spec.js
│  │  │     │  ├─ infrastructure
│  │  │     │  │  ├─ event-broadcasters.js
│  │  │     │  │  ├─ event-client.js
│  │  │     │  │  ├─ payload-builders
│  │  │     │  │  │  ├─ applicant.js
│  │  │     │  │  │  ├─ constants.js
│  │  │     │  │  │  └─ nsip-project.js
│  │  │     │  │  └─ topics.js
│  │  │     │  ├─ middleware
│  │  │     │  │  ├─ async-handler.js
│  │  │     │  │  ├─ error-handler.js
│  │  │     │  │  ├─ errors.js
│  │  │     │  │  ├─ handle-validation-error.js
│  │  │     │  │  ├─ pagination-validation.js
│  │  │     │  │  ├─ trim-unexpected-request-parameters.js
│  │  │     │  │  ├─ validate-file-upload.js
│  │  │     │  │  ├─ validate-sort-by.js
│  │  │     │  │  ├─ version-routes.js
│  │  │     │  │  └─ __tests__
│  │  │     │  │     └─ validate-sort-by.test.js
│  │  │     │  ├─ migration
│  │  │     │  │  ├─ migration.controller.js
│  │  │     │  │  ├─ migration.routes.js
│  │  │     │  │  ├─ migrator.consts.js
│  │  │     │  │  ├─ migrator.service.js
│  │  │     │  │  ├─ migrators
│  │  │     │  │  │  ├─ nsip-project-migrator.js
│  │  │     │  │  │  ├─ nsip-project-update-migrator.js
│  │  │     │  │  │  ├─ nsip-subscription-migrator.js
│  │  │     │  │  │  ├─ sql-tools.js
│  │  │     │  │  │  └─ utils.js
│  │  │     │  │  └─ README.md
│  │  │     │  ├─ repositories
│  │  │     │  │  ├─ case.repository.js
│  │  │     │  │  ├─ document-activity-log.repository.js
│  │  │     │  │  ├─ document-metadata.repository.js
│  │  │     │  │  ├─ document.repository.js
│  │  │     │  │  ├─ examination-timetable-items.repository.js
│  │  │     │  │  ├─ examination-timetable-types.repository.js
│  │  │     │  │  ├─ examination-timetable.repository.js
│  │  │     │  │  ├─ folder.repository.js
│  │  │     │  │  ├─ key-dates.repository.js
│  │  │     │  │  ├─ project-team.repository.js
│  │  │     │  │  ├─ project-update.respository.js
│  │  │     │  │  ├─ raw_sql_queries
│  │  │     │  │  │  └─ update-application-reference.sql
│  │  │     │  │  ├─ region.repository.js
│  │  │     │  │  ├─ representation.repository.js
│  │  │     │  │  ├─ s51-advice-document.repository.js
│  │  │     │  │  ├─ s51-advice.repository.js
│  │  │     │  │  ├─ sector.repository.js
│  │  │     │  │  ├─ separate-statuses-to-save-and-invalidate.js
│  │  │     │  │  ├─ sub-sector.repository.js
│  │  │     │  │  ├─ subscription.respository.js
│  │  │     │  │  ├─ zoom-level.repository.js
│  │  │     │  │  └─ __tests__
│  │  │     │  │     ├─ folder.repository.test.js
│  │  │     │  │     ├─ representation.repository.test.js
│  │  │     │  │     └─ subscription.repository.test.js
│  │  │     │  ├─ swagger-output.json
│  │  │     │  ├─ swagger-types.ts
│  │  │     │  ├─ swagger.js
│  │  │     │  └─ utils
│  │  │     │     ├─ address-block-formtter.js
│  │  │     │     ├─ address-formatter-lowercase.js
│  │  │     │     ├─ api-errors.js
│  │  │     │     ├─ app-error.js
│  │  │     │     ├─ application-factory-for-tests.js
│  │  │     │     ├─ break-up-compound-status.js
│  │  │     │     ├─ build-appeal-compound-status.js
│  │  │     │     ├─ cache-data.js
│  │  │     │     ├─ create-enums.js
│  │  │     │     ├─ database-connector.js
│  │  │     │     ├─ database-pagination.js
│  │  │     │     ├─ date-formatter.js
│  │  │     │     ├─ days-between-dates.js
│  │  │     │     ├─ document-storage.js
│  │  │     │     ├─ express-debug.js
│  │  │     │     ├─ feature-flags.js
│  │  │     │     ├─ logger.js
│  │  │     │     ├─ map-states-to-strings.js
│  │  │     │     ├─ mapping
│  │  │     │     │  ├─ map-application-with-search-criteria.js
│  │  │     │     │  ├─ map-application-with-sector-and-subsector.js
│  │  │     │     │  ├─ map-application.js
│  │  │     │     │  ├─ map-case-details.js
│  │  │     │     │  ├─ map-case-status-string.js
│  │  │     │     │  ├─ map-case-status.js
│  │  │     │     │  ├─ map-date-string-to-unix-timestamp.js
│  │  │     │     │  ├─ map-date-to-unix-timestamp.js
│  │  │     │     │  ├─ map-document-details.js
│  │  │     │     │  ├─ map-examination-timetable-item.js
│  │  │     │     │  ├─ map-folder-details.js
│  │  │     │     │  ├─ map-grid-reference.js
│  │  │     │     │  ├─ map-key-dates.js
│  │  │     │     │  ├─ map-keys-using-object.js
│  │  │     │     │  ├─ map-project-team.js
│  │  │     │     │  ├─ map-region.js
│  │  │     │     │  ├─ map-s51-advice-details.js
│  │  │     │     │  ├─ map-sector.js
│  │  │     │     │  ├─ map-service-user.js
│  │  │     │     │  ├─ map-unix-timestamp-to-date.js
│  │  │     │     │  ├─ map-values-using-object.js
│  │  │     │     │  └─ map-zoom-level.js
│  │  │     │     ├─ object.js
│  │  │     │     ├─ prisma-instrumentation.js
│  │  │     │     ├─ prisma-middleware.js
│  │  │     │     ├─ published-case-fields-changed.js
│  │  │     │     ├─ query
│  │  │     │     │  ├─ sort-by.js
│  │  │     │     │  └─ __tests__
│  │  │     │     │     └─ sort-by.test.js
│  │  │     │     ├─ schema-test-utils.js
│  │  │     │     ├─ transition-state.js
│  │  │     │     └─ __tests__
│  │  │     │        ├─ break-up-compound-status.test.js
│  │  │     │        ├─ create-enums.test.js
│  │  │     │        ├─ days-between-dates.test.js
│  │  │     │        ├─ feature-flags.test.js
│  │  │     │        └─ object.test.js
│  │  │     └─ server.js
│  │  ├─ api-testing
│  │  │  ├─ .env.example
│  │  │  ├─ api-test.sh
│  │  │  ├─ config
│  │  │  │  ├─ config.cjs
│  │  │  │  └─ supertest.js
│  │  │  ├─ fixtures
│  │  │  │  └─ options.js
│  │  │  ├─ package.json
│  │  │  ├─ README.md
│  │  │  ├─ services
│  │  │  │  └─ test-service.js
│  │  │  ├─ tests
│  │  │  │  ├─ inspector
│  │  │  │  │  ├─ index.js
│  │  │  │  │  └─ inspector.test.js
│  │  │  │  ├─ region
│  │  │  │  │  ├─ index.js
│  │  │  │  │  └─ region.test.js
│  │  │  │  ├─ search
│  │  │  │  │  ├─ index.js
│  │  │  │  │  └─ search.test.js
│  │  │  │  ├─ sector
│  │  │  │  │  ├─ index.js
│  │  │  │  │  └─ sector.test.js
│  │  │  │  ├─ subscriptions
│  │  │  │  │  ├─ data.js
│  │  │  │  │  ├─ index.js
│  │  │  │  │  ├─ subscriptions-get.test.js
│  │  │  │  │  ├─ subscriptions-patch.test.js
│  │  │  │  │  └─ subscriptions-put.test.js
│  │  │  │  └─ zoom-level
│  │  │  │     ├─ index.js
│  │  │  │     └─ zoom-level.test.js
│  │  │  └─ utils
│  │  │     ├─ generate-schema.js
│  │  │     ├─ logger.js
│  │  │     ├─ schema-validation.js
│  │  │     └─ test-data.js
│  │  ├─ e2e
│  │  │  ├─ .env.sample
│  │  │  ├─ cypress
│  │  │  │  ├─ e2e
│  │  │  │  │  ├─ back-office-appeals
│  │  │  │  │  │  ├─ assignUserToCase.spec.js
│  │  │  │  │  │  ├─ nationalListSearch.spec.js
│  │  │  │  │  │  ├─ reviewAppellantCase.spec.js
│  │  │  │  │  │  ├─ reviewLpaq.spec.js
│  │  │  │  │  │  └─ scheduleSiteVisit.spec.js
│  │  │  │  │  └─ back-office-applications
│  │  │  │  │     ├─ addTeam.spec.js
│  │  │  │  │     ├─ createCase.spec.js
│  │  │  │  │     ├─ documentDownload.spec.js
│  │  │  │  │     ├─ documentProperties.spec.js
│  │  │  │  │     ├─ documentUpload.spec.js
│  │  │  │  │     ├─ documentVersioning.spec.js
│  │  │  │  │     ├─ examTimetable.spec.js
│  │  │  │  │     ├─ keyDates.spec.js
│  │  │  │  │     ├─ publishDocuments.spec.js
│  │  │  │  │     ├─ s51Advice.spec.js
│  │  │  │  │     ├─ search.spec.js
│  │  │  │  │     ├─ searchDocuments.spec.js
│  │  │  │  │     ├─ unpublishDocuments.spec.js
│  │  │  │  │     ├─ updateAndRemoveTeam.spec.js
│  │  │  │  │     └─ updateProjectInformation.spec.js
│  │  │  │  ├─ fixtures
│  │  │  │  │  ├─ browser-auth-data.js
│  │  │  │  │  ├─ case-search.json
│  │  │  │  │  ├─ dmap.dbf
│  │  │  │  │  ├─ folder-structure.json
│  │  │  │  │  ├─ NI_Template_2.html
│  │  │  │  │  ├─ NI_Video_Template_2.html
│  │  │  │  │  ├─ ptest-prj.prj
│  │  │  │  │  ├─ sample-doc.pdf
│  │  │  │  │  ├─ sample-error-file.html
│  │  │  │  │  ├─ sample-file.doc
│  │  │  │  │  ├─ sample-file.html
│  │  │  │  │  ├─ sample-img.gif
│  │  │  │  │  ├─ sample-img.jpeg
│  │  │  │  │  ├─ sample-img.jpg
│  │  │  │  │  ├─ sample-video.mp4
│  │  │  │  │  ├─ Sample.mp3
│  │  │  │  │  ├─ smap.shp
│  │  │  │  │  ├─ test.pdf
│  │  │  │  │  ├─ users.js
│  │  │  │  │  └─ xmap.shx
│  │  │  │  ├─ page_objects
│  │  │  │  │  ├─ appealsListPage.js
│  │  │  │  │  ├─ applicationsHomePage.js
│  │  │  │  │  ├─ basePage.js
│  │  │  │  │  ├─ casePage.js
│  │  │  │  │  ├─ createCasePage.js
│  │  │  │  │  ├─ createCaseSections
│  │  │  │  │  │  ├─ applicantAddress.js
│  │  │  │  │  │  ├─ applicantEmail.js
│  │  │  │  │  │  ├─ applicantInformationAvailable.js
│  │  │  │  │  │  ├─ applicantName.js
│  │  │  │  │  │  ├─ applicantOrganisation.js
│  │  │  │  │  │  ├─ applicantPhoneNumber.js
│  │  │  │  │  │  ├─ applicantWebsite.js
│  │  │  │  │  │  ├─ caseCreated.js
│  │  │  │  │  │  ├─ checkYourAnswers.js
│  │  │  │  │  │  ├─ geographicalInformation.js
│  │  │  │  │  │  ├─ index.js
│  │  │  │  │  │  ├─ keyDates.js
│  │  │  │  │  │  ├─ nameAndDescription.js
│  │  │  │  │  │  ├─ projectEmail.js
│  │  │  │  │  │  ├─ regions.js
│  │  │  │  │  │  ├─ sectionBase.js
│  │  │  │  │  │  ├─ sector.js
│  │  │  │  │  │  ├─ subSector.js
│  │  │  │  │  │  └─ zoomLevel.js
│  │  │  │  │  ├─ documentPropertiesPage.js
│  │  │  │  │  ├─ examinationTimetablePage.js
│  │  │  │  │  ├─ folderDocumentsPage.js
│  │  │  │  │  ├─ keyDatesPage.js
│  │  │  │  │  ├─ projectTeamPage.js
│  │  │  │  │  ├─ publishingQueue.js
│  │  │  │  │  ├─ s51AdvicePage.js
│  │  │  │  │  ├─ s51AdviceProperties.js
│  │  │  │  │  ├─ searchResultsPage.js
│  │  │  │  │  ├─ updateDueDatePage.js
│  │  │  │  │  └─ uploadFiles.js
│  │  │  │  └─ support
│  │  │  │     ├─ commands.js
│  │  │  │     ├─ cypressUtils.js
│  │  │  │     ├─ e2e.js
│  │  │  │     ├─ login.js
│  │  │  │     └─ utils
│  │  │  │        ├─ assertType.js
│  │  │  │        ├─ createProjectInformation.js
│  │  │  │        ├─ createS51Advice.js
│  │  │  │        ├─ createTimetableItemInfo.js
│  │  │  │        ├─ getSpecPattern.js
│  │  │  │        ├─ isCI.js
│  │  │  │        ├─ options.js
│  │  │  │        └─ utils.js
│  │  │  ├─ cypress.config.js
│  │  │  ├─ install-chromium.sh
│  │  │  ├─ package.json
│  │  │  ├─ README.md
│  │  │  └─ run-tests.sh
│  │  ├─ functions
│  │  │  ├─ applications-migration
│  │  │  │  ├─ .funcignore
│  │  │  │  ├─ common
│  │  │  │  │  ├─ config.js
│  │  │  │  │  └─ synapse-db.js
│  │  │  │  ├─ host.json
│  │  │  │  ├─ jsconfig.json
│  │  │  │  ├─ local.settings.json
│  │  │  │  ├─ package.json
│  │  │  │  ├─ project-updates-migration
│  │  │  │  │  ├─ function.json
│  │  │  │  │  ├─ index.js
│  │  │  │  │  └─ src
│  │  │  │  │     ├─ back-office-api-client.js
│  │  │  │  │     ├─ config.js
│  │  │  │  │     └─ project-updates-migration.js
│  │  │  │  └─ service-user-migration
│  │  │  │     ├─ debug.js
│  │  │  │     ├─ function.json
│  │  │  │     ├─ index.js
│  │  │  │     └─ src
│  │  │  │        └─ service-user-migration.js
│  │  │  ├─ deadline-submissions
│  │  │  │  ├─ .funcignore
│  │  │  │  ├─ .vscode
│  │  │  │  │  └─ extensions.json
│  │  │  │  ├─ deadline-submission-command
│  │  │  │  │  ├─ back-office-api-client.js
│  │  │  │  │  ├─ blob-client.js
│  │  │  │  │  ├─ config.js
│  │  │  │  │  ├─ event-client.js
│  │  │  │  │  ├─ function.json
│  │  │  │  │  ├─ index.js
│  │  │  │  │  └─ __tests__
│  │  │  │  │     └─ deadline-submission-command.test.js
│  │  │  │  ├─ host.json
│  │  │  │  ├─ jest.config.js
│  │  │  │  ├─ package.json
│  │  │  │  ├─ README.md
│  │  │  │  └─ test-deadline-submission
│  │  │  │     ├─ config.js
│  │  │  │     ├─ function.json
│  │  │  │     └─ index.js
│  │  │  ├─ document-check
│  │  │  │  ├─ .env.test
│  │  │  │  ├─ .funcignore
│  │  │  │  ├─ check-document
│  │  │  │  │  ├─ back-office-api-client.js
│  │  │  │  │  ├─ blob-utils.js
│  │  │  │  │  ├─ check-my-blob.js
│  │  │  │  │  ├─ clam-av-client.js
│  │  │  │  │  ├─ config.js
│  │  │  │  │  ├─ event-client.js
│  │  │  │  │  ├─ function.json
│  │  │  │  │  ├─ index.js
│  │  │  │  │  ├─ scan-stream.js
│  │  │  │  │  └─ __tests__
│  │  │  │  │     ├─ blob-utils.test.js
│  │  │  │  │     └─ check-new-document.test.js
│  │  │  │  ├─ host.json
│  │  │  │  ├─ jest.config.js
│  │  │  │  ├─ local.settings.json
│  │  │  │  ├─ package.json
│  │  │  │  └─ README.md
│  │  │  ├─ document-publish
│  │  │  │  ├─ .env.test
│  │  │  │  ├─ .funcignore
│  │  │  │  ├─ host.json
│  │  │  │  ├─ jest.config.js
│  │  │  │  ├─ local.settings.json
│  │  │  │  ├─ package.json
│  │  │  │  ├─ publish-document
│  │  │  │  │  ├─ blob-client.js
│  │  │  │  │  ├─ config.js
│  │  │  │  │  ├─ function.json
│  │  │  │  │  ├─ index.js
│  │  │  │  │  └─ __tests__
│  │  │  │  │     ├─ publish-document.test.js
│  │  │  │  │     └─ test-event.json
│  │  │  │  ├─ setup-tests.js
│  │  │  │  └─ unpublish-document
│  │  │  │     ├─ blob-client.js
│  │  │  │     ├─ config.js
│  │  │  │     ├─ function.json
│  │  │  │     ├─ index.js
│  │  │  │     └─ utils.js
│  │  │  ├─ handle-subscriptions
│  │  │  │  ├─ handle-subscription-command
│  │  │  │  │  ├─ back-office-api-client.js
│  │  │  │  │  ├─ config.js
│  │  │  │  │  ├─ function.json
│  │  │  │  │  ├─ index.js
│  │  │  │  │  ├─ logging-utils.js
│  │  │  │  │  └─ __tests__
│  │  │  │  │     └─ handle-subscription-command.test.js
│  │  │  │  ├─ host.json
│  │  │  │  ├─ local.settings.json
│  │  │  │  ├─ package.json
│  │  │  │  └─ README.md
│  │  │  ├─ malware-detected
│  │  │  │  ├─ .funcignore
│  │  │  │  ├─ .vscode
│  │  │  │  │  └─ extensions.json
│  │  │  │  ├─ host.json
│  │  │  │  ├─ local.settings.json
│  │  │  │  ├─ malware-detected
│  │  │  │  │  ├─ back-office-api-client.js
│  │  │  │  │  ├─ config.js
│  │  │  │  │  ├─ function.json
│  │  │  │  │  └─ index.js
│  │  │  │  └─ package.json
│  │  │  ├─ notify-subscribers
│  │  │  │  ├─ .funcignore
│  │  │  │  ├─ host.json
│  │  │  │  ├─ notify-subscribers
│  │  │  │  │  ├─ function.json
│  │  │  │  │  ├─ index.js
│  │  │  │  │  ├─ run-local.js
│  │  │  │  │  └─ src
│  │  │  │  │     ├─ back-office-api-client.js
│  │  │  │  │     ├─ config.js
│  │  │  │  │     ├─ modules.d.ts
│  │  │  │  │     ├─ notify-subscribers.js
│  │  │  │  │     ├─ paged-request.js
│  │  │  │  │     ├─ types.d.ts
│  │  │  │  │     ├─ util.js
│  │  │  │  │     └─ __tests__
│  │  │  │  │        ├─ notify-subscribers.test.js
│  │  │  │  │        └─ page-request.test.js
│  │  │  │  ├─ package.json
│  │  │  │  └─ README.md
│  │  │  ├─ odw-integration
│  │  │  │  ├─ .funcignore
│  │  │  │  ├─ host.json
│  │  │  │  ├─ local.settings.json
│  │  │  │  ├─ package.json
│  │  │  │  └─ update-employee
│  │  │  │     ├─ function.json
│  │  │  │     └─ index.js
│  │  │  └─ README.md
│  │  └─ web
│  │     ├─ .browserslistrc
│  │     ├─ .dockerignore
│  │     ├─ .env.example
│  │     ├─ .env.test
│  │     ├─ babel.config.js
│  │     ├─ Dockerfile
│  │     ├─ environment
│  │     │  ├─ base-config.js
│  │     │  ├─ config.d.ts
│  │     │  ├─ config.js
│  │     │  └─ schema.js
│  │     ├─ index.html
│  │     ├─ jest.config.js
│  │     ├─ jsconfig.json
│  │     ├─ nodemon.json
│  │     ├─ package.json
│  │     ├─ scripts
│  │     │  └─ rollup
│  │     │     ├─ bundle-js.js
│  │     │     ├─ compile-css.js
│  │     │     ├─ get-logger.js
│  │     │     ├─ hash.js
│  │     │     ├─ minify-js.js
│  │     │     └─ rollup-plugin-virtual-json.js
│  │     ├─ setup-tests.js
│  │     ├─ src
│  │     │  ├─ client
│  │     │  │  ├─ app.js
│  │     │  │  ├─ components
│  │     │  │  │  ├─ accessible-autocomplete.js
│  │     │  │  │  ├─ base.js
│  │     │  │  │  ├─ excerpts
│  │     │  │  │  │  ├─ excerpt.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     └─ excerpt.test.js
│  │     │  │  │  ├─ file-uploader
│  │     │  │  │  │  ├─ file-uploader.module.js
│  │     │  │  │  │  ├─ _client-actions.js
│  │     │  │  │  │  ├─ _errors.js
│  │     │  │  │  │  ├─ _html.js
│  │     │  │  │  │  ├─ _relevant_representations_attachment.js
│  │     │  │  │  │  ├─ _server-actions.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     └─ file-uploader.test.js
│  │     │  │  │  ├─ files-list
│  │     │  │  │  │  ├─ files-list.module.js
│  │     │  │  │  │  ├─ _html.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     └─ files-list.test.js
│  │     │  │  │  ├─ html-content-editor
│  │     │  │  │  │  ├─ html-content-editor.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     └─ html-content-editor.test.js
│  │     │  │  │  └─ select-all-checkbox
│  │     │  │  │     ├─ select-all-checkbox.js
│  │     │  │  │     └─ __tests__
│  │     │  │  │        └─ select-all-checkbox.test.js
│  │     │  │  └─ pages
│  │     │  │     └─ default.js
│  │     │  ├─ common
│  │     │  │  ├─ feature-flags.js
│  │     │  │  └─ __tests__
│  │     │  │     └─ feature-flags.test.js
│  │     │  ├─ server
│  │     │  │  ├─ app
│  │     │  │  │  ├─ app.controller.js
│  │     │  │  │  ├─ app.express.js
│  │     │  │  │  ├─ app.router.js
│  │     │  │  │  ├─ auth
│  │     │  │  │  │  ├─ auth-session.service.js
│  │     │  │  │  │  ├─ auth.controller.js
│  │     │  │  │  │  ├─ auth.guards.js
│  │     │  │  │  │  ├─ auth.pipes.js
│  │     │  │  │  │  ├─ auth.router.js
│  │     │  │  │  │  ├─ auth.service.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     ├─ auth.test.js
│  │     │  │  │  │     └─ __snapshots__
│  │     │  │  │  │        └─ auth.test.js.snap
│  │     │  │  │  ├─ components
│  │     │  │  │  │  ├─ file-downloader.component.js
│  │     │  │  │  │  └─ file-uploader.component.js
│  │     │  │  │  └─ config
│  │     │  │  │     ├─ locals.js
│  │     │  │  │     ├─ nunjucks.js
│  │     │  │  │     └─ session.js
│  │     │  │  ├─ applications
│  │     │  │  │  ├─ applications.controller.js
│  │     │  │  │  ├─ applications.filters.js
│  │     │  │  │  ├─ applications.locals.js
│  │     │  │  │  ├─ applications.router.js
│  │     │  │  │  ├─ applications.service.js
│  │     │  │  │  ├─ applications.types.d.ts
│  │     │  │  │  ├─ case
│  │     │  │  │  │  ├─ applications-case.controller.js
│  │     │  │  │  │  ├─ applications-case.locals.js
│  │     │  │  │  │  ├─ applications-case.router.js
│  │     │  │  │  │  ├─ documentation
│  │     │  │  │  │  │  ├─ applications-documentation.controller.js
│  │     │  │  │  │  │  ├─ applications-documentation.guard.js
│  │     │  │  │  │  │  ├─ applications-documentation.router.js
│  │     │  │  │  │  │  ├─ applications-documentation.service.js
│  │     │  │  │  │  │  ├─ applications-documentation.session.js
│  │     │  │  │  │  │  ├─ applications-documentation.types.d.ts
│  │     │  │  │  │  │  ├─ applications-documentation.validators.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ applications-documentation.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ applications-documentation.test.js.snap
│  │     │  │  │  │  ├─ documentation-metadata
│  │     │  │  │  │  │  ├─ documentation-metadata.controller.js
│  │     │  │  │  │  │  ├─ documentation-metadata.locals.js
│  │     │  │  │  │  │  ├─ documentation-metadata.router.js
│  │     │  │  │  │  │  ├─ documentation-metadata.service.js
│  │     │  │  │  │  │  ├─ documentation-metadata.validators.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ documentation-metadata.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ documentation-metadata.test.js.snap
│  │     │  │  │  │  ├─ edit
│  │     │  │  │  │  │  ├─ applicant
│  │     │  │  │  │  │  │  ├─ applications-edit-applicant.controller.js
│  │     │  │  │  │  │  │  ├─ applications-edit-applicant.router.js
│  │     │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │     ├─ applications-edit-applicant.test.js
│  │     │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │        └─ applications-edit-applicant.test.js.snap
│  │     │  │  │  │  │  ├─ applications-edit.locals.js
│  │     │  │  │  │  │  ├─ applications-edit.router.js
│  │     │  │  │  │  │  └─ case
│  │     │  │  │  │  │     ├─ applications-edit-case.controller.js
│  │     │  │  │  │  │     ├─ applications-edit-case.router.js
│  │     │  │  │  │  │     └─ __tests__
│  │     │  │  │  │  │        ├─ applications-edit-case.test.js
│  │     │  │  │  │  │        └─ __snapshots__
│  │     │  │  │  │  │           └─ applications-edit-case.test.js.snap
│  │     │  │  │  │  ├─ examination-timetable
│  │     │  │  │  │  │  ├─ applications-timetable.controller.js
│  │     │  │  │  │  │  ├─ applications-timetable.mappers.js
│  │     │  │  │  │  │  ├─ applications-timetable.router.js
│  │     │  │  │  │  │  ├─ applications-timetable.service.js
│  │     │  │  │  │  │  ├─ applications-timetable.types.d.ts
│  │     │  │  │  │  │  ├─ applications-timetable.validators.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ applications-timetable.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ applications-timetable.test.js.snap
│  │     │  │  │  │  ├─ key-dates
│  │     │  │  │  │  │  ├─ applications-key-dates.controller.js
│  │     │  │  │  │  │  ├─ applications-key-dates.router.js
│  │     │  │  │  │  │  ├─ applications-key-dates.service.js
│  │     │  │  │  │  │  ├─ applications-key-dates.validators.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ applications-key-dates.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ applications-key-dates.test.js.snap
│  │     │  │  │  │  ├─ project-team
│  │     │  │  │  │  │  ├─ application-project-team.azure-service.js
│  │     │  │  │  │  │  ├─ applications-project-team.controller.js
│  │     │  │  │  │  │  ├─ applications-project-team.router.js
│  │     │  │  │  │  │  ├─ applications-project-team.service.js
│  │     │  │  │  │  │  ├─ applications-project-team.validators.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ applications-project-team.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ applications-project-team.test.js.snap
│  │     │  │  │  │  ├─ project-updates
│  │     │  │  │  │  │  ├─ project-updates-views.d.ts
│  │     │  │  │  │  │  ├─ project-updates.controller.js
│  │     │  │  │  │  │  ├─ project-updates.mapper.js
│  │     │  │  │  │  │  ├─ project-updates.router.js
│  │     │  │  │  │  │  ├─ project-updates.service.js
│  │     │  │  │  │  │  ├─ project-updates.session.js
│  │     │  │  │  │  │  ├─ project-updates.validators.js
│  │     │  │  │  │  │  ├─ project-updates.view-model.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ project-updates.test.js
│  │     │  │  │  │  │     ├─ project-updates.view-model.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ project-updates.test.js.snap
│  │     │  │  │  │  ├─ representations
│  │     │  │  │  │  │  ├─ application-representations.view-model.js
│  │     │  │  │  │  │  ├─ applications-relevant-reps.controller.js
│  │     │  │  │  │  │  ├─ applications-relevant-reps.router.js
│  │     │  │  │  │  │  ├─ applications-relevant-reps.service.js
│  │     │  │  │  │  │  ├─ config.js
│  │     │  │  │  │  │  ├─ download
│  │     │  │  │  │  │  │  └─ download.controller.js
│  │     │  │  │  │  │  ├─ file-upload
│  │     │  │  │  │  │  │  ├─ file-upload.controller.js
│  │     │  │  │  │  │  │  ├─ file-upload.service.js
│  │     │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │     └─ file-upload.test.js
│  │     │  │  │  │  │  ├─ publish-representations-error
│  │     │  │  │  │  │  │  ├─ publish-representations-error.controller.js
│  │     │  │  │  │  │  │  ├─ publish-representations-error.router.js
│  │     │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │     ├─ publish-representations-error.test.js
│  │     │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │        └─ publish-representations-error.test.js.snap
│  │     │  │  │  │  │  ├─ publish-updated-representations
│  │     │  │  │  │  │  │  ├─ publish-updated-representations.config.js
│  │     │  │  │  │  │  │  ├─ publish-updated-representations.controller.js
│  │     │  │  │  │  │  │  ├─ publish-updated-representations.controller.validators.js
│  │     │  │  │  │  │  │  ├─ publish-updated-representations.router.js
│  │     │  │  │  │  │  │  ├─ publish-updated-representations.view-model.js
│  │     │  │  │  │  │  │  ├─ utils
│  │     │  │  │  │  │  │  │  └─ format-representation-ids.js
│  │     │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │     ├─ publish-updated-representations.test.js
│  │     │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │        └─ publish-updated-representations.test.js.snap
│  │     │  │  │  │  │  ├─ publish-valid-representations
│  │     │  │  │  │  │  │  ├─ publish-valid-reps.controller.js
│  │     │  │  │  │  │  │  ├─ publish-valid-reps.router.js
│  │     │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │     ├─ publish-valid-reps.test.js
│  │     │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │        └─ publish-valid-reps.test.js.snap
│  │     │  │  │  │  │  ├─ relevant-representation.types.d.ts
│  │     │  │  │  │  │  ├─ representation
│  │     │  │  │  │  │  │  ├─ address-details
│  │     │  │  │  │  │  │  │  ├─ address-details.controller.js
│  │     │  │  │  │  │  │  │  ├─ address-details.router.js
│  │     │  │  │  │  │  │  │  ├─ address-details.validators.js
│  │     │  │  │  │  │  │  │  ├─ address-details.view-model.js
│  │     │  │  │  │  │  │  │  ├─ utils
│  │     │  │  │  │  │  │  │  │  ├─ common-validators.js
│  │     │  │  │  │  │  │  │  │  ├─ format-address.js
│  │     │  │  │  │  │  │  │  │  ├─ get-address-list.js
│  │     │  │  │  │  │  │  │  │  ├─ get-back-link-url.js
│  │     │  │  │  │  │  │  │  │  ├─ get-selected-address.js
│  │     │  │  │  │  │  │  │  │  ├─ get-stage-errors.js
│  │     │  │  │  │  │  │  │  │  ├─ get-stage-params.js
│  │     │  │  │  │  │  │  │  │  └─ get-stage.js
│  │     │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │     ├─ address-details.test.js
│  │     │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │        └─ address-details.test.js.snap
│  │     │  │  │  │  │  │  ├─ attachment-upload
│  │     │  │  │  │  │  │  │  ├─ attachment-upload.controller.js
│  │     │  │  │  │  │  │  │  ├─ attachment-upload.router.js
│  │     │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │     ├─ attachment-upload.controller.test.js
│  │     │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │        └─ attachment-upload.controller.test.js.snap
│  │     │  │  │  │  │  │  ├─ contact-details
│  │     │  │  │  │  │  │  │  ├─ contact-details.controller.js
│  │     │  │  │  │  │  │  │  ├─ contact-details.router.js
│  │     │  │  │  │  │  │  │  ├─ contact-details.validators.js
│  │     │  │  │  │  │  │  │  ├─ contact-details.view-model.js
│  │     │  │  │  │  │  │  │  ├─ utils
│  │     │  │  │  │  │  │  │  │  └─ common-validators.js
│  │     │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │     ├─ rr-contact-details.test.js
│  │     │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │        └─ rr-contact-details.test.js.snap
│  │     │  │  │  │  │  │  ├─ contact-method
│  │     │  │  │  │  │  │  │  ├─ contact-method.controller.js
│  │     │  │  │  │  │  │  │  ├─ contact-method.router.js
│  │     │  │  │  │  │  │  │  ├─ contact-method.validators.js
│  │     │  │  │  │  │  │  │  ├─ contact-method.view-model.js
│  │     │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │     ├─ rr-contact-method.test.js
│  │     │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │        └─ rr-contact-method.test.js.snap
│  │     │  │  │  │  │  │  ├─ representation-comment
│  │     │  │  │  │  │  │  │  ├─ config.js
│  │     │  │  │  │  │  │  │  ├─ representation-comment.controller.js
│  │     │  │  │  │  │  │  │  ├─ representation-comment.router.js
│  │     │  │  │  │  │  │  │  ├─ representation-comment.validators.js
│  │     │  │  │  │  │  │  │  ├─ representation-comment.view-model.js
│  │     │  │  │  │  │  │  │  ├─ utils
│  │     │  │  │  │  │  │  │  │  ├─ date-validator.js
│  │     │  │  │  │  │  │  │  │  └─ received-date-validator.js
│  │     │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │     ├─ representation-comment.test.js
│  │     │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │        └─ representation-comment.test.js.snap
│  │     │  │  │  │  │  │  ├─ representation-entity
│  │     │  │  │  │  │  │  │  ├─ entity.controller.js
│  │     │  │  │  │  │  │  │  ├─ entity.router.js
│  │     │  │  │  │  │  │  │  ├─ entity.validators.js
│  │     │  │  │  │  │  │  │  ├─ entity.view-model.js
│  │     │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │     ├─ represetation-entity.test.js
│  │     │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │        └─ represetation-entity.test.js.snap
│  │     │  │  │  │  │  │  ├─ representation-type
│  │     │  │  │  │  │  │  │  ├─ representation-type.controller.js
│  │     │  │  │  │  │  │  │  ├─ representation-type.router.js
│  │     │  │  │  │  │  │  │  ├─ representation-type.validators.js
│  │     │  │  │  │  │  │  │  ├─ representation-type.view-model.js
│  │     │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │     ├─ represetation-type.test.js
│  │     │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │        └─ represetation-type.test.js.snap
│  │     │  │  │  │  │  │  ├─ representation.middleware.js
│  │     │  │  │  │  │  │  ├─ representation.service.js
│  │     │  │  │  │  │  │  ├─ representation.utilities.js
│  │     │  │  │  │  │  │  ├─ under-18
│  │     │  │  │  │  │  │  │  ├─ under-18.controller.js
│  │     │  │  │  │  │  │  │  ├─ under-18.router.js
│  │     │  │  │  │  │  │  │  ├─ under-18.view-model.js
│  │     │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │     ├─ represetation-under-18.test.js
│  │     │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │        └─ represetation-under-18.test.js.snap
│  │     │  │  │  │  │  │  └─ utils
│  │     │  │  │  │  │  │     ├─ get-page-links.js
│  │     │  │  │  │  │  │     ├─ get-page-titles.js
│  │     │  │  │  │  │  │     ├─ get-rep-type-page-titles.js
│  │     │  │  │  │  │  │     ├─ get-representation-page-urls.js
│  │     │  │  │  │  │  │     ├─ get-selected-options-text.js
│  │     │  │  │  │  │  │     └─ map-titles.js
│  │     │  │  │  │  │  ├─ representation-details
│  │     │  │  │  │  │  │  ├─ application-representation-details.router.js
│  │     │  │  │  │  │  │  ├─ applications-relevant-rep-details.controller.js
│  │     │  │  │  │  │  │  ├─ applications-relevant-rep-details.middleware.js
│  │     │  │  │  │  │  │  ├─ applications-relevant-rep-details.service.js
│  │     │  │  │  │  │  │  ├─ applications-relevant-rep-details.validators.js
│  │     │  │  │  │  │  │  ├─ applications-relevant-rep-details.view-model.js
│  │     │  │  │  │  │  │  ├─ change-redaction
│  │     │  │  │  │  │  │  │  ├─ change-redaction.controller.js
│  │     │  │  │  │  │  │  │  ├─ change-redaction.service.js
│  │     │  │  │  │  │  │  │  ├─ change-redaction.validator.js
│  │     │  │  │  │  │  │  │  ├─ change-redaction.view-model.js
│  │     │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │     ├─ change-redaction.test.js
│  │     │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │        └─ change-redaction.test.js.snap
│  │     │  │  │  │  │  │  ├─ redact-representation
│  │     │  │  │  │  │  │  │  ├─ redact-representation.controller.js
│  │     │  │  │  │  │  │  │  ├─ redact-representation.view-model.js
│  │     │  │  │  │  │  │  │  ├─ redact-represntation.service.js
│  │     │  │  │  │  │  │  │  ├─ __fixtures__
│  │     │  │  │  │  │  │  │  │  └─ redact-representation.fixture.js
│  │     │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │     ├─ redact-representation.test.js
│  │     │  │  │  │  │  │  │     ├─ redact-representation.test.view-model.unit.test.js
│  │     │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │        └─ redact-representation.test.js.snap
│  │     │  │  │  │  │  │  ├─ representation-status
│  │     │  │  │  │  │  │  │  ├─ representation-status-notes
│  │     │  │  │  │  │  │  │  │  ├─ representation-status-notes.controller.js
│  │     │  │  │  │  │  │  │  │  ├─ representation-status-notes.validators.js
│  │     │  │  │  │  │  │  │  │  ├─ representation-status-notes.view-model.js
│  │     │  │  │  │  │  │  │  │  ├─ utils
│  │     │  │  │  │  │  │  │  │  │  └─ is-representation-depublished.js
│  │     │  │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │  │     ├─ representation-status-notes.test.js
│  │     │  │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │  │        └─ representation-status-notes.test.js.snap
│  │     │  │  │  │  │  │  │  ├─ representation-status.controller.js
│  │     │  │  │  │  │  │  │  ├─ representation-status.service.js
│  │     │  │  │  │  │  │  │  ├─ representation-status.utils.js
│  │     │  │  │  │  │  │  │  ├─ representation-status.validators.js
│  │     │  │  │  │  │  │  │  ├─ representation-status.view-model.js
│  │     │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │     ├─ representation-status.test.js
│  │     │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │        └─ representation-status.test.js.snap
│  │     │  │  │  │  │  │  ├─ task-log
│  │     │  │  │  │  │  │  │  ├─ task-list.view-model.js
│  │     │  │  │  │  │  │  │  ├─ task-log.controller.js
│  │     │  │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │  │     ├─ task-log.test.js
│  │     │  │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │  │        └─ task-log.test.js.snap
│  │     │  │  │  │  │  │  ├─ utils
│  │     │  │  │  │  │  │  │  ├─ get-check-answer-errors.js
│  │     │  │  │  │  │  │  │  ├─ get-organisation-or-fullname.js
│  │     │  │  │  │  │  │  │  ├─ get-page-links.js
│  │     │  │  │  │  │  │  │  ├─ get-page-titles.js
│  │     │  │  │  │  │  │  │  ├─ get-rep-mode-page-urls.js
│  │     │  │  │  │  │  │  │  ├─ get-representation-excerpts.js
│  │     │  │  │  │  │  │  │  ├─ get-representation-workflow-values.js
│  │     │  │  │  │  │  │  │  └─ representation-status-map.js
│  │     │  │  │  │  │  │  ├─ __fixtures__
│  │     │  │  │  │  │  │  │  └─ representation-details.fixture.js
│  │     │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │     ├─ applications-relevant-rep-details.test.js
│  │     │  │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │  │        └─ applications-relevant-rep-details.test.js.snap
│  │     │  │  │  │  │  ├─ utils
│  │     │  │  │  │  │  │  ├─ filter
│  │     │  │  │  │  │  │  │  └─ filter-view-model.js
│  │     │  │  │  │  │  │  ├─ get-key-dates.js
│  │     │  │  │  │  │  │  ├─ get-publish-queue-url.js
│  │     │  │  │  │  │  │  ├─ get-rep-mode-links.js
│  │     │  │  │  │  │  │  ├─ has-unpublished-rep-updates.js
│  │     │  │  │  │  │  │  ├─ is-relevant-reps-period-closed.js
│  │     │  │  │  │  │  │  ├─ pagination.js
│  │     │  │  │  │  │  │  ├─ publish-representations.js
│  │     │  │  │  │  │  │  ├─ search
│  │     │  │  │  │  │  │  │  └─ has-search-updated.js
│  │     │  │  │  │  │  │  └─ table.js
│  │     │  │  │  │  │  ├─ __fixtures__
│  │     │  │  │  │  │  │  ├─ publishable-representations.fixture.js
│  │     │  │  │  │  │  │  └─ representations.fixture.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ application-representations.view-model.unit.test.js
│  │     │  │  │  │  │     ├─ applications-representaions.test.js
│  │     │  │  │  │  │     ├─ filter-view-model.test.js
│  │     │  │  │  │  │     ├─ get-key-dates.test.js
│  │     │  │  │  │  │     ├─ is-relevant-reps-period-closed.unit.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ applications-representaions.test.js.snap
│  │     │  │  │  │  ├─ s51
│  │     │  │  │  │  │  ├─ applications-s51.controller.js
│  │     │  │  │  │  │  ├─ applications-s51.mapper.js
│  │     │  │  │  │  │  ├─ applications-s51.router.js
│  │     │  │  │  │  │  ├─ applications-s51.service.js
│  │     │  │  │  │  │  ├─ applications-s51.session.js
│  │     │  │  │  │  │  ├─ applications-s51.types.d.ts
│  │     │  │  │  │  │  ├─ applications-s51.validators.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ applications-s51.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ applications-s51.test.js.snap
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     ├─ applications-case.test.js
│  │     │  │  │  │     └─ __snapshots__
│  │     │  │  │  │        └─ applications-case.test.js.snap
│  │     │  │  │  ├─ common
│  │     │  │  │  │  ├─ components
│  │     │  │  │  │  │  ├─ build-query-string.js
│  │     │  │  │  │  │  ├─ error-handler
│  │     │  │  │  │  │  │  └─ error-handler.component.js
│  │     │  │  │  │  │  ├─ form
│  │     │  │  │  │  │  │  ├─ form-applicant.component.js
│  │     │  │  │  │  │  │  ├─ form-case.component.js
│  │     │  │  │  │  │  │  └─ form-key-dates.component.js
│  │     │  │  │  │  │  ├─ pagination
│  │     │  │  │  │  │  │  ├─ pagination-links.js
│  │     │  │  │  │  │  │  ├─ pagination-results-per-page.js
│  │     │  │  │  │  │  │  ├─ pagination.js
│  │     │  │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │  │     ├─ pagination-links.unit.test.js
│  │     │  │  │  │  │  │     └─ pagination-results-per-page.unit.test.js
│  │     │  │  │  │  │  └─ table
│  │     │  │  │  │  │     ├─ table-sorting-header-links.js
│  │     │  │  │  │  │     └─ __tests__
│  │     │  │  │  │  │        └─ table-sorting-header-links.unit.test.js
│  │     │  │  │  │  ├─ services
│  │     │  │  │  │  │  ├─ case.service.js
│  │     │  │  │  │  │  ├─ entities.service.js
│  │     │  │  │  │  │  └─ session.service.js
│  │     │  │  │  │  └─ validators
│  │     │  │  │  │     ├─ dates.validators.js
│  │     │  │  │  │     └─ times.validators.js
│  │     │  │  │  ├─ create-new-case
│  │     │  │  │  │  ├─ applicant
│  │     │  │  │  │  │  ├─ applications-create-applicant.controller.js
│  │     │  │  │  │  │  ├─ applications-create-applicant.guards.js
│  │     │  │  │  │  │  ├─ applications-create-applicant.locals.js
│  │     │  │  │  │  │  ├─ applications-create-applicant.router.js
│  │     │  │  │  │  │  ├─ applications-create-applicant.service.js
│  │     │  │  │  │  │  ├─ applications-create-applicant.types.d.ts
│  │     │  │  │  │  │  ├─ applications-create-applicant.validators.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ applications-create-applicant.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ applications-create-applicant.test.js.snap
│  │     │  │  │  │  ├─ applications-create.locals.js
│  │     │  │  │  │  ├─ applications-create.router.js
│  │     │  │  │  │  ├─ applications-create.service.js
│  │     │  │  │  │  ├─ case
│  │     │  │  │  │  │  ├─ applications-create-case.controller.js
│  │     │  │  │  │  │  ├─ applications-create-case.router.js
│  │     │  │  │  │  │  ├─ applications-create-case.types.d.ts
│  │     │  │  │  │  │  ├─ applications-create-case.validators.js
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ applications-create-case.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ applications-create-case.test.js.snap
│  │     │  │  │  │  ├─ check-your-answers
│  │     │  │  │  │  │  ├─ applications-create-check-your-answers.controller.js
│  │     │  │  │  │  │  ├─ applications-create-check-your-answers.router.js
│  │     │  │  │  │  │  ├─ applications-create-check-your-answers.service.js
│  │     │  │  │  │  │  ├─ applications-create-check-your-answers.types.d.ts
│  │     │  │  │  │  │  └─ __tests__
│  │     │  │  │  │  │     ├─ applications-create-check-your-answers.test.js
│  │     │  │  │  │  │     └─ __snapshots__
│  │     │  │  │  │  │        └─ applications-create-check-your-answers.test.js.snap
│  │     │  │  │  │  └─ key-dates
│  │     │  │  │  │     ├─ applications-create-key-dates.controller.js
│  │     │  │  │  │     ├─ applications-create-key-dates.router.js
│  │     │  │  │  │     ├─ applications-create-key-dates.types.d.ts
│  │     │  │  │  │     ├─ applications-create-key-dates.validators.js
│  │     │  │  │  │     └─ __tests__
│  │     │  │  │  │        ├─ applications-create-key-dates.test.js
│  │     │  │  │  │        └─ __snapshots__
│  │     │  │  │  │           └─ applications-create-key-dates.test.js.snap
│  │     │  │  │  ├─ search-results
│  │     │  │  │  │  ├─ application-search.service.js
│  │     │  │  │  │  ├─ application-search.validators.js
│  │     │  │  │  │  ├─ applications-search.controller.js
│  │     │  │  │  │  ├─ applications-search.router.js
│  │     │  │  │  │  ├─ applications-search.types.d.ts
│  │     │  │  │  │  └─ __tests
│  │     │  │  │  │     ├─ applications-search.test.js
│  │     │  │  │  │     └─ __snapshots__
│  │     │  │  │  │        └─ applications-search.test.js.snap
│  │     │  │  │  └─ __tests__
│  │     │  │  │     ├─ applications.test.js
│  │     │  │  │     └─ __snapshots__
│  │     │  │  │        └─ applications.test.js.snap
│  │     │  │  ├─ lib
│  │     │  │  │  ├─ active-directory-token.js
│  │     │  │  │  ├─ add-business-days-to-date.js
│  │     │  │  │  ├─ address-formatter.js
│  │     │  │  │  ├─ async-route.js
│  │     │  │  │  ├─ body-formatter.js
│  │     │  │  │  ├─ boolean-formatter.js
│  │     │  │  │  ├─ cache-handler.js
│  │     │  │  │  ├─ camel-to-snake.js
│  │     │  │  │  ├─ dates.js
│  │     │  │  │  ├─ http-error.js
│  │     │  │  │  ├─ logger.js
│  │     │  │  │  ├─ middleware
│  │     │  │  │  │  ├─ skip-middleware-if-errors-in-body.js
│  │     │  │  │  │  └─ __tests__
│  │     │  │  │  │     └─ skip-middleware-if-errors-in-body.test.js
│  │     │  │  │  ├─ msal.js
│  │     │  │  │  ├─ msGraphRequest.js
│  │     │  │  │  ├─ nunjucks-filters
│  │     │  │  │  │  ├─ actions-parameter-for-document-status.js
│  │     │  │  │  │  ├─ boolean-answer.js
│  │     │  │  │  │  ├─ collapse.js
│  │     │  │  │  │  ├─ date.js
│  │     │  │  │  │  ├─ ends-with.js
│  │     │  │  │  │  ├─ error-message.js
│  │     │  │  │  │  ├─ error-summary.js
│  │     │  │  │  │  ├─ file-size.js
│  │     │  │  │  │  ├─ format-name-org.js
│  │     │  │  │  │  ├─ index.js
│  │     │  │  │  │  ├─ json.js
│  │     │  │  │  │  ├─ key-dates-property.js
│  │     │  │  │  │  ├─ mime-type.js
│  │     │  │  │  │  ├─ object.js
│  │     │  │  │  │  ├─ sanitize.js
│  │     │  │  │  │  ├─ select-items.js
│  │     │  │  │  │  ├─ set-attribute.js
│  │     │  │  │  │  ├─ status-name.js
│  │     │  │  │  │  ├─ strip-query-parameters.js
│  │     │  │  │  │  └─ url.js
│  │     │  │  │  ├─ nunjucks-globals
│  │     │  │  │  │  ├─ index.js
│  │     │  │  │  │  └─ now.js
│  │     │  │  │  ├─ nunjucks-template-builders
│  │     │  │  │  │  └─ summary-list-builder.js
│  │     │  │  │  ├─ pagination-params.js
│  │     │  │  │  ├─ person-name-formatter.js
│  │     │  │  │  ├─ request.js
│  │     │  │  │  └─ __tests__
│  │     │  │  │     ├─ add-business-days-to-date.test.js
│  │     │  │  │     └─ libraries.test.js
│  │     │  │  ├─ server.js
│  │     │  │  ├─ static
│  │     │  │  │  └─ images
│  │     │  │  │     ├─ favicon.ico
│  │     │  │  │     ├─ govuk-apple-touch-icon-152x152.png
│  │     │  │  │     ├─ govuk-apple-touch-icon-167x167.png
│  │     │  │  │     ├─ govuk-apple-touch-icon-180x180.png
│  │     │  │  │     ├─ govuk-apple-touch-icon.png
│  │     │  │  │     ├─ govuk-crest-2x.png
│  │     │  │  │     ├─ govuk-crest.png
│  │     │  │  │     ├─ govuk-logotype-crown.png
│  │     │  │  │     ├─ govuk-mask-icon.svg
│  │     │  │  │     ├─ govuk-opengraph-image.png
│  │     │  │  │     └─ toastui-icons.png
│  │     │  │  └─ views
│  │     │  │     ├─ app
│  │     │  │     │  ├─ 401.njk
│  │     │  │     │  ├─ 403.njk
│  │     │  │     │  ├─ 404.njk
│  │     │  │     │  ├─ 500.njk
│  │     │  │     │  ├─ components
│  │     │  │     │  │  ├─ document-link.component.njk
│  │     │  │     │  │  ├─ document-list.component.njk
│  │     │  │     │  │  ├─ document-upload-info.njk
│  │     │  │     │  │  ├─ file-uploader.component.njk
│  │     │  │     │  │  ├─ file-uploader_legacy.njk
│  │     │  │     │  │  ├─ global-header.njk
│  │     │  │     │  │  ├─ govuk-date-input-extended.njk
│  │     │  │     │  │  └─ info-box.njk
│  │     │  │     │  ├─ confirmation.njk
│  │     │  │     │  ├─ dashboard.njk
│  │     │  │     │  ├─ includes
│  │     │  │     │  │  └─ csrf.njk
│  │     │  │     │  └─ layouts
│  │     │  │     │     ├─ app-three-column.layout.njk
│  │     │  │     │     ├─ app-two-column.layout.njk
│  │     │  │     │     ├─ app.layout.njk
│  │     │  │     │     └─ README.md
│  │     │  │     └─ applications
│  │     │  │        ├─ case
│  │     │  │        │  ├─ components
│  │     │  │        │  │  ├─ case-applicant-table.component.njk
│  │     │  │        │  │  ├─ case-details-table.component.njk
│  │     │  │        │  │  ├─ case-edit-link.component.njk
│  │     │  │        │  │  ├─ case-info-table-preview.component.njk
│  │     │  │        │  │  ├─ case-info-table.component.njk
│  │     │  │        │  │  ├─ case-key-dates-table.component.njk
│  │     │  │        │  │  └─ case-page-navigation.component.njk
│  │     │  │        │  ├─ fees.njk
│  │     │  │        │  ├─ layouts
│  │     │  │        │  │  └─ applications-case-layout.njk
│  │     │  │        │  ├─ overview.njk
│  │     │  │        │  ├─ preview-and-publish.njk
│  │     │  │        │  ├─ project-documentation.njk
│  │     │  │        │  ├─ project-information.njk
│  │     │  │        │  ├─ project-success-banner.njk
│  │     │  │        │  ├─ project-updates
│  │     │  │        │  │  ├─ project-updates-details.njk
│  │     │  │        │  │  ├─ project-updates-form.njk
│  │     │  │        │  │  └─ project-updates-table.njk
│  │     │  │        │  ├─ project-updates.njk
│  │     │  │        │  └─ unpublish.njk
│  │     │  │        ├─ case-documentation
│  │     │  │        │  ├─ documentation-delete.njk
│  │     │  │        │  ├─ documentation-edit.njk
│  │     │  │        │  ├─ documentation-publish.njk
│  │     │  │        │  ├─ documentation-success-banner.njk
│  │     │  │        │  ├─ documentation-table.njk
│  │     │  │        │  ├─ documentation-unpublish.njk
│  │     │  │        │  ├─ documentation-upload.njk
│  │     │  │        │  ├─ documentation-version-upload.njk
│  │     │  │        │  ├─ edit
│  │     │  │        │  │  ├─ checkboxes-input.njk
│  │     │  │        │  │  └─ max-length-input.njk
│  │     │  │        │  ├─ properties
│  │     │  │        │  │  ├─ documentation-properties.njk
│  │     │  │        │  │  ├─ tab-details.component.njk
│  │     │  │        │  │  └─ tab-history.component.njk
│  │     │  │        │  └─ search
│  │     │  │        │     ├─ document-search-results.njk
│  │     │  │        │     └─ document-search.component.njk
│  │     │  │        ├─ case-key-dates
│  │     │  │        │  ├─ key-dates-index.njk
│  │     │  │        │  └─ key-dates-section.njk
│  │     │  │        ├─ case-project-team
│  │     │  │        │  ├─ project-team-choose-role.njk
│  │     │  │        │  ├─ project-team-list.njk
│  │     │  │        │  ├─ project-team-remove.njk
│  │     │  │        │  └─ project-team-search.njk
│  │     │  │        ├─ case-s51
│  │     │  │        │  ├─ components
│  │     │  │        │  │  └─ enquirer-string.njk
│  │     │  │        │  ├─ properties
│  │     │  │        │  │  ├─ edit
│  │     │  │        │  │  │  ├─ s51-edit-advice-date.njk
│  │     │  │        │  │  │  ├─ s51-edit-advice-detail.njk
│  │     │  │        │  │  │  ├─ s51-edit-adviser.njk
│  │     │  │        │  │  │  ├─ s51-edit-enquirer.njk
│  │     │  │        │  │  │  ├─ s51-edit-enquiry-date.njk
│  │     │  │        │  │  │  ├─ s51-edit-enquiry-details.njk
│  │     │  │        │  │  │  ├─ s51-edit-method.njk
│  │     │  │        │  │  │  ├─ s51-edit-redaction.njk
│  │     │  │        │  │  │  ├─ s51-edit-status.njk
│  │     │  │        │  │  │  └─ s51-edit-title.njk
│  │     │  │        │  │  ├─ s51-properties.njk
│  │     │  │        │  │  ├─ s51-upload.njk
│  │     │  │        │  │  ├─ tab-attachments.component.njk
│  │     │  │        │  │  └─ tab-details.component.njk
│  │     │  │        │  ├─ s51-advice-details.njk
│  │     │  │        │  ├─ s51-attachment-successfully-deleted.njk
│  │     │  │        │  ├─ s51-check-your-answers.njk
│  │     │  │        │  ├─ s51-delete-attachment.njk
│  │     │  │        │  ├─ s51-delete.njk
│  │     │  │        │  ├─ s51-enquirer.njk
│  │     │  │        │  ├─ s51-enquiry-details.njk
│  │     │  │        │  ├─ s51-method.njk
│  │     │  │        │  ├─ s51-person.njk
│  │     │  │        │  ├─ s51-publishing-queue.njk
│  │     │  │        │  ├─ s51-successfully-deleted.njk
│  │     │  │        │  ├─ s51-successfully-published.njk
│  │     │  │        │  ├─ s51-successfully-unpublished.njk
│  │     │  │        │  ├─ s51-table.njk
│  │     │  │        │  ├─ s51-title.njk
│  │     │  │        │  └─ s51-unpublish.njk
│  │     │  │        ├─ case-timetable
│  │     │  │        │  ├─ components
│  │     │  │        │  │  ├─ timetable-item-summary.component.njk
│  │     │  │        │  │  └─ timetable-items-list.component.njk
│  │     │  │        │  ├─ timetable-check-your-answers.njk
│  │     │  │        │  ├─ timetable-delete.njk
│  │     │  │        │  ├─ timetable-details-form.njk
│  │     │  │        │  ├─ timetable-list.njk
│  │     │  │        │  ├─ timetable-new-item-type.njk
│  │     │  │        │  ├─ timetable-preview.njk
│  │     │  │        │  └─ timetable-success-banner.njk
│  │     │  │        ├─ components
│  │     │  │        │  ├─ application-summary.component.njk
│  │     │  │        │  ├─ case-form
│  │     │  │        │  │  ├─ applicant
│  │     │  │        │  │  │  ├─ address-view.njk
│  │     │  │        │  │  │  ├─ address.njk
│  │     │  │        │  │  │  ├─ applicant-email.njk
│  │     │  │        │  │  │  ├─ full-name.njk
│  │     │  │        │  │  │  ├─ info-types.njk
│  │     │  │        │  │  │  ├─ organisation-name.njk
│  │     │  │        │  │  │  ├─ telephone-number.njk
│  │     │  │        │  │  │  └─ website.njk
│  │     │  │        │  │  ├─ case
│  │     │  │        │  │  │  ├─ description.njk
│  │     │  │        │  │  │  ├─ grid-references.njk
│  │     │  │        │  │  │  ├─ project-location.njk
│  │     │  │        │  │  │  ├─ regions.njk
│  │     │  │        │  │  │  ├─ sector.njk
│  │     │  │        │  │  │  ├─ stage.njk
│  │     │  │        │  │  │  ├─ sub-sector.njk
│  │     │  │        │  │  │  ├─ team-email.njk
│  │     │  │        │  │  │  ├─ title.njk
│  │     │  │        │  │  │  └─ zoom-level.njk
│  │     │  │        │  │  ├─ case-form-layout.njk
│  │     │  │        │  │  └─ key-dates
│  │     │  │        │  │     ├─ date-internal.njk
│  │     │  │        │  │     └─ date-published.njk
│  │     │  │        │  ├─ excerpt.component.njk
│  │     │  │        │  ├─ folder
│  │     │  │        │  │  ├─ folder-actions.component.njk
│  │     │  │        │  │  ├─ folder-header.component.njk
│  │     │  │        │  │  ├─ folder-status.component.njk
│  │     │  │        │  │  └─ folder.njk
│  │     │  │        │  ├─ html-content-editor.njk
│  │     │  │        │  ├─ inputs
│  │     │  │        │  │  ├─ date-input.component.njk
│  │     │  │        │  │  └─ time-input.component.njk
│  │     │  │        │  ├─ pagination
│  │     │  │        │  │  ├─ pagination.d.ts
│  │     │  │        │  │  └─ results-per-page.component.njk
│  │     │  │        │  ├─ published-tag.component.njk
│  │     │  │        │  ├─ status-tag.component.njk
│  │     │  │        │  └─ __tests__
│  │     │  │        │     ├─ excerpt.component.test.js
│  │     │  │        │     └─ __snapshots__
│  │     │  │        │        └─ excerpt.component.test.js.snap
│  │     │  │        ├─ create-new-case
│  │     │  │        │  ├─ check-your-answers.njk
│  │     │  │        │  └─ confirmation.njk
│  │     │  │        ├─ dashboard.njk
│  │     │  │        ├─ layouts
│  │     │  │        │  ├─ applications.layout.njk
│  │     │  │        │  └─ s51-edit.layout.njk
│  │     │  │        ├─ representations
│  │     │  │        │  ├─ components
│  │     │  │        │  │  ├─ pre-search.component.njk
│  │     │  │        │  │  └─ table
│  │     │  │        │  │     └─ representations-table.component.njk
│  │     │  │        │  ├─ publish-representations-error.njk
│  │     │  │        │  ├─ publish-updated-representations.njk
│  │     │  │        │  ├─ publish-valid-representations
│  │     │  │        │  │  └─ index.njk
│  │     │  │        │  ├─ representation
│  │     │  │        │  │  ├─ address-details
│  │     │  │        │  │  │  ├─ includes
│  │     │  │        │  │  │  │  ├─ enter.include.njk
│  │     │  │        │  │  │  │  ├─ find.include.njk
│  │     │  │        │  │  │  │  └─ lookup.include.njk
│  │     │  │        │  │  │  └─ index.njk
│  │     │  │        │  │  ├─ attachment-upload.njk
│  │     │  │        │  │  ├─ components
│  │     │  │        │  │  │  ├─ representation-details-heading.component.njk
│  │     │  │        │  │  │  └─ representation-heading.component.njk
│  │     │  │        │  │  ├─ contact-details.njk
│  │     │  │        │  │  ├─ contact-method.njk
│  │     │  │        │  │  ├─ representation-comment.njk
│  │     │  │        │  │  ├─ representation-entity.njk
│  │     │  │        │  │  ├─ representation-type.njk
│  │     │  │        │  │  └─ under-18.njk
│  │     │  │        │  ├─ representation-details
│  │     │  │        │  │  ├─ change-redaction.njk
│  │     │  │        │  │  ├─ components
│  │     │  │        │  │  │  ├─ representation-address.component.njk
│  │     │  │        │  │  │  ├─ representation-status-tag.njk
│  │     │  │        │  │  │  └─ representation-summary-list.component.njk
│  │     │  │        │  │  ├─ includes
│  │     │  │        │  │  │  ├─ change
│  │     │  │        │  │  │  │  ├─ attachments.include.njk
│  │     │  │        │  │  │  │  ├─ representation.include.njk
│  │     │  │        │  │  │  │  └─ workflow.include.njk
│  │     │  │        │  │  │  ├─ check
│  │     │  │        │  │  │  │  ├─ attachments.include.njk
│  │     │  │        │  │  │  │  └─ representation.include.njk
│  │     │  │        │  │  │  ├─ representative-details.include.njk
│  │     │  │        │  │  │  └─ represented-details.include.njk
│  │     │  │        │  │  ├─ index.njk
│  │     │  │        │  │  ├─ redact-representation
│  │     │  │        │  │  │  └─ redact-representation.njk
│  │     │  │        │  │  ├─ representation-status
│  │     │  │        │  │  │  ├─ representation-status-notes.njk
│  │     │  │        │  │  │  └─ representation-status.njk
│  │     │  │        │  │  └─ task-log.njk
│  │     │  │        │  └─ representations.njk
│  │     │  │        └─ search-results
│  │     │  │           ├─ application-search.component.njk
│  │     │  │           └─ search-results.njk
│  │     │  └─ styles
│  │     │     ├─ .prettierrc
│  │     │     ├─ 1-settings
│  │     │     │  ├─ _settings.config.scss
│  │     │     │  └─ _settings.global.scss
│  │     │     ├─ 2-design-tokens
│  │     │     ├─ 3-tools
│  │     │     │  ├─ _index.scss
│  │     │     │  ├─ _tools.functions.scss
│  │     │     │  └─ _tools.z-index.scss
│  │     │     ├─ 4-generic
│  │     │     │  ├─ _generic.align-items.scss
│  │     │     │  ├─ _generic.box-sizing.scss
│  │     │     │  ├─ _generic.colours.scss
│  │     │     │  ├─ _generic.display.scss
│  │     │     │  ├─ _generic.flex-grow.scss
│  │     │     │  ├─ _generic.flex-wrap.scss
│  │     │     │  ├─ _generic.font-weight.scss
│  │     │     │  ├─ _generic.reset.scss
│  │     │     │  ├─ _generic.text-align.scss
│  │     │     │  ├─ _generic.white-space.scss
│  │     │     │  ├─ _generic.width.scss
│  │     │     │  └─ _generic.word-break.scss
│  │     │     ├─ 5-elements
│  │     │     │  ├─ _elements.form-group.scss
│  │     │     │  ├─ _elements.images.scss
│  │     │     │  └─ _elements.page.scss
│  │     │     ├─ 6-skeleton
│  │     │     │  └─ _container.scss
│  │     │     ├─ 7-components
│  │     │     │  ├─ app-header.scss
│  │     │     │  ├─ DashboardBox
│  │     │     │  │  └─ DashboardBox.scss
│  │     │     │  ├─ file-upload.scss
│  │     │     │  ├─ files-list.scss
│  │     │     │  ├─ filter-box.scss
│  │     │     │  ├─ html-content-editor.scss
│  │     │     │  ├─ InfoBox
│  │     │     │  │  └─ InfoBox.scss
│  │     │     │  ├─ key-dates-section.scss
│  │     │     │  ├─ list-menu.scss
│  │     │     │  ├─ project-update.scss
│  │     │     │  ├─ results-per-page.scss
│  │     │     │  ├─ sort-table.scss
│  │     │     │  ├─ status-tag.scss
│  │     │     │  ├─ _autocomplete.scss
│  │     │     │  ├─ _button-group.scss
│  │     │     │  ├─ _header.scss
│  │     │     │  ├─ _masthead.scss
│  │     │     │  ├─ _preview-table.scss
│  │     │     │  ├─ _related.scss
│  │     │     │  ├─ _summary-list.scss
│  │     │     │  └─ _table.scss
│  │     │     ├─ 8-utilities
│  │     │     ├─ 9-pages
│  │     │     ├─ dev
│  │     │     │  ├─ dev
│  │     │     │  │  └─ _dev.scss
│  │     │     │  └─ release
│  │     │     │     └─ _dev.scss
│  │     │     ├─ env
│  │     │     │  ├─ development
│  │     │     │  │  └─ _env-vars.scss
│  │     │     │  └─ production
│  │     │     │     └─ _env-vars.scss
│  │     │     ├─ main.scss
│  │     │     ├─ README.md
│  │     │     └─ _shame.scss
│  │     ├─ testing
│  │     │  ├─ app
│  │     │  │  ├─ app.js
│  │     │  │  ├─ factory
│  │     │  │  │  └─ account-info.js
│  │     │  │  └─ mocks
│  │     │  │     ├─ auth.js
│  │     │  │     ├─ client-side.js
│  │     │  │     ├─ msal.js
│  │     │  │     └─ project-team.js
│  │     │  ├─ applications
│  │     │  │  ├─ applications.js
│  │     │  │  ├─ applications.test.d.ts
│  │     │  │  ├─ factory
│  │     │  │  │  ├─ application.js
│  │     │  │  │  ├─ documentation-file.js
│  │     │  │  │  ├─ options-item.js
│  │     │  │  │  ├─ project-team.js
│  │     │  │  │  ├─ s51-advice.js
│  │     │  │  │  └─ util.js
│  │     │  │  └─ fixtures
│  │     │  │     ├─ cases.js
│  │     │  │     ├─ documentation-files.js
│  │     │  │     ├─ key-dates.js
│  │     │  │     ├─ options-item.js
│  │     │  │     ├─ project-team.js
│  │     │  │     ├─ s51-advice.js
│  │     │  │     └─ timetable-types.js
│  │     │  ├─ index.js
│  │     │  └─ util
│  │     │     └─ date.js
│  │     └─ typings.d.ts
│  ├─ azure-pipelines-api-test.yml
│  ├─ azure-pipelines-build.yml
│  ├─ azure-pipelines-ci.yml
│  ├─ azure-pipelines-db-seed-appeals-production.yml
│  ├─ azure-pipelines-db-seed-appeals.yml
│  ├─ azure-pipelines-db-seed.yml
│  ├─ azure-pipelines-deploy-appeals.yml
│  ├─ azure-pipelines-deploy.yml
│  ├─ azure-pipelines-e2e-appeals.yml
│  ├─ azure-pipelines-e2e-applications.yml
│  ├─ azure-pipelines-release.yml
│  ├─ azure-pipelines-variables.yml
│  ├─ commitlint.config.cjs
│  ├─ docs
│  │  ├─ appeals-integration.md
│  │  ├─ azurite-blob-emulator-windows.md
│  │  ├─ azurite-blob-emulator.md
│  │  ├─ database-migration.md
│  │  ├─ document-state-transitions.md
│  │  ├─ documents-versions-relationship.md
│  │  ├─ enabling-ad-locally.md
│  │  ├─ event-repository.md
│  │  ├─ fix-duplicate-data-migration.md
│  │  ├─ front-office-submissions.md
│  │  ├─ prisma-runbook.md
│  │  ├─ README.md
│  │  ├─ self-signed-ssl.md
│  │  ├─ types.md
│  │  ├─ uploading-files.md
│  │  └─ web-overview.md
│  ├─ jsconfig.json
│  ├─ LICENSE
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ packages
│  │  ├─ appeals
│  │  │  ├─ index.d.ts
│  │  │  ├─ package.json
│  │  │  └─ types
│  │  │     ├─ appeal.d.ts
│  │  │     ├─ case-officer.d.ts
│  │  │     ├─ document.d.ts
│  │  │     ├─ index.d.ts
│  │  │     ├─ inspector.d.ts
│  │  │     └─ validation.d.ts
│  │  ├─ applications
│  │  │  ├─ index.d.ts
│  │  │  ├─ lib
│  │  │  │  └─ application
│  │  │  │     ├─ project-update.js
│  │  │  │     └─ subscription.js
│  │  │  ├─ package.json
│  │  │  └─ types
│  │  │     ├─ address.d.ts
│  │  │     ├─ application.d.ts
│  │  │     ├─ file-folders.d.ts
│  │  │     ├─ index.d.ts
│  │  │     ├─ project-update.d.ts
│  │  │     ├─ representation.d.ts
│  │  │     ├─ s51-advice.d.ts
│  │  │     └─ subscription.d.ts
│  │  ├─ blob-storage-client
│  │  │  ├─ index.d.ts
│  │  │  ├─ index.js
│  │  │  ├─ jsconfig.json
│  │  │  ├─ package.json
│  │  │  └─ src
│  │  │     └─ blob-storage-client.js
│  │  ├─ event-client
│  │  │  ├─ index.d.ts
│  │  │  ├─ index.js
│  │  │  ├─ jsconfig.json
│  │  │  ├─ package.json
│  │  │  └─ src
│  │  │     ├─ event-client.js
│  │  │     ├─ event-type.js
│  │  │     ├─ local-event-client.js
│  │  │     └─ service-bus-event-client.js
│  │  ├─ express
│  │  │  ├─ index.d.ts
│  │  │  ├─ index.js
│  │  │  ├─ jsconfig.json
│  │  │  ├─ middleware
│  │  │  │  ├─ locals.js
│  │  │  │  ├─ multer.js
│  │  │  │  ├─ session.js
│  │  │  │  └─ validation.js
│  │  │  ├─ package.json
│  │  │  ├─ types
│  │  │  │  ├─ express.d.ts
│  │  │  │  └─ multer.d.ts
│  │  │  ├─ utils
│  │  │  │  ├─ compose.js
│  │  │  │  ├─ formdata.js
│  │  │  │  └─ helpers.js
│  │  │  └─ validators
│  │  │     └─ date-input.js
│  │  └─ platform
│  │     ├─ http
│  │     ├─ index.d.ts
│  │     ├─ index.js
│  │     ├─ jsconfig.json
│  │     ├─ package.json
│  │     ├─ testing
│  │     │  ├─ assets
│  │     │  │  ├─ anthropods.pdf
│  │     │  │  ├─ assets.js
│  │     │  │  └─ simple.pdf
│  │     │  ├─ fake.js
│  │     │  └─ html-parser.js
│  │     ├─ types
│  │     │  └─ account.d.ts
│  │     ├─ utils
│  │     │  ├─ date.js
│  │     │  ├─ dotenv.js
│  │     │  ├─ filter.js
│  │     │  ├─ redis.js
│  │     │  └─ __tests__
│  │     │     └─ redis.test.js
│  │     └─ validators
│  │        ├─ date.js
│  │        └─ postcode.js
│  ├─ rabbitmq_config
│  │  ├─ enabled_plugins
│  │  └─ rabbitmq.conf
│  ├─ README.md
│  └─ turbo.json
├─ class_test.ipynb
├─ CODEOWNERS
├─ config.yaml
├─ custom_fields.json
├─ dart_api_test.ipynb
├─ data-model
│  ├─ .ruff_cache
│  │  ├─ CACHEDIR.TAG
│  │  └─ content
│  │     └─ a7616b1ea20ca27c
│  ├─ docs
│  │  ├─ case-schedule.md
│  │  ├─ employee.md
│  │  ├─ interested-party.md
│  │  ├─ nsip-document.md
│  │  ├─ nsip-exam-timetable-defs-event.md
│  │  ├─ nsip-exam-timetable-defs-line-item.md
│  │  ├─ nsip-exam-timetable-defs.md
│  │  ├─ nsip-exam-timetable-submission.md
│  │  ├─ nsip-exam-timetable.md
│  │  ├─ nsip-project-update.md
│  │  ├─ nsip-project.md
│  │  ├─ nsip-representation-defs-attachment.md
│  │  ├─ nsip-representation-defs.md
│  │  ├─ nsip-representation.md
│  │  ├─ nsip-subscription.md
│  │  ├─ README.md
│  │  ├─ s51-advice.md
│  │  └─ service-user.md
│  ├─ jsconfig.json
│  ├─ LICENSE
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ pins_data_model
│  │  ├─ .ruff_cache
│  │  │  ├─ 0.1.6
│  │  │  │  └─ 9229715226369089989
│  │  │  ├─ CACHEDIR.TAG
│  │  │  └─ content
│  │  │     ├─ 14a3f53316ae7022
│  │  │     ├─ 1d4582ea1541e1a2
│  │  │     ├─ 253d8058089f85ce
│  │  │     ├─ 40c3bfbcc78b15eb
│  │  │     ├─ 46ed9c4feff004d
│  │  │     ├─ 9274464bbae3fb70
│  │  │     ├─ 9353e223d4e74549
│  │  │     ├─ a0b5e1c65fb9d34a
│  │  │     ├─ a3c95b69e79764b
│  │  │     ├─ b35088221760a891
│  │  │     ├─ bb932667808e11da
│  │  │     ├─ c3879f72c29d7e38
│  │  │     ├─ d73dea5b3f1b2ca1
│  │  │     └─ e2c310a5be0a3007
│  │  ├─ gen_models.py
│  │  ├─ load_schemas.py
│  │  ├─ models
│  │  │  ├─ .ruff_cache
│  │  │  │  ├─ 0.1.6
│  │  │  │  │  └─ 6663750638476131151
│  │  │  │  └─ CACHEDIR.TAG
│  │  │  ├─ model_case_schedule.py
│  │  │  ├─ model_employee.py
│  │  │  ├─ model_nsip_document.py
│  │  │  ├─ model_nsip_exam_timetable.py
│  │  │  ├─ model_nsip_project.py
│  │  │  ├─ model_nsip_project_update.py
│  │  │  ├─ model_nsip_representation.py
│  │  │  ├─ model_nsip_subscription.py
│  │  │  ├─ model_s51_advice.py
│  │  │  ├─ model_service_user.py
│  │  │  └─ __init__.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     └─ load_schemas.cpython-311.pyc
│  ├─ README.md
│  ├─ requirements.txt
│  ├─ schemas
│  │  ├─ case-schedule.schema.json
│  │  ├─ commands
│  │  │  ├─ interested-party.schema.json
│  │  │  ├─ new-deadline-submission.schema.json
│  │  │  ├─ nsip-exam-timetable-submission.schema.json
│  │  │  ├─ register-nsip-subscription.schema.json
│  │  │  ├─ register-representation.schema.json
│  │  │  └─ __init__.py
│  │  ├─ employee.schema.json
│  │  ├─ nsip-document.schema.json
│  │  ├─ nsip-exam-timetable.schema.json
│  │  ├─ nsip-project-update.schema.json
│  │  ├─ nsip-project.schema.json
│  │  ├─ nsip-representation.schema.json
│  │  ├─ nsip-subscription.schema.json
│  │  ├─ s51-advice.schema.json
│  │  ├─ service-user.schema.json
│  │  └─ __init__.py
│  ├─ setup.py
│  └─ src
│     ├─ gen-docs.js
│     ├─ gen-types.js
│     ├─ index.d.ts
│     ├─ index.js
│     ├─ lib
│     │  └─ load.js
│     └─ schemas.d.ts
├─ data-models-test-notebook.ipynb
├─ diagram.drawio
├─ diagram.png
├─ diagrams
│  ├─ logicapp-architecture.ipynb
│  ├─ README.md
│  └─ requirements-diagrams.txt
├─ exercism.py
├─ function-test.ipynb
├─ function-test.py
├─ Functions.code-workspace
├─ functions_workspace.code-workspace
├─ github-testing.ipynb
├─ github-testing.py
├─ gpt-engineer
│  ├─ archive
│  │  ├─ 20231009_142526
│  │  │  ├─ memory
│  │  │  │  └─ logs
│  │  │  └─ workspace
│  │  ├─ 20231009_142840
│  │  │  ├─ memory
│  │  │  │  └─ logs
│  │  │  │     └─ clarify
│  │  │  └─ workspace
│  │  └─ 20231009_143456
│  │     ├─ memory
│  │     │  └─ logs
│  │     │     └─ clarify
│  │     └─ workspace
│  ├─ gpt-engineer
│  │  ├─ archive
│  │  │  └─ 20231010_125320
│  │  │     ├─ memory
│  │  │     │  └─ logs
│  │  │     └─ workspace
│  │  └─ prompt
│  ├─ memory
│  │  └─ logs
│  │     └─ clarify
│  └─ prompt
├─ gpt-engineerclear
│  └─ archive
│     └─ 20231009_142823
│        ├─ memory
│        │  └─ logs
│        └─ workspace
├─ IMS-API.py
├─ ims-request-body.json
├─ ims_notebook.ipynb
├─ investment.ipynb
├─ jsonToYaml.ipynb
├─ kwargs.ipynb
├─ lasagna.py
├─ listfunctionkeys.ipynb
├─ loguru_test.py
├─ markdown-test.md
├─ mermaid.md
├─ mslearn-ai-challenge
│  └─ ml-services
│     ├─ deployment.json
│     ├─ deployment_operations.json
│     ├─ parameters.json
│     └─ template.json
├─ ODW-Service
│  ├─ .checkov.yaml
│  ├─ .pre-commit-config.yaml
│  ├─ .terraform
│  │  └─ modules
│  │     └─ modules.json
│  ├─ .tflint.hcl
│  ├─ .vscode
│  │  └─ settings.json
│  ├─ DaRT
│  │  ├─ dart_sql.sql
│  │  ├─ function_app.py
│  │  └─ model_dart.py
│  ├─ docs
│  │  ├─ architecture
│  │  │  └─ apim-and-function-apps.md
│  │  ├─ entities
│  │  │  └─ zendesk
│  │  │     └─ readme.md
│  │  ├─ layers
│  │  │  ├─ 0_layers_overview.md
│  │  │  ├─ 1_raw.md
│  │  │  ├─ 2_standardised.md
│  │  │  ├─ 3_harmonised.md
│  │  │  ├─ 4_curated.md
│  │  │  └─ 5_publish.md
│  │  ├─ pull_request_template.md
│  │  ├─ standards
│  │  │  ├─ brach_standards.md
│  │  │  ├─ data-standards.md
│  │  │  ├─ get-data-from-external-api.md
│  │  │  ├─ infrastructure_standards.md
│  │  │  ├─ naming_standards.md
│  │  │  ├─ notebooks_standards.md
│  │  │  └─ pipeline_standards.md
│  │  └─ zendesk
│  │     └─ zendesk_readme.md
│  ├─ functionapp
│  │  └─ service-bus-to-storage
│  │     ├─ host.json
│  │     └─ onNewServiceUserMessage
│  │        ├─ function.json
│  │        └─ index.js
│  ├─ functions
│  │  ├─ .funcignore
│  │  ├─ .python_packages
│  │  ├─ .ruff_cache
│  │  │  ├─ 0.1.6
│  │  │  │  ├─ 1276037581768381079
│  │  │  │  ├─ 13326032602809239537
│  │  │  │  ├─ 14155531134347745027
│  │  │  │  ├─ 16806372439394627971
│  │  │  │  ├─ 16954368038463131736
│  │  │  │  ├─ 1750149486543734826
│  │  │  │  ├─ 5436457025811949359
│  │  │  │  ├─ 6373995126180455448
│  │  │  │  └─ 8467928824308975702
│  │  │  └─ CACHEDIR.TAG
│  │  ├─ .venv
│  │  │  ├─ Include
│  │  │  ├─ Lib
│  │  │  │  └─ site-packages
│  │  │  │     ├─ 629853fdff261ed89b74__mypyc.cp310-win_amd64.pyd
│  │  │  │     ├─ adodbapi
│  │  │  │     │  ├─ adodbapi.py
│  │  │  │     │  ├─ ado_consts.py
│  │  │  │     │  ├─ apibase.py
│  │  │  │     │  ├─ examples
│  │  │  │     │  │  ├─ db_print.py
│  │  │  │     │  │  ├─ db_table_names.py
│  │  │  │     │  │  ├─ xls_read.py
│  │  │  │     │  │  ├─ xls_write.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ db_print.cpython-310.pyc
│  │  │  │     │  │     ├─ db_table_names.cpython-310.pyc
│  │  │  │     │  │     ├─ xls_read.cpython-310.pyc
│  │  │  │     │  │     └─ xls_write.cpython-310.pyc
│  │  │  │     │  ├─ is64bit.py
│  │  │  │     │  ├─ license.txt
│  │  │  │     │  ├─ process_connect_string.py
│  │  │  │     │  ├─ readme.txt
│  │  │  │     │  ├─ remote.py
│  │  │  │     │  ├─ schema_table.py
│  │  │  │     │  ├─ setup.py
│  │  │  │     │  ├─ test
│  │  │  │     │  │  ├─ adodbapitest.py
│  │  │  │     │  │  ├─ adodbapitestconfig.py
│  │  │  │     │  │  ├─ dbapi20.py
│  │  │  │     │  │  ├─ is64bit.py
│  │  │  │     │  │  ├─ setuptestframework.py
│  │  │  │     │  │  ├─ test_adodbapi_dbapi20.py
│  │  │  │     │  │  ├─ tryconnection.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ adodbapitest.cpython-310.pyc
│  │  │  │     │  │     ├─ adodbapitestconfig.cpython-310.pyc
│  │  │  │     │  │     ├─ dbapi20.cpython-310.pyc
│  │  │  │     │  │     ├─ is64bit.cpython-310.pyc
│  │  │  │     │  │     ├─ setuptestframework.cpython-310.pyc
│  │  │  │     │  │     ├─ test_adodbapi_dbapi20.cpython-310.pyc
│  │  │  │     │  │     └─ tryconnection.cpython-310.pyc
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ adodbapi.cpython-310.pyc
│  │  │  │     │     ├─ ado_consts.cpython-310.pyc
│  │  │  │     │     ├─ apibase.cpython-310.pyc
│  │  │  │     │     ├─ is64bit.cpython-310.pyc
│  │  │  │     │     ├─ process_connect_string.cpython-310.pyc
│  │  │  │     │     ├─ remote.cpython-310.pyc
│  │  │  │     │     ├─ schema_table.cpython-310.pyc
│  │  │  │     │     ├─ setup.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ annotated_types
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ test_cases.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ test_cases.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ annotated_types-0.6.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  └─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ anyio
│  │  │  │     │  ├─ abc
│  │  │  │     │  │  ├─ _eventloop.py
│  │  │  │     │  │  ├─ _resources.py
│  │  │  │     │  │  ├─ _sockets.py
│  │  │  │     │  │  ├─ _streams.py
│  │  │  │     │  │  ├─ _subprocesses.py
│  │  │  │     │  │  ├─ _tasks.py
│  │  │  │     │  │  ├─ _testing.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ _eventloop.cpython-310.pyc
│  │  │  │     │  │     ├─ _resources.cpython-310.pyc
│  │  │  │     │  │     ├─ _sockets.cpython-310.pyc
│  │  │  │     │  │     ├─ _streams.cpython-310.pyc
│  │  │  │     │  │     ├─ _subprocesses.cpython-310.pyc
│  │  │  │     │  │     ├─ _tasks.cpython-310.pyc
│  │  │  │     │  │     ├─ _testing.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ from_thread.py
│  │  │  │     │  ├─ lowlevel.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ pytest_plugin.py
│  │  │  │     │  ├─ streams
│  │  │  │     │  │  ├─ buffered.py
│  │  │  │     │  │  ├─ file.py
│  │  │  │     │  │  ├─ memory.py
│  │  │  │     │  │  ├─ stapled.py
│  │  │  │     │  │  ├─ text.py
│  │  │  │     │  │  ├─ tls.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ buffered.cpython-310.pyc
│  │  │  │     │  │     ├─ file.cpython-310.pyc
│  │  │  │     │  │     ├─ memory.cpython-310.pyc
│  │  │  │     │  │     ├─ stapled.cpython-310.pyc
│  │  │  │     │  │     ├─ text.cpython-310.pyc
│  │  │  │     │  │     ├─ tls.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ to_process.py
│  │  │  │     │  ├─ to_thread.py
│  │  │  │     │  ├─ _backends
│  │  │  │     │  │  ├─ _asyncio.py
│  │  │  │     │  │  ├─ _trio.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ _asyncio.cpython-310.pyc
│  │  │  │     │  │     ├─ _trio.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _core
│  │  │  │     │  │  ├─ _eventloop.py
│  │  │  │     │  │  ├─ _exceptions.py
│  │  │  │     │  │  ├─ _fileio.py
│  │  │  │     │  │  ├─ _resources.py
│  │  │  │     │  │  ├─ _signals.py
│  │  │  │     │  │  ├─ _sockets.py
│  │  │  │     │  │  ├─ _streams.py
│  │  │  │     │  │  ├─ _subprocesses.py
│  │  │  │     │  │  ├─ _synchronization.py
│  │  │  │     │  │  ├─ _tasks.py
│  │  │  │     │  │  ├─ _testing.py
│  │  │  │     │  │  ├─ _typedattr.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ _eventloop.cpython-310.pyc
│  │  │  │     │  │     ├─ _exceptions.cpython-310.pyc
│  │  │  │     │  │     ├─ _fileio.cpython-310.pyc
│  │  │  │     │  │     ├─ _resources.cpython-310.pyc
│  │  │  │     │  │     ├─ _signals.cpython-310.pyc
│  │  │  │     │  │     ├─ _sockets.cpython-310.pyc
│  │  │  │     │  │     ├─ _streams.cpython-310.pyc
│  │  │  │     │  │     ├─ _subprocesses.cpython-310.pyc
│  │  │  │     │  │     ├─ _synchronization.cpython-310.pyc
│  │  │  │     │  │     ├─ _tasks.cpython-310.pyc
│  │  │  │     │  │     ├─ _testing.cpython-310.pyc
│  │  │  │     │  │     ├─ _typedattr.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ from_thread.cpython-310.pyc
│  │  │  │     │     ├─ lowlevel.cpython-310.pyc
│  │  │  │     │     ├─ pytest_plugin.cpython-310.pyc
│  │  │  │     │     ├─ to_process.cpython-310.pyc
│  │  │  │     │     ├─ to_thread.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ anyio-4.1.0.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ argcomplete
│  │  │  │     │  ├─ bash_completion.d
│  │  │  │     │  │  └─ _python-argcomplete
│  │  │  │     │  ├─ completers.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ finders.py
│  │  │  │     │  ├─ io.py
│  │  │  │     │  ├─ lexers.py
│  │  │  │     │  ├─ packages
│  │  │  │     │  │  ├─ _argparse.py
│  │  │  │     │  │  ├─ _shlex.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ _argparse.cpython-310.pyc
│  │  │  │     │  │     ├─ _shlex.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ shell_integration.py
│  │  │  │     │  ├─ _check_console_script.py
│  │  │  │     │  ├─ _check_module.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ completers.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ finders.cpython-310.pyc
│  │  │  │     │     ├─ io.cpython-310.pyc
│  │  │  │     │     ├─ lexers.cpython-310.pyc
│  │  │  │     │     ├─ shell_integration.cpython-310.pyc
│  │  │  │     │     ├─ _check_console_script.cpython-310.pyc
│  │  │  │     │     ├─ _check_module.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ argcomplete-3.2.1.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE.rst
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ NOTICE
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ attr
│  │  │  │     │  ├─ converters.py
│  │  │  │     │  ├─ converters.pyi
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ exceptions.pyi
│  │  │  │     │  ├─ filters.py
│  │  │  │     │  ├─ filters.pyi
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ setters.py
│  │  │  │     │  ├─ setters.pyi
│  │  │  │     │  ├─ validators.py
│  │  │  │     │  ├─ validators.pyi
│  │  │  │     │  ├─ _cmp.py
│  │  │  │     │  ├─ _cmp.pyi
│  │  │  │     │  ├─ _compat.py
│  │  │  │     │  ├─ _config.py
│  │  │  │     │  ├─ _funcs.py
│  │  │  │     │  ├─ _make.py
│  │  │  │     │  ├─ _next_gen.py
│  │  │  │     │  ├─ _typing_compat.pyi
│  │  │  │     │  ├─ _version_info.py
│  │  │  │     │  ├─ _version_info.pyi
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __init__.pyi
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ converters.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ filters.cpython-310.pyc
│  │  │  │     │     ├─ setters.cpython-310.pyc
│  │  │  │     │     ├─ validators.cpython-310.pyc
│  │  │  │     │     ├─ _cmp.cpython-310.pyc
│  │  │  │     │     ├─ _compat.cpython-310.pyc
│  │  │  │     │     ├─ _config.cpython-310.pyc
│  │  │  │     │     ├─ _funcs.cpython-310.pyc
│  │  │  │     │     ├─ _make.cpython-310.pyc
│  │  │  │     │     ├─ _next_gen.cpython-310.pyc
│  │  │  │     │     ├─ _version_info.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ attrs
│  │  │  │     │  ├─ converters.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ filters.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ setters.py
│  │  │  │     │  ├─ validators.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __init__.pyi
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ converters.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ filters.cpython-310.pyc
│  │  │  │     │     ├─ setters.cpython-310.pyc
│  │  │  │     │     ├─ validators.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ attrs-23.2.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  └─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ azure
│  │  │  │     │  ├─ core
│  │  │  │     │  │  ├─ async_paging.py
│  │  │  │     │  │  ├─ configuration.py
│  │  │  │     │  │  ├─ credentials.py
│  │  │  │     │  │  ├─ credentials_async.py
│  │  │  │     │  │  ├─ exceptions.py
│  │  │  │     │  │  ├─ messaging.py
│  │  │  │     │  │  ├─ paging.py
│  │  │  │     │  │  ├─ pipeline
│  │  │  │     │  │  │  ├─ policies
│  │  │  │     │  │  │  │  ├─ _authentication.py
│  │  │  │     │  │  │  │  ├─ _authentication_async.py
│  │  │  │     │  │  │  │  ├─ _base.py
│  │  │  │     │  │  │  │  ├─ _base_async.py
│  │  │  │     │  │  │  │  ├─ _custom_hook.py
│  │  │  │     │  │  │  │  ├─ _distributed_tracing.py
│  │  │  │     │  │  │  │  ├─ _redirect.py
│  │  │  │     │  │  │  │  ├─ _redirect_async.py
│  │  │  │     │  │  │  │  ├─ _retry.py
│  │  │  │     │  │  │  │  ├─ _retry_async.py
│  │  │  │     │  │  │  │  ├─ _sensitive_header_cleanup_policy.py
│  │  │  │     │  │  │  │  ├─ _universal.py
│  │  │  │     │  │  │  │  ├─ _utils.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ _authentication.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _authentication_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _base.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _base_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _custom_hook.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _distributed_tracing.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _redirect.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _redirect_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _retry.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _retry_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _sensitive_header_cleanup_policy.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _universal.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _utils.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ transport
│  │  │  │     │  │  │  │  ├─ _aiohttp.py
│  │  │  │     │  │  │  │  ├─ _base.py
│  │  │  │     │  │  │  │  ├─ _base_async.py
│  │  │  │     │  │  │  │  ├─ _base_requests_async.py
│  │  │  │     │  │  │  │  ├─ _bigger_block_size_http_adapters.py
│  │  │  │     │  │  │  │  ├─ _requests_asyncio.py
│  │  │  │     │  │  │  │  ├─ _requests_basic.py
│  │  │  │     │  │  │  │  ├─ _requests_trio.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ _aiohttp.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _base.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _base_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _base_requests_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _bigger_block_size_http_adapters.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _requests_asyncio.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _requests_basic.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _requests_trio.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _base.py
│  │  │  │     │  │  │  ├─ _base_async.py
│  │  │  │     │  │  │  ├─ _tools.py
│  │  │  │     │  │  │  ├─ _tools_async.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _base_async.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _tools.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _tools_async.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ polling
│  │  │  │     │  │  │  ├─ async_base_polling.py
│  │  │  │     │  │  │  ├─ base_polling.py
│  │  │  │     │  │  │  ├─ _async_poller.py
│  │  │  │     │  │  │  ├─ _poller.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ async_base_polling.cpython-310.pyc
│  │  │  │     │  │  │     ├─ base_polling.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _async_poller.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _poller.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ py.typed
│  │  │  │     │  │  ├─ rest
│  │  │  │     │  │  │  ├─ _aiohttp.py
│  │  │  │     │  │  │  ├─ _helpers.py
│  │  │  │     │  │  │  ├─ _http_response_impl.py
│  │  │  │     │  │  │  ├─ _http_response_impl_async.py
│  │  │  │     │  │  │  ├─ _requests_asyncio.py
│  │  │  │     │  │  │  ├─ _requests_basic.py
│  │  │  │     │  │  │  ├─ _requests_trio.py
│  │  │  │     │  │  │  ├─ _rest_py3.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _aiohttp.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _helpers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _http_response_impl.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _http_response_impl_async.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _requests_asyncio.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _requests_basic.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _requests_trio.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _rest_py3.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ serialization.py
│  │  │  │     │  │  ├─ settings.py
│  │  │  │     │  │  ├─ tracing
│  │  │  │     │  │  │  ├─ common.py
│  │  │  │     │  │  │  ├─ decorator.py
│  │  │  │     │  │  │  ├─ decorator_async.py
│  │  │  │     │  │  │  ├─ ext
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _abstract_span.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ common.cpython-310.pyc
│  │  │  │     │  │  │     ├─ decorator.cpython-310.pyc
│  │  │  │     │  │  │     ├─ decorator_async.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _abstract_span.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ utils
│  │  │  │     │  │  │  ├─ _connection_string_parser.py
│  │  │  │     │  │  │  ├─ _messaging_shared.py
│  │  │  │     │  │  │  ├─ _pipeline_transport_rest_shared.py
│  │  │  │     │  │  │  ├─ _pipeline_transport_rest_shared_async.py
│  │  │  │     │  │  │  ├─ _utils.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _connection_string_parser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _messaging_shared.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _pipeline_transport_rest_shared.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _pipeline_transport_rest_shared_async.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _utils.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ _enum_meta.py
│  │  │  │     │  │  ├─ _match_conditions.py
│  │  │  │     │  │  ├─ _pipeline_client.py
│  │  │  │     │  │  ├─ _pipeline_client_async.py
│  │  │  │     │  │  ├─ _version.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ async_paging.cpython-310.pyc
│  │  │  │     │  │     ├─ configuration.cpython-310.pyc
│  │  │  │     │  │     ├─ credentials.cpython-310.pyc
│  │  │  │     │  │     ├─ credentials_async.cpython-310.pyc
│  │  │  │     │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │     ├─ messaging.cpython-310.pyc
│  │  │  │     │  │     ├─ paging.cpython-310.pyc
│  │  │  │     │  │     ├─ serialization.cpython-310.pyc
│  │  │  │     │  │     ├─ settings.cpython-310.pyc
│  │  │  │     │  │     ├─ _enum_meta.cpython-310.pyc
│  │  │  │     │  │     ├─ _match_conditions.cpython-310.pyc
│  │  │  │     │  │     ├─ _pipeline_client.cpython-310.pyc
│  │  │  │     │  │     ├─ _pipeline_client_async.cpython-310.pyc
│  │  │  │     │  │     ├─ _version.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ functions
│  │  │  │     │  │  ├─ blob.py
│  │  │  │     │  │  ├─ cosmosdb.py
│  │  │  │     │  │  ├─ decorators
│  │  │  │     │  │  │  ├─ blob.py
│  │  │  │     │  │  │  ├─ constants.py
│  │  │  │     │  │  │  ├─ core.py
│  │  │  │     │  │  │  ├─ cosmosdb.py
│  │  │  │     │  │  │  ├─ eventgrid.py
│  │  │  │     │  │  │  ├─ eventhub.py
│  │  │  │     │  │  │  ├─ function_app.py
│  │  │  │     │  │  │  ├─ generic.py
│  │  │  │     │  │  │  ├─ http.py
│  │  │  │     │  │  │  ├─ queue.py
│  │  │  │     │  │  │  ├─ servicebus.py
│  │  │  │     │  │  │  ├─ table.py
│  │  │  │     │  │  │  ├─ timer.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ warmup.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ blob.cpython-310.pyc
│  │  │  │     │  │  │     ├─ constants.cpython-310.pyc
│  │  │  │     │  │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cosmosdb.cpython-310.pyc
│  │  │  │     │  │  │     ├─ eventgrid.cpython-310.pyc
│  │  │  │     │  │  │     ├─ eventhub.cpython-310.pyc
│  │  │  │     │  │  │     ├─ function_app.cpython-310.pyc
│  │  │  │     │  │  │     ├─ generic.cpython-310.pyc
│  │  │  │     │  │  │     ├─ http.cpython-310.pyc
│  │  │  │     │  │  │     ├─ queue.cpython-310.pyc
│  │  │  │     │  │  │     ├─ servicebus.cpython-310.pyc
│  │  │  │     │  │  │     ├─ table.cpython-310.pyc
│  │  │  │     │  │  │     ├─ timer.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ warmup.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ durable_functions.py
│  │  │  │     │  │  ├─ eventgrid.py
│  │  │  │     │  │  ├─ eventhub.py
│  │  │  │     │  │  ├─ extension
│  │  │  │     │  │  │  ├─ app_extension_base.py
│  │  │  │     │  │  │  ├─ extension_hook_meta.py
│  │  │  │     │  │  │  ├─ extension_meta.py
│  │  │  │     │  │  │  ├─ extension_scope.py
│  │  │  │     │  │  │  ├─ function_extension_exception.py
│  │  │  │     │  │  │  ├─ func_extension_base.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ app_extension_base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ extension_hook_meta.cpython-310.pyc
│  │  │  │     │  │  │     ├─ extension_meta.cpython-310.pyc
│  │  │  │     │  │  │     ├─ extension_scope.cpython-310.pyc
│  │  │  │     │  │  │     ├─ function_extension_exception.cpython-310.pyc
│  │  │  │     │  │  │     ├─ func_extension_base.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ http.py
│  │  │  │     │  │  ├─ kafka.py
│  │  │  │     │  │  ├─ meta.py
│  │  │  │     │  │  ├─ py.typed
│  │  │  │     │  │  ├─ queue.py
│  │  │  │     │  │  ├─ servicebus.py
│  │  │  │     │  │  ├─ sql.py
│  │  │  │     │  │  ├─ timer.py
│  │  │  │     │  │  ├─ warmup.py
│  │  │  │     │  │  ├─ _abc.py
│  │  │  │     │  │  ├─ _cosmosdb.py
│  │  │  │     │  │  ├─ _durable_functions.py
│  │  │  │     │  │  ├─ _eventgrid.py
│  │  │  │     │  │  ├─ _eventhub.py
│  │  │  │     │  │  ├─ _http.py
│  │  │  │     │  │  ├─ _http_asgi.py
│  │  │  │     │  │  ├─ _http_wsgi.py
│  │  │  │     │  │  ├─ _kafka.py
│  │  │  │     │  │  ├─ _queue.py
│  │  │  │     │  │  ├─ _servicebus.py
│  │  │  │     │  │  ├─ _sql.py
│  │  │  │     │  │  ├─ _thirdparty
│  │  │  │     │  │  │  ├─ typing_inspect.py
│  │  │  │     │  │  │  ├─ werkzeug
│  │  │  │     │  │  │  │  ├─ datastructures.py
│  │  │  │     │  │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  │  ├─ formparser.py
│  │  │  │     │  │  │  │  ├─ http.py
│  │  │  │     │  │  │  │  ├─ urls.py
│  │  │  │     │  │  │  │  ├─ utils.py
│  │  │  │     │  │  │  │  ├─ wsgi.py
│  │  │  │     │  │  │  │  ├─ _compat.py
│  │  │  │     │  │  │  │  ├─ _internal.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ datastructures.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ formparser.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ http.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ urls.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ wsgi.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _compat.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _internal.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ typing_inspect.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ _utils.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ blob.cpython-310.pyc
│  │  │  │     │  │     ├─ cosmosdb.cpython-310.pyc
│  │  │  │     │  │     ├─ durable_functions.cpython-310.pyc
│  │  │  │     │  │     ├─ eventgrid.cpython-310.pyc
│  │  │  │     │  │     ├─ eventhub.cpython-310.pyc
│  │  │  │     │  │     ├─ http.cpython-310.pyc
│  │  │  │     │  │     ├─ kafka.cpython-310.pyc
│  │  │  │     │  │     ├─ meta.cpython-310.pyc
│  │  │  │     │  │     ├─ queue.cpython-310.pyc
│  │  │  │     │  │     ├─ servicebus.cpython-310.pyc
│  │  │  │     │  │     ├─ sql.cpython-310.pyc
│  │  │  │     │  │     ├─ timer.cpython-310.pyc
│  │  │  │     │  │     ├─ warmup.cpython-310.pyc
│  │  │  │     │  │     ├─ _abc.cpython-310.pyc
│  │  │  │     │  │     ├─ _cosmosdb.cpython-310.pyc
│  │  │  │     │  │     ├─ _durable_functions.cpython-310.pyc
│  │  │  │     │  │     ├─ _eventgrid.cpython-310.pyc
│  │  │  │     │  │     ├─ _eventhub.cpython-310.pyc
│  │  │  │     │  │     ├─ _http.cpython-310.pyc
│  │  │  │     │  │     ├─ _http_asgi.cpython-310.pyc
│  │  │  │     │  │     ├─ _http_wsgi.cpython-310.pyc
│  │  │  │     │  │     ├─ _kafka.cpython-310.pyc
│  │  │  │     │  │     ├─ _queue.cpython-310.pyc
│  │  │  │     │  │     ├─ _servicebus.cpython-310.pyc
│  │  │  │     │  │     ├─ _sql.cpython-310.pyc
│  │  │  │     │  │     ├─ _utils.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ identity
│  │  │  │     │  │  ├─ aio
│  │  │  │     │  │  │  ├─ _bearer_token_provider.py
│  │  │  │     │  │  │  ├─ _credentials
│  │  │  │     │  │  │  │  ├─ application.py
│  │  │  │     │  │  │  │  ├─ app_service.py
│  │  │  │     │  │  │  │  ├─ authorization_code.py
│  │  │  │     │  │  │  │  ├─ azd_cli.py
│  │  │  │     │  │  │  │  ├─ azure_arc.py
│  │  │  │     │  │  │  │  ├─ azure_cli.py
│  │  │  │     │  │  │  │  ├─ azure_ml.py
│  │  │  │     │  │  │  │  ├─ azure_powershell.py
│  │  │  │     │  │  │  │  ├─ certificate.py
│  │  │  │     │  │  │  │  ├─ chained.py
│  │  │  │     │  │  │  │  ├─ client_assertion.py
│  │  │  │     │  │  │  │  ├─ client_secret.py
│  │  │  │     │  │  │  │  ├─ cloud_shell.py
│  │  │  │     │  │  │  │  ├─ default.py
│  │  │  │     │  │  │  │  ├─ environment.py
│  │  │  │     │  │  │  │  ├─ imds.py
│  │  │  │     │  │  │  │  ├─ managed_identity.py
│  │  │  │     │  │  │  │  ├─ on_behalf_of.py
│  │  │  │     │  │  │  │  ├─ service_fabric.py
│  │  │  │     │  │  │  │  ├─ shared_cache.py
│  │  │  │     │  │  │  │  ├─ vscode.py
│  │  │  │     │  │  │  │  ├─ workload_identity.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ application.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ app_service.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ authorization_code.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ azd_cli.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ azure_arc.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ azure_cli.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ azure_ml.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ azure_powershell.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ certificate.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ chained.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ client_assertion.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ client_secret.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ cloud_shell.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ default.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ environment.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ imds.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ managed_identity.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ on_behalf_of.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ service_fabric.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ shared_cache.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ vscode.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ workload_identity.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _internal
│  │  │  │     │  │  │  │  ├─ aad_client.py
│  │  │  │     │  │  │  │  ├─ decorators.py
│  │  │  │     │  │  │  │  ├─ get_token_mixin.py
│  │  │  │     │  │  │  │  ├─ managed_identity_base.py
│  │  │  │     │  │  │  │  ├─ managed_identity_client.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ aad_client.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ decorators.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ get_token_mixin.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ managed_identity_base.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ managed_identity_client.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _bearer_token_provider.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ py.typed
│  │  │  │     │  │  ├─ _auth_record.py
│  │  │  │     │  │  ├─ _bearer_token_provider.py
│  │  │  │     │  │  ├─ _constants.py
│  │  │  │     │  │  ├─ _credentials
│  │  │  │     │  │  │  ├─ application.py
│  │  │  │     │  │  │  ├─ app_service.py
│  │  │  │     │  │  │  ├─ authorization_code.py
│  │  │  │     │  │  │  ├─ azd_cli.py
│  │  │  │     │  │  │  ├─ azure_arc.py
│  │  │  │     │  │  │  ├─ azure_cli.py
│  │  │  │     │  │  │  ├─ azure_ml.py
│  │  │  │     │  │  │  ├─ azure_powershell.py
│  │  │  │     │  │  │  ├─ browser.py
│  │  │  │     │  │  │  ├─ certificate.py
│  │  │  │     │  │  │  ├─ chained.py
│  │  │  │     │  │  │  ├─ client_assertion.py
│  │  │  │     │  │  │  ├─ client_secret.py
│  │  │  │     │  │  │  ├─ cloud_shell.py
│  │  │  │     │  │  │  ├─ default.py
│  │  │  │     │  │  │  ├─ device_code.py
│  │  │  │     │  │  │  ├─ environment.py
│  │  │  │     │  │  │  ├─ imds.py
│  │  │  │     │  │  │  ├─ managed_identity.py
│  │  │  │     │  │  │  ├─ on_behalf_of.py
│  │  │  │     │  │  │  ├─ service_fabric.py
│  │  │  │     │  │  │  ├─ shared_cache.py
│  │  │  │     │  │  │  ├─ silent.py
│  │  │  │     │  │  │  ├─ user_password.py
│  │  │  │     │  │  │  ├─ vscode.py
│  │  │  │     │  │  │  ├─ workload_identity.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ application.cpython-310.pyc
│  │  │  │     │  │  │     ├─ app_service.cpython-310.pyc
│  │  │  │     │  │  │     ├─ authorization_code.cpython-310.pyc
│  │  │  │     │  │  │     ├─ azd_cli.cpython-310.pyc
│  │  │  │     │  │  │     ├─ azure_arc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ azure_cli.cpython-310.pyc
│  │  │  │     │  │  │     ├─ azure_ml.cpython-310.pyc
│  │  │  │     │  │  │     ├─ azure_powershell.cpython-310.pyc
│  │  │  │     │  │  │     ├─ browser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ certificate.cpython-310.pyc
│  │  │  │     │  │  │     ├─ chained.cpython-310.pyc
│  │  │  │     │  │  │     ├─ client_assertion.cpython-310.pyc
│  │  │  │     │  │  │     ├─ client_secret.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cloud_shell.cpython-310.pyc
│  │  │  │     │  │  │     ├─ default.cpython-310.pyc
│  │  │  │     │  │  │     ├─ device_code.cpython-310.pyc
│  │  │  │     │  │  │     ├─ environment.cpython-310.pyc
│  │  │  │     │  │  │     ├─ imds.cpython-310.pyc
│  │  │  │     │  │  │     ├─ managed_identity.cpython-310.pyc
│  │  │  │     │  │  │     ├─ on_behalf_of.cpython-310.pyc
│  │  │  │     │  │  │     ├─ service_fabric.cpython-310.pyc
│  │  │  │     │  │  │     ├─ shared_cache.cpython-310.pyc
│  │  │  │     │  │  │     ├─ silent.cpython-310.pyc
│  │  │  │     │  │  │     ├─ user_password.cpython-310.pyc
│  │  │  │     │  │  │     ├─ vscode.cpython-310.pyc
│  │  │  │     │  │  │     ├─ workload_identity.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ _enums.py
│  │  │  │     │  │  ├─ _exceptions.py
│  │  │  │     │  │  ├─ _internal
│  │  │  │     │  │  │  ├─ aadclient_certificate.py
│  │  │  │     │  │  │  ├─ aad_client.py
│  │  │  │     │  │  │  ├─ aad_client_base.py
│  │  │  │     │  │  │  ├─ auth_code_redirect_handler.py
│  │  │  │     │  │  │  ├─ client_credential_base.py
│  │  │  │     │  │  │  ├─ decorators.py
│  │  │  │     │  │  │  ├─ get_token_mixin.py
│  │  │  │     │  │  │  ├─ interactive.py
│  │  │  │     │  │  │  ├─ linux_vscode_adapter.py
│  │  │  │     │  │  │  ├─ macos_vscode_adapter.py
│  │  │  │     │  │  │  ├─ managed_identity_base.py
│  │  │  │     │  │  │  ├─ managed_identity_client.py
│  │  │  │     │  │  │  ├─ msal_client.py
│  │  │  │     │  │  │  ├─ msal_credentials.py
│  │  │  │     │  │  │  ├─ pipeline.py
│  │  │  │     │  │  │  ├─ shared_token_cache.py
│  │  │  │     │  │  │  ├─ user_agent.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ win_vscode_adapter.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ aadclient_certificate.cpython-310.pyc
│  │  │  │     │  │  │     ├─ aad_client.cpython-310.pyc
│  │  │  │     │  │  │     ├─ aad_client_base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ auth_code_redirect_handler.cpython-310.pyc
│  │  │  │     │  │  │     ├─ client_credential_base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ decorators.cpython-310.pyc
│  │  │  │     │  │  │     ├─ get_token_mixin.cpython-310.pyc
│  │  │  │     │  │  │     ├─ interactive.cpython-310.pyc
│  │  │  │     │  │  │     ├─ linux_vscode_adapter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ macos_vscode_adapter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ managed_identity_base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ managed_identity_client.cpython-310.pyc
│  │  │  │     │  │  │     ├─ msal_client.cpython-310.pyc
│  │  │  │     │  │  │     ├─ msal_credentials.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pipeline.cpython-310.pyc
│  │  │  │     │  │  │     ├─ shared_token_cache.cpython-310.pyc
│  │  │  │     │  │  │     ├─ user_agent.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ win_vscode_adapter.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ _persistent_cache.py
│  │  │  │     │  │  ├─ _version.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ _auth_record.cpython-310.pyc
│  │  │  │     │  │     ├─ _bearer_token_provider.cpython-310.pyc
│  │  │  │     │  │     ├─ _constants.cpython-310.pyc
│  │  │  │     │  │     ├─ _enums.cpython-310.pyc
│  │  │  │     │  │     ├─ _exceptions.cpython-310.pyc
│  │  │  │     │  │     ├─ _persistent_cache.cpython-310.pyc
│  │  │  │     │  │     ├─ _version.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ servicebus
│  │  │  │     │  │  ├─ aio
│  │  │  │     │  │  │  ├─ management
│  │  │  │     │  │  │  │  ├─ _management_client_async.py
│  │  │  │     │  │  │  │  ├─ _shared_key_policy_async.py
│  │  │  │     │  │  │  │  ├─ _utils.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ _management_client_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _shared_key_policy_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _utils.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _async_auto_lock_renewer.py
│  │  │  │     │  │  │  ├─ _async_utils.py
│  │  │  │     │  │  │  ├─ _base_handler_async.py
│  │  │  │     │  │  │  ├─ _servicebus_client_async.py
│  │  │  │     │  │  │  ├─ _servicebus_receiver_async.py
│  │  │  │     │  │  │  ├─ _servicebus_sender_async.py
│  │  │  │     │  │  │  ├─ _servicebus_session_async.py
│  │  │  │     │  │  │  ├─ _transport
│  │  │  │     │  │  │  │  ├─ _base_async.py
│  │  │  │     │  │  │  │  ├─ _pyamqp_transport_async.py
│  │  │  │     │  │  │  │  ├─ _uamqp_transport_async.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ _base_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _pyamqp_transport_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _uamqp_transport_async.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _async_auto_lock_renewer.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _async_utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _base_handler_async.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _servicebus_client_async.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _servicebus_receiver_async.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _servicebus_sender_async.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _servicebus_session_async.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ amqp
│  │  │  │     │  │  │  ├─ _amqp_message.py
│  │  │  │     │  │  │  ├─ _amqp_utils.py
│  │  │  │     │  │  │  ├─ _constants.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _amqp_message.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _amqp_utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _constants.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ exceptions.py
│  │  │  │     │  │  ├─ management
│  │  │  │     │  │  │  ├─ _api_version.py
│  │  │  │     │  │  │  ├─ _constants.py
│  │  │  │     │  │  │  ├─ _generated
│  │  │  │     │  │  │  │  ├─ aio
│  │  │  │     │  │  │  │  │  ├─ operations
│  │  │  │     │  │  │  │  │  │  ├─ _operations.py
│  │  │  │     │  │  │  │  │  │  ├─ _patch.py
│  │  │  │     │  │  │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │  │  │     ├─ _operations.cpython-310.pyc
│  │  │  │     │  │  │  │  │  │     ├─ _patch.cpython-310.pyc
│  │  │  │     │  │  │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  │  │  ├─ _client.py
│  │  │  │     │  │  │  │  │  ├─ _configuration.py
│  │  │  │     │  │  │  │  │  ├─ _patch.py
│  │  │  │     │  │  │  │  │  ├─ _vendor.py
│  │  │  │     │  │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │  │     ├─ _client.cpython-310.pyc
│  │  │  │     │  │  │  │  │     ├─ _configuration.cpython-310.pyc
│  │  │  │     │  │  │  │  │     ├─ _patch.cpython-310.pyc
│  │  │  │     │  │  │  │  │     ├─ _vendor.cpython-310.pyc
│  │  │  │     │  │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ models
│  │  │  │     │  │  │  │  │  ├─ _enums.py
│  │  │  │     │  │  │  │  │  ├─ _models.py
│  │  │  │     │  │  │  │  │  ├─ _patch.py
│  │  │  │     │  │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │  │     ├─ _enums.cpython-310.pyc
│  │  │  │     │  │  │  │  │     ├─ _models.cpython-310.pyc
│  │  │  │     │  │  │  │  │     ├─ _patch.cpython-310.pyc
│  │  │  │     │  │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ operations
│  │  │  │     │  │  │  │  │  ├─ _operations.py
│  │  │  │     │  │  │  │  │  ├─ _patch.py
│  │  │  │     │  │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │  │     ├─ _operations.cpython-310.pyc
│  │  │  │     │  │  │  │  │     ├─ _patch.cpython-310.pyc
│  │  │  │     │  │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ _client.py
│  │  │  │     │  │  │  │  ├─ _configuration.py
│  │  │  │     │  │  │  │  ├─ _patch.py
│  │  │  │     │  │  │  │  ├─ _serialization.py
│  │  │  │     │  │  │  │  ├─ _vendor.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ _client.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _configuration.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _patch.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _serialization.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _vendor.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _handle_response_error.py
│  │  │  │     │  │  │  ├─ _management_client.py
│  │  │  │     │  │  │  ├─ _models.py
│  │  │  │     │  │  │  ├─ _model_workaround.py
│  │  │  │     │  │  │  ├─ _shared_key_policy.py
│  │  │  │     │  │  │  ├─ _utils.py
│  │  │  │     │  │  │  ├─ _xml_workaround_policy.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _api_version.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _constants.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _handle_response_error.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _management_client.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _models.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _model_workaround.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _shared_key_policy.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _xml_workaround_policy.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ py.typed
│  │  │  │     │  │  ├─ _base_handler.py
│  │  │  │     │  │  ├─ _common
│  │  │  │     │  │  │  ├─ auto_lock_renewer.py
│  │  │  │     │  │  │  ├─ constants.py
│  │  │  │     │  │  │  ├─ message.py
│  │  │  │     │  │  │  ├─ mgmt_handlers.py
│  │  │  │     │  │  │  ├─ receiver_mixins.py
│  │  │  │     │  │  │  ├─ tracing.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ _configuration.py
│  │  │  │     │  │  │  ├─ _connection_string_parser.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ auto_lock_renewer.cpython-310.pyc
│  │  │  │     │  │  │     ├─ constants.cpython-310.pyc
│  │  │  │     │  │  │     ├─ message.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mgmt_handlers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ receiver_mixins.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tracing.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _configuration.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _connection_string_parser.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ _pyamqp
│  │  │  │     │  │  │  ├─ aio
│  │  │  │     │  │  │  │  ├─ _authentication_async.py
│  │  │  │     │  │  │  │  ├─ _cbs_async.py
│  │  │  │     │  │  │  │  ├─ _client_async.py
│  │  │  │     │  │  │  │  ├─ _connection_async.py
│  │  │  │     │  │  │  │  ├─ _link_async.py
│  │  │  │     │  │  │  │  ├─ _management_link_async.py
│  │  │  │     │  │  │  │  ├─ _management_operation_async.py
│  │  │  │     │  │  │  │  ├─ _receiver_async.py
│  │  │  │     │  │  │  │  ├─ _sasl_async.py
│  │  │  │     │  │  │  │  ├─ _sender_async.py
│  │  │  │     │  │  │  │  ├─ _session_async.py
│  │  │  │     │  │  │  │  ├─ _transport_async.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ _authentication_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _cbs_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _client_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _connection_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _link_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _management_link_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _management_operation_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _receiver_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _sasl_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _sender_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _session_async.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _transport_async.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ authentication.py
│  │  │  │     │  │  │  ├─ cbs.py
│  │  │  │     │  │  │  ├─ client.py
│  │  │  │     │  │  │  ├─ constants.py
│  │  │  │     │  │  │  ├─ endpoints.py
│  │  │  │     │  │  │  ├─ error.py
│  │  │  │     │  │  │  ├─ link.py
│  │  │  │     │  │  │  ├─ management_link.py
│  │  │  │     │  │  │  ├─ management_operation.py
│  │  │  │     │  │  │  ├─ message.py
│  │  │  │     │  │  │  ├─ outcomes.py
│  │  │  │     │  │  │  ├─ performatives.py
│  │  │  │     │  │  │  ├─ receiver.py
│  │  │  │     │  │  │  ├─ sasl.py
│  │  │  │     │  │  │  ├─ sender.py
│  │  │  │     │  │  │  ├─ session.py
│  │  │  │     │  │  │  ├─ types.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ _connection.py
│  │  │  │     │  │  │  ├─ _decode.py
│  │  │  │     │  │  │  ├─ _encode.py
│  │  │  │     │  │  │  ├─ _message_backcompat.py
│  │  │  │     │  │  │  ├─ _platform.py
│  │  │  │     │  │  │  ├─ _transport.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ authentication.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cbs.cpython-310.pyc
│  │  │  │     │  │  │     ├─ client.cpython-310.pyc
│  │  │  │     │  │  │     ├─ constants.cpython-310.pyc
│  │  │  │     │  │  │     ├─ endpoints.cpython-310.pyc
│  │  │  │     │  │  │     ├─ error.cpython-310.pyc
│  │  │  │     │  │  │     ├─ link.cpython-310.pyc
│  │  │  │     │  │  │     ├─ management_link.cpython-310.pyc
│  │  │  │     │  │  │     ├─ management_operation.cpython-310.pyc
│  │  │  │     │  │  │     ├─ message.cpython-310.pyc
│  │  │  │     │  │  │     ├─ outcomes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ performatives.cpython-310.pyc
│  │  │  │     │  │  │     ├─ receiver.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sasl.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sender.cpython-310.pyc
│  │  │  │     │  │  │     ├─ session.cpython-310.pyc
│  │  │  │     │  │  │     ├─ types.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _connection.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _decode.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _encode.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _message_backcompat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _platform.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _transport.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ _servicebus_client.py
│  │  │  │     │  │  ├─ _servicebus_receiver.py
│  │  │  │     │  │  ├─ _servicebus_sender.py
│  │  │  │     │  │  ├─ _servicebus_session.py
│  │  │  │     │  │  ├─ _transport
│  │  │  │     │  │  │  ├─ _base.py
│  │  │  │     │  │  │  ├─ _pyamqp_transport.py
│  │  │  │     │  │  │  ├─ _uamqp_transport.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _pyamqp_transport.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _uamqp_transport.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ _version.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │     ├─ _base_handler.cpython-310.pyc
│  │  │  │     │  │     ├─ _servicebus_client.cpython-310.pyc
│  │  │  │     │  │     ├─ _servicebus_receiver.cpython-310.pyc
│  │  │  │     │  │     ├─ _servicebus_sender.cpython-310.pyc
│  │  │  │     │  │     ├─ _servicebus_session.cpython-310.pyc
│  │  │  │     │  │     ├─ _version.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  └─ storage
│  │  │  │     │     └─ blob
│  │  │  │     │        ├─ aio
│  │  │  │     │        │  ├─ _blob_client_async.py
│  │  │  │     │        │  ├─ _blob_service_client_async.py
│  │  │  │     │        │  ├─ _container_client_async.py
│  │  │  │     │        │  ├─ _download_async.py
│  │  │  │     │        │  ├─ _lease_async.py
│  │  │  │     │        │  ├─ _list_blobs_helper.py
│  │  │  │     │        │  ├─ _models.py
│  │  │  │     │        │  ├─ _upload_helpers.py
│  │  │  │     │        │  ├─ __init__.py
│  │  │  │     │        │  └─ __pycache__
│  │  │  │     │        │     ├─ _blob_client_async.cpython-310.pyc
│  │  │  │     │        │     ├─ _blob_service_client_async.cpython-310.pyc
│  │  │  │     │        │     ├─ _container_client_async.cpython-310.pyc
│  │  │  │     │        │     ├─ _download_async.cpython-310.pyc
│  │  │  │     │        │     ├─ _lease_async.cpython-310.pyc
│  │  │  │     │        │     ├─ _list_blobs_helper.cpython-310.pyc
│  │  │  │     │        │     ├─ _models.cpython-310.pyc
│  │  │  │     │        │     ├─ _upload_helpers.cpython-310.pyc
│  │  │  │     │        │     └─ __init__.cpython-310.pyc
│  │  │  │     │        ├─ py.typed
│  │  │  │     │        ├─ _blob_client.py
│  │  │  │     │        ├─ _blob_service_client.py
│  │  │  │     │        ├─ _container_client.py
│  │  │  │     │        ├─ _deserialize.py
│  │  │  │     │        ├─ _download.py
│  │  │  │     │        ├─ _encryption.py
│  │  │  │     │        ├─ _generated
│  │  │  │     │        │  ├─ aio
│  │  │  │     │        │  │  ├─ operations
│  │  │  │     │        │  │  │  ├─ _append_blob_operations.py
│  │  │  │     │        │  │  │  ├─ _blob_operations.py
│  │  │  │     │        │  │  │  ├─ _block_blob_operations.py
│  │  │  │     │        │  │  │  ├─ _container_operations.py
│  │  │  │     │        │  │  │  ├─ _page_blob_operations.py
│  │  │  │     │        │  │  │  ├─ _patch.py
│  │  │  │     │        │  │  │  ├─ _service_operations.py
│  │  │  │     │        │  │  │  ├─ __init__.py
│  │  │  │     │        │  │  │  └─ __pycache__
│  │  │  │     │        │  │  │     ├─ _append_blob_operations.cpython-310.pyc
│  │  │  │     │        │  │  │     ├─ _blob_operations.cpython-310.pyc
│  │  │  │     │        │  │  │     ├─ _block_blob_operations.cpython-310.pyc
│  │  │  │     │        │  │  │     ├─ _container_operations.cpython-310.pyc
│  │  │  │     │        │  │  │     ├─ _page_blob_operations.cpython-310.pyc
│  │  │  │     │        │  │  │     ├─ _patch.cpython-310.pyc
│  │  │  │     │        │  │  │     ├─ _service_operations.cpython-310.pyc
│  │  │  │     │        │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │        │  │  ├─ _azure_blob_storage.py
│  │  │  │     │        │  │  ├─ _configuration.py
│  │  │  │     │        │  │  ├─ _patch.py
│  │  │  │     │        │  │  ├─ __init__.py
│  │  │  │     │        │  │  └─ __pycache__
│  │  │  │     │        │  │     ├─ _azure_blob_storage.cpython-310.pyc
│  │  │  │     │        │  │     ├─ _configuration.cpython-310.pyc
│  │  │  │     │        │  │     ├─ _patch.cpython-310.pyc
│  │  │  │     │        │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │        │  ├─ models
│  │  │  │     │        │  │  ├─ _azure_blob_storage_enums.py
│  │  │  │     │        │  │  ├─ _models_py3.py
│  │  │  │     │        │  │  ├─ _patch.py
│  │  │  │     │        │  │  ├─ __init__.py
│  │  │  │     │        │  │  └─ __pycache__
│  │  │  │     │        │  │     ├─ _azure_blob_storage_enums.cpython-310.pyc
│  │  │  │     │        │  │     ├─ _models_py3.cpython-310.pyc
│  │  │  │     │        │  │     ├─ _patch.cpython-310.pyc
│  │  │  │     │        │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │        │  ├─ operations
│  │  │  │     │        │  │  ├─ _append_blob_operations.py
│  │  │  │     │        │  │  ├─ _blob_operations.py
│  │  │  │     │        │  │  ├─ _block_blob_operations.py
│  │  │  │     │        │  │  ├─ _container_operations.py
│  │  │  │     │        │  │  ├─ _page_blob_operations.py
│  │  │  │     │        │  │  ├─ _patch.py
│  │  │  │     │        │  │  ├─ _service_operations.py
│  │  │  │     │        │  │  ├─ __init__.py
│  │  │  │     │        │  │  └─ __pycache__
│  │  │  │     │        │  │     ├─ _append_blob_operations.cpython-310.pyc
│  │  │  │     │        │  │     ├─ _blob_operations.cpython-310.pyc
│  │  │  │     │        │  │     ├─ _block_blob_operations.cpython-310.pyc
│  │  │  │     │        │  │     ├─ _container_operations.cpython-310.pyc
│  │  │  │     │        │  │     ├─ _page_blob_operations.cpython-310.pyc
│  │  │  │     │        │  │     ├─ _patch.cpython-310.pyc
│  │  │  │     │        │  │     ├─ _service_operations.cpython-310.pyc
│  │  │  │     │        │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │        │  ├─ _azure_blob_storage.py
│  │  │  │     │        │  ├─ _configuration.py
│  │  │  │     │        │  ├─ _patch.py
│  │  │  │     │        │  ├─ _serialization.py
│  │  │  │     │        │  ├─ _vendor.py
│  │  │  │     │        │  ├─ __init__.py
│  │  │  │     │        │  └─ __pycache__
│  │  │  │     │        │     ├─ _azure_blob_storage.cpython-310.pyc
│  │  │  │     │        │     ├─ _configuration.cpython-310.pyc
│  │  │  │     │        │     ├─ _patch.cpython-310.pyc
│  │  │  │     │        │     ├─ _serialization.cpython-310.pyc
│  │  │  │     │        │     ├─ _vendor.cpython-310.pyc
│  │  │  │     │        │     └─ __init__.cpython-310.pyc
│  │  │  │     │        ├─ _lease.py
│  │  │  │     │        ├─ _list_blobs_helper.py
│  │  │  │     │        ├─ _models.py
│  │  │  │     │        ├─ _quick_query_helper.py
│  │  │  │     │        ├─ _serialize.py
│  │  │  │     │        ├─ _shared
│  │  │  │     │        │  ├─ authentication.py
│  │  │  │     │        │  ├─ avro
│  │  │  │     │        │  │  ├─ avro_io.py
│  │  │  │     │        │  │  ├─ avro_io_async.py
│  │  │  │     │        │  │  ├─ datafile.py
│  │  │  │     │        │  │  ├─ datafile_async.py
│  │  │  │     │        │  │  ├─ schema.py
│  │  │  │     │        │  │  ├─ __init__.py
│  │  │  │     │        │  │  └─ __pycache__
│  │  │  │     │        │  │     ├─ avro_io.cpython-310.pyc
│  │  │  │     │        │  │     ├─ avro_io_async.cpython-310.pyc
│  │  │  │     │        │  │     ├─ datafile.cpython-310.pyc
│  │  │  │     │        │  │     ├─ datafile_async.cpython-310.pyc
│  │  │  │     │        │  │     ├─ schema.cpython-310.pyc
│  │  │  │     │        │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │        │  ├─ base_client.py
│  │  │  │     │        │  ├─ base_client_async.py
│  │  │  │     │        │  ├─ constants.py
│  │  │  │     │        │  ├─ models.py
│  │  │  │     │        │  ├─ parser.py
│  │  │  │     │        │  ├─ policies.py
│  │  │  │     │        │  ├─ policies_async.py
│  │  │  │     │        │  ├─ request_handlers.py
│  │  │  │     │        │  ├─ response_handlers.py
│  │  │  │     │        │  ├─ shared_access_signature.py
│  │  │  │     │        │  ├─ uploads.py
│  │  │  │     │        │  ├─ uploads_async.py
│  │  │  │     │        │  ├─ __init__.py
│  │  │  │     │        │  └─ __pycache__
│  │  │  │     │        │     ├─ authentication.cpython-310.pyc
│  │  │  │     │        │     ├─ base_client.cpython-310.pyc
│  │  │  │     │        │     ├─ base_client_async.cpython-310.pyc
│  │  │  │     │        │     ├─ constants.cpython-310.pyc
│  │  │  │     │        │     ├─ models.cpython-310.pyc
│  │  │  │     │        │     ├─ parser.cpython-310.pyc
│  │  │  │     │        │     ├─ policies.cpython-310.pyc
│  │  │  │     │        │     ├─ policies_async.cpython-310.pyc
│  │  │  │     │        │     ├─ request_handlers.cpython-310.pyc
│  │  │  │     │        │     ├─ response_handlers.cpython-310.pyc
│  │  │  │     │        │     ├─ shared_access_signature.cpython-310.pyc
│  │  │  │     │        │     ├─ uploads.cpython-310.pyc
│  │  │  │     │        │     ├─ uploads_async.cpython-310.pyc
│  │  │  │     │        │     └─ __init__.cpython-310.pyc
│  │  │  │     │        ├─ _shared_access_signature.py
│  │  │  │     │        ├─ _upload_helpers.py
│  │  │  │     │        ├─ _version.py
│  │  │  │     │        ├─ __init__.py
│  │  │  │     │        └─ __pycache__
│  │  │  │     │           ├─ _blob_client.cpython-310.pyc
│  │  │  │     │           ├─ _blob_service_client.cpython-310.pyc
│  │  │  │     │           ├─ _container_client.cpython-310.pyc
│  │  │  │     │           ├─ _deserialize.cpython-310.pyc
│  │  │  │     │           ├─ _download.cpython-310.pyc
│  │  │  │     │           ├─ _encryption.cpython-310.pyc
│  │  │  │     │           ├─ _lease.cpython-310.pyc
│  │  │  │     │           ├─ _list_blobs_helper.cpython-310.pyc
│  │  │  │     │           ├─ _models.cpython-310.pyc
│  │  │  │     │           ├─ _quick_query_helper.cpython-310.pyc
│  │  │  │     │           ├─ _serialize.cpython-310.pyc
│  │  │  │     │           ├─ _shared_access_signature.cpython-310.pyc
│  │  │  │     │           ├─ _upload_helpers.cpython-310.pyc
│  │  │  │     │           ├─ _version.cpython-310.pyc
│  │  │  │     │           └─ __init__.cpython-310.pyc
│  │  │  │     ├─ azure_core-1.29.5.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ azure_functions-1.17.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ azure_identity-1.15.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ azure_servicebus-7.11.4.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ azure_storage_blob-12.19.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ black
│  │  │  │     │  ├─ brackets.cp310-win_amd64.pyd
│  │  │  │     │  ├─ brackets.py
│  │  │  │     │  ├─ cache.cp310-win_amd64.pyd
│  │  │  │     │  ├─ cache.py
│  │  │  │     │  ├─ comments.cp310-win_amd64.pyd
│  │  │  │     │  ├─ comments.py
│  │  │  │     │  ├─ concurrency.py
│  │  │  │     │  ├─ const.cp310-win_amd64.pyd
│  │  │  │     │  ├─ const.py
│  │  │  │     │  ├─ debug.py
│  │  │  │     │  ├─ files.py
│  │  │  │     │  ├─ handle_ipynb_magics.cp310-win_amd64.pyd
│  │  │  │     │  ├─ handle_ipynb_magics.py
│  │  │  │     │  ├─ linegen.cp310-win_amd64.pyd
│  │  │  │     │  ├─ linegen.py
│  │  │  │     │  ├─ lines.cp310-win_amd64.pyd
│  │  │  │     │  ├─ lines.py
│  │  │  │     │  ├─ mode.cp310-win_amd64.pyd
│  │  │  │     │  ├─ mode.py
│  │  │  │     │  ├─ nodes.cp310-win_amd64.pyd
│  │  │  │     │  ├─ nodes.py
│  │  │  │     │  ├─ numerics.cp310-win_amd64.pyd
│  │  │  │     │  ├─ numerics.py
│  │  │  │     │  ├─ output.py
│  │  │  │     │  ├─ parsing.cp310-win_amd64.pyd
│  │  │  │     │  ├─ parsing.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ ranges.cp310-win_amd64.pyd
│  │  │  │     │  ├─ ranges.py
│  │  │  │     │  ├─ report.py
│  │  │  │     │  ├─ rusty.cp310-win_amd64.pyd
│  │  │  │     │  ├─ rusty.py
│  │  │  │     │  ├─ strings.cp310-win_amd64.pyd
│  │  │  │     │  ├─ strings.py
│  │  │  │     │  ├─ trans.cp310-win_amd64.pyd
│  │  │  │     │  ├─ trans.py
│  │  │  │     │  ├─ _width_table.cp310-win_amd64.pyd
│  │  │  │     │  ├─ _width_table.py
│  │  │  │     │  ├─ __init__.cp310-win_amd64.pyd
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ brackets.cpython-310.pyc
│  │  │  │     │     ├─ cache.cpython-310.pyc
│  │  │  │     │     ├─ comments.cpython-310.pyc
│  │  │  │     │     ├─ concurrency.cpython-310.pyc
│  │  │  │     │     ├─ const.cpython-310.pyc
│  │  │  │     │     ├─ debug.cpython-310.pyc
│  │  │  │     │     ├─ files.cpython-310.pyc
│  │  │  │     │     ├─ handle_ipynb_magics.cpython-310.pyc
│  │  │  │     │     ├─ linegen.cpython-310.pyc
│  │  │  │     │     ├─ lines.cpython-310.pyc
│  │  │  │     │     ├─ mode.cpython-310.pyc
│  │  │  │     │     ├─ nodes.cpython-310.pyc
│  │  │  │     │     ├─ numerics.cpython-310.pyc
│  │  │  │     │     ├─ output.cpython-310.pyc
│  │  │  │     │     ├─ parsing.cpython-310.pyc
│  │  │  │     │     ├─ ranges.cpython-310.pyc
│  │  │  │     │     ├─ report.cpython-310.pyc
│  │  │  │     │     ├─ rusty.cpython-310.pyc
│  │  │  │     │     ├─ strings.cpython-310.pyc
│  │  │  │     │     ├─ trans.cpython-310.pyc
│  │  │  │     │     ├─ _width_table.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ black-23.11.0.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  ├─ AUTHORS.md
│  │  │  │     │  │  └─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ blackd
│  │  │  │     │  ├─ middlewares.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ middlewares.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ blib2to3
│  │  │  │     │  ├─ Grammar.txt
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ PatternGrammar.txt
│  │  │  │     │  ├─ pgen2
│  │  │  │     │  │  ├─ conv.cp310-win_amd64.pyd
│  │  │  │     │  │  ├─ conv.py
│  │  │  │     │  │  ├─ driver.cp310-win_amd64.pyd
│  │  │  │     │  │  ├─ driver.py
│  │  │  │     │  │  ├─ grammar.cp310-win_amd64.pyd
│  │  │  │     │  │  ├─ grammar.py
│  │  │  │     │  │  ├─ literals.cp310-win_amd64.pyd
│  │  │  │     │  │  ├─ literals.py
│  │  │  │     │  │  ├─ parse.cp310-win_amd64.pyd
│  │  │  │     │  │  ├─ parse.py
│  │  │  │     │  │  ├─ pgen.cp310-win_amd64.pyd
│  │  │  │     │  │  ├─ pgen.py
│  │  │  │     │  │  ├─ token.cp310-win_amd64.pyd
│  │  │  │     │  │  ├─ token.py
│  │  │  │     │  │  ├─ tokenize.cp310-win_amd64.pyd
│  │  │  │     │  │  ├─ tokenize.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ conv.cpython-310.pyc
│  │  │  │     │  │     ├─ driver.cpython-310.pyc
│  │  │  │     │  │     ├─ grammar.cpython-310.pyc
│  │  │  │     │  │     ├─ literals.cpython-310.pyc
│  │  │  │     │  │     ├─ parse.cpython-310.pyc
│  │  │  │     │  │     ├─ pgen.cpython-310.pyc
│  │  │  │     │  │     ├─ token.cpython-310.pyc
│  │  │  │     │  │     ├─ tokenize.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ pygram.cp310-win_amd64.pyd
│  │  │  │     │  ├─ pygram.py
│  │  │  │     │  ├─ pytree.cp310-win_amd64.pyd
│  │  │  │     │  ├─ pytree.py
│  │  │  │     │  ├─ README
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ pygram.cpython-310.pyc
│  │  │  │     │     ├─ pytree.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ cerberus
│  │  │  │     │  ├─ errors.py
│  │  │  │     │  ├─ platform.py
│  │  │  │     │  ├─ schema.py
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ validator.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ errors.cpython-310.pyc
│  │  │  │     │     ├─ platform.cpython-310.pyc
│  │  │  │     │     ├─ schema.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ validator.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ Cerberus-1.3.5.dist-info
│  │  │  │     │  ├─ AUTHORS
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ certifi
│  │  │  │     │  ├─ cacert.pem
│  │  │  │     │  ├─ core.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ core.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ certifi-2023.11.17.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ cffi
│  │  │  │     │  ├─ api.py
│  │  │  │     │  ├─ backend_ctypes.py
│  │  │  │     │  ├─ cffi_opcode.py
│  │  │  │     │  ├─ commontypes.py
│  │  │  │     │  ├─ cparser.py
│  │  │  │     │  ├─ error.py
│  │  │  │     │  ├─ ffiplatform.py
│  │  │  │     │  ├─ lock.py
│  │  │  │     │  ├─ model.py
│  │  │  │     │  ├─ parse_c_type.h
│  │  │  │     │  ├─ pkgconfig.py
│  │  │  │     │  ├─ recompiler.py
│  │  │  │     │  ├─ setuptools_ext.py
│  │  │  │     │  ├─ vengine_cpy.py
│  │  │  │     │  ├─ vengine_gen.py
│  │  │  │     │  ├─ verifier.py
│  │  │  │     │  ├─ _cffi_errors.h
│  │  │  │     │  ├─ _cffi_include.h
│  │  │  │     │  ├─ _embedding.h
│  │  │  │     │  ├─ _imp_emulation.py
│  │  │  │     │  ├─ _shimmed_dist_utils.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ api.cpython-310.pyc
│  │  │  │     │     ├─ backend_ctypes.cpython-310.pyc
│  │  │  │     │     ├─ cffi_opcode.cpython-310.pyc
│  │  │  │     │     ├─ commontypes.cpython-310.pyc
│  │  │  │     │     ├─ cparser.cpython-310.pyc
│  │  │  │     │     ├─ error.cpython-310.pyc
│  │  │  │     │     ├─ ffiplatform.cpython-310.pyc
│  │  │  │     │     ├─ lock.cpython-310.pyc
│  │  │  │     │     ├─ model.cpython-310.pyc
│  │  │  │     │     ├─ pkgconfig.cpython-310.pyc
│  │  │  │     │     ├─ recompiler.cpython-310.pyc
│  │  │  │     │     ├─ setuptools_ext.cpython-310.pyc
│  │  │  │     │     ├─ vengine_cpy.cpython-310.pyc
│  │  │  │     │     ├─ vengine_gen.cpython-310.pyc
│  │  │  │     │     ├─ verifier.cpython-310.pyc
│  │  │  │     │     ├─ _imp_emulation.cpython-310.pyc
│  │  │  │     │     ├─ _shimmed_dist_utils.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ cffi-1.16.0.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ charset_normalizer
│  │  │  │     │  ├─ api.py
│  │  │  │     │  ├─ cd.py
│  │  │  │     │  ├─ cli
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  ├─ __main__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ __init__.cpython-310.pyc
│  │  │  │     │  │     └─ __main__.cpython-310.pyc
│  │  │  │     │  ├─ constant.py
│  │  │  │     │  ├─ legacy.py
│  │  │  │     │  ├─ md.cp310-win_amd64.pyd
│  │  │  │     │  ├─ md.py
│  │  │  │     │  ├─ md__mypyc.cp310-win_amd64.pyd
│  │  │  │     │  ├─ models.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ version.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ api.cpython-310.pyc
│  │  │  │     │     ├─ cd.cpython-310.pyc
│  │  │  │     │     ├─ constant.cpython-310.pyc
│  │  │  │     │     ├─ legacy.cpython-310.pyc
│  │  │  │     │     ├─ md.cpython-310.pyc
│  │  │  │     │     ├─ models.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ version.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ charset_normalizer-3.3.2.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ click
│  │  │  │     │  ├─ core.py
│  │  │  │     │  ├─ decorators.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ formatting.py
│  │  │  │     │  ├─ globals.py
│  │  │  │     │  ├─ parser.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ shell_completion.py
│  │  │  │     │  ├─ termui.py
│  │  │  │     │  ├─ testing.py
│  │  │  │     │  ├─ types.py
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ _compat.py
│  │  │  │     │  ├─ _termui_impl.py
│  │  │  │     │  ├─ _textwrap.py
│  │  │  │     │  ├─ _winconsole.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ core.cpython-310.pyc
│  │  │  │     │     ├─ decorators.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ formatting.cpython-310.pyc
│  │  │  │     │     ├─ globals.cpython-310.pyc
│  │  │  │     │     ├─ parser.cpython-310.pyc
│  │  │  │     │     ├─ shell_completion.cpython-310.pyc
│  │  │  │     │     ├─ termui.cpython-310.pyc
│  │  │  │     │     ├─ testing.cpython-310.pyc
│  │  │  │     │     ├─ types.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ _compat.cpython-310.pyc
│  │  │  │     │     ├─ _termui_impl.cpython-310.pyc
│  │  │  │     │     ├─ _textwrap.cpython-310.pyc
│  │  │  │     │     ├─ _winconsole.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ click-8.1.7.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE.rst
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ colorama
│  │  │  │     │  ├─ ansi.py
│  │  │  │     │  ├─ ansitowin32.py
│  │  │  │     │  ├─ initialise.py
│  │  │  │     │  ├─ tests
│  │  │  │     │  │  ├─ ansitowin32_test.py
│  │  │  │     │  │  ├─ ansi_test.py
│  │  │  │     │  │  ├─ initialise_test.py
│  │  │  │     │  │  ├─ isatty_test.py
│  │  │  │     │  │  ├─ utils.py
│  │  │  │     │  │  ├─ winterm_test.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ ansitowin32_test.cpython-310.pyc
│  │  │  │     │  │     ├─ ansi_test.cpython-310.pyc
│  │  │  │     │  │     ├─ initialise_test.cpython-310.pyc
│  │  │  │     │  │     ├─ isatty_test.cpython-310.pyc
│  │  │  │     │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │     ├─ winterm_test.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ win32.py
│  │  │  │     │  ├─ winterm.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ ansi.cpython-310.pyc
│  │  │  │     │     ├─ ansitowin32.cpython-310.pyc
│  │  │  │     │     ├─ initialise.cpython-310.pyc
│  │  │  │     │     ├─ win32.cpython-310.pyc
│  │  │  │     │     ├─ winterm.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ colorama-0.4.6.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  └─ LICENSE.txt
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ cryptography
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ fernet.py
│  │  │  │     │  ├─ hazmat
│  │  │  │     │  │  ├─ backends
│  │  │  │     │  │  │  ├─ openssl
│  │  │  │     │  │  │  │  ├─ aead.py
│  │  │  │     │  │  │  │  ├─ backend.py
│  │  │  │     │  │  │  │  ├─ ciphers.py
│  │  │  │     │  │  │  │  ├─ cmac.py
│  │  │  │     │  │  │  │  ├─ decode_asn1.py
│  │  │  │     │  │  │  │  ├─ ec.py
│  │  │  │     │  │  │  │  ├─ rsa.py
│  │  │  │     │  │  │  │  ├─ utils.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ aead.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ backend.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ciphers.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ cmac.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ decode_asn1.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ec.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ rsa.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ bindings
│  │  │  │     │  │  │  ├─ openssl
│  │  │  │     │  │  │  │  ├─ binding.py
│  │  │  │     │  │  │  │  ├─ _conditional.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ binding.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _conditional.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _rust
│  │  │  │     │  │  │  │  ├─ asn1.pyi
│  │  │  │     │  │  │  │  ├─ exceptions.pyi
│  │  │  │     │  │  │  │  ├─ ocsp.pyi
│  │  │  │     │  │  │  │  ├─ openssl
│  │  │  │     │  │  │  │  │  ├─ dh.pyi
│  │  │  │     │  │  │  │  │  ├─ dsa.pyi
│  │  │  │     │  │  │  │  │  ├─ ed25519.pyi
│  │  │  │     │  │  │  │  │  ├─ ed448.pyi
│  │  │  │     │  │  │  │  │  ├─ hashes.pyi
│  │  │  │     │  │  │  │  │  ├─ hmac.pyi
│  │  │  │     │  │  │  │  │  ├─ kdf.pyi
│  │  │  │     │  │  │  │  │  ├─ poly1305.pyi
│  │  │  │     │  │  │  │  │  ├─ x25519.pyi
│  │  │  │     │  │  │  │  │  ├─ x448.pyi
│  │  │  │     │  │  │  │  │  └─ __init__.pyi
│  │  │  │     │  │  │  │  ├─ pkcs7.pyi
│  │  │  │     │  │  │  │  ├─ x509.pyi
│  │  │  │     │  │  │  │  ├─ _openssl.pyi
│  │  │  │     │  │  │  │  └─ __init__.pyi
│  │  │  │     │  │  │  ├─ _rust.pyd
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ primitives
│  │  │  │     │  │  │  ├─ asymmetric
│  │  │  │     │  │  │  │  ├─ dh.py
│  │  │  │     │  │  │  │  ├─ dsa.py
│  │  │  │     │  │  │  │  ├─ ec.py
│  │  │  │     │  │  │  │  ├─ ed25519.py
│  │  │  │     │  │  │  │  ├─ ed448.py
│  │  │  │     │  │  │  │  ├─ padding.py
│  │  │  │     │  │  │  │  ├─ rsa.py
│  │  │  │     │  │  │  │  ├─ types.py
│  │  │  │     │  │  │  │  ├─ utils.py
│  │  │  │     │  │  │  │  ├─ x25519.py
│  │  │  │     │  │  │  │  ├─ x448.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ dh.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ dsa.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ec.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ed25519.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ed448.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ padding.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ rsa.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ types.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ x25519.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ x448.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ ciphers
│  │  │  │     │  │  │  │  ├─ aead.py
│  │  │  │     │  │  │  │  ├─ algorithms.py
│  │  │  │     │  │  │  │  ├─ base.py
│  │  │  │     │  │  │  │  ├─ modes.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ aead.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ algorithms.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ modes.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ cmac.py
│  │  │  │     │  │  │  ├─ constant_time.py
│  │  │  │     │  │  │  ├─ hashes.py
│  │  │  │     │  │  │  ├─ hmac.py
│  │  │  │     │  │  │  ├─ kdf
│  │  │  │     │  │  │  │  ├─ concatkdf.py
│  │  │  │     │  │  │  │  ├─ hkdf.py
│  │  │  │     │  │  │  │  ├─ kbkdf.py
│  │  │  │     │  │  │  │  ├─ pbkdf2.py
│  │  │  │     │  │  │  │  ├─ scrypt.py
│  │  │  │     │  │  │  │  ├─ x963kdf.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ concatkdf.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ hkdf.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ kbkdf.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ pbkdf2.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ scrypt.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ x963kdf.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ keywrap.py
│  │  │  │     │  │  │  ├─ padding.py
│  │  │  │     │  │  │  ├─ poly1305.py
│  │  │  │     │  │  │  ├─ serialization
│  │  │  │     │  │  │  │  ├─ base.py
│  │  │  │     │  │  │  │  ├─ pkcs12.py
│  │  │  │     │  │  │  │  ├─ pkcs7.py
│  │  │  │     │  │  │  │  ├─ ssh.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ pkcs12.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ pkcs7.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ssh.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ twofactor
│  │  │  │     │  │  │  │  ├─ hotp.py
│  │  │  │     │  │  │  │  ├─ totp.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ hotp.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ totp.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _asymmetric.py
│  │  │  │     │  │  │  ├─ _cipheralgorithm.py
│  │  │  │     │  │  │  ├─ _serialization.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ cmac.cpython-310.pyc
│  │  │  │     │  │  │     ├─ constant_time.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hashes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hmac.cpython-310.pyc
│  │  │  │     │  │  │     ├─ keywrap.cpython-310.pyc
│  │  │  │     │  │  │     ├─ padding.cpython-310.pyc
│  │  │  │     │  │  │     ├─ poly1305.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _asymmetric.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _cipheralgorithm.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _serialization.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ _oid.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ _oid.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ x509
│  │  │  │     │  │  ├─ base.py
│  │  │  │     │  │  ├─ certificate_transparency.py
│  │  │  │     │  │  ├─ extensions.py
│  │  │  │     │  │  ├─ general_name.py
│  │  │  │     │  │  ├─ name.py
│  │  │  │     │  │  ├─ ocsp.py
│  │  │  │     │  │  ├─ oid.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │     ├─ certificate_transparency.cpython-310.pyc
│  │  │  │     │  │     ├─ extensions.cpython-310.pyc
│  │  │  │     │  │     ├─ general_name.cpython-310.pyc
│  │  │  │     │  │     ├─ name.cpython-310.pyc
│  │  │  │     │  │     ├─ ocsp.cpython-310.pyc
│  │  │  │     │  │     ├─ oid.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ __about__.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ fernet.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ __about__.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ cryptography-41.0.7.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ LICENSE.APACHE
│  │  │  │     │  ├─ LICENSE.BSD
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ datamodel_code_generator
│  │  │  │     │  ├─ arguments.py
│  │  │  │     │  ├─ format.py
│  │  │  │     │  ├─ http.py
│  │  │  │     │  ├─ imports.py
│  │  │  │     │  ├─ model
│  │  │  │     │  │  ├─ base.py
│  │  │  │     │  │  ├─ dataclass.py
│  │  │  │     │  │  ├─ enum.py
│  │  │  │     │  │  ├─ imports.py
│  │  │  │     │  │  ├─ msgspec.py
│  │  │  │     │  │  ├─ pydantic
│  │  │  │     │  │  │  ├─ base_model.py
│  │  │  │     │  │  │  ├─ custom_root_type.py
│  │  │  │     │  │  │  ├─ dataclass.py
│  │  │  │     │  │  │  ├─ imports.py
│  │  │  │     │  │  │  ├─ types.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ base_model.cpython-310.pyc
│  │  │  │     │  │  │     ├─ custom_root_type.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dataclass.cpython-310.pyc
│  │  │  │     │  │  │     ├─ imports.cpython-310.pyc
│  │  │  │     │  │  │     ├─ types.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ pydantic_v2
│  │  │  │     │  │  │  ├─ base_model.py
│  │  │  │     │  │  │  ├─ imports.py
│  │  │  │     │  │  │  ├─ root_model.py
│  │  │  │     │  │  │  ├─ types.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ base_model.cpython-310.pyc
│  │  │  │     │  │  │     ├─ imports.cpython-310.pyc
│  │  │  │     │  │  │     ├─ root_model.cpython-310.pyc
│  │  │  │     │  │  │     ├─ types.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ rootmodel.py
│  │  │  │     │  │  ├─ scalar.py
│  │  │  │     │  │  ├─ template
│  │  │  │     │  │  │  ├─ dataclass.jinja2
│  │  │  │     │  │  │  ├─ Enum.jinja2
│  │  │  │     │  │  │  ├─ msgspec.jinja2
│  │  │  │     │  │  │  ├─ pydantic
│  │  │  │     │  │  │  │  ├─ BaseModel.jinja2
│  │  │  │     │  │  │  │  ├─ BaseModel_root.jinja2
│  │  │  │     │  │  │  │  ├─ Config.jinja2
│  │  │  │     │  │  │  │  └─ dataclass.jinja2
│  │  │  │     │  │  │  ├─ pydantic_v2
│  │  │  │     │  │  │  │  ├─ BaseModel.jinja2
│  │  │  │     │  │  │  │  ├─ ConfigDict.jinja2
│  │  │  │     │  │  │  │  └─ RootModel.jinja2
│  │  │  │     │  │  │  ├─ root.jinja2
│  │  │  │     │  │  │  ├─ Scalar.jinja2
│  │  │  │     │  │  │  ├─ TypedDict.jinja2
│  │  │  │     │  │  │  ├─ TypedDictClass.jinja2
│  │  │  │     │  │  │  ├─ TypedDictFunction.jinja2
│  │  │  │     │  │  │  └─ Union.jinja2
│  │  │  │     │  │  ├─ typed_dict.py
│  │  │  │     │  │  ├─ types.py
│  │  │  │     │  │  ├─ union.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │     ├─ dataclass.cpython-310.pyc
│  │  │  │     │  │     ├─ enum.cpython-310.pyc
│  │  │  │     │  │     ├─ imports.cpython-310.pyc
│  │  │  │     │  │     ├─ msgspec.cpython-310.pyc
│  │  │  │     │  │     ├─ rootmodel.cpython-310.pyc
│  │  │  │     │  │     ├─ scalar.cpython-310.pyc
│  │  │  │     │  │     ├─ typed_dict.cpython-310.pyc
│  │  │  │     │  │     ├─ types.cpython-310.pyc
│  │  │  │     │  │     ├─ union.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ parser
│  │  │  │     │  │  ├─ base.py
│  │  │  │     │  │  ├─ graphql.py
│  │  │  │     │  │  ├─ jsonschema.py
│  │  │  │     │  │  ├─ openapi.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │     ├─ graphql.cpython-310.pyc
│  │  │  │     │  │     ├─ jsonschema.cpython-310.pyc
│  │  │  │     │  │     ├─ openapi.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ reference.py
│  │  │  │     │  ├─ types.py
│  │  │  │     │  ├─ util.py
│  │  │  │     │  ├─ version.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ arguments.cpython-310.pyc
│  │  │  │     │     ├─ format.cpython-310.pyc
│  │  │  │     │     ├─ http.cpython-310.pyc
│  │  │  │     │     ├─ imports.cpython-310.pyc
│  │  │  │     │     ├─ reference.cpython-310.pyc
│  │  │  │     │     ├─ types.cpython-310.pyc
│  │  │  │     │     ├─ util.cpython-310.pyc
│  │  │  │     │     ├─ version.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ datamodel_code_generator-0.25.1.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ distlib
│  │  │  │     │  ├─ compat.py
│  │  │  │     │  ├─ database.py
│  │  │  │     │  ├─ index.py
│  │  │  │     │  ├─ locators.py
│  │  │  │     │  ├─ manifest.py
│  │  │  │     │  ├─ markers.py
│  │  │  │     │  ├─ metadata.py
│  │  │  │     │  ├─ resources.py
│  │  │  │     │  ├─ scripts.py
│  │  │  │     │  ├─ t32.exe
│  │  │  │     │  ├─ t64-arm.exe
│  │  │  │     │  ├─ t64.exe
│  │  │  │     │  ├─ util.py
│  │  │  │     │  ├─ version.py
│  │  │  │     │  ├─ w32.exe
│  │  │  │     │  ├─ w64-arm.exe
│  │  │  │     │  ├─ w64.exe
│  │  │  │     │  ├─ wheel.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ compat.cpython-310.pyc
│  │  │  │     │     ├─ database.cpython-310.pyc
│  │  │  │     │     ├─ index.cpython-310.pyc
│  │  │  │     │     ├─ locators.cpython-310.pyc
│  │  │  │     │     ├─ manifest.cpython-310.pyc
│  │  │  │     │     ├─ markers.cpython-310.pyc
│  │  │  │     │     ├─ metadata.cpython-310.pyc
│  │  │  │     │     ├─ resources.cpython-310.pyc
│  │  │  │     │     ├─ scripts.cpython-310.pyc
│  │  │  │     │     ├─ util.cpython-310.pyc
│  │  │  │     │     ├─ version.cpython-310.pyc
│  │  │  │     │     ├─ wheel.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ distlib-0.3.7.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE.txt
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ distutils-precedence.pth
│  │  │  │     ├─ dns
│  │  │  │     │  ├─ asyncbackend.py
│  │  │  │     │  ├─ asyncquery.py
│  │  │  │     │  ├─ asyncresolver.py
│  │  │  │     │  ├─ dnssec.py
│  │  │  │     │  ├─ dnssecalgs
│  │  │  │     │  │  ├─ base.py
│  │  │  │     │  │  ├─ cryptography.py
│  │  │  │     │  │  ├─ dsa.py
│  │  │  │     │  │  ├─ ecdsa.py
│  │  │  │     │  │  ├─ eddsa.py
│  │  │  │     │  │  ├─ rsa.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │     ├─ cryptography.cpython-310.pyc
│  │  │  │     │  │     ├─ dsa.cpython-310.pyc
│  │  │  │     │  │     ├─ ecdsa.cpython-310.pyc
│  │  │  │     │  │     ├─ eddsa.cpython-310.pyc
│  │  │  │     │  │     ├─ rsa.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ dnssectypes.py
│  │  │  │     │  ├─ e164.py
│  │  │  │     │  ├─ edns.py
│  │  │  │     │  ├─ entropy.py
│  │  │  │     │  ├─ enum.py
│  │  │  │     │  ├─ exception.py
│  │  │  │     │  ├─ flags.py
│  │  │  │     │  ├─ grange.py
│  │  │  │     │  ├─ immutable.py
│  │  │  │     │  ├─ inet.py
│  │  │  │     │  ├─ ipv4.py
│  │  │  │     │  ├─ ipv6.py
│  │  │  │     │  ├─ message.py
│  │  │  │     │  ├─ name.py
│  │  │  │     │  ├─ namedict.py
│  │  │  │     │  ├─ nameserver.py
│  │  │  │     │  ├─ node.py
│  │  │  │     │  ├─ opcode.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ query.py
│  │  │  │     │  ├─ quic
│  │  │  │     │  │  ├─ _asyncio.py
│  │  │  │     │  │  ├─ _common.py
│  │  │  │     │  │  ├─ _sync.py
│  │  │  │     │  │  ├─ _trio.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ _asyncio.cpython-310.pyc
│  │  │  │     │  │     ├─ _common.cpython-310.pyc
│  │  │  │     │  │     ├─ _sync.cpython-310.pyc
│  │  │  │     │  │     ├─ _trio.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ rcode.py
│  │  │  │     │  ├─ rdata.py
│  │  │  │     │  ├─ rdataclass.py
│  │  │  │     │  ├─ rdataset.py
│  │  │  │     │  ├─ rdatatype.py
│  │  │  │     │  ├─ rdtypes
│  │  │  │     │  │  ├─ ANY
│  │  │  │     │  │  │  ├─ AFSDB.py
│  │  │  │     │  │  │  ├─ AMTRELAY.py
│  │  │  │     │  │  │  ├─ AVC.py
│  │  │  │     │  │  │  ├─ CAA.py
│  │  │  │     │  │  │  ├─ CDNSKEY.py
│  │  │  │     │  │  │  ├─ CDS.py
│  │  │  │     │  │  │  ├─ CERT.py
│  │  │  │     │  │  │  ├─ CNAME.py
│  │  │  │     │  │  │  ├─ CSYNC.py
│  │  │  │     │  │  │  ├─ DLV.py
│  │  │  │     │  │  │  ├─ DNAME.py
│  │  │  │     │  │  │  ├─ DNSKEY.py
│  │  │  │     │  │  │  ├─ DS.py
│  │  │  │     │  │  │  ├─ EUI48.py
│  │  │  │     │  │  │  ├─ EUI64.py
│  │  │  │     │  │  │  ├─ GPOS.py
│  │  │  │     │  │  │  ├─ HINFO.py
│  │  │  │     │  │  │  ├─ HIP.py
│  │  │  │     │  │  │  ├─ ISDN.py
│  │  │  │     │  │  │  ├─ L32.py
│  │  │  │     │  │  │  ├─ L64.py
│  │  │  │     │  │  │  ├─ LOC.py
│  │  │  │     │  │  │  ├─ LP.py
│  │  │  │     │  │  │  ├─ MX.py
│  │  │  │     │  │  │  ├─ NID.py
│  │  │  │     │  │  │  ├─ NINFO.py
│  │  │  │     │  │  │  ├─ NS.py
│  │  │  │     │  │  │  ├─ NSEC.py
│  │  │  │     │  │  │  ├─ NSEC3.py
│  │  │  │     │  │  │  ├─ NSEC3PARAM.py
│  │  │  │     │  │  │  ├─ OPENPGPKEY.py
│  │  │  │     │  │  │  ├─ OPT.py
│  │  │  │     │  │  │  ├─ PTR.py
│  │  │  │     │  │  │  ├─ RP.py
│  │  │  │     │  │  │  ├─ RRSIG.py
│  │  │  │     │  │  │  ├─ RT.py
│  │  │  │     │  │  │  ├─ SMIMEA.py
│  │  │  │     │  │  │  ├─ SOA.py
│  │  │  │     │  │  │  ├─ SPF.py
│  │  │  │     │  │  │  ├─ SSHFP.py
│  │  │  │     │  │  │  ├─ TKEY.py
│  │  │  │     │  │  │  ├─ TLSA.py
│  │  │  │     │  │  │  ├─ TSIG.py
│  │  │  │     │  │  │  ├─ TXT.py
│  │  │  │     │  │  │  ├─ URI.py
│  │  │  │     │  │  │  ├─ X25.py
│  │  │  │     │  │  │  ├─ ZONEMD.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ AFSDB.cpython-310.pyc
│  │  │  │     │  │  │     ├─ AMTRELAY.cpython-310.pyc
│  │  │  │     │  │  │     ├─ AVC.cpython-310.pyc
│  │  │  │     │  │  │     ├─ CAA.cpython-310.pyc
│  │  │  │     │  │  │     ├─ CDNSKEY.cpython-310.pyc
│  │  │  │     │  │  │     ├─ CDS.cpython-310.pyc
│  │  │  │     │  │  │     ├─ CERT.cpython-310.pyc
│  │  │  │     │  │  │     ├─ CNAME.cpython-310.pyc
│  │  │  │     │  │  │     ├─ CSYNC.cpython-310.pyc
│  │  │  │     │  │  │     ├─ DLV.cpython-310.pyc
│  │  │  │     │  │  │     ├─ DNAME.cpython-310.pyc
│  │  │  │     │  │  │     ├─ DNSKEY.cpython-310.pyc
│  │  │  │     │  │  │     ├─ DS.cpython-310.pyc
│  │  │  │     │  │  │     ├─ EUI48.cpython-310.pyc
│  │  │  │     │  │  │     ├─ EUI64.cpython-310.pyc
│  │  │  │     │  │  │     ├─ GPOS.cpython-310.pyc
│  │  │  │     │  │  │     ├─ HINFO.cpython-310.pyc
│  │  │  │     │  │  │     ├─ HIP.cpython-310.pyc
│  │  │  │     │  │  │     ├─ ISDN.cpython-310.pyc
│  │  │  │     │  │  │     ├─ L32.cpython-310.pyc
│  │  │  │     │  │  │     ├─ L64.cpython-310.pyc
│  │  │  │     │  │  │     ├─ LOC.cpython-310.pyc
│  │  │  │     │  │  │     ├─ LP.cpython-310.pyc
│  │  │  │     │  │  │     ├─ MX.cpython-310.pyc
│  │  │  │     │  │  │     ├─ NID.cpython-310.pyc
│  │  │  │     │  │  │     ├─ NINFO.cpython-310.pyc
│  │  │  │     │  │  │     ├─ NS.cpython-310.pyc
│  │  │  │     │  │  │     ├─ NSEC.cpython-310.pyc
│  │  │  │     │  │  │     ├─ NSEC3.cpython-310.pyc
│  │  │  │     │  │  │     ├─ NSEC3PARAM.cpython-310.pyc
│  │  │  │     │  │  │     ├─ OPENPGPKEY.cpython-310.pyc
│  │  │  │     │  │  │     ├─ OPT.cpython-310.pyc
│  │  │  │     │  │  │     ├─ PTR.cpython-310.pyc
│  │  │  │     │  │  │     ├─ RP.cpython-310.pyc
│  │  │  │     │  │  │     ├─ RRSIG.cpython-310.pyc
│  │  │  │     │  │  │     ├─ RT.cpython-310.pyc
│  │  │  │     │  │  │     ├─ SMIMEA.cpython-310.pyc
│  │  │  │     │  │  │     ├─ SOA.cpython-310.pyc
│  │  │  │     │  │  │     ├─ SPF.cpython-310.pyc
│  │  │  │     │  │  │     ├─ SSHFP.cpython-310.pyc
│  │  │  │     │  │  │     ├─ TKEY.cpython-310.pyc
│  │  │  │     │  │  │     ├─ TLSA.cpython-310.pyc
│  │  │  │     │  │  │     ├─ TSIG.cpython-310.pyc
│  │  │  │     │  │  │     ├─ TXT.cpython-310.pyc
│  │  │  │     │  │  │     ├─ URI.cpython-310.pyc
│  │  │  │     │  │  │     ├─ X25.cpython-310.pyc
│  │  │  │     │  │  │     ├─ ZONEMD.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ CH
│  │  │  │     │  │  │  ├─ A.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ A.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ dnskeybase.py
│  │  │  │     │  │  ├─ dsbase.py
│  │  │  │     │  │  ├─ euibase.py
│  │  │  │     │  │  ├─ IN
│  │  │  │     │  │  │  ├─ A.py
│  │  │  │     │  │  │  ├─ AAAA.py
│  │  │  │     │  │  │  ├─ APL.py
│  │  │  │     │  │  │  ├─ DHCID.py
│  │  │  │     │  │  │  ├─ HTTPS.py
│  │  │  │     │  │  │  ├─ IPSECKEY.py
│  │  │  │     │  │  │  ├─ KX.py
│  │  │  │     │  │  │  ├─ NAPTR.py
│  │  │  │     │  │  │  ├─ NSAP.py
│  │  │  │     │  │  │  ├─ NSAP_PTR.py
│  │  │  │     │  │  │  ├─ PX.py
│  │  │  │     │  │  │  ├─ SRV.py
│  │  │  │     │  │  │  ├─ SVCB.py
│  │  │  │     │  │  │  ├─ WKS.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ A.cpython-310.pyc
│  │  │  │     │  │  │     ├─ AAAA.cpython-310.pyc
│  │  │  │     │  │  │     ├─ APL.cpython-310.pyc
│  │  │  │     │  │  │     ├─ DHCID.cpython-310.pyc
│  │  │  │     │  │  │     ├─ HTTPS.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IPSECKEY.cpython-310.pyc
│  │  │  │     │  │  │     ├─ KX.cpython-310.pyc
│  │  │  │     │  │  │     ├─ NAPTR.cpython-310.pyc
│  │  │  │     │  │  │     ├─ NSAP.cpython-310.pyc
│  │  │  │     │  │  │     ├─ NSAP_PTR.cpython-310.pyc
│  │  │  │     │  │  │     ├─ PX.cpython-310.pyc
│  │  │  │     │  │  │     ├─ SRV.cpython-310.pyc
│  │  │  │     │  │  │     ├─ SVCB.cpython-310.pyc
│  │  │  │     │  │  │     ├─ WKS.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ mxbase.py
│  │  │  │     │  │  ├─ nsbase.py
│  │  │  │     │  │  ├─ svcbbase.py
│  │  │  │     │  │  ├─ tlsabase.py
│  │  │  │     │  │  ├─ txtbase.py
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ dnskeybase.cpython-310.pyc
│  │  │  │     │  │     ├─ dsbase.cpython-310.pyc
│  │  │  │     │  │     ├─ euibase.cpython-310.pyc
│  │  │  │     │  │     ├─ mxbase.cpython-310.pyc
│  │  │  │     │  │     ├─ nsbase.cpython-310.pyc
│  │  │  │     │  │     ├─ svcbbase.cpython-310.pyc
│  │  │  │     │  │     ├─ tlsabase.cpython-310.pyc
│  │  │  │     │  │     ├─ txtbase.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ renderer.py
│  │  │  │     │  ├─ resolver.py
│  │  │  │     │  ├─ reversename.py
│  │  │  │     │  ├─ rrset.py
│  │  │  │     │  ├─ serial.py
│  │  │  │     │  ├─ set.py
│  │  │  │     │  ├─ tokenizer.py
│  │  │  │     │  ├─ transaction.py
│  │  │  │     │  ├─ tsig.py
│  │  │  │     │  ├─ tsigkeyring.py
│  │  │  │     │  ├─ ttl.py
│  │  │  │     │  ├─ update.py
│  │  │  │     │  ├─ version.py
│  │  │  │     │  ├─ versioned.py
│  │  │  │     │  ├─ win32util.py
│  │  │  │     │  ├─ wire.py
│  │  │  │     │  ├─ xfr.py
│  │  │  │     │  ├─ zone.py
│  │  │  │     │  ├─ zonefile.py
│  │  │  │     │  ├─ zonetypes.py
│  │  │  │     │  ├─ _asyncbackend.py
│  │  │  │     │  ├─ _asyncio_backend.py
│  │  │  │     │  ├─ _ddr.py
│  │  │  │     │  ├─ _immutable_ctx.py
│  │  │  │     │  ├─ _trio_backend.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ asyncbackend.cpython-310.pyc
│  │  │  │     │     ├─ asyncquery.cpython-310.pyc
│  │  │  │     │     ├─ asyncresolver.cpython-310.pyc
│  │  │  │     │     ├─ dnssec.cpython-310.pyc
│  │  │  │     │     ├─ dnssectypes.cpython-310.pyc
│  │  │  │     │     ├─ e164.cpython-310.pyc
│  │  │  │     │     ├─ edns.cpython-310.pyc
│  │  │  │     │     ├─ entropy.cpython-310.pyc
│  │  │  │     │     ├─ enum.cpython-310.pyc
│  │  │  │     │     ├─ exception.cpython-310.pyc
│  │  │  │     │     ├─ flags.cpython-310.pyc
│  │  │  │     │     ├─ grange.cpython-310.pyc
│  │  │  │     │     ├─ immutable.cpython-310.pyc
│  │  │  │     │     ├─ inet.cpython-310.pyc
│  │  │  │     │     ├─ ipv4.cpython-310.pyc
│  │  │  │     │     ├─ ipv6.cpython-310.pyc
│  │  │  │     │     ├─ message.cpython-310.pyc
│  │  │  │     │     ├─ name.cpython-310.pyc
│  │  │  │     │     ├─ namedict.cpython-310.pyc
│  │  │  │     │     ├─ nameserver.cpython-310.pyc
│  │  │  │     │     ├─ node.cpython-310.pyc
│  │  │  │     │     ├─ opcode.cpython-310.pyc
│  │  │  │     │     ├─ query.cpython-310.pyc
│  │  │  │     │     ├─ rcode.cpython-310.pyc
│  │  │  │     │     ├─ rdata.cpython-310.pyc
│  │  │  │     │     ├─ rdataclass.cpython-310.pyc
│  │  │  │     │     ├─ rdataset.cpython-310.pyc
│  │  │  │     │     ├─ rdatatype.cpython-310.pyc
│  │  │  │     │     ├─ renderer.cpython-310.pyc
│  │  │  │     │     ├─ resolver.cpython-310.pyc
│  │  │  │     │     ├─ reversename.cpython-310.pyc
│  │  │  │     │     ├─ rrset.cpython-310.pyc
│  │  │  │     │     ├─ serial.cpython-310.pyc
│  │  │  │     │     ├─ set.cpython-310.pyc
│  │  │  │     │     ├─ tokenizer.cpython-310.pyc
│  │  │  │     │     ├─ transaction.cpython-310.pyc
│  │  │  │     │     ├─ tsig.cpython-310.pyc
│  │  │  │     │     ├─ tsigkeyring.cpython-310.pyc
│  │  │  │     │     ├─ ttl.cpython-310.pyc
│  │  │  │     │     ├─ update.cpython-310.pyc
│  │  │  │     │     ├─ version.cpython-310.pyc
│  │  │  │     │     ├─ versioned.cpython-310.pyc
│  │  │  │     │     ├─ win32util.cpython-310.pyc
│  │  │  │     │     ├─ wire.cpython-310.pyc
│  │  │  │     │     ├─ xfr.cpython-310.pyc
│  │  │  │     │     ├─ zone.cpython-310.pyc
│  │  │  │     │     ├─ zonefile.cpython-310.pyc
│  │  │  │     │     ├─ zonetypes.cpython-310.pyc
│  │  │  │     │     ├─ _asyncbackend.cpython-310.pyc
│  │  │  │     │     ├─ _asyncio_backend.cpython-310.pyc
│  │  │  │     │     ├─ _ddr.cpython-310.pyc
│  │  │  │     │     ├─ _immutable_ctx.cpython-310.pyc
│  │  │  │     │     ├─ _trio_backend.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ dnspython-2.4.2.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ docopt-0.6.2-py3.10.egg-info
│  │  │  │     │  ├─ dependency_links.txt
│  │  │  │     │  ├─ installed-files.txt
│  │  │  │     │  ├─ PKG-INFO
│  │  │  │     │  ├─ SOURCES.txt
│  │  │  │     │  └─ top_level.txt
│  │  │  │     ├─ docopt.py
│  │  │  │     ├─ email_validator
│  │  │  │     │  ├─ deliverability.py
│  │  │  │     │  ├─ exceptions_types.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ rfc_constants.py
│  │  │  │     │  ├─ syntax.py
│  │  │  │     │  ├─ validate_email.py
│  │  │  │     │  ├─ version.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ deliverability.cpython-310.pyc
│  │  │  │     │     ├─ exceptions_types.cpython-310.pyc
│  │  │  │     │     ├─ rfc_constants.cpython-310.pyc
│  │  │  │     │     ├─ syntax.cpython-310.pyc
│  │  │  │     │     ├─ validate_email.cpython-310.pyc
│  │  │  │     │     ├─ version.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ email_validator-2.1.0.post1.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ exceptiongroup
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ _catch.py
│  │  │  │     │  ├─ _exceptions.py
│  │  │  │     │  ├─ _formatting.py
│  │  │  │     │  ├─ _suppress.py
│  │  │  │     │  ├─ _version.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ _catch.cpython-310.pyc
│  │  │  │     │     ├─ _exceptions.cpython-310.pyc
│  │  │  │     │     ├─ _formatting.cpython-310.pyc
│  │  │  │     │     ├─ _suppress.cpython-310.pyc
│  │  │  │     │     ├─ _version.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ exceptiongroup-1.2.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ genson
│  │  │  │     │  ├─ cli.py
│  │  │  │     │  ├─ schema
│  │  │  │     │  │  ├─ builder.py
│  │  │  │     │  │  ├─ node.py
│  │  │  │     │  │  ├─ strategies
│  │  │  │     │  │  │  ├─ array.py
│  │  │  │     │  │  │  ├─ base.py
│  │  │  │     │  │  │  ├─ object.py
│  │  │  │     │  │  │  ├─ scalar.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ array.cpython-310.pyc
│  │  │  │     │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ object.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scalar.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ builder.cpython-310.pyc
│  │  │  │     │  │     ├─ node.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ cli.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ genson-1.2.2-py3.10.egg-info
│  │  │  │     │  ├─ dependency_links.txt
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ installed-files.txt
│  │  │  │     │  ├─ PKG-INFO
│  │  │  │     │  ├─ SOURCES.txt
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ zip-safe
│  │  │  │     ├─ h11
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ tests
│  │  │  │     │  │  ├─ data
│  │  │  │     │  │  │  └─ test-file
│  │  │  │     │  │  ├─ helpers.py
│  │  │  │     │  │  ├─ test_against_stdlib_http.py
│  │  │  │     │  │  ├─ test_connection.py
│  │  │  │     │  │  ├─ test_events.py
│  │  │  │     │  │  ├─ test_headers.py
│  │  │  │     │  │  ├─ test_helpers.py
│  │  │  │     │  │  ├─ test_io.py
│  │  │  │     │  │  ├─ test_receivebuffer.py
│  │  │  │     │  │  ├─ test_state.py
│  │  │  │     │  │  ├─ test_util.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ helpers.cpython-310.pyc
│  │  │  │     │  │     ├─ test_against_stdlib_http.cpython-310.pyc
│  │  │  │     │  │     ├─ test_connection.cpython-310.pyc
│  │  │  │     │  │     ├─ test_events.cpython-310.pyc
│  │  │  │     │  │     ├─ test_headers.cpython-310.pyc
│  │  │  │     │  │     ├─ test_helpers.cpython-310.pyc
│  │  │  │     │  │     ├─ test_io.cpython-310.pyc
│  │  │  │     │  │     ├─ test_receivebuffer.cpython-310.pyc
│  │  │  │     │  │     ├─ test_state.cpython-310.pyc
│  │  │  │     │  │     ├─ test_util.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _abnf.py
│  │  │  │     │  ├─ _connection.py
│  │  │  │     │  ├─ _events.py
│  │  │  │     │  ├─ _headers.py
│  │  │  │     │  ├─ _readers.py
│  │  │  │     │  ├─ _receivebuffer.py
│  │  │  │     │  ├─ _state.py
│  │  │  │     │  ├─ _util.py
│  │  │  │     │  ├─ _version.py
│  │  │  │     │  ├─ _writers.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ _abnf.cpython-310.pyc
│  │  │  │     │     ├─ _connection.cpython-310.pyc
│  │  │  │     │     ├─ _events.cpython-310.pyc
│  │  │  │     │     ├─ _headers.cpython-310.pyc
│  │  │  │     │     ├─ _readers.cpython-310.pyc
│  │  │  │     │     ├─ _receivebuffer.cpython-310.pyc
│  │  │  │     │     ├─ _state.cpython-310.pyc
│  │  │  │     │     ├─ _util.cpython-310.pyc
│  │  │  │     │     ├─ _version.cpython-310.pyc
│  │  │  │     │     ├─ _writers.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ h11-0.14.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE.txt
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ httpcore
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ _api.py
│  │  │  │     │  ├─ _async
│  │  │  │     │  │  ├─ connection.py
│  │  │  │     │  │  ├─ connection_pool.py
│  │  │  │     │  │  ├─ http11.py
│  │  │  │     │  │  ├─ http2.py
│  │  │  │     │  │  ├─ http_proxy.py
│  │  │  │     │  │  ├─ interfaces.py
│  │  │  │     │  │  ├─ socks_proxy.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ connection.cpython-310.pyc
│  │  │  │     │  │     ├─ connection_pool.cpython-310.pyc
│  │  │  │     │  │     ├─ http11.cpython-310.pyc
│  │  │  │     │  │     ├─ http2.cpython-310.pyc
│  │  │  │     │  │     ├─ http_proxy.cpython-310.pyc
│  │  │  │     │  │     ├─ interfaces.cpython-310.pyc
│  │  │  │     │  │     ├─ socks_proxy.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _backends
│  │  │  │     │  │  ├─ anyio.py
│  │  │  │     │  │  ├─ auto.py
│  │  │  │     │  │  ├─ base.py
│  │  │  │     │  │  ├─ mock.py
│  │  │  │     │  │  ├─ sync.py
│  │  │  │     │  │  ├─ trio.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ anyio.cpython-310.pyc
│  │  │  │     │  │     ├─ auto.cpython-310.pyc
│  │  │  │     │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │     ├─ mock.cpython-310.pyc
│  │  │  │     │  │     ├─ sync.cpython-310.pyc
│  │  │  │     │  │     ├─ trio.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _exceptions.py
│  │  │  │     │  ├─ _models.py
│  │  │  │     │  ├─ _ssl.py
│  │  │  │     │  ├─ _sync
│  │  │  │     │  │  ├─ connection.py
│  │  │  │     │  │  ├─ connection_pool.py
│  │  │  │     │  │  ├─ http11.py
│  │  │  │     │  │  ├─ http2.py
│  │  │  │     │  │  ├─ http_proxy.py
│  │  │  │     │  │  ├─ interfaces.py
│  │  │  │     │  │  ├─ socks_proxy.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ connection.cpython-310.pyc
│  │  │  │     │  │     ├─ connection_pool.cpython-310.pyc
│  │  │  │     │  │     ├─ http11.cpython-310.pyc
│  │  │  │     │  │     ├─ http2.cpython-310.pyc
│  │  │  │     │  │     ├─ http_proxy.cpython-310.pyc
│  │  │  │     │  │     ├─ interfaces.cpython-310.pyc
│  │  │  │     │  │     ├─ socks_proxy.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _synchronization.py
│  │  │  │     │  ├─ _trace.py
│  │  │  │     │  ├─ _utils.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ _api.cpython-310.pyc
│  │  │  │     │     ├─ _exceptions.cpython-310.pyc
│  │  │  │     │     ├─ _models.cpython-310.pyc
│  │  │  │     │     ├─ _ssl.cpython-310.pyc
│  │  │  │     │     ├─ _synchronization.cpython-310.pyc
│  │  │  │     │     ├─ _trace.cpython-310.pyc
│  │  │  │     │     ├─ _utils.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ httpcore-1.0.2.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  └─ LICENSE.md
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ httpx
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ _api.py
│  │  │  │     │  ├─ _auth.py
│  │  │  │     │  ├─ _client.py
│  │  │  │     │  ├─ _compat.py
│  │  │  │     │  ├─ _config.py
│  │  │  │     │  ├─ _content.py
│  │  │  │     │  ├─ _decoders.py
│  │  │  │     │  ├─ _exceptions.py
│  │  │  │     │  ├─ _main.py
│  │  │  │     │  ├─ _models.py
│  │  │  │     │  ├─ _multipart.py
│  │  │  │     │  ├─ _status_codes.py
│  │  │  │     │  ├─ _transports
│  │  │  │     │  │  ├─ asgi.py
│  │  │  │     │  │  ├─ base.py
│  │  │  │     │  │  ├─ default.py
│  │  │  │     │  │  ├─ mock.py
│  │  │  │     │  │  ├─ wsgi.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ asgi.cpython-310.pyc
│  │  │  │     │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │     ├─ default.cpython-310.pyc
│  │  │  │     │  │     ├─ mock.cpython-310.pyc
│  │  │  │     │  │     ├─ wsgi.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _types.py
│  │  │  │     │  ├─ _urlparse.py
│  │  │  │     │  ├─ _urls.py
│  │  │  │     │  ├─ _utils.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __pycache__
│  │  │  │     │  │  ├─ _api.cpython-310.pyc
│  │  │  │     │  │  ├─ _auth.cpython-310.pyc
│  │  │  │     │  │  ├─ _client.cpython-310.pyc
│  │  │  │     │  │  ├─ _compat.cpython-310.pyc
│  │  │  │     │  │  ├─ _config.cpython-310.pyc
│  │  │  │     │  │  ├─ _content.cpython-310.pyc
│  │  │  │     │  │  ├─ _decoders.cpython-310.pyc
│  │  │  │     │  │  ├─ _exceptions.cpython-310.pyc
│  │  │  │     │  │  ├─ _main.cpython-310.pyc
│  │  │  │     │  │  ├─ _models.cpython-310.pyc
│  │  │  │     │  │  ├─ _multipart.cpython-310.pyc
│  │  │  │     │  │  ├─ _status_codes.cpython-310.pyc
│  │  │  │     │  │  ├─ _types.cpython-310.pyc
│  │  │  │     │  │  ├─ _urlparse.cpython-310.pyc
│  │  │  │     │  │  ├─ _urls.cpython-310.pyc
│  │  │  │     │  │  ├─ _utils.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  └─ __version__.cpython-310.pyc
│  │  │  │     │  └─ __version__.py
│  │  │  │     ├─ httpx-0.25.2.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  └─ LICENSE.md
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ idna
│  │  │  │     │  ├─ codec.py
│  │  │  │     │  ├─ compat.py
│  │  │  │     │  ├─ core.py
│  │  │  │     │  ├─ idnadata.py
│  │  │  │     │  ├─ intranges.py
│  │  │  │     │  ├─ package_data.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ uts46data.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ codec.cpython-310.pyc
│  │  │  │     │     ├─ compat.cpython-310.pyc
│  │  │  │     │     ├─ core.cpython-310.pyc
│  │  │  │     │     ├─ idnadata.cpython-310.pyc
│  │  │  │     │     ├─ intranges.cpython-310.pyc
│  │  │  │     │     ├─ package_data.cpython-310.pyc
│  │  │  │     │     ├─ uts46data.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ idna-3.6.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE.md
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ inflect
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ inflect-5.6.2.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ isapi
│  │  │  │     │  ├─ doc
│  │  │  │     │  │  └─ isapi.html
│  │  │  │     │  ├─ install.py
│  │  │  │     │  ├─ isapicon.py
│  │  │  │     │  ├─ PyISAPI_loader.dll
│  │  │  │     │  ├─ README.txt
│  │  │  │     │  ├─ samples
│  │  │  │     │  │  ├─ advanced.py
│  │  │  │     │  │  ├─ README.txt
│  │  │  │     │  │  ├─ redirector.py
│  │  │  │     │  │  ├─ redirector_asynch.py
│  │  │  │     │  │  ├─ redirector_with_filter.py
│  │  │  │     │  │  ├─ test.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ advanced.cpython-310.pyc
│  │  │  │     │  │     ├─ redirector.cpython-310.pyc
│  │  │  │     │  │     ├─ redirector_asynch.cpython-310.pyc
│  │  │  │     │  │     ├─ redirector_with_filter.cpython-310.pyc
│  │  │  │     │  │     └─ test.cpython-310.pyc
│  │  │  │     │  ├─ simple.py
│  │  │  │     │  ├─ test
│  │  │  │     │  │  ├─ extension_simple.py
│  │  │  │     │  │  ├─ README.txt
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ extension_simple.cpython-310.pyc
│  │  │  │     │  ├─ threaded_extension.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ install.cpython-310.pyc
│  │  │  │     │     ├─ isapicon.cpython-310.pyc
│  │  │  │     │     ├─ simple.cpython-310.pyc
│  │  │  │     │     ├─ threaded_extension.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ iso8601
│  │  │  │     │  ├─ iso8601.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ test_iso8601.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ iso8601.cpython-310.pyc
│  │  │  │     │     ├─ test_iso8601.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ iso8601-2.1.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ isodate
│  │  │  │     │  ├─ duration.py
│  │  │  │     │  ├─ isodates.py
│  │  │  │     │  ├─ isodatetime.py
│  │  │  │     │  ├─ isoduration.py
│  │  │  │     │  ├─ isoerror.py
│  │  │  │     │  ├─ isostrf.py
│  │  │  │     │  ├─ isotime.py
│  │  │  │     │  ├─ isotzinfo.py
│  │  │  │     │  ├─ tests
│  │  │  │     │  │  ├─ test_date.py
│  │  │  │     │  │  ├─ test_datetime.py
│  │  │  │     │  │  ├─ test_duration.py
│  │  │  │     │  │  ├─ test_pickle.py
│  │  │  │     │  │  ├─ test_strf.py
│  │  │  │     │  │  ├─ test_time.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ test_date.cpython-310.pyc
│  │  │  │     │  │     ├─ test_datetime.cpython-310.pyc
│  │  │  │     │  │     ├─ test_duration.cpython-310.pyc
│  │  │  │     │  │     ├─ test_pickle.cpython-310.pyc
│  │  │  │     │  │     ├─ test_strf.cpython-310.pyc
│  │  │  │     │  │     ├─ test_time.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ tzinfo.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ duration.cpython-310.pyc
│  │  │  │     │     ├─ isodates.cpython-310.pyc
│  │  │  │     │     ├─ isodatetime.cpython-310.pyc
│  │  │  │     │     ├─ isoduration.cpython-310.pyc
│  │  │  │     │     ├─ isoerror.cpython-310.pyc
│  │  │  │     │     ├─ isostrf.cpython-310.pyc
│  │  │  │     │     ├─ isotime.cpython-310.pyc
│  │  │  │     │     ├─ isotzinfo.cpython-310.pyc
│  │  │  │     │     ├─ tzinfo.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ isodate-0.6.1.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ isort
│  │  │  │     │  ├─ api.py
│  │  │  │     │  ├─ comments.py
│  │  │  │     │  ├─ core.py
│  │  │  │     │  ├─ deprecated
│  │  │  │     │  │  ├─ finders.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ finders.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ files.py
│  │  │  │     │  ├─ format.py
│  │  │  │     │  ├─ identify.py
│  │  │  │     │  ├─ io.py
│  │  │  │     │  ├─ literal.py
│  │  │  │     │  ├─ logo.py
│  │  │  │     │  ├─ main.py
│  │  │  │     │  ├─ output.py
│  │  │  │     │  ├─ parse.py
│  │  │  │     │  ├─ place.py
│  │  │  │     │  ├─ profiles.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ pylama_isort.py
│  │  │  │     │  ├─ sections.py
│  │  │  │     │  ├─ settings.py
│  │  │  │     │  ├─ setuptools_commands.py
│  │  │  │     │  ├─ sorting.py
│  │  │  │     │  ├─ stdlibs
│  │  │  │     │  │  ├─ all.py
│  │  │  │     │  │  ├─ py2.py
│  │  │  │     │  │  ├─ py27.py
│  │  │  │     │  │  ├─ py3.py
│  │  │  │     │  │  ├─ py310.py
│  │  │  │     │  │  ├─ py311.py
│  │  │  │     │  │  ├─ py312.py
│  │  │  │     │  │  ├─ py36.py
│  │  │  │     │  │  ├─ py37.py
│  │  │  │     │  │  ├─ py38.py
│  │  │  │     │  │  ├─ py39.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ all.cpython-310.pyc
│  │  │  │     │  │     ├─ py2.cpython-310.pyc
│  │  │  │     │  │     ├─ py27.cpython-310.pyc
│  │  │  │     │  │     ├─ py3.cpython-310.pyc
│  │  │  │     │  │     ├─ py310.cpython-310.pyc
│  │  │  │     │  │     ├─ py311.cpython-310.pyc
│  │  │  │     │  │     ├─ py312.cpython-310.pyc
│  │  │  │     │  │     ├─ py36.cpython-310.pyc
│  │  │  │     │  │     ├─ py37.cpython-310.pyc
│  │  │  │     │  │     ├─ py38.cpython-310.pyc
│  │  │  │     │  │     ├─ py39.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ wrap.py
│  │  │  │     │  ├─ wrap_modes.py
│  │  │  │     │  ├─ _vendored
│  │  │  │     │  │  └─ tomli
│  │  │  │     │  │     ├─ LICENSE
│  │  │  │     │  │     ├─ py.typed
│  │  │  │     │  │     ├─ _parser.py
│  │  │  │     │  │     ├─ _re.py
│  │  │  │     │  │     ├─ __init__.py
│  │  │  │     │  │     └─ __pycache__
│  │  │  │     │  │        ├─ _parser.cpython-310.pyc
│  │  │  │     │  │        ├─ _re.cpython-310.pyc
│  │  │  │     │  │        └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _version.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ api.cpython-310.pyc
│  │  │  │     │     ├─ comments.cpython-310.pyc
│  │  │  │     │     ├─ core.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ files.cpython-310.pyc
│  │  │  │     │     ├─ format.cpython-310.pyc
│  │  │  │     │     ├─ identify.cpython-310.pyc
│  │  │  │     │     ├─ io.cpython-310.pyc
│  │  │  │     │     ├─ literal.cpython-310.pyc
│  │  │  │     │     ├─ logo.cpython-310.pyc
│  │  │  │     │     ├─ main.cpython-310.pyc
│  │  │  │     │     ├─ output.cpython-310.pyc
│  │  │  │     │     ├─ parse.cpython-310.pyc
│  │  │  │     │     ├─ place.cpython-310.pyc
│  │  │  │     │     ├─ profiles.cpython-310.pyc
│  │  │  │     │     ├─ pylama_isort.cpython-310.pyc
│  │  │  │     │     ├─ sections.cpython-310.pyc
│  │  │  │     │     ├─ settings.cpython-310.pyc
│  │  │  │     │     ├─ setuptools_commands.cpython-310.pyc
│  │  │  │     │     ├─ sorting.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ wrap.cpython-310.pyc
│  │  │  │     │     ├─ wrap_modes.cpython-310.pyc
│  │  │  │     │     ├─ _version.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ isort-5.13.0.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ jinja2
│  │  │  │     │  ├─ async_utils.py
│  │  │  │     │  ├─ bccache.py
│  │  │  │     │  ├─ compiler.py
│  │  │  │     │  ├─ constants.py
│  │  │  │     │  ├─ debug.py
│  │  │  │     │  ├─ defaults.py
│  │  │  │     │  ├─ environment.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ ext.py
│  │  │  │     │  ├─ filters.py
│  │  │  │     │  ├─ idtracking.py
│  │  │  │     │  ├─ lexer.py
│  │  │  │     │  ├─ loaders.py
│  │  │  │     │  ├─ meta.py
│  │  │  │     │  ├─ nativetypes.py
│  │  │  │     │  ├─ nodes.py
│  │  │  │     │  ├─ optimizer.py
│  │  │  │     │  ├─ parser.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ runtime.py
│  │  │  │     │  ├─ sandbox.py
│  │  │  │     │  ├─ tests.py
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ visitor.py
│  │  │  │     │  ├─ _identifier.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ async_utils.cpython-310.pyc
│  │  │  │     │     ├─ bccache.cpython-310.pyc
│  │  │  │     │     ├─ compiler.cpython-310.pyc
│  │  │  │     │     ├─ constants.cpython-310.pyc
│  │  │  │     │     ├─ debug.cpython-310.pyc
│  │  │  │     │     ├─ defaults.cpython-310.pyc
│  │  │  │     │     ├─ environment.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ ext.cpython-310.pyc
│  │  │  │     │     ├─ filters.cpython-310.pyc
│  │  │  │     │     ├─ idtracking.cpython-310.pyc
│  │  │  │     │     ├─ lexer.cpython-310.pyc
│  │  │  │     │     ├─ loaders.cpython-310.pyc
│  │  │  │     │     ├─ meta.cpython-310.pyc
│  │  │  │     │     ├─ nativetypes.cpython-310.pyc
│  │  │  │     │     ├─ nodes.cpython-310.pyc
│  │  │  │     │     ├─ optimizer.cpython-310.pyc
│  │  │  │     │     ├─ parser.cpython-310.pyc
│  │  │  │     │     ├─ runtime.cpython-310.pyc
│  │  │  │     │     ├─ sandbox.cpython-310.pyc
│  │  │  │     │     ├─ tests.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ visitor.cpython-310.pyc
│  │  │  │     │     ├─ _identifier.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ Jinja2-3.1.2.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE.rst
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ jsonc_parser
│  │  │  │     │  ├─ errors.py
│  │  │  │     │  ├─ parser.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ errors.cpython-310.pyc
│  │  │  │     │     ├─ parser.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ jsonc_parser-1.1.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE.txt
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ jsonschema
│  │  │  │     │  ├─ benchmarks
│  │  │  │     │  │  ├─ issue232
│  │  │  │     │  │  │  └─ issue.json
│  │  │  │     │  │  ├─ issue232.py
│  │  │  │     │  │  ├─ json_schema_test_suite.py
│  │  │  │     │  │  ├─ nested_schemas.py
│  │  │  │     │  │  ├─ subcomponents.py
│  │  │  │     │  │  ├─ unused_registry.py
│  │  │  │     │  │  ├─ validator_creation.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ issue232.cpython-310.pyc
│  │  │  │     │  │     ├─ json_schema_test_suite.cpython-310.pyc
│  │  │  │     │  │     ├─ nested_schemas.cpython-310.pyc
│  │  │  │     │  │     ├─ subcomponents.cpython-310.pyc
│  │  │  │     │  │     ├─ unused_registry.cpython-310.pyc
│  │  │  │     │  │     ├─ validator_creation.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ cli.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ protocols.py
│  │  │  │     │  ├─ tests
│  │  │  │     │  │  ├─ fuzz_validate.py
│  │  │  │     │  │  ├─ test_cli.py
│  │  │  │     │  │  ├─ test_deprecations.py
│  │  │  │     │  │  ├─ test_exceptions.py
│  │  │  │     │  │  ├─ test_format.py
│  │  │  │     │  │  ├─ test_jsonschema_test_suite.py
│  │  │  │     │  │  ├─ test_types.py
│  │  │  │     │  │  ├─ test_utils.py
│  │  │  │     │  │  ├─ test_validators.py
│  │  │  │     │  │  ├─ _suite.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ fuzz_validate.cpython-310.pyc
│  │  │  │     │  │     ├─ test_cli.cpython-310.pyc
│  │  │  │     │  │     ├─ test_deprecations.cpython-310.pyc
│  │  │  │     │  │     ├─ test_exceptions.cpython-310.pyc
│  │  │  │     │  │     ├─ test_format.cpython-310.pyc
│  │  │  │     │  │     ├─ test_jsonschema_test_suite.cpython-310.pyc
│  │  │  │     │  │     ├─ test_types.cpython-310.pyc
│  │  │  │     │  │     ├─ test_utils.cpython-310.pyc
│  │  │  │     │  │     ├─ test_validators.cpython-310.pyc
│  │  │  │     │  │     ├─ _suite.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ validators.py
│  │  │  │     │  ├─ _format.py
│  │  │  │     │  ├─ _keywords.py
│  │  │  │     │  ├─ _legacy_keywords.py
│  │  │  │     │  ├─ _types.py
│  │  │  │     │  ├─ _typing.py
│  │  │  │     │  ├─ _utils.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ cli.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ protocols.cpython-310.pyc
│  │  │  │     │     ├─ validators.cpython-310.pyc
│  │  │  │     │     ├─ _format.cpython-310.pyc
│  │  │  │     │     ├─ _keywords.cpython-310.pyc
│  │  │  │     │     ├─ _legacy_keywords.cpython-310.pyc
│  │  │  │     │     ├─ _types.cpython-310.pyc
│  │  │  │     │     ├─ _typing.cpython-310.pyc
│  │  │  │     │     ├─ _utils.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ jsonschema-4.20.0.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  └─ COPYING
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ jsonschema_specifications
│  │  │  │     │  ├─ schemas
│  │  │  │     │  │  ├─ draft201909
│  │  │  │     │  │  │  ├─ metaschema.json
│  │  │  │     │  │  │  └─ vocabularies
│  │  │  │     │  │  │     ├─ applicator
│  │  │  │     │  │  │     ├─ content
│  │  │  │     │  │  │     ├─ core
│  │  │  │     │  │  │     ├─ meta-data
│  │  │  │     │  │  │     └─ validation
│  │  │  │     │  │  ├─ draft202012
│  │  │  │     │  │  │  ├─ metaschema.json
│  │  │  │     │  │  │  └─ vocabularies
│  │  │  │     │  │  │     ├─ applicator
│  │  │  │     │  │  │     ├─ content
│  │  │  │     │  │  │     ├─ core
│  │  │  │     │  │  │     ├─ format
│  │  │  │     │  │  │     ├─ format-annotation
│  │  │  │     │  │  │     ├─ format-assertion
│  │  │  │     │  │  │     ├─ meta-data
│  │  │  │     │  │  │     ├─ unevaluated
│  │  │  │     │  │  │     └─ validation
│  │  │  │     │  │  ├─ draft3
│  │  │  │     │  │  │  └─ metaschema.json
│  │  │  │     │  │  ├─ draft4
│  │  │  │     │  │  │  └─ metaschema.json
│  │  │  │     │  │  ├─ draft6
│  │  │  │     │  │  │  └─ metaschema.json
│  │  │  │     │  │  └─ draft7
│  │  │  │     │  │     └─ metaschema.json
│  │  │  │     │  ├─ tests
│  │  │  │     │  │  ├─ test_jsonschema_specifications.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ test_jsonschema_specifications.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _core.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ _core.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ jsonschema_specifications-2023.12.1.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  └─ COPYING
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ jwt
│  │  │  │     │  ├─ algorithms.py
│  │  │  │     │  ├─ api_jwk.py
│  │  │  │     │  ├─ api_jws.py
│  │  │  │     │  ├─ api_jwt.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ help.py
│  │  │  │     │  ├─ jwks_client.py
│  │  │  │     │  ├─ jwk_set_cache.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ types.py
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ warnings.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ algorithms.cpython-310.pyc
│  │  │  │     │     ├─ api_jwk.cpython-310.pyc
│  │  │  │     │     ├─ api_jws.cpython-310.pyc
│  │  │  │     │     ├─ api_jwt.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ help.cpython-310.pyc
│  │  │  │     │     ├─ jwks_client.cpython-310.pyc
│  │  │  │     │     ├─ jwk_set_cache.cpython-310.pyc
│  │  │  │     │     ├─ types.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ warnings.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ markupsafe
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ _native.py
│  │  │  │     │  ├─ _speedups.c
│  │  │  │     │  ├─ _speedups.cp310-win_amd64.pyd
│  │  │  │     │  ├─ _speedups.pyi
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ _native.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ MarkupSafe-2.1.3.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE.rst
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ msal
│  │  │  │     │  ├─ application.py
│  │  │  │     │  ├─ authority.py
│  │  │  │     │  ├─ broker.py
│  │  │  │     │  ├─ cloudshell.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ individual_cache.py
│  │  │  │     │  ├─ mex.py
│  │  │  │     │  ├─ oauth2cli
│  │  │  │     │  │  ├─ assertion.py
│  │  │  │     │  │  ├─ authcode.py
│  │  │  │     │  │  ├─ http.py
│  │  │  │     │  │  ├─ oauth2.py
│  │  │  │     │  │  ├─ oidc.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ assertion.cpython-310.pyc
│  │  │  │     │  │     ├─ authcode.cpython-310.pyc
│  │  │  │     │  │     ├─ http.cpython-310.pyc
│  │  │  │     │  │     ├─ oauth2.cpython-310.pyc
│  │  │  │     │  │     ├─ oidc.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ region.py
│  │  │  │     │  ├─ telemetry.py
│  │  │  │     │  ├─ throttled_http_client.py
│  │  │  │     │  ├─ token_cache.py
│  │  │  │     │  ├─ wstrust_request.py
│  │  │  │     │  ├─ wstrust_response.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ application.cpython-310.pyc
│  │  │  │     │     ├─ authority.cpython-310.pyc
│  │  │  │     │     ├─ broker.cpython-310.pyc
│  │  │  │     │     ├─ cloudshell.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ individual_cache.cpython-310.pyc
│  │  │  │     │     ├─ mex.cpython-310.pyc
│  │  │  │     │     ├─ region.cpython-310.pyc
│  │  │  │     │     ├─ telemetry.cpython-310.pyc
│  │  │  │     │     ├─ throttled_http_client.cpython-310.pyc
│  │  │  │     │     ├─ token_cache.cpython-310.pyc
│  │  │  │     │     ├─ wstrust_request.cpython-310.pyc
│  │  │  │     │     ├─ wstrust_response.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ msal-1.25.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ msal_extensions
│  │  │  │     │  ├─ cache_lock.py
│  │  │  │     │  ├─ libsecret.py
│  │  │  │     │  ├─ osx.py
│  │  │  │     │  ├─ persistence.py
│  │  │  │     │  ├─ token_cache.py
│  │  │  │     │  ├─ windows.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ cache_lock.cpython-310.pyc
│  │  │  │     │     ├─ libsecret.cpython-310.pyc
│  │  │  │     │     ├─ osx.cpython-310.pyc
│  │  │  │     │     ├─ persistence.cpython-310.pyc
│  │  │  │     │     ├─ token_cache.cpython-310.pyc
│  │  │  │     │     ├─ windows.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ msal_extensions-1.0.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ mypy_extensions-1.0.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ mypy_extensions.py
│  │  │  │     ├─ packaging
│  │  │  │     │  ├─ markers.py
│  │  │  │     │  ├─ metadata.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ requirements.py
│  │  │  │     │  ├─ specifiers.py
│  │  │  │     │  ├─ tags.py
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ version.py
│  │  │  │     │  ├─ _elffile.py
│  │  │  │     │  ├─ _manylinux.py
│  │  │  │     │  ├─ _musllinux.py
│  │  │  │     │  ├─ _parser.py
│  │  │  │     │  ├─ _structures.py
│  │  │  │     │  ├─ _tokenizer.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ markers.cpython-310.pyc
│  │  │  │     │     ├─ metadata.cpython-310.pyc
│  │  │  │     │     ├─ requirements.cpython-310.pyc
│  │  │  │     │     ├─ specifiers.cpython-310.pyc
│  │  │  │     │     ├─ tags.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ version.cpython-310.pyc
│  │  │  │     │     ├─ _elffile.cpython-310.pyc
│  │  │  │     │     ├─ _manylinux.cpython-310.pyc
│  │  │  │     │     ├─ _musllinux.cpython-310.pyc
│  │  │  │     │     ├─ _parser.cpython-310.pyc
│  │  │  │     │     ├─ _structures.cpython-310.pyc
│  │  │  │     │     ├─ _tokenizer.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ packaging-23.2.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ LICENSE.APACHE
│  │  │  │     │  ├─ LICENSE.BSD
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pathspec
│  │  │  │     │  ├─ gitignore.py
│  │  │  │     │  ├─ pathspec.py
│  │  │  │     │  ├─ pattern.py
│  │  │  │     │  ├─ patterns
│  │  │  │     │  │  ├─ gitwildmatch.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ gitwildmatch.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ util.py
│  │  │  │     │  ├─ _meta.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ gitignore.cpython-310.pyc
│  │  │  │     │     ├─ pathspec.cpython-310.pyc
│  │  │  │     │     ├─ pattern.cpython-310.pyc
│  │  │  │     │     ├─ util.cpython-310.pyc
│  │  │  │     │     ├─ _meta.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ pathspec-0.12.1.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pep517
│  │  │  │     │  ├─ build.py
│  │  │  │     │  ├─ check.py
│  │  │  │     │  ├─ colorlog.py
│  │  │  │     │  ├─ dirtools.py
│  │  │  │     │  ├─ envbuild.py
│  │  │  │     │  ├─ in_process
│  │  │  │     │  │  ├─ _in_process.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ _in_process.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ meta.py
│  │  │  │     │  ├─ wrappers.py
│  │  │  │     │  ├─ _compat.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ build.cpython-310.pyc
│  │  │  │     │     ├─ check.cpython-310.pyc
│  │  │  │     │     ├─ colorlog.cpython-310.pyc
│  │  │  │     │     ├─ dirtools.cpython-310.pyc
│  │  │  │     │     ├─ envbuild.cpython-310.pyc
│  │  │  │     │     ├─ meta.cpython-310.pyc
│  │  │  │     │     ├─ wrappers.cpython-310.pyc
│  │  │  │     │     ├─ _compat.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ pep517-0.13.1.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pins_data_model
│  │  │  │     │  ├─ gen_models.py
│  │  │  │     │  ├─ load_schemas.py
│  │  │  │     │  ├─ models
│  │  │  │     │  │  ├─ model_case_schedule.py
│  │  │  │     │  │  ├─ model_employee.py
│  │  │  │     │  │  ├─ model_nsip_document.py
│  │  │  │     │  │  ├─ model_nsip_exam_timetable.py
│  │  │  │     │  │  ├─ model_nsip_project.py
│  │  │  │     │  │  ├─ model_nsip_project_update.py
│  │  │  │     │  │  ├─ model_nsip_representation.py
│  │  │  │     │  │  ├─ model_nsip_subscription.py
│  │  │  │     │  │  ├─ model_s51_advice.py
│  │  │  │     │  │  ├─ model_service_user.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ model_case_schedule.cpython-310.pyc
│  │  │  │     │  │     ├─ model_employee.cpython-310.pyc
│  │  │  │     │  │     ├─ model_nsip_document.cpython-310.pyc
│  │  │  │     │  │     ├─ model_nsip_exam_timetable.cpython-310.pyc
│  │  │  │     │  │     ├─ model_nsip_project.cpython-310.pyc
│  │  │  │     │  │     ├─ model_nsip_project_update.cpython-310.pyc
│  │  │  │     │  │     ├─ model_nsip_representation.cpython-310.pyc
│  │  │  │     │  │     ├─ model_nsip_subscription.cpython-310.pyc
│  │  │  │     │  │     ├─ model_s51_advice.cpython-310.pyc
│  │  │  │     │  │     ├─ model_service_user.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ gen_models.cpython-310.pyc
│  │  │  │     │     ├─ load_schemas.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ pins_data_model-1.0.0.dist-info
│  │  │  │     │  ├─ direct_url.json
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pip
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ _internal
│  │  │  │     │  │  ├─ build_env.py
│  │  │  │     │  │  ├─ cache.py
│  │  │  │     │  │  ├─ cli
│  │  │  │     │  │  │  ├─ autocompletion.py
│  │  │  │     │  │  │  ├─ base_command.py
│  │  │  │     │  │  │  ├─ cmdoptions.py
│  │  │  │     │  │  │  ├─ command_context.py
│  │  │  │     │  │  │  ├─ main.py
│  │  │  │     │  │  │  ├─ main_parser.py
│  │  │  │     │  │  │  ├─ parser.py
│  │  │  │     │  │  │  ├─ progress_bars.py
│  │  │  │     │  │  │  ├─ req_command.py
│  │  │  │     │  │  │  ├─ spinners.py
│  │  │  │     │  │  │  ├─ status_codes.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ autocompletion.cpython-310.pyc
│  │  │  │     │  │  │     ├─ base_command.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cmdoptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ command_context.cpython-310.pyc
│  │  │  │     │  │  │     ├─ main.cpython-310.pyc
│  │  │  │     │  │  │     ├─ main_parser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ parser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ progress_bars.cpython-310.pyc
│  │  │  │     │  │  │     ├─ req_command.cpython-310.pyc
│  │  │  │     │  │  │     ├─ spinners.cpython-310.pyc
│  │  │  │     │  │  │     ├─ status_codes.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ commands
│  │  │  │     │  │  │  ├─ cache.py
│  │  │  │     │  │  │  ├─ check.py
│  │  │  │     │  │  │  ├─ completion.py
│  │  │  │     │  │  │  ├─ configuration.py
│  │  │  │     │  │  │  ├─ debug.py
│  │  │  │     │  │  │  ├─ download.py
│  │  │  │     │  │  │  ├─ freeze.py
│  │  │  │     │  │  │  ├─ hash.py
│  │  │  │     │  │  │  ├─ help.py
│  │  │  │     │  │  │  ├─ index.py
│  │  │  │     │  │  │  ├─ inspect.py
│  │  │  │     │  │  │  ├─ install.py
│  │  │  │     │  │  │  ├─ list.py
│  │  │  │     │  │  │  ├─ search.py
│  │  │  │     │  │  │  ├─ show.py
│  │  │  │     │  │  │  ├─ uninstall.py
│  │  │  │     │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ cache.cpython-310.pyc
│  │  │  │     │  │  │     ├─ check.cpython-310.pyc
│  │  │  │     │  │  │     ├─ completion.cpython-310.pyc
│  │  │  │     │  │  │     ├─ configuration.cpython-310.pyc
│  │  │  │     │  │  │     ├─ debug.cpython-310.pyc
│  │  │  │     │  │  │     ├─ download.cpython-310.pyc
│  │  │  │     │  │  │     ├─ freeze.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hash.cpython-310.pyc
│  │  │  │     │  │  │     ├─ help.cpython-310.pyc
│  │  │  │     │  │  │     ├─ index.cpython-310.pyc
│  │  │  │     │  │  │     ├─ inspect.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install.cpython-310.pyc
│  │  │  │     │  │  │     ├─ list.cpython-310.pyc
│  │  │  │     │  │  │     ├─ search.cpython-310.pyc
│  │  │  │     │  │  │     ├─ show.cpython-310.pyc
│  │  │  │     │  │  │     ├─ uninstall.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ configuration.py
│  │  │  │     │  │  ├─ distributions
│  │  │  │     │  │  │  ├─ base.py
│  │  │  │     │  │  │  ├─ installed.py
│  │  │  │     │  │  │  ├─ sdist.py
│  │  │  │     │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ installed.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sdist.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ exceptions.py
│  │  │  │     │  │  ├─ index
│  │  │  │     │  │  │  ├─ collector.py
│  │  │  │     │  │  │  ├─ package_finder.py
│  │  │  │     │  │  │  ├─ sources.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ collector.cpython-310.pyc
│  │  │  │     │  │  │     ├─ package_finder.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sources.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ locations
│  │  │  │     │  │  │  ├─ base.py
│  │  │  │     │  │  │  ├─ _distutils.py
│  │  │  │     │  │  │  ├─ _sysconfig.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _distutils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _sysconfig.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ main.py
│  │  │  │     │  │  ├─ metadata
│  │  │  │     │  │  │  ├─ base.py
│  │  │  │     │  │  │  ├─ importlib
│  │  │  │     │  │  │  │  ├─ _compat.py
│  │  │  │     │  │  │  │  ├─ _dists.py
│  │  │  │     │  │  │  │  ├─ _envs.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ _compat.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _dists.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _envs.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ pkg_resources.py
│  │  │  │     │  │  │  ├─ _json.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pkg_resources.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _json.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ models
│  │  │  │     │  │  │  ├─ candidate.py
│  │  │  │     │  │  │  ├─ direct_url.py
│  │  │  │     │  │  │  ├─ format_control.py
│  │  │  │     │  │  │  ├─ index.py
│  │  │  │     │  │  │  ├─ installation_report.py
│  │  │  │     │  │  │  ├─ link.py
│  │  │  │     │  │  │  ├─ scheme.py
│  │  │  │     │  │  │  ├─ search_scope.py
│  │  │  │     │  │  │  ├─ selection_prefs.py
│  │  │  │     │  │  │  ├─ target_python.py
│  │  │  │     │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ candidate.cpython-310.pyc
│  │  │  │     │  │  │     ├─ direct_url.cpython-310.pyc
│  │  │  │     │  │  │     ├─ format_control.cpython-310.pyc
│  │  │  │     │  │  │     ├─ index.cpython-310.pyc
│  │  │  │     │  │  │     ├─ installation_report.cpython-310.pyc
│  │  │  │     │  │  │     ├─ link.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scheme.cpython-310.pyc
│  │  │  │     │  │  │     ├─ search_scope.cpython-310.pyc
│  │  │  │     │  │  │     ├─ selection_prefs.cpython-310.pyc
│  │  │  │     │  │  │     ├─ target_python.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ network
│  │  │  │     │  │  │  ├─ auth.py
│  │  │  │     │  │  │  ├─ cache.py
│  │  │  │     │  │  │  ├─ download.py
│  │  │  │     │  │  │  ├─ lazy_wheel.py
│  │  │  │     │  │  │  ├─ session.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ xmlrpc.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ auth.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cache.cpython-310.pyc
│  │  │  │     │  │  │     ├─ download.cpython-310.pyc
│  │  │  │     │  │  │     ├─ lazy_wheel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ session.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ xmlrpc.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ operations
│  │  │  │     │  │  │  ├─ build
│  │  │  │     │  │  │  │  ├─ build_tracker.py
│  │  │  │     │  │  │  │  ├─ metadata.py
│  │  │  │     │  │  │  │  ├─ metadata_editable.py
│  │  │  │     │  │  │  │  ├─ metadata_legacy.py
│  │  │  │     │  │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  │  ├─ wheel_editable.py
│  │  │  │     │  │  │  │  ├─ wheel_legacy.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ build_tracker.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ metadata.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ metadata_editable.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ metadata_legacy.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ wheel_editable.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ wheel_legacy.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ check.py
│  │  │  │     │  │  │  ├─ freeze.py
│  │  │  │     │  │  │  ├─ install
│  │  │  │     │  │  │  │  ├─ editable_legacy.py
│  │  │  │     │  │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ editable_legacy.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ prepare.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ check.cpython-310.pyc
│  │  │  │     │  │  │     ├─ freeze.cpython-310.pyc
│  │  │  │     │  │  │     ├─ prepare.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ pyproject.py
│  │  │  │     │  │  ├─ req
│  │  │  │     │  │  │  ├─ constructors.py
│  │  │  │     │  │  │  ├─ req_file.py
│  │  │  │     │  │  │  ├─ req_install.py
│  │  │  │     │  │  │  ├─ req_set.py
│  │  │  │     │  │  │  ├─ req_uninstall.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ constructors.cpython-310.pyc
│  │  │  │     │  │  │     ├─ req_file.cpython-310.pyc
│  │  │  │     │  │  │     ├─ req_install.cpython-310.pyc
│  │  │  │     │  │  │     ├─ req_set.cpython-310.pyc
│  │  │  │     │  │  │     ├─ req_uninstall.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ resolution
│  │  │  │     │  │  │  ├─ base.py
│  │  │  │     │  │  │  ├─ legacy
│  │  │  │     │  │  │  │  ├─ resolver.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ resolver.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ resolvelib
│  │  │  │     │  │  │  │  ├─ base.py
│  │  │  │     │  │  │  │  ├─ candidates.py
│  │  │  │     │  │  │  │  ├─ factory.py
│  │  │  │     │  │  │  │  ├─ found_candidates.py
│  │  │  │     │  │  │  │  ├─ provider.py
│  │  │  │     │  │  │  │  ├─ reporter.py
│  │  │  │     │  │  │  │  ├─ requirements.py
│  │  │  │     │  │  │  │  ├─ resolver.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ candidates.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ factory.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ found_candidates.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ provider.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ reporter.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ requirements.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ resolver.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ self_outdated_check.py
│  │  │  │     │  │  ├─ utils
│  │  │  │     │  │  │  ├─ appdirs.py
│  │  │  │     │  │  │  ├─ compat.py
│  │  │  │     │  │  │  ├─ compatibility_tags.py
│  │  │  │     │  │  │  ├─ datetime.py
│  │  │  │     │  │  │  ├─ deprecation.py
│  │  │  │     │  │  │  ├─ direct_url_helpers.py
│  │  │  │     │  │  │  ├─ egg_link.py
│  │  │  │     │  │  │  ├─ encoding.py
│  │  │  │     │  │  │  ├─ entrypoints.py
│  │  │  │     │  │  │  ├─ filesystem.py
│  │  │  │     │  │  │  ├─ filetypes.py
│  │  │  │     │  │  │  ├─ glibc.py
│  │  │  │     │  │  │  ├─ hashes.py
│  │  │  │     │  │  │  ├─ logging.py
│  │  │  │     │  │  │  ├─ misc.py
│  │  │  │     │  │  │  ├─ models.py
│  │  │  │     │  │  │  ├─ packaging.py
│  │  │  │     │  │  │  ├─ setuptools_build.py
│  │  │  │     │  │  │  ├─ subprocess.py
│  │  │  │     │  │  │  ├─ temp_dir.py
│  │  │  │     │  │  │  ├─ unpacking.py
│  │  │  │     │  │  │  ├─ urls.py
│  │  │  │     │  │  │  ├─ virtualenv.py
│  │  │  │     │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  ├─ _jaraco_text.py
│  │  │  │     │  │  │  ├─ _log.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ appdirs.cpython-310.pyc
│  │  │  │     │  │  │     ├─ compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ compatibility_tags.cpython-310.pyc
│  │  │  │     │  │  │     ├─ datetime.cpython-310.pyc
│  │  │  │     │  │  │     ├─ deprecation.cpython-310.pyc
│  │  │  │     │  │  │     ├─ direct_url_helpers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ egg_link.cpython-310.pyc
│  │  │  │     │  │  │     ├─ encoding.cpython-310.pyc
│  │  │  │     │  │  │     ├─ entrypoints.cpython-310.pyc
│  │  │  │     │  │  │     ├─ filesystem.cpython-310.pyc
│  │  │  │     │  │  │     ├─ filetypes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ glibc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hashes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ logging.cpython-310.pyc
│  │  │  │     │  │  │     ├─ misc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ models.cpython-310.pyc
│  │  │  │     │  │  │     ├─ packaging.cpython-310.pyc
│  │  │  │     │  │  │     ├─ setuptools_build.cpython-310.pyc
│  │  │  │     │  │  │     ├─ subprocess.cpython-310.pyc
│  │  │  │     │  │  │     ├─ temp_dir.cpython-310.pyc
│  │  │  │     │  │  │     ├─ unpacking.cpython-310.pyc
│  │  │  │     │  │  │     ├─ urls.cpython-310.pyc
│  │  │  │     │  │  │     ├─ virtualenv.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _jaraco_text.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _log.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ vcs
│  │  │  │     │  │  │  ├─ bazaar.py
│  │  │  │     │  │  │  ├─ git.py
│  │  │  │     │  │  │  ├─ mercurial.py
│  │  │  │     │  │  │  ├─ subversion.py
│  │  │  │     │  │  │  ├─ versioncontrol.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ bazaar.cpython-310.pyc
│  │  │  │     │  │  │     ├─ git.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mercurial.cpython-310.pyc
│  │  │  │     │  │  │     ├─ subversion.cpython-310.pyc
│  │  │  │     │  │  │     ├─ versioncontrol.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ wheel_builder.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ build_env.cpython-310.pyc
│  │  │  │     │  │     ├─ cache.cpython-310.pyc
│  │  │  │     │  │     ├─ configuration.cpython-310.pyc
│  │  │  │     │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │     ├─ main.cpython-310.pyc
│  │  │  │     │  │     ├─ pyproject.cpython-310.pyc
│  │  │  │     │  │     ├─ self_outdated_check.cpython-310.pyc
│  │  │  │     │  │     ├─ wheel_builder.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _vendor
│  │  │  │     │  │  ├─ cachecontrol
│  │  │  │     │  │  │  ├─ adapter.py
│  │  │  │     │  │  │  ├─ cache.py
│  │  │  │     │  │  │  ├─ caches
│  │  │  │     │  │  │  │  ├─ file_cache.py
│  │  │  │     │  │  │  │  ├─ redis_cache.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ file_cache.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ redis_cache.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ controller.py
│  │  │  │     │  │  │  ├─ filewrapper.py
│  │  │  │     │  │  │  ├─ heuristics.py
│  │  │  │     │  │  │  ├─ serialize.py
│  │  │  │     │  │  │  ├─ wrapper.py
│  │  │  │     │  │  │  ├─ _cmd.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ adapter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cache.cpython-310.pyc
│  │  │  │     │  │  │     ├─ controller.cpython-310.pyc
│  │  │  │     │  │  │     ├─ filewrapper.cpython-310.pyc
│  │  │  │     │  │  │     ├─ heuristics.cpython-310.pyc
│  │  │  │     │  │  │     ├─ serialize.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wrapper.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _cmd.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ certifi
│  │  │  │     │  │  │  ├─ cacert.pem
│  │  │  │     │  │  │  ├─ core.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  ├─ __main__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __main__.cpython-310.pyc
│  │  │  │     │  │  ├─ chardet
│  │  │  │     │  │  │  ├─ big5freq.py
│  │  │  │     │  │  │  ├─ big5prober.py
│  │  │  │     │  │  │  ├─ chardistribution.py
│  │  │  │     │  │  │  ├─ charsetgroupprober.py
│  │  │  │     │  │  │  ├─ charsetprober.py
│  │  │  │     │  │  │  ├─ cli
│  │  │  │     │  │  │  │  ├─ chardetect.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ chardetect.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ codingstatemachine.py
│  │  │  │     │  │  │  ├─ codingstatemachinedict.py
│  │  │  │     │  │  │  ├─ cp949prober.py
│  │  │  │     │  │  │  ├─ enums.py
│  │  │  │     │  │  │  ├─ escprober.py
│  │  │  │     │  │  │  ├─ escsm.py
│  │  │  │     │  │  │  ├─ eucjpprober.py
│  │  │  │     │  │  │  ├─ euckrfreq.py
│  │  │  │     │  │  │  ├─ euckrprober.py
│  │  │  │     │  │  │  ├─ euctwfreq.py
│  │  │  │     │  │  │  ├─ euctwprober.py
│  │  │  │     │  │  │  ├─ gb2312freq.py
│  │  │  │     │  │  │  ├─ gb2312prober.py
│  │  │  │     │  │  │  ├─ hebrewprober.py
│  │  │  │     │  │  │  ├─ jisfreq.py
│  │  │  │     │  │  │  ├─ johabfreq.py
│  │  │  │     │  │  │  ├─ johabprober.py
│  │  │  │     │  │  │  ├─ jpcntx.py
│  │  │  │     │  │  │  ├─ langbulgarianmodel.py
│  │  │  │     │  │  │  ├─ langgreekmodel.py
│  │  │  │     │  │  │  ├─ langhebrewmodel.py
│  │  │  │     │  │  │  ├─ langhungarianmodel.py
│  │  │  │     │  │  │  ├─ langrussianmodel.py
│  │  │  │     │  │  │  ├─ langthaimodel.py
│  │  │  │     │  │  │  ├─ langturkishmodel.py
│  │  │  │     │  │  │  ├─ latin1prober.py
│  │  │  │     │  │  │  ├─ macromanprober.py
│  │  │  │     │  │  │  ├─ mbcharsetprober.py
│  │  │  │     │  │  │  ├─ mbcsgroupprober.py
│  │  │  │     │  │  │  ├─ mbcssm.py
│  │  │  │     │  │  │  ├─ metadata
│  │  │  │     │  │  │  │  ├─ languages.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ languages.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ resultdict.py
│  │  │  │     │  │  │  ├─ sbcharsetprober.py
│  │  │  │     │  │  │  ├─ sbcsgroupprober.py
│  │  │  │     │  │  │  ├─ sjisprober.py
│  │  │  │     │  │  │  ├─ universaldetector.py
│  │  │  │     │  │  │  ├─ utf1632prober.py
│  │  │  │     │  │  │  ├─ utf8prober.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ big5freq.cpython-310.pyc
│  │  │  │     │  │  │     ├─ big5prober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ chardistribution.cpython-310.pyc
│  │  │  │     │  │  │     ├─ charsetgroupprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ charsetprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ codingstatemachine.cpython-310.pyc
│  │  │  │     │  │  │     ├─ codingstatemachinedict.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cp949prober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ enums.cpython-310.pyc
│  │  │  │     │  │  │     ├─ escprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ escsm.cpython-310.pyc
│  │  │  │     │  │  │     ├─ eucjpprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ euckrfreq.cpython-310.pyc
│  │  │  │     │  │  │     ├─ euckrprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ euctwfreq.cpython-310.pyc
│  │  │  │     │  │  │     ├─ euctwprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ gb2312freq.cpython-310.pyc
│  │  │  │     │  │  │     ├─ gb2312prober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hebrewprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ jisfreq.cpython-310.pyc
│  │  │  │     │  │  │     ├─ johabfreq.cpython-310.pyc
│  │  │  │     │  │  │     ├─ johabprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ jpcntx.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langbulgarianmodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langgreekmodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langhebrewmodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langhungarianmodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langrussianmodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langthaimodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ langturkishmodel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ latin1prober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ macromanprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mbcharsetprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mbcsgroupprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mbcssm.cpython-310.pyc
│  │  │  │     │  │  │     ├─ resultdict.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sbcharsetprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sbcsgroupprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sjisprober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ universaldetector.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utf1632prober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utf8prober.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ colorama
│  │  │  │     │  │  │  ├─ ansi.py
│  │  │  │     │  │  │  ├─ ansitowin32.py
│  │  │  │     │  │  │  ├─ initialise.py
│  │  │  │     │  │  │  ├─ tests
│  │  │  │     │  │  │  │  ├─ ansitowin32_test.py
│  │  │  │     │  │  │  │  ├─ ansi_test.py
│  │  │  │     │  │  │  │  ├─ initialise_test.py
│  │  │  │     │  │  │  │  ├─ isatty_test.py
│  │  │  │     │  │  │  │  ├─ utils.py
│  │  │  │     │  │  │  │  ├─ winterm_test.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ ansitowin32_test.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ansi_test.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ initialise_test.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ isatty_test.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ winterm_test.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ win32.py
│  │  │  │     │  │  │  ├─ winterm.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ ansi.cpython-310.pyc
│  │  │  │     │  │  │     ├─ ansitowin32.cpython-310.pyc
│  │  │  │     │  │  │     ├─ initialise.cpython-310.pyc
│  │  │  │     │  │  │     ├─ win32.cpython-310.pyc
│  │  │  │     │  │  │     ├─ winterm.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ distlib
│  │  │  │     │  │  │  ├─ compat.py
│  │  │  │     │  │  │  ├─ database.py
│  │  │  │     │  │  │  ├─ index.py
│  │  │  │     │  │  │  ├─ locators.py
│  │  │  │     │  │  │  ├─ manifest.py
│  │  │  │     │  │  │  ├─ markers.py
│  │  │  │     │  │  │  ├─ metadata.py
│  │  │  │     │  │  │  ├─ resources.py
│  │  │  │     │  │  │  ├─ scripts.py
│  │  │  │     │  │  │  ├─ t32.exe
│  │  │  │     │  │  │  ├─ t64-arm.exe
│  │  │  │     │  │  │  ├─ t64.exe
│  │  │  │     │  │  │  ├─ util.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ w32.exe
│  │  │  │     │  │  │  ├─ w64-arm.exe
│  │  │  │     │  │  │  ├─ w64.exe
│  │  │  │     │  │  │  ├─ wheel.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ database.cpython-310.pyc
│  │  │  │     │  │  │     ├─ index.cpython-310.pyc
│  │  │  │     │  │  │     ├─ locators.cpython-310.pyc
│  │  │  │     │  │  │     ├─ manifest.cpython-310.pyc
│  │  │  │     │  │  │     ├─ markers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ metadata.cpython-310.pyc
│  │  │  │     │  │  │     ├─ resources.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scripts.cpython-310.pyc
│  │  │  │     │  │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wheel.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ distro
│  │  │  │     │  │  │  ├─ distro.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  ├─ __main__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ distro.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __main__.cpython-310.pyc
│  │  │  │     │  │  ├─ idna
│  │  │  │     │  │  │  ├─ codec.py
│  │  │  │     │  │  │  ├─ compat.py
│  │  │  │     │  │  │  ├─ core.py
│  │  │  │     │  │  │  ├─ idnadata.py
│  │  │  │     │  │  │  ├─ intranges.py
│  │  │  │     │  │  │  ├─ package_data.py
│  │  │  │     │  │  │  ├─ uts46data.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ codec.cpython-310.pyc
│  │  │  │     │  │  │     ├─ compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │  │     ├─ idnadata.cpython-310.pyc
│  │  │  │     │  │  │     ├─ intranges.cpython-310.pyc
│  │  │  │     │  │  │     ├─ package_data.cpython-310.pyc
│  │  │  │     │  │  │     ├─ uts46data.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ msgpack
│  │  │  │     │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  ├─ ext.py
│  │  │  │     │  │  │  ├─ fallback.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ ext.cpython-310.pyc
│  │  │  │     │  │  │     ├─ fallback.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ packaging
│  │  │  │     │  │  │  ├─ markers.py
│  │  │  │     │  │  │  ├─ requirements.py
│  │  │  │     │  │  │  ├─ specifiers.py
│  │  │  │     │  │  │  ├─ tags.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ _manylinux.py
│  │  │  │     │  │  │  ├─ _musllinux.py
│  │  │  │     │  │  │  ├─ _structures.py
│  │  │  │     │  │  │  ├─ __about__.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ markers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ requirements.cpython-310.pyc
│  │  │  │     │  │  │     ├─ specifiers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tags.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _manylinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _musllinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _structures.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __about__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ pkg_resources
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ platformdirs
│  │  │  │     │  │  │  ├─ android.py
│  │  │  │     │  │  │  ├─ api.py
│  │  │  │     │  │  │  ├─ macos.py
│  │  │  │     │  │  │  ├─ unix.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ windows.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  ├─ __main__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ android.cpython-310.pyc
│  │  │  │     │  │  │     ├─ api.cpython-310.pyc
│  │  │  │     │  │  │     ├─ macos.cpython-310.pyc
│  │  │  │     │  │  │     ├─ unix.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     ├─ windows.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __main__.cpython-310.pyc
│  │  │  │     │  │  ├─ pygments
│  │  │  │     │  │  │  ├─ cmdline.py
│  │  │  │     │  │  │  ├─ console.py
│  │  │  │     │  │  │  ├─ filter.py
│  │  │  │     │  │  │  ├─ filters
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ formatter.py
│  │  │  │     │  │  │  ├─ formatters
│  │  │  │     │  │  │  │  ├─ bbcode.py
│  │  │  │     │  │  │  │  ├─ groff.py
│  │  │  │     │  │  │  │  ├─ html.py
│  │  │  │     │  │  │  │  ├─ img.py
│  │  │  │     │  │  │  │  ├─ irc.py
│  │  │  │     │  │  │  │  ├─ latex.py
│  │  │  │     │  │  │  │  ├─ other.py
│  │  │  │     │  │  │  │  ├─ pangomarkup.py
│  │  │  │     │  │  │  │  ├─ rtf.py
│  │  │  │     │  │  │  │  ├─ svg.py
│  │  │  │     │  │  │  │  ├─ terminal.py
│  │  │  │     │  │  │  │  ├─ terminal256.py
│  │  │  │     │  │  │  │  ├─ _mapping.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ bbcode.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ groff.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ html.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ img.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ irc.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ latex.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ other.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ pangomarkup.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ rtf.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ svg.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ terminal.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ terminal256.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _mapping.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ lexer.py
│  │  │  │     │  │  │  ├─ lexers
│  │  │  │     │  │  │  │  ├─ python.py
│  │  │  │     │  │  │  │  ├─ _mapping.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ python.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _mapping.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ modeline.py
│  │  │  │     │  │  │  ├─ plugin.py
│  │  │  │     │  │  │  ├─ regexopt.py
│  │  │  │     │  │  │  ├─ scanner.py
│  │  │  │     │  │  │  ├─ sphinxext.py
│  │  │  │     │  │  │  ├─ style.py
│  │  │  │     │  │  │  ├─ styles
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ token.py
│  │  │  │     │  │  │  ├─ unistring.py
│  │  │  │     │  │  │  ├─ util.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  ├─ __main__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ cmdline.cpython-310.pyc
│  │  │  │     │  │  │     ├─ console.cpython-310.pyc
│  │  │  │     │  │  │     ├─ filter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ formatter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ lexer.cpython-310.pyc
│  │  │  │     │  │  │     ├─ modeline.cpython-310.pyc
│  │  │  │     │  │  │     ├─ plugin.cpython-310.pyc
│  │  │  │     │  │  │     ├─ regexopt.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scanner.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sphinxext.cpython-310.pyc
│  │  │  │     │  │  │     ├─ style.cpython-310.pyc
│  │  │  │     │  │  │     ├─ token.cpython-310.pyc
│  │  │  │     │  │  │     ├─ unistring.cpython-310.pyc
│  │  │  │     │  │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __main__.cpython-310.pyc
│  │  │  │     │  │  ├─ pyparsing
│  │  │  │     │  │  │  ├─ actions.py
│  │  │  │     │  │  │  ├─ common.py
│  │  │  │     │  │  │  ├─ core.py
│  │  │  │     │  │  │  ├─ diagram
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  ├─ helpers.py
│  │  │  │     │  │  │  ├─ results.py
│  │  │  │     │  │  │  ├─ testing.py
│  │  │  │     │  │  │  ├─ unicode.py
│  │  │  │     │  │  │  ├─ util.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ actions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ common.cpython-310.pyc
│  │  │  │     │  │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ helpers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ results.cpython-310.pyc
│  │  │  │     │  │  │     ├─ testing.cpython-310.pyc
│  │  │  │     │  │  │     ├─ unicode.cpython-310.pyc
│  │  │  │     │  │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ requests
│  │  │  │     │  │  │  ├─ adapters.py
│  │  │  │     │  │  │  ├─ api.py
│  │  │  │     │  │  │  ├─ auth.py
│  │  │  │     │  │  │  ├─ certs.py
│  │  │  │     │  │  │  ├─ compat.py
│  │  │  │     │  │  │  ├─ cookies.py
│  │  │  │     │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  ├─ help.py
│  │  │  │     │  │  │  ├─ models.py
│  │  │  │     │  │  │  ├─ packages.py
│  │  │  │     │  │  │  ├─ sessions.py
│  │  │  │     │  │  │  ├─ status_codes.py
│  │  │  │     │  │  │  ├─ structures.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ _internal_utils.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  ├─ __pycache__
│  │  │  │     │  │  │  │  ├─ adapters.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ api.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ auth.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ certs.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ compat.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ cookies.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ help.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ models.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ packages.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ sessions.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ status_codes.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ structures.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ _internal_utils.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  │  └─ __version__.cpython-310.pyc
│  │  │  │     │  │  │  └─ __version__.py
│  │  │  │     │  │  ├─ resolvelib
│  │  │  │     │  │  │  ├─ compat
│  │  │  │     │  │  │  │  ├─ collections_abc.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ collections_abc.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ providers.py
│  │  │  │     │  │  │  ├─ reporters.py
│  │  │  │     │  │  │  ├─ resolvers.py
│  │  │  │     │  │  │  ├─ structs.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ providers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ reporters.cpython-310.pyc
│  │  │  │     │  │  │     ├─ resolvers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ structs.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ rich
│  │  │  │     │  │  │  ├─ abc.py
│  │  │  │     │  │  │  ├─ align.py
│  │  │  │     │  │  │  ├─ ansi.py
│  │  │  │     │  │  │  ├─ bar.py
│  │  │  │     │  │  │  ├─ box.py
│  │  │  │     │  │  │  ├─ cells.py
│  │  │  │     │  │  │  ├─ color.py
│  │  │  │     │  │  │  ├─ color_triplet.py
│  │  │  │     │  │  │  ├─ columns.py
│  │  │  │     │  │  │  ├─ console.py
│  │  │  │     │  │  │  ├─ constrain.py
│  │  │  │     │  │  │  ├─ containers.py
│  │  │  │     │  │  │  ├─ control.py
│  │  │  │     │  │  │  ├─ default_styles.py
│  │  │  │     │  │  │  ├─ diagnose.py
│  │  │  │     │  │  │  ├─ emoji.py
│  │  │  │     │  │  │  ├─ errors.py
│  │  │  │     │  │  │  ├─ filesize.py
│  │  │  │     │  │  │  ├─ file_proxy.py
│  │  │  │     │  │  │  ├─ highlighter.py
│  │  │  │     │  │  │  ├─ json.py
│  │  │  │     │  │  │  ├─ jupyter.py
│  │  │  │     │  │  │  ├─ layout.py
│  │  │  │     │  │  │  ├─ live.py
│  │  │  │     │  │  │  ├─ live_render.py
│  │  │  │     │  │  │  ├─ logging.py
│  │  │  │     │  │  │  ├─ markup.py
│  │  │  │     │  │  │  ├─ measure.py
│  │  │  │     │  │  │  ├─ padding.py
│  │  │  │     │  │  │  ├─ pager.py
│  │  │  │     │  │  │  ├─ palette.py
│  │  │  │     │  │  │  ├─ panel.py
│  │  │  │     │  │  │  ├─ pretty.py
│  │  │  │     │  │  │  ├─ progress.py
│  │  │  │     │  │  │  ├─ progress_bar.py
│  │  │  │     │  │  │  ├─ prompt.py
│  │  │  │     │  │  │  ├─ protocol.py
│  │  │  │     │  │  │  ├─ region.py
│  │  │  │     │  │  │  ├─ repr.py
│  │  │  │     │  │  │  ├─ rule.py
│  │  │  │     │  │  │  ├─ scope.py
│  │  │  │     │  │  │  ├─ screen.py
│  │  │  │     │  │  │  ├─ segment.py
│  │  │  │     │  │  │  ├─ spinner.py
│  │  │  │     │  │  │  ├─ status.py
│  │  │  │     │  │  │  ├─ style.py
│  │  │  │     │  │  │  ├─ styled.py
│  │  │  │     │  │  │  ├─ syntax.py
│  │  │  │     │  │  │  ├─ table.py
│  │  │  │     │  │  │  ├─ terminal_theme.py
│  │  │  │     │  │  │  ├─ text.py
│  │  │  │     │  │  │  ├─ theme.py
│  │  │  │     │  │  │  ├─ themes.py
│  │  │  │     │  │  │  ├─ traceback.py
│  │  │  │     │  │  │  ├─ tree.py
│  │  │  │     │  │  │  ├─ _cell_widths.py
│  │  │  │     │  │  │  ├─ _emoji_codes.py
│  │  │  │     │  │  │  ├─ _emoji_replace.py
│  │  │  │     │  │  │  ├─ _export_format.py
│  │  │  │     │  │  │  ├─ _extension.py
│  │  │  │     │  │  │  ├─ _fileno.py
│  │  │  │     │  │  │  ├─ _inspect.py
│  │  │  │     │  │  │  ├─ _log_render.py
│  │  │  │     │  │  │  ├─ _loop.py
│  │  │  │     │  │  │  ├─ _null_file.py
│  │  │  │     │  │  │  ├─ _palettes.py
│  │  │  │     │  │  │  ├─ _pick.py
│  │  │  │     │  │  │  ├─ _ratio.py
│  │  │  │     │  │  │  ├─ _spinners.py
│  │  │  │     │  │  │  ├─ _stack.py
│  │  │  │     │  │  │  ├─ _timer.py
│  │  │  │     │  │  │  ├─ _win32_console.py
│  │  │  │     │  │  │  ├─ _windows.py
│  │  │  │     │  │  │  ├─ _windows_renderer.py
│  │  │  │     │  │  │  ├─ _wrap.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  ├─ __main__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ abc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ align.cpython-310.pyc
│  │  │  │     │  │  │     ├─ ansi.cpython-310.pyc
│  │  │  │     │  │  │     ├─ bar.cpython-310.pyc
│  │  │  │     │  │  │     ├─ box.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cells.cpython-310.pyc
│  │  │  │     │  │  │     ├─ color.cpython-310.pyc
│  │  │  │     │  │  │     ├─ color_triplet.cpython-310.pyc
│  │  │  │     │  │  │     ├─ columns.cpython-310.pyc
│  │  │  │     │  │  │     ├─ console.cpython-310.pyc
│  │  │  │     │  │  │     ├─ constrain.cpython-310.pyc
│  │  │  │     │  │  │     ├─ containers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ control.cpython-310.pyc
│  │  │  │     │  │  │     ├─ default_styles.cpython-310.pyc
│  │  │  │     │  │  │     ├─ diagnose.cpython-310.pyc
│  │  │  │     │  │  │     ├─ emoji.cpython-310.pyc
│  │  │  │     │  │  │     ├─ errors.cpython-310.pyc
│  │  │  │     │  │  │     ├─ filesize.cpython-310.pyc
│  │  │  │     │  │  │     ├─ file_proxy.cpython-310.pyc
│  │  │  │     │  │  │     ├─ highlighter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ json.cpython-310.pyc
│  │  │  │     │  │  │     ├─ jupyter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ layout.cpython-310.pyc
│  │  │  │     │  │  │     ├─ live.cpython-310.pyc
│  │  │  │     │  │  │     ├─ live_render.cpython-310.pyc
│  │  │  │     │  │  │     ├─ logging.cpython-310.pyc
│  │  │  │     │  │  │     ├─ markup.cpython-310.pyc
│  │  │  │     │  │  │     ├─ measure.cpython-310.pyc
│  │  │  │     │  │  │     ├─ padding.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pager.cpython-310.pyc
│  │  │  │     │  │  │     ├─ palette.cpython-310.pyc
│  │  │  │     │  │  │     ├─ panel.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pretty.cpython-310.pyc
│  │  │  │     │  │  │     ├─ progress.cpython-310.pyc
│  │  │  │     │  │  │     ├─ progress_bar.cpython-310.pyc
│  │  │  │     │  │  │     ├─ prompt.cpython-310.pyc
│  │  │  │     │  │  │     ├─ protocol.cpython-310.pyc
│  │  │  │     │  │  │     ├─ region.cpython-310.pyc
│  │  │  │     │  │  │     ├─ repr.cpython-310.pyc
│  │  │  │     │  │  │     ├─ rule.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scope.cpython-310.pyc
│  │  │  │     │  │  │     ├─ screen.cpython-310.pyc
│  │  │  │     │  │  │     ├─ segment.cpython-310.pyc
│  │  │  │     │  │  │     ├─ spinner.cpython-310.pyc
│  │  │  │     │  │  │     ├─ status.cpython-310.pyc
│  │  │  │     │  │  │     ├─ style.cpython-310.pyc
│  │  │  │     │  │  │     ├─ styled.cpython-310.pyc
│  │  │  │     │  │  │     ├─ syntax.cpython-310.pyc
│  │  │  │     │  │  │     ├─ table.cpython-310.pyc
│  │  │  │     │  │  │     ├─ terminal_theme.cpython-310.pyc
│  │  │  │     │  │  │     ├─ text.cpython-310.pyc
│  │  │  │     │  │  │     ├─ theme.cpython-310.pyc
│  │  │  │     │  │  │     ├─ themes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ traceback.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tree.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _cell_widths.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _emoji_codes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _emoji_replace.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _export_format.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _extension.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _fileno.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _inspect.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _log_render.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _loop.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _null_file.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _palettes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _pick.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _ratio.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _spinners.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _stack.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _timer.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _win32_console.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _windows.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _windows_renderer.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _wrap.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __main__.cpython-310.pyc
│  │  │  │     │  │  ├─ six.py
│  │  │  │     │  │  ├─ tenacity
│  │  │  │     │  │  │  ├─ after.py
│  │  │  │     │  │  │  ├─ before.py
│  │  │  │     │  │  │  ├─ before_sleep.py
│  │  │  │     │  │  │  ├─ nap.py
│  │  │  │     │  │  │  ├─ retry.py
│  │  │  │     │  │  │  ├─ stop.py
│  │  │  │     │  │  │  ├─ tornadoweb.py
│  │  │  │     │  │  │  ├─ wait.py
│  │  │  │     │  │  │  ├─ _asyncio.py
│  │  │  │     │  │  │  ├─ _utils.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ after.cpython-310.pyc
│  │  │  │     │  │  │     ├─ before.cpython-310.pyc
│  │  │  │     │  │  │     ├─ before_sleep.cpython-310.pyc
│  │  │  │     │  │  │     ├─ nap.cpython-310.pyc
│  │  │  │     │  │  │     ├─ retry.cpython-310.pyc
│  │  │  │     │  │  │     ├─ stop.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tornadoweb.cpython-310.pyc
│  │  │  │     │  │  │     ├─ wait.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _asyncio.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _utils.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ tomli
│  │  │  │     │  │  │  ├─ _parser.py
│  │  │  │     │  │  │  ├─ _re.py
│  │  │  │     │  │  │  ├─ _types.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _parser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _re.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _types.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ truststore
│  │  │  │     │  │  │  ├─ _api.py
│  │  │  │     │  │  │  ├─ _macos.py
│  │  │  │     │  │  │  ├─ _openssl.py
│  │  │  │     │  │  │  ├─ _ssl_constants.py
│  │  │  │     │  │  │  ├─ _windows.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _api.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _macos.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _openssl.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _ssl_constants.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _windows.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ typing_extensions.py
│  │  │  │     │  │  ├─ urllib3
│  │  │  │     │  │  │  ├─ connection.py
│  │  │  │     │  │  │  ├─ connectionpool.py
│  │  │  │     │  │  │  ├─ contrib
│  │  │  │     │  │  │  │  ├─ appengine.py
│  │  │  │     │  │  │  │  ├─ ntlmpool.py
│  │  │  │     │  │  │  │  ├─ pyopenssl.py
│  │  │  │     │  │  │  │  ├─ securetransport.py
│  │  │  │     │  │  │  │  ├─ socks.py
│  │  │  │     │  │  │  │  ├─ _appengine_environ.py
│  │  │  │     │  │  │  │  ├─ _securetransport
│  │  │  │     │  │  │  │  │  ├─ bindings.py
│  │  │  │     │  │  │  │  │  ├─ low_level.py
│  │  │  │     │  │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │  │     ├─ bindings.cpython-310.pyc
│  │  │  │     │  │  │  │  │     ├─ low_level.cpython-310.pyc
│  │  │  │     │  │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ appengine.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ntlmpool.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ pyopenssl.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ securetransport.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ socks.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ _appengine_environ.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  ├─ fields.py
│  │  │  │     │  │  │  ├─ filepost.py
│  │  │  │     │  │  │  ├─ packages
│  │  │  │     │  │  │  │  ├─ backports
│  │  │  │     │  │  │  │  │  ├─ makefile.py
│  │  │  │     │  │  │  │  │  ├─ weakref_finalize.py
│  │  │  │     │  │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │  │     ├─ makefile.cpython-310.pyc
│  │  │  │     │  │  │  │  │     ├─ weakref_finalize.cpython-310.pyc
│  │  │  │     │  │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ six.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ six.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ poolmanager.py
│  │  │  │     │  │  │  ├─ request.py
│  │  │  │     │  │  │  ├─ response.py
│  │  │  │     │  │  │  ├─ util
│  │  │  │     │  │  │  │  ├─ connection.py
│  │  │  │     │  │  │  │  ├─ proxy.py
│  │  │  │     │  │  │  │  ├─ queue.py
│  │  │  │     │  │  │  │  ├─ request.py
│  │  │  │     │  │  │  │  ├─ response.py
│  │  │  │     │  │  │  │  ├─ retry.py
│  │  │  │     │  │  │  │  ├─ ssltransport.py
│  │  │  │     │  │  │  │  ├─ ssl_.py
│  │  │  │     │  │  │  │  ├─ ssl_match_hostname.py
│  │  │  │     │  │  │  │  ├─ timeout.py
│  │  │  │     │  │  │  │  ├─ url.py
│  │  │  │     │  │  │  │  ├─ wait.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ connection.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ proxy.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ queue.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ request.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ response.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ retry.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ssltransport.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ssl_.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ssl_match_hostname.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ timeout.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ url.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ wait.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ _collections.py
│  │  │  │     │  │  │  ├─ _version.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ connection.cpython-310.pyc
│  │  │  │     │  │  │     ├─ connectionpool.cpython-310.pyc
│  │  │  │     │  │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ fields.cpython-310.pyc
│  │  │  │     │  │  │     ├─ filepost.cpython-310.pyc
│  │  │  │     │  │  │     ├─ poolmanager.cpython-310.pyc
│  │  │  │     │  │  │     ├─ request.cpython-310.pyc
│  │  │  │     │  │  │     ├─ response.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _collections.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _version.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ vendor.txt
│  │  │  │     │  │  ├─ webencodings
│  │  │  │     │  │  │  ├─ labels.py
│  │  │  │     │  │  │  ├─ mklabels.py
│  │  │  │     │  │  │  ├─ tests.py
│  │  │  │     │  │  │  ├─ x_user_defined.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ labels.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mklabels.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tests.cpython-310.pyc
│  │  │  │     │  │  │     ├─ x_user_defined.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ six.cpython-310.pyc
│  │  │  │     │  │     ├─ typing_extensions.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  ├─ __pip-runner__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     ├─ __main__.cpython-310.pyc
│  │  │  │     │     └─ __pip-runner__.cpython-310.pyc
│  │  │  │     ├─ pip-23.3.1.dist-info
│  │  │  │     │  ├─ AUTHORS.txt
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE.txt
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pipreqs
│  │  │  │     │  ├─ mapping
│  │  │  │     │  ├─ pipreqs.py
│  │  │  │     │  ├─ stdlib
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ pipreqs.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ pipreqs-0.4.13.dist-info
│  │  │  │     │  ├─ AUTHORS.rst
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pip_api
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ _call.py
│  │  │  │     │  ├─ _hash.py
│  │  │  │     │  ├─ _installed_distributions.py
│  │  │  │     │  ├─ _parse_requirements.py
│  │  │  │     │  ├─ _pep650.py
│  │  │  │     │  ├─ _vendor
│  │  │  │     │  │  ├─ packaging
│  │  │  │     │  │  │  ├─ markers.py
│  │  │  │     │  │  │  ├─ requirements.py
│  │  │  │     │  │  │  ├─ specifiers.py
│  │  │  │     │  │  │  ├─ tags.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ _manylinux.py
│  │  │  │     │  │  │  ├─ _musllinux.py
│  │  │  │     │  │  │  ├─ _structures.py
│  │  │  │     │  │  │  ├─ __about__.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ markers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ requirements.cpython-310.pyc
│  │  │  │     │  │  │     ├─ specifiers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tags.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _manylinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _musllinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _structures.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __about__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ pyparsing.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ pyparsing.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _version.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ _call.cpython-310.pyc
│  │  │  │     │     ├─ _hash.cpython-310.pyc
│  │  │  │     │     ├─ _installed_distributions.cpython-310.pyc
│  │  │  │     │     ├─ _parse_requirements.cpython-310.pyc
│  │  │  │     │     ├─ _pep650.cpython-310.pyc
│  │  │  │     │     ├─ _version.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ pip_api-0.0.30.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pkg_resources
│  │  │  │     │  ├─ extern
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _vendor
│  │  │  │     │  │  ├─ appdirs.py
│  │  │  │     │  │  ├─ importlib_resources
│  │  │  │     │  │  │  ├─ abc.py
│  │  │  │     │  │  │  ├─ readers.py
│  │  │  │     │  │  │  ├─ simple.py
│  │  │  │     │  │  │  ├─ _adapters.py
│  │  │  │     │  │  │  ├─ _common.py
│  │  │  │     │  │  │  ├─ _compat.py
│  │  │  │     │  │  │  ├─ _itertools.py
│  │  │  │     │  │  │  ├─ _legacy.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ abc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ readers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ simple.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _adapters.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _common.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _itertools.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _legacy.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ jaraco
│  │  │  │     │  │  │  ├─ context.py
│  │  │  │     │  │  │  ├─ functools.py
│  │  │  │     │  │  │  ├─ text
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ context.cpython-310.pyc
│  │  │  │     │  │  │     ├─ functools.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ more_itertools
│  │  │  │     │  │  │  ├─ more.py
│  │  │  │     │  │  │  ├─ recipes.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ more.cpython-310.pyc
│  │  │  │     │  │  │     ├─ recipes.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ packaging
│  │  │  │     │  │  │  ├─ markers.py
│  │  │  │     │  │  │  ├─ requirements.py
│  │  │  │     │  │  │  ├─ specifiers.py
│  │  │  │     │  │  │  ├─ tags.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ _manylinux.py
│  │  │  │     │  │  │  ├─ _musllinux.py
│  │  │  │     │  │  │  ├─ _structures.py
│  │  │  │     │  │  │  ├─ __about__.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ markers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ requirements.cpython-310.pyc
│  │  │  │     │  │  │     ├─ specifiers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tags.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _manylinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _musllinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _structures.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __about__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ pyparsing
│  │  │  │     │  │  │  ├─ actions.py
│  │  │  │     │  │  │  ├─ common.py
│  │  │  │     │  │  │  ├─ core.py
│  │  │  │     │  │  │  ├─ diagram
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  ├─ helpers.py
│  │  │  │     │  │  │  ├─ results.py
│  │  │  │     │  │  │  ├─ testing.py
│  │  │  │     │  │  │  ├─ unicode.py
│  │  │  │     │  │  │  ├─ util.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ actions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ common.cpython-310.pyc
│  │  │  │     │  │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ helpers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ results.cpython-310.pyc
│  │  │  │     │  │  │     ├─ testing.cpython-310.pyc
│  │  │  │     │  │  │     ├─ unicode.cpython-310.pyc
│  │  │  │     │  │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ zipp.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ appdirs.cpython-310.pyc
│  │  │  │     │  │     ├─ zipp.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ platformdirs
│  │  │  │     │  ├─ android.py
│  │  │  │     │  ├─ api.py
│  │  │  │     │  ├─ macos.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ unix.py
│  │  │  │     │  ├─ version.py
│  │  │  │     │  ├─ windows.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ android.cpython-310.pyc
│  │  │  │     │     ├─ api.cpython-310.pyc
│  │  │  │     │     ├─ macos.cpython-310.pyc
│  │  │  │     │     ├─ unix.cpython-310.pyc
│  │  │  │     │     ├─ version.cpython-310.pyc
│  │  │  │     │     ├─ windows.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ platformdirs-4.1.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  └─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ plette
│  │  │  │     │  ├─ lockfiles.py
│  │  │  │     │  ├─ models
│  │  │  │     │  │  ├─ base.py
│  │  │  │     │  │  ├─ hashes.py
│  │  │  │     │  │  ├─ packages.py
│  │  │  │     │  │  ├─ scripts.py
│  │  │  │     │  │  ├─ sections.py
│  │  │  │     │  │  ├─ sources.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ base.cpython-310.pyc
│  │  │  │     │  │     ├─ hashes.cpython-310.pyc
│  │  │  │     │  │     ├─ packages.cpython-310.pyc
│  │  │  │     │  │     ├─ scripts.cpython-310.pyc
│  │  │  │     │  │     ├─ sections.cpython-310.pyc
│  │  │  │     │  │     ├─ sources.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ pipfiles.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ lockfiles.cpython-310.pyc
│  │  │  │     │     ├─ pipfiles.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ plette-0.4.4.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  ├─ WHEEL
│  │  │  │     │  └─ zip-safe
│  │  │  │     ├─ portalocker
│  │  │  │     │  ├─ constants.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ portalocker.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ redis.py
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ __about__.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ constants.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ portalocker.cpython-310.pyc
│  │  │  │     │     ├─ redis.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ __about__.cpython-310.pyc
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ portalocker-2.8.2.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pycparser
│  │  │  │     │  ├─ ast_transforms.py
│  │  │  │     │  ├─ c_ast.py
│  │  │  │     │  ├─ c_generator.py
│  │  │  │     │  ├─ c_lexer.py
│  │  │  │     │  ├─ c_parser.py
│  │  │  │     │  ├─ lextab.py
│  │  │  │     │  ├─ ply
│  │  │  │     │  │  ├─ cpp.py
│  │  │  │     │  │  ├─ ctokens.py
│  │  │  │     │  │  ├─ lex.py
│  │  │  │     │  │  ├─ yacc.py
│  │  │  │     │  │  ├─ ygen.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ cpp.cpython-310.pyc
│  │  │  │     │  │     ├─ ctokens.cpython-310.pyc
│  │  │  │     │  │     ├─ lex.cpython-310.pyc
│  │  │  │     │  │     ├─ yacc.cpython-310.pyc
│  │  │  │     │  │     ├─ ygen.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ plyparser.py
│  │  │  │     │  ├─ yacctab.py
│  │  │  │     │  ├─ _ast_gen.py
│  │  │  │     │  ├─ _build_tables.py
│  │  │  │     │  ├─ _c_ast.cfg
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ ast_transforms.cpython-310.pyc
│  │  │  │     │     ├─ c_ast.cpython-310.pyc
│  │  │  │     │     ├─ c_generator.cpython-310.pyc
│  │  │  │     │     ├─ c_lexer.cpython-310.pyc
│  │  │  │     │     ├─ c_parser.cpython-310.pyc
│  │  │  │     │     ├─ lextab.cpython-310.pyc
│  │  │  │     │     ├─ plyparser.cpython-310.pyc
│  │  │  │     │     ├─ yacctab.cpython-310.pyc
│  │  │  │     │     ├─ _ast_gen.cpython-310.pyc
│  │  │  │     │     ├─ _build_tables.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ pycparser-2.21.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pydantic
│  │  │  │     │  ├─ alias_generators.py
│  │  │  │     │  ├─ annotated_handlers.py
│  │  │  │     │  ├─ class_validators.py
│  │  │  │     │  ├─ color.py
│  │  │  │     │  ├─ config.py
│  │  │  │     │  ├─ dataclasses.py
│  │  │  │     │  ├─ datetime_parse.py
│  │  │  │     │  ├─ decorator.py
│  │  │  │     │  ├─ deprecated
│  │  │  │     │  │  ├─ class_validators.py
│  │  │  │     │  │  ├─ config.py
│  │  │  │     │  │  ├─ copy_internals.py
│  │  │  │     │  │  ├─ decorator.py
│  │  │  │     │  │  ├─ json.py
│  │  │  │     │  │  ├─ parse.py
│  │  │  │     │  │  ├─ tools.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ class_validators.cpython-310.pyc
│  │  │  │     │  │     ├─ config.cpython-310.pyc
│  │  │  │     │  │     ├─ copy_internals.cpython-310.pyc
│  │  │  │     │  │     ├─ decorator.cpython-310.pyc
│  │  │  │     │  │     ├─ json.cpython-310.pyc
│  │  │  │     │  │     ├─ parse.cpython-310.pyc
│  │  │  │     │  │     ├─ tools.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ env_settings.py
│  │  │  │     │  ├─ errors.py
│  │  │  │     │  ├─ error_wrappers.py
│  │  │  │     │  ├─ fields.py
│  │  │  │     │  ├─ functional_serializers.py
│  │  │  │     │  ├─ functional_validators.py
│  │  │  │     │  ├─ generics.py
│  │  │  │     │  ├─ json.py
│  │  │  │     │  ├─ json_schema.py
│  │  │  │     │  ├─ main.py
│  │  │  │     │  ├─ mypy.py
│  │  │  │     │  ├─ networks.py
│  │  │  │     │  ├─ parse.py
│  │  │  │     │  ├─ plugin
│  │  │  │     │  │  ├─ _loader.py
│  │  │  │     │  │  ├─ _schema_validator.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ _loader.cpython-310.pyc
│  │  │  │     │  │     ├─ _schema_validator.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ root_model.py
│  │  │  │     │  ├─ schema.py
│  │  │  │     │  ├─ tools.py
│  │  │  │     │  ├─ types.py
│  │  │  │     │  ├─ type_adapter.py
│  │  │  │     │  ├─ typing.py
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ v1
│  │  │  │     │  │  ├─ annotated_types.py
│  │  │  │     │  │  ├─ class_validators.py
│  │  │  │     │  │  ├─ color.py
│  │  │  │     │  │  ├─ config.py
│  │  │  │     │  │  ├─ dataclasses.py
│  │  │  │     │  │  ├─ datetime_parse.py
│  │  │  │     │  │  ├─ decorator.py
│  │  │  │     │  │  ├─ env_settings.py
│  │  │  │     │  │  ├─ errors.py
│  │  │  │     │  │  ├─ error_wrappers.py
│  │  │  │     │  │  ├─ fields.py
│  │  │  │     │  │  ├─ generics.py
│  │  │  │     │  │  ├─ json.py
│  │  │  │     │  │  ├─ main.py
│  │  │  │     │  │  ├─ mypy.py
│  │  │  │     │  │  ├─ networks.py
│  │  │  │     │  │  ├─ parse.py
│  │  │  │     │  │  ├─ py.typed
│  │  │  │     │  │  ├─ schema.py
│  │  │  │     │  │  ├─ tools.py
│  │  │  │     │  │  ├─ types.py
│  │  │  │     │  │  ├─ typing.py
│  │  │  │     │  │  ├─ utils.py
│  │  │  │     │  │  ├─ validators.py
│  │  │  │     │  │  ├─ version.py
│  │  │  │     │  │  ├─ _hypothesis_plugin.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ annotated_types.cpython-310.pyc
│  │  │  │     │  │     ├─ class_validators.cpython-310.pyc
│  │  │  │     │  │     ├─ color.cpython-310.pyc
│  │  │  │     │  │     ├─ config.cpython-310.pyc
│  │  │  │     │  │     ├─ dataclasses.cpython-310.pyc
│  │  │  │     │  │     ├─ datetime_parse.cpython-310.pyc
│  │  │  │     │  │     ├─ decorator.cpython-310.pyc
│  │  │  │     │  │     ├─ env_settings.cpython-310.pyc
│  │  │  │     │  │     ├─ errors.cpython-310.pyc
│  │  │  │     │  │     ├─ error_wrappers.cpython-310.pyc
│  │  │  │     │  │     ├─ fields.cpython-310.pyc
│  │  │  │     │  │     ├─ generics.cpython-310.pyc
│  │  │  │     │  │     ├─ json.cpython-310.pyc
│  │  │  │     │  │     ├─ main.cpython-310.pyc
│  │  │  │     │  │     ├─ mypy.cpython-310.pyc
│  │  │  │     │  │     ├─ networks.cpython-310.pyc
│  │  │  │     │  │     ├─ parse.cpython-310.pyc
│  │  │  │     │  │     ├─ schema.cpython-310.pyc
│  │  │  │     │  │     ├─ tools.cpython-310.pyc
│  │  │  │     │  │     ├─ types.cpython-310.pyc
│  │  │  │     │  │     ├─ typing.cpython-310.pyc
│  │  │  │     │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │     ├─ validators.cpython-310.pyc
│  │  │  │     │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │     ├─ _hypothesis_plugin.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ validate_call_decorator.py
│  │  │  │     │  ├─ validators.py
│  │  │  │     │  ├─ version.py
│  │  │  │     │  ├─ warnings.py
│  │  │  │     │  ├─ _internal
│  │  │  │     │  │  ├─ _config.py
│  │  │  │     │  │  ├─ _core_metadata.py
│  │  │  │     │  │  ├─ _core_utils.py
│  │  │  │     │  │  ├─ _dataclasses.py
│  │  │  │     │  │  ├─ _decorators.py
│  │  │  │     │  │  ├─ _decorators_v1.py
│  │  │  │     │  │  ├─ _discriminated_union.py
│  │  │  │     │  │  ├─ _fields.py
│  │  │  │     │  │  ├─ _forward_ref.py
│  │  │  │     │  │  ├─ _generate_schema.py
│  │  │  │     │  │  ├─ _generics.py
│  │  │  │     │  │  ├─ _internal_dataclass.py
│  │  │  │     │  │  ├─ _known_annotated_metadata.py
│  │  │  │     │  │  ├─ _mock_val_ser.py
│  │  │  │     │  │  ├─ _model_construction.py
│  │  │  │     │  │  ├─ _repr.py
│  │  │  │     │  │  ├─ _schema_generation_shared.py
│  │  │  │     │  │  ├─ _std_types_schema.py
│  │  │  │     │  │  ├─ _typing_extra.py
│  │  │  │     │  │  ├─ _utils.py
│  │  │  │     │  │  ├─ _validate_call.py
│  │  │  │     │  │  ├─ _validators.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ _config.cpython-310.pyc
│  │  │  │     │  │     ├─ _core_metadata.cpython-310.pyc
│  │  │  │     │  │     ├─ _core_utils.cpython-310.pyc
│  │  │  │     │  │     ├─ _dataclasses.cpython-310.pyc
│  │  │  │     │  │     ├─ _decorators.cpython-310.pyc
│  │  │  │     │  │     ├─ _decorators_v1.cpython-310.pyc
│  │  │  │     │  │     ├─ _discriminated_union.cpython-310.pyc
│  │  │  │     │  │     ├─ _fields.cpython-310.pyc
│  │  │  │     │  │     ├─ _forward_ref.cpython-310.pyc
│  │  │  │     │  │     ├─ _generate_schema.cpython-310.pyc
│  │  │  │     │  │     ├─ _generics.cpython-310.pyc
│  │  │  │     │  │     ├─ _internal_dataclass.cpython-310.pyc
│  │  │  │     │  │     ├─ _known_annotated_metadata.cpython-310.pyc
│  │  │  │     │  │     ├─ _mock_val_ser.cpython-310.pyc
│  │  │  │     │  │     ├─ _model_construction.cpython-310.pyc
│  │  │  │     │  │     ├─ _repr.cpython-310.pyc
│  │  │  │     │  │     ├─ _schema_generation_shared.cpython-310.pyc
│  │  │  │     │  │     ├─ _std_types_schema.cpython-310.pyc
│  │  │  │     │  │     ├─ _typing_extra.cpython-310.pyc
│  │  │  │     │  │     ├─ _utils.cpython-310.pyc
│  │  │  │     │  │     ├─ _validate_call.cpython-310.pyc
│  │  │  │     │  │     ├─ _validators.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _migration.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ alias_generators.cpython-310.pyc
│  │  │  │     │     ├─ annotated_handlers.cpython-310.pyc
│  │  │  │     │     ├─ class_validators.cpython-310.pyc
│  │  │  │     │     ├─ color.cpython-310.pyc
│  │  │  │     │     ├─ config.cpython-310.pyc
│  │  │  │     │     ├─ dataclasses.cpython-310.pyc
│  │  │  │     │     ├─ datetime_parse.cpython-310.pyc
│  │  │  │     │     ├─ decorator.cpython-310.pyc
│  │  │  │     │     ├─ env_settings.cpython-310.pyc
│  │  │  │     │     ├─ errors.cpython-310.pyc
│  │  │  │     │     ├─ error_wrappers.cpython-310.pyc
│  │  │  │     │     ├─ fields.cpython-310.pyc
│  │  │  │     │     ├─ functional_serializers.cpython-310.pyc
│  │  │  │     │     ├─ functional_validators.cpython-310.pyc
│  │  │  │     │     ├─ generics.cpython-310.pyc
│  │  │  │     │     ├─ json.cpython-310.pyc
│  │  │  │     │     ├─ json_schema.cpython-310.pyc
│  │  │  │     │     ├─ main.cpython-310.pyc
│  │  │  │     │     ├─ mypy.cpython-310.pyc
│  │  │  │     │     ├─ networks.cpython-310.pyc
│  │  │  │     │     ├─ parse.cpython-310.pyc
│  │  │  │     │     ├─ root_model.cpython-310.pyc
│  │  │  │     │     ├─ schema.cpython-310.pyc
│  │  │  │     │     ├─ tools.cpython-310.pyc
│  │  │  │     │     ├─ types.cpython-310.pyc
│  │  │  │     │     ├─ type_adapter.cpython-310.pyc
│  │  │  │     │     ├─ typing.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     ├─ validate_call_decorator.cpython-310.pyc
│  │  │  │     │     ├─ validators.cpython-310.pyc
│  │  │  │     │     ├─ version.cpython-310.pyc
│  │  │  │     │     ├─ warnings.cpython-310.pyc
│  │  │  │     │     ├─ _migration.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ pydantic-2.5.1.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  └─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pydantic_core
│  │  │  │     │  ├─ core_schema.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ _pydantic_core.cp310-win_amd64.pyd
│  │  │  │     │  ├─ _pydantic_core.pyi
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ core_schema.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ pydantic_core-2.14.3.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ license_files
│  │  │  │     │  │  └─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ PyJWT-2.8.0.dist-info
│  │  │  │     │  ├─ AUTHORS.rst
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ pythoncom.py
│  │  │  │     ├─ pythonwin
│  │  │  │     │  ├─ dde.pyd
│  │  │  │     │  ├─ license.txt
│  │  │  │     │  ├─ mfc140u.dll
│  │  │  │     │  ├─ Pythonwin.exe
│  │  │  │     │  ├─ pywin
│  │  │  │     │  │  ├─ debugger
│  │  │  │     │  │  │  ├─ configui.py
│  │  │  │     │  │  │  ├─ dbgcon.py
│  │  │  │     │  │  │  ├─ dbgpyapp.py
│  │  │  │     │  │  │  ├─ debugger.py
│  │  │  │     │  │  │  ├─ fail.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ configui.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dbgcon.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dbgpyapp.cpython-310.pyc
│  │  │  │     │  │  │     ├─ debugger.cpython-310.pyc
│  │  │  │     │  │  │     ├─ fail.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ default.cfg
│  │  │  │     │  │  ├─ Demos
│  │  │  │     │  │  │  ├─ app
│  │  │  │     │  │  │  │  ├─ basictimerapp.py
│  │  │  │     │  │  │  │  ├─ customprint.py
│  │  │  │     │  │  │  │  ├─ demoutils.py
│  │  │  │     │  │  │  │  ├─ dlgappdemo.py
│  │  │  │     │  │  │  │  ├─ dojobapp.py
│  │  │  │     │  │  │  │  ├─ helloapp.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ basictimerapp.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ customprint.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ demoutils.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ dlgappdemo.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ dojobapp.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ helloapp.cpython-310.pyc
│  │  │  │     │  │  │  ├─ cmdserver.py
│  │  │  │     │  │  │  ├─ createwin.py
│  │  │  │     │  │  │  ├─ demoutils.py
│  │  │  │     │  │  │  ├─ dibdemo.py
│  │  │  │     │  │  │  ├─ dlgtest.py
│  │  │  │     │  │  │  ├─ dyndlg.py
│  │  │  │     │  │  │  ├─ fontdemo.py
│  │  │  │     │  │  │  ├─ guidemo.py
│  │  │  │     │  │  │  ├─ hiertest.py
│  │  │  │     │  │  │  ├─ menutest.py
│  │  │  │     │  │  │  ├─ objdoc.py
│  │  │  │     │  │  │  ├─ ocx
│  │  │  │     │  │  │  │  ├─ demoutils.py
│  │  │  │     │  │  │  │  ├─ flash.py
│  │  │  │     │  │  │  │  ├─ msoffice.py
│  │  │  │     │  │  │  │  ├─ ocxserialtest.py
│  │  │  │     │  │  │  │  ├─ ocxtest.py
│  │  │  │     │  │  │  │  ├─ webbrowser.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ demoutils.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ flash.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ msoffice.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ocxserialtest.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ocxtest.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ webbrowser.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ openGLDemo.py
│  │  │  │     │  │  │  ├─ progressbar.py
│  │  │  │     │  │  │  ├─ sliderdemo.py
│  │  │  │     │  │  │  ├─ splittst.py
│  │  │  │     │  │  │  ├─ threadedgui.py
│  │  │  │     │  │  │  ├─ toolbar.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ cmdserver.cpython-310.pyc
│  │  │  │     │  │  │     ├─ createwin.cpython-310.pyc
│  │  │  │     │  │  │     ├─ demoutils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dibdemo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dlgtest.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dyndlg.cpython-310.pyc
│  │  │  │     │  │  │     ├─ fontdemo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ guidemo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hiertest.cpython-310.pyc
│  │  │  │     │  │  │     ├─ menutest.cpython-310.pyc
│  │  │  │     │  │  │     ├─ objdoc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ openGLDemo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ progressbar.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sliderdemo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ splittst.cpython-310.pyc
│  │  │  │     │  │  │     ├─ threadedgui.cpython-310.pyc
│  │  │  │     │  │  │     └─ toolbar.cpython-310.pyc
│  │  │  │     │  │  ├─ dialogs
│  │  │  │     │  │  │  ├─ ideoptions.py
│  │  │  │     │  │  │  ├─ list.py
│  │  │  │     │  │  │  ├─ login.py
│  │  │  │     │  │  │  ├─ status.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ ideoptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ list.cpython-310.pyc
│  │  │  │     │  │  │     ├─ login.cpython-310.pyc
│  │  │  │     │  │  │     ├─ status.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ docking
│  │  │  │     │  │  │  ├─ DockingBar.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ DockingBar.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ framework
│  │  │  │     │  │  │  ├─ app.py
│  │  │  │     │  │  │  ├─ bitmap.py
│  │  │  │     │  │  │  ├─ cmdline.py
│  │  │  │     │  │  │  ├─ dbgcommands.py
│  │  │  │     │  │  │  ├─ dlgappcore.py
│  │  │  │     │  │  │  ├─ editor
│  │  │  │     │  │  │  │  ├─ color
│  │  │  │     │  │  │  │  │  ├─ coloreditor.py
│  │  │  │     │  │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │  │     ├─ coloreditor.cpython-310.pyc
│  │  │  │     │  │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  │  ├─ configui.py
│  │  │  │     │  │  │  │  ├─ document.py
│  │  │  │     │  │  │  │  ├─ editor.py
│  │  │  │     │  │  │  │  ├─ frame.py
│  │  │  │     │  │  │  │  ├─ ModuleBrowser.py
│  │  │  │     │  │  │  │  ├─ template.py
│  │  │  │     │  │  │  │  ├─ vss.py
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ configui.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ document.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ editor.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ frame.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ ModuleBrowser.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ template.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ vss.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ help.py
│  │  │  │     │  │  │  ├─ interact.py
│  │  │  │     │  │  │  ├─ intpyapp.py
│  │  │  │     │  │  │  ├─ intpydde.py
│  │  │  │     │  │  │  ├─ mdi_pychecker.py
│  │  │  │     │  │  │  ├─ scriptutils.py
│  │  │  │     │  │  │  ├─ sgrepmdi.py
│  │  │  │     │  │  │  ├─ startup.py
│  │  │  │     │  │  │  ├─ stdin.py
│  │  │  │     │  │  │  ├─ toolmenu.py
│  │  │  │     │  │  │  ├─ window.py
│  │  │  │     │  │  │  ├─ winout.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ app.cpython-310.pyc
│  │  │  │     │  │  │     ├─ bitmap.cpython-310.pyc
│  │  │  │     │  │  │     ├─ cmdline.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dbgcommands.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dlgappcore.cpython-310.pyc
│  │  │  │     │  │  │     ├─ help.cpython-310.pyc
│  │  │  │     │  │  │     ├─ interact.cpython-310.pyc
│  │  │  │     │  │  │     ├─ intpyapp.cpython-310.pyc
│  │  │  │     │  │  │     ├─ intpydde.cpython-310.pyc
│  │  │  │     │  │  │     ├─ mdi_pychecker.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scriptutils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sgrepmdi.cpython-310.pyc
│  │  │  │     │  │  │     ├─ startup.cpython-310.pyc
│  │  │  │     │  │  │     ├─ stdin.cpython-310.pyc
│  │  │  │     │  │  │     ├─ toolmenu.cpython-310.pyc
│  │  │  │     │  │  │     ├─ window.cpython-310.pyc
│  │  │  │     │  │  │     ├─ winout.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ idle
│  │  │  │     │  │  │  ├─ AutoExpand.py
│  │  │  │     │  │  │  ├─ AutoIndent.py
│  │  │  │     │  │  │  ├─ CallTips.py
│  │  │  │     │  │  │  ├─ FormatParagraph.py
│  │  │  │     │  │  │  ├─ IdleHistory.py
│  │  │  │     │  │  │  ├─ PyParse.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ AutoExpand.cpython-310.pyc
│  │  │  │     │  │  │     ├─ AutoIndent.cpython-310.pyc
│  │  │  │     │  │  │     ├─ CallTips.cpython-310.pyc
│  │  │  │     │  │  │     ├─ FormatParagraph.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IdleHistory.cpython-310.pyc
│  │  │  │     │  │  │     ├─ PyParse.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ IDLE.cfg
│  │  │  │     │  │  ├─ mfc
│  │  │  │     │  │  │  ├─ activex.py
│  │  │  │     │  │  │  ├─ afxres.py
│  │  │  │     │  │  │  ├─ dialog.py
│  │  │  │     │  │  │  ├─ docview.py
│  │  │  │     │  │  │  ├─ object.py
│  │  │  │     │  │  │  ├─ thread.py
│  │  │  │     │  │  │  ├─ window.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ activex.cpython-310.pyc
│  │  │  │     │  │  │     ├─ afxres.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dialog.cpython-310.pyc
│  │  │  │     │  │  │     ├─ docview.cpython-310.pyc
│  │  │  │     │  │  │     ├─ object.cpython-310.pyc
│  │  │  │     │  │  │     ├─ thread.cpython-310.pyc
│  │  │  │     │  │  │     ├─ window.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ scintilla
│  │  │  │     │  │  │  ├─ bindings.py
│  │  │  │     │  │  │  ├─ config.py
│  │  │  │     │  │  │  ├─ configui.py
│  │  │  │     │  │  │  ├─ control.py
│  │  │  │     │  │  │  ├─ document.py
│  │  │  │     │  │  │  ├─ find.py
│  │  │  │     │  │  │  ├─ formatter.py
│  │  │  │     │  │  │  ├─ IDLEenvironment.py
│  │  │  │     │  │  │  ├─ keycodes.py
│  │  │  │     │  │  │  ├─ scintillacon.py
│  │  │  │     │  │  │  ├─ view.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ bindings.cpython-310.pyc
│  │  │  │     │  │  │     ├─ config.cpython-310.pyc
│  │  │  │     │  │  │     ├─ configui.cpython-310.pyc
│  │  │  │     │  │  │     ├─ control.cpython-310.pyc
│  │  │  │     │  │  │     ├─ document.cpython-310.pyc
│  │  │  │     │  │  │     ├─ find.cpython-310.pyc
│  │  │  │     │  │  │     ├─ formatter.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IDLEenvironment.cpython-310.pyc
│  │  │  │     │  │  │     ├─ keycodes.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scintillacon.cpython-310.pyc
│  │  │  │     │  │  │     ├─ view.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ tools
│  │  │  │     │  │  │  ├─ browseProjects.py
│  │  │  │     │  │  │  ├─ browser.py
│  │  │  │     │  │  │  ├─ hierlist.py
│  │  │  │     │  │  │  ├─ regedit.py
│  │  │  │     │  │  │  ├─ regpy.py
│  │  │  │     │  │  │  ├─ TraceCollector.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ browseProjects.cpython-310.pyc
│  │  │  │     │  │  │     ├─ browser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ hierlist.cpython-310.pyc
│  │  │  │     │  │  │     ├─ regedit.cpython-310.pyc
│  │  │  │     │  │  │     ├─ regpy.cpython-310.pyc
│  │  │  │     │  │  │     ├─ TraceCollector.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ scintilla.dll
│  │  │  │     │  ├─ start_pythonwin.pyw
│  │  │  │     │  ├─ win32ui.pyd
│  │  │  │     │  └─ win32uiole.pyd
│  │  │  │     ├─ pywin32-306.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ PyWin32.chm
│  │  │  │     ├─ pywin32.pth
│  │  │  │     ├─ pywin32.version.txt
│  │  │  │     ├─ pywin32_system32
│  │  │  │     │  ├─ pythoncom310.dll
│  │  │  │     │  └─ pywintypes310.dll
│  │  │  │     ├─ PyYAML-6.0.1.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ referencing
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ jsonschema.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ retrieval.py
│  │  │  │     │  ├─ tests
│  │  │  │     │  │  ├─ test_core.py
│  │  │  │     │  │  ├─ test_exceptions.py
│  │  │  │     │  │  ├─ test_jsonschema.py
│  │  │  │     │  │  ├─ test_referencing_suite.py
│  │  │  │     │  │  ├─ test_retrieval.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ test_core.cpython-310.pyc
│  │  │  │     │  │     ├─ test_exceptions.cpython-310.pyc
│  │  │  │     │  │     ├─ test_jsonschema.cpython-310.pyc
│  │  │  │     │  │     ├─ test_referencing_suite.cpython-310.pyc
│  │  │  │     │  │     ├─ test_retrieval.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ typing.py
│  │  │  │     │  ├─ _attrs.py
│  │  │  │     │  ├─ _attrs.pyi
│  │  │  │     │  ├─ _core.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ jsonschema.cpython-310.pyc
│  │  │  │     │     ├─ retrieval.cpython-310.pyc
│  │  │  │     │     ├─ typing.cpython-310.pyc
│  │  │  │     │     ├─ _attrs.cpython-310.pyc
│  │  │  │     │     ├─ _core.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ referencing-0.32.1.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  └─ COPYING
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ requests
│  │  │  │     │  ├─ adapters.py
│  │  │  │     │  ├─ api.py
│  │  │  │     │  ├─ auth.py
│  │  │  │     │  ├─ certs.py
│  │  │  │     │  ├─ compat.py
│  │  │  │     │  ├─ cookies.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ help.py
│  │  │  │     │  ├─ models.py
│  │  │  │     │  ├─ packages.py
│  │  │  │     │  ├─ sessions.py
│  │  │  │     │  ├─ status_codes.py
│  │  │  │     │  ├─ structures.py
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ _internal_utils.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __pycache__
│  │  │  │     │  │  ├─ adapters.cpython-310.pyc
│  │  │  │     │  │  ├─ api.cpython-310.pyc
│  │  │  │     │  │  ├─ auth.cpython-310.pyc
│  │  │  │     │  │  ├─ certs.cpython-310.pyc
│  │  │  │     │  │  ├─ compat.cpython-310.pyc
│  │  │  │     │  │  ├─ cookies.cpython-310.pyc
│  │  │  │     │  │  ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  ├─ help.cpython-310.pyc
│  │  │  │     │  │  ├─ models.cpython-310.pyc
│  │  │  │     │  │  ├─ packages.cpython-310.pyc
│  │  │  │     │  │  ├─ sessions.cpython-310.pyc
│  │  │  │     │  │  ├─ status_codes.cpython-310.pyc
│  │  │  │     │  │  ├─ structures.cpython-310.pyc
│  │  │  │     │  │  ├─ utils.cpython-310.pyc
│  │  │  │     │  │  ├─ _internal_utils.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.cpython-310.pyc
│  │  │  │     │  │  └─ __version__.cpython-310.pyc
│  │  │  │     │  └─ __version__.py
│  │  │  │     ├─ requests-2.31.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ requirementslib
│  │  │  │     │  ├─ environment.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ fileutils.py
│  │  │  │     │  ├─ funktools.py
│  │  │  │     │  ├─ models
│  │  │  │     │  │  ├─ common.py
│  │  │  │     │  │  ├─ dependencies.py
│  │  │  │     │  │  ├─ lockfile.py
│  │  │  │     │  │  ├─ markers.py
│  │  │  │     │  │  ├─ metadata.py
│  │  │  │     │  │  ├─ old_pip_utils.py
│  │  │  │     │  │  ├─ pipfile.py
│  │  │  │     │  │  ├─ project.py
│  │  │  │     │  │  ├─ requirements.py
│  │  │  │     │  │  ├─ setup_info.py
│  │  │  │     │  │  ├─ url.py
│  │  │  │     │  │  ├─ utils.py
│  │  │  │     │  │  ├─ vcs.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ common.cpython-310.pyc
│  │  │  │     │  │     ├─ dependencies.cpython-310.pyc
│  │  │  │     │  │     ├─ lockfile.cpython-310.pyc
│  │  │  │     │  │     ├─ markers.cpython-310.pyc
│  │  │  │     │  │     ├─ metadata.cpython-310.pyc
│  │  │  │     │  │     ├─ old_pip_utils.cpython-310.pyc
│  │  │  │     │  │     ├─ pipfile.cpython-310.pyc
│  │  │  │     │  │     ├─ project.cpython-310.pyc
│  │  │  │     │  │     ├─ requirements.cpython-310.pyc
│  │  │  │     │  │     ├─ setup_info.cpython-310.pyc
│  │  │  │     │  │     ├─ url.cpython-310.pyc
│  │  │  │     │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │     ├─ vcs.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ utils.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ environment.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ fileutils.cpython-310.pyc
│  │  │  │     │     ├─ funktools.cpython-310.pyc
│  │  │  │     │     ├─ utils.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ requirementslib-3.0.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  ├─ WHEEL
│  │  │  │     │  └─ zip-safe
│  │  │  │     ├─ rpds
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ rpds.cp310-win_amd64.pyd
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __init__.pyi
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ rpds_py-0.17.1.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ license_files
│  │  │  │     │  │  └─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ ruff
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  ├─ __main__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ __init__.cpython-310.pyc
│  │  │  │     │     └─ __main__.cpython-310.pyc
│  │  │  │     ├─ ruff-0.1.6.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ license_files
│  │  │  │     │  │  └─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ schemas
│  │  │  │     │  ├─ case-schedule.schema.json
│  │  │  │     │  ├─ commands
│  │  │  │     │  │  ├─ interested-party.schema.json
│  │  │  │     │  │  ├─ new-deadline-submission.schema.json
│  │  │  │     │  │  ├─ nsip-exam-timetable-submission.schema.json
│  │  │  │     │  │  ├─ register-nsip-subscription.schema.json
│  │  │  │     │  │  ├─ register-representation.schema.json
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ employee.schema.json
│  │  │  │     │  ├─ nsip-document.schema.json
│  │  │  │     │  ├─ nsip-exam-timetable.schema.json
│  │  │  │     │  ├─ nsip-project-update.schema.json
│  │  │  │     │  ├─ nsip-project.schema.json
│  │  │  │     │  ├─ nsip-representation.schema.json
│  │  │  │     │  ├─ nsip-subscription.schema.json
│  │  │  │     │  ├─ s51-advice.schema.json
│  │  │  │     │  ├─ service-user.schema.json
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ setuptools
│  │  │  │     │  ├─ archive_util.py
│  │  │  │     │  ├─ build_meta.py
│  │  │  │     │  ├─ cli-32.exe
│  │  │  │     │  ├─ cli-64.exe
│  │  │  │     │  ├─ cli-arm64.exe
│  │  │  │     │  ├─ cli.exe
│  │  │  │     │  ├─ command
│  │  │  │     │  │  ├─ alias.py
│  │  │  │     │  │  ├─ bdist_egg.py
│  │  │  │     │  │  ├─ bdist_rpm.py
│  │  │  │     │  │  ├─ build.py
│  │  │  │     │  │  ├─ build_clib.py
│  │  │  │     │  │  ├─ build_ext.py
│  │  │  │     │  │  ├─ build_py.py
│  │  │  │     │  │  ├─ develop.py
│  │  │  │     │  │  ├─ dist_info.py
│  │  │  │     │  │  ├─ easy_install.py
│  │  │  │     │  │  ├─ editable_wheel.py
│  │  │  │     │  │  ├─ egg_info.py
│  │  │  │     │  │  ├─ install.py
│  │  │  │     │  │  ├─ install_egg_info.py
│  │  │  │     │  │  ├─ install_lib.py
│  │  │  │     │  │  ├─ install_scripts.py
│  │  │  │     │  │  ├─ launcher manifest.xml
│  │  │  │     │  │  ├─ py36compat.py
│  │  │  │     │  │  ├─ register.py
│  │  │  │     │  │  ├─ rotate.py
│  │  │  │     │  │  ├─ saveopts.py
│  │  │  │     │  │  ├─ sdist.py
│  │  │  │     │  │  ├─ setopt.py
│  │  │  │     │  │  ├─ test.py
│  │  │  │     │  │  ├─ upload.py
│  │  │  │     │  │  ├─ upload_docs.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ alias.cpython-310.pyc
│  │  │  │     │  │     ├─ bdist_egg.cpython-310.pyc
│  │  │  │     │  │     ├─ bdist_rpm.cpython-310.pyc
│  │  │  │     │  │     ├─ build.cpython-310.pyc
│  │  │  │     │  │     ├─ build_clib.cpython-310.pyc
│  │  │  │     │  │     ├─ build_ext.cpython-310.pyc
│  │  │  │     │  │     ├─ build_py.cpython-310.pyc
│  │  │  │     │  │     ├─ develop.cpython-310.pyc
│  │  │  │     │  │     ├─ dist_info.cpython-310.pyc
│  │  │  │     │  │     ├─ easy_install.cpython-310.pyc
│  │  │  │     │  │     ├─ editable_wheel.cpython-310.pyc
│  │  │  │     │  │     ├─ egg_info.cpython-310.pyc
│  │  │  │     │  │     ├─ install.cpython-310.pyc
│  │  │  │     │  │     ├─ install_egg_info.cpython-310.pyc
│  │  │  │     │  │     ├─ install_lib.cpython-310.pyc
│  │  │  │     │  │     ├─ install_scripts.cpython-310.pyc
│  │  │  │     │  │     ├─ py36compat.cpython-310.pyc
│  │  │  │     │  │     ├─ register.cpython-310.pyc
│  │  │  │     │  │     ├─ rotate.cpython-310.pyc
│  │  │  │     │  │     ├─ saveopts.cpython-310.pyc
│  │  │  │     │  │     ├─ sdist.cpython-310.pyc
│  │  │  │     │  │     ├─ setopt.cpython-310.pyc
│  │  │  │     │  │     ├─ test.cpython-310.pyc
│  │  │  │     │  │     ├─ upload.cpython-310.pyc
│  │  │  │     │  │     ├─ upload_docs.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ config
│  │  │  │     │  │  ├─ expand.py
│  │  │  │     │  │  ├─ pyprojecttoml.py
│  │  │  │     │  │  ├─ setupcfg.py
│  │  │  │     │  │  ├─ _apply_pyprojecttoml.py
│  │  │  │     │  │  ├─ _validate_pyproject
│  │  │  │     │  │  │  ├─ error_reporting.py
│  │  │  │     │  │  │  ├─ extra_validations.py
│  │  │  │     │  │  │  ├─ fastjsonschema_exceptions.py
│  │  │  │     │  │  │  ├─ fastjsonschema_validations.py
│  │  │  │     │  │  │  ├─ formats.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ error_reporting.cpython-310.pyc
│  │  │  │     │  │  │     ├─ extra_validations.cpython-310.pyc
│  │  │  │     │  │  │     ├─ fastjsonschema_exceptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ fastjsonschema_validations.cpython-310.pyc
│  │  │  │     │  │  │     ├─ formats.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ expand.cpython-310.pyc
│  │  │  │     │  │     ├─ pyprojecttoml.cpython-310.pyc
│  │  │  │     │  │     ├─ setupcfg.cpython-310.pyc
│  │  │  │     │  │     ├─ _apply_pyprojecttoml.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ depends.py
│  │  │  │     │  ├─ dep_util.py
│  │  │  │     │  ├─ discovery.py
│  │  │  │     │  ├─ dist.py
│  │  │  │     │  ├─ errors.py
│  │  │  │     │  ├─ extension.py
│  │  │  │     │  ├─ extern
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ glob.py
│  │  │  │     │  ├─ gui-32.exe
│  │  │  │     │  ├─ gui-64.exe
│  │  │  │     │  ├─ gui-arm64.exe
│  │  │  │     │  ├─ gui.exe
│  │  │  │     │  ├─ installer.py
│  │  │  │     │  ├─ launch.py
│  │  │  │     │  ├─ logging.py
│  │  │  │     │  ├─ monkey.py
│  │  │  │     │  ├─ msvc.py
│  │  │  │     │  ├─ namespaces.py
│  │  │  │     │  ├─ package_index.py
│  │  │  │     │  ├─ py34compat.py
│  │  │  │     │  ├─ sandbox.py
│  │  │  │     │  ├─ script (dev).tmpl
│  │  │  │     │  ├─ script.tmpl
│  │  │  │     │  ├─ unicode_utils.py
│  │  │  │     │  ├─ version.py
│  │  │  │     │  ├─ wheel.py
│  │  │  │     │  ├─ windows_support.py
│  │  │  │     │  ├─ _deprecation_warning.py
│  │  │  │     │  ├─ _distutils
│  │  │  │     │  │  ├─ archive_util.py
│  │  │  │     │  │  ├─ bcppcompiler.py
│  │  │  │     │  │  ├─ ccompiler.py
│  │  │  │     │  │  ├─ cmd.py
│  │  │  │     │  │  ├─ command
│  │  │  │     │  │  │  ├─ bdist.py
│  │  │  │     │  │  │  ├─ bdist_dumb.py
│  │  │  │     │  │  │  ├─ bdist_rpm.py
│  │  │  │     │  │  │  ├─ build.py
│  │  │  │     │  │  │  ├─ build_clib.py
│  │  │  │     │  │  │  ├─ build_ext.py
│  │  │  │     │  │  │  ├─ build_py.py
│  │  │  │     │  │  │  ├─ build_scripts.py
│  │  │  │     │  │  │  ├─ check.py
│  │  │  │     │  │  │  ├─ clean.py
│  │  │  │     │  │  │  ├─ config.py
│  │  │  │     │  │  │  ├─ install.py
│  │  │  │     │  │  │  ├─ install_data.py
│  │  │  │     │  │  │  ├─ install_egg_info.py
│  │  │  │     │  │  │  ├─ install_headers.py
│  │  │  │     │  │  │  ├─ install_lib.py
│  │  │  │     │  │  │  ├─ install_scripts.py
│  │  │  │     │  │  │  ├─ py37compat.py
│  │  │  │     │  │  │  ├─ register.py
│  │  │  │     │  │  │  ├─ sdist.py
│  │  │  │     │  │  │  ├─ upload.py
│  │  │  │     │  │  │  ├─ _framework_compat.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ bdist.cpython-310.pyc
│  │  │  │     │  │  │     ├─ bdist_dumb.cpython-310.pyc
│  │  │  │     │  │  │     ├─ bdist_rpm.cpython-310.pyc
│  │  │  │     │  │  │     ├─ build.cpython-310.pyc
│  │  │  │     │  │  │     ├─ build_clib.cpython-310.pyc
│  │  │  │     │  │  │     ├─ build_ext.cpython-310.pyc
│  │  │  │     │  │  │     ├─ build_py.cpython-310.pyc
│  │  │  │     │  │  │     ├─ build_scripts.cpython-310.pyc
│  │  │  │     │  │  │     ├─ check.cpython-310.pyc
│  │  │  │     │  │  │     ├─ clean.cpython-310.pyc
│  │  │  │     │  │  │     ├─ config.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install_data.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install_egg_info.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install_headers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install_lib.cpython-310.pyc
│  │  │  │     │  │  │     ├─ install_scripts.cpython-310.pyc
│  │  │  │     │  │  │     ├─ py37compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ register.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sdist.cpython-310.pyc
│  │  │  │     │  │  │     ├─ upload.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _framework_compat.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ config.py
│  │  │  │     │  │  ├─ core.py
│  │  │  │     │  │  ├─ cygwinccompiler.py
│  │  │  │     │  │  ├─ debug.py
│  │  │  │     │  │  ├─ dep_util.py
│  │  │  │     │  │  ├─ dir_util.py
│  │  │  │     │  │  ├─ dist.py
│  │  │  │     │  │  ├─ errors.py
│  │  │  │     │  │  ├─ extension.py
│  │  │  │     │  │  ├─ fancy_getopt.py
│  │  │  │     │  │  ├─ filelist.py
│  │  │  │     │  │  ├─ file_util.py
│  │  │  │     │  │  ├─ log.py
│  │  │  │     │  │  ├─ msvc9compiler.py
│  │  │  │     │  │  ├─ msvccompiler.py
│  │  │  │     │  │  ├─ py38compat.py
│  │  │  │     │  │  ├─ py39compat.py
│  │  │  │     │  │  ├─ spawn.py
│  │  │  │     │  │  ├─ sysconfig.py
│  │  │  │     │  │  ├─ text_file.py
│  │  │  │     │  │  ├─ unixccompiler.py
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ version.py
│  │  │  │     │  │  ├─ versionpredicate.py
│  │  │  │     │  │  ├─ _collections.py
│  │  │  │     │  │  ├─ _functools.py
│  │  │  │     │  │  ├─ _macos_compat.py
│  │  │  │     │  │  ├─ _msvccompiler.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ archive_util.cpython-310.pyc
│  │  │  │     │  │     ├─ bcppcompiler.cpython-310.pyc
│  │  │  │     │  │     ├─ ccompiler.cpython-310.pyc
│  │  │  │     │  │     ├─ cmd.cpython-310.pyc
│  │  │  │     │  │     ├─ config.cpython-310.pyc
│  │  │  │     │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │     ├─ cygwinccompiler.cpython-310.pyc
│  │  │  │     │  │     ├─ debug.cpython-310.pyc
│  │  │  │     │  │     ├─ dep_util.cpython-310.pyc
│  │  │  │     │  │     ├─ dir_util.cpython-310.pyc
│  │  │  │     │  │     ├─ dist.cpython-310.pyc
│  │  │  │     │  │     ├─ errors.cpython-310.pyc
│  │  │  │     │  │     ├─ extension.cpython-310.pyc
│  │  │  │     │  │     ├─ fancy_getopt.cpython-310.pyc
│  │  │  │     │  │     ├─ filelist.cpython-310.pyc
│  │  │  │     │  │     ├─ file_util.cpython-310.pyc
│  │  │  │     │  │     ├─ log.cpython-310.pyc
│  │  │  │     │  │     ├─ msvc9compiler.cpython-310.pyc
│  │  │  │     │  │     ├─ msvccompiler.cpython-310.pyc
│  │  │  │     │  │     ├─ py38compat.cpython-310.pyc
│  │  │  │     │  │     ├─ py39compat.cpython-310.pyc
│  │  │  │     │  │     ├─ spawn.cpython-310.pyc
│  │  │  │     │  │     ├─ sysconfig.cpython-310.pyc
│  │  │  │     │  │     ├─ text_file.cpython-310.pyc
│  │  │  │     │  │     ├─ unixccompiler.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │     ├─ versionpredicate.cpython-310.pyc
│  │  │  │     │  │     ├─ _collections.cpython-310.pyc
│  │  │  │     │  │     ├─ _functools.cpython-310.pyc
│  │  │  │     │  │     ├─ _macos_compat.cpython-310.pyc
│  │  │  │     │  │     ├─ _msvccompiler.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _entry_points.py
│  │  │  │     │  ├─ _imp.py
│  │  │  │     │  ├─ _importlib.py
│  │  │  │     │  ├─ _itertools.py
│  │  │  │     │  ├─ _path.py
│  │  │  │     │  ├─ _reqs.py
│  │  │  │     │  ├─ _vendor
│  │  │  │     │  │  ├─ importlib_metadata
│  │  │  │     │  │  │  ├─ _adapters.py
│  │  │  │     │  │  │  ├─ _collections.py
│  │  │  │     │  │  │  ├─ _compat.py
│  │  │  │     │  │  │  ├─ _functools.py
│  │  │  │     │  │  │  ├─ _itertools.py
│  │  │  │     │  │  │  ├─ _meta.py
│  │  │  │     │  │  │  ├─ _text.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _adapters.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _collections.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _functools.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _itertools.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _meta.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _text.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ importlib_resources
│  │  │  │     │  │  │  ├─ abc.py
│  │  │  │     │  │  │  ├─ readers.py
│  │  │  │     │  │  │  ├─ simple.py
│  │  │  │     │  │  │  ├─ _adapters.py
│  │  │  │     │  │  │  ├─ _common.py
│  │  │  │     │  │  │  ├─ _compat.py
│  │  │  │     │  │  │  ├─ _itertools.py
│  │  │  │     │  │  │  ├─ _legacy.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ abc.cpython-310.pyc
│  │  │  │     │  │  │     ├─ readers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ simple.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _adapters.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _common.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _compat.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _itertools.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _legacy.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ jaraco
│  │  │  │     │  │  │  ├─ context.py
│  │  │  │     │  │  │  ├─ functools.py
│  │  │  │     │  │  │  ├─ text
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ context.cpython-310.pyc
│  │  │  │     │  │  │     ├─ functools.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ more_itertools
│  │  │  │     │  │  │  ├─ more.py
│  │  │  │     │  │  │  ├─ recipes.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ more.cpython-310.pyc
│  │  │  │     │  │  │     ├─ recipes.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ ordered_set.py
│  │  │  │     │  │  ├─ packaging
│  │  │  │     │  │  │  ├─ markers.py
│  │  │  │     │  │  │  ├─ requirements.py
│  │  │  │     │  │  │  ├─ specifiers.py
│  │  │  │     │  │  │  ├─ tags.py
│  │  │  │     │  │  │  ├─ utils.py
│  │  │  │     │  │  │  ├─ version.py
│  │  │  │     │  │  │  ├─ _manylinux.py
│  │  │  │     │  │  │  ├─ _musllinux.py
│  │  │  │     │  │  │  ├─ _structures.py
│  │  │  │     │  │  │  ├─ __about__.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ markers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ requirements.cpython-310.pyc
│  │  │  │     │  │  │     ├─ specifiers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ tags.cpython-310.pyc
│  │  │  │     │  │  │     ├─ utils.cpython-310.pyc
│  │  │  │     │  │  │     ├─ version.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _manylinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _musllinux.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _structures.cpython-310.pyc
│  │  │  │     │  │  │     ├─ __about__.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ pyparsing
│  │  │  │     │  │  │  ├─ actions.py
│  │  │  │     │  │  │  ├─ common.py
│  │  │  │     │  │  │  ├─ core.py
│  │  │  │     │  │  │  ├─ diagram
│  │  │  │     │  │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  │  ├─ exceptions.py
│  │  │  │     │  │  │  ├─ helpers.py
│  │  │  │     │  │  │  ├─ results.py
│  │  │  │     │  │  │  ├─ testing.py
│  │  │  │     │  │  │  ├─ unicode.py
│  │  │  │     │  │  │  ├─ util.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ actions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ common.cpython-310.pyc
│  │  │  │     │  │  │     ├─ core.cpython-310.pyc
│  │  │  │     │  │  │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │  │  │     ├─ helpers.cpython-310.pyc
│  │  │  │     │  │  │     ├─ results.cpython-310.pyc
│  │  │  │     │  │  │     ├─ testing.cpython-310.pyc
│  │  │  │     │  │  │     ├─ unicode.cpython-310.pyc
│  │  │  │     │  │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ tomli
│  │  │  │     │  │  │  ├─ _parser.py
│  │  │  │     │  │  │  ├─ _re.py
│  │  │  │     │  │  │  ├─ _types.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ _parser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _re.cpython-310.pyc
│  │  │  │     │  │  │     ├─ _types.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ typing_extensions.py
│  │  │  │     │  │  ├─ zipp.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ ordered_set.cpython-310.pyc
│  │  │  │     │  │     ├─ typing_extensions.cpython-310.pyc
│  │  │  │     │  │     ├─ zipp.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ archive_util.cpython-310.pyc
│  │  │  │     │     ├─ build_meta.cpython-310.pyc
│  │  │  │     │     ├─ depends.cpython-310.pyc
│  │  │  │     │     ├─ dep_util.cpython-310.pyc
│  │  │  │     │     ├─ discovery.cpython-310.pyc
│  │  │  │     │     ├─ dist.cpython-310.pyc
│  │  │  │     │     ├─ errors.cpython-310.pyc
│  │  │  │     │     ├─ extension.cpython-310.pyc
│  │  │  │     │     ├─ glob.cpython-310.pyc
│  │  │  │     │     ├─ installer.cpython-310.pyc
│  │  │  │     │     ├─ launch.cpython-310.pyc
│  │  │  │     │     ├─ logging.cpython-310.pyc
│  │  │  │     │     ├─ monkey.cpython-310.pyc
│  │  │  │     │     ├─ msvc.cpython-310.pyc
│  │  │  │     │     ├─ namespaces.cpython-310.pyc
│  │  │  │     │     ├─ package_index.cpython-310.pyc
│  │  │  │     │     ├─ py34compat.cpython-310.pyc
│  │  │  │     │     ├─ sandbox.cpython-310.pyc
│  │  │  │     │     ├─ unicode_utils.cpython-310.pyc
│  │  │  │     │     ├─ version.cpython-310.pyc
│  │  │  │     │     ├─ wheel.cpython-310.pyc
│  │  │  │     │     ├─ windows_support.cpython-310.pyc
│  │  │  │     │     ├─ _deprecation_warning.cpython-310.pyc
│  │  │  │     │     ├─ _entry_points.cpython-310.pyc
│  │  │  │     │     ├─ _imp.cpython-310.pyc
│  │  │  │     │     ├─ _importlib.cpython-310.pyc
│  │  │  │     │     ├─ _itertools.cpython-310.pyc
│  │  │  │     │     ├─ _path.cpython-310.pyc
│  │  │  │     │     ├─ _reqs.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ setuptools-65.5.0.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ six-1.16.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ six.py
│  │  │  │     ├─ sniffio
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ _impl.py
│  │  │  │     │  ├─ _tests
│  │  │  │     │  │  ├─ test_sniffio.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ test_sniffio.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _version.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ _impl.cpython-310.pyc
│  │  │  │     │     ├─ _version.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ sniffio-1.3.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ LICENSE.APACHE2
│  │  │  │     │  ├─ LICENSE.MIT
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ sourcery
│  │  │  │     │  ├─ annoy
│  │  │  │     │  │  └─ annoylib.pyd
│  │  │  │     │  ├─ black
│  │  │  │     │  │  ├─ brackets.pyd
│  │  │  │     │  │  ├─ cache.pyd
│  │  │  │     │  │  ├─ comments.pyd
│  │  │  │     │  │  ├─ const.pyd
│  │  │  │     │  │  ├─ handle_ipynb_magics.pyd
│  │  │  │     │  │  ├─ linegen.pyd
│  │  │  │     │  │  ├─ lines.pyd
│  │  │  │     │  │  ├─ mode.pyd
│  │  │  │     │  │  ├─ nodes.pyd
│  │  │  │     │  │  ├─ numerics.pyd
│  │  │  │     │  │  ├─ parsing.pyd
│  │  │  │     │  │  ├─ ranges.pyd
│  │  │  │     │  │  ├─ rusty.pyd
│  │  │  │     │  │  ├─ strings.pyd
│  │  │  │     │  │  ├─ trans.pyd
│  │  │  │     │  │  └─ _width_table.pyd
│  │  │  │     │  ├─ blib2to3
│  │  │  │     │  │  ├─ Grammar.txt
│  │  │  │     │  │  ├─ LICENSE
│  │  │  │     │  │  ├─ PatternGrammar.txt
│  │  │  │     │  │  ├─ pgen2
│  │  │  │     │  │  │  ├─ driver.pyd
│  │  │  │     │  │  │  ├─ grammar.pyd
│  │  │  │     │  │  │  ├─ parse.pyd
│  │  │  │     │  │  │  ├─ pgen.pyd
│  │  │  │     │  │  │  ├─ token.pyd
│  │  │  │     │  │  │  └─ tokenize.pyd
│  │  │  │     │  │  ├─ pygram.pyd
│  │  │  │     │  │  ├─ pytree.pyd
│  │  │  │     │  │  └─ README
│  │  │  │     │  ├─ certifi
│  │  │  │     │  │  └─ cacert.pem
│  │  │  │     │  ├─ charset_normalizer
│  │  │  │     │  │  ├─ md.pyd
│  │  │  │     │  │  └─ md__mypyc.pyd
│  │  │  │     │  ├─ coding-assistant-app
│  │  │  │     │  │  └─ dist
│  │  │  │     │  │     └─ assets
│  │  │  │     │  │        ├─ index.css
│  │  │  │     │  │        ├─ index.js
│  │  │  │     │  │        └─ sourcery-logo.svg
│  │  │  │     │  ├─ concrt140.dll
│  │  │  │     │  ├─ cryptography
│  │  │  │     │  │  └─ hazmat
│  │  │  │     │  │     └─ bindings
│  │  │  │     │  │        ├─ _openssl.pyd
│  │  │  │     │  │        └─ _rust.pyd
│  │  │  │     │  ├─ google
│  │  │  │     │  │  └─ _upb
│  │  │  │     │  │     └─ _message.pyd
│  │  │  │     │  ├─ greenlet
│  │  │  │     │  │  └─ _greenlet.pyd
│  │  │  │     │  ├─ grpc
│  │  │  │     │  │  └─ _cython
│  │  │  │     │  │     ├─ cygrpc.pyd
│  │  │  │     │  │     └─ _credentials
│  │  │  │     │  │        └─ roots.pem
│  │  │  │     │  ├─ hub
│  │  │  │     │  │  └─ static
│  │  │  │     │  │     ├─ asset-manifest.json
│  │  │  │     │  │     ├─ favicon.png
│  │  │  │     │  │     ├─ index.html
│  │  │  │     │  │     ├─ input.css
│  │  │  │     │  │     ├─ manifest.json
│  │  │  │     │  │     ├─ MessinaSansMonoWeb-Bold.woff
│  │  │  │     │  │     ├─ MessinaSansMonoWeb-Regular.woff
│  │  │  │     │  │     ├─ MessinaSansWeb-Bold.woff
│  │  │  │     │  │     ├─ MessinaSansWeb-Regular.woff
│  │  │  │     │  │     ├─ output.css
│  │  │  │     │  │     ├─ robots.txt
│  │  │  │     │  │     └─ static
│  │  │  │     │  │        ├─ css
│  │  │  │     │  │        │  ├─ main.ed53125f.css
│  │  │  │     │  │        │  └─ main.ed53125f.css.map
│  │  │  │     │  │        ├─ js
│  │  │  │     │  │        │  ├─ main.658b590c.js
│  │  │  │     │  │        │  ├─ main.658b590c.js.LICENSE.txt
│  │  │  │     │  │        │  └─ main.658b590c.js.map
│  │  │  │     │  │        └─ media
│  │  │  │     │  │           ├─ icons.07ed0b60c13965581675.woff
│  │  │  │     │  │           ├─ icons.33055a2699783178df55.svg
│  │  │  │     │  │           ├─ icons.e3d35e8153c5ffaa069f.eot
│  │  │  │     │  │           ├─ icons.f39232cd335dc12e7d4f.woff2
│  │  │  │     │  │           ├─ icons.fdecd2d880938cae502a.ttf
│  │  │  │     │  │           ├─ javascript-original.7398a2b698ded0287e177bf456f9fd50.svg
│  │  │  │     │  │           ├─ lower-bg.ef732f44d29337d626ef.svg
│  │  │  │     │  │           ├─ python-original.ffa1251f749f6ab8768c5f32548e5b14.svg
│  │  │  │     │  │           ├─ simple-bg.5d316ef4d19ee3b7987c.svg
│  │  │  │     │  │           ├─ sourcery-logo.ab9811e301fd9354cd78e9d3500b014d.svg
│  │  │  │     │  │           └─ typescript-original.3505cfe6fdd885b1efaa87decf82f4d9.svg
│  │  │  │     │  ├─ languages.so
│  │  │  │     │  ├─ lib2to3
│  │  │  │     │  │  ├─ Grammar.txt
│  │  │  │     │  │  ├─ Grammar3.10.11.final.0.pickle
│  │  │  │     │  │  ├─ PatternGrammar.txt
│  │  │  │     │  │  ├─ PatternGrammar3.10.11.final.0.pickle
│  │  │  │     │  │  └─ tests
│  │  │  │     │  │     └─ data
│  │  │  │     │  │        └─ README
│  │  │  │     │  ├─ libcrypto-1_1.dll
│  │  │  │     │  ├─ libffi-7.dll
│  │  │  │     │  ├─ libssl-1_1.dll
│  │  │  │     │  ├─ lxml
│  │  │  │     │  │  ├─ builder.pyd
│  │  │  │     │  │  ├─ etree.pyd
│  │  │  │     │  │  ├─ objectify.pyd
│  │  │  │     │  │  ├─ sax.pyd
│  │  │  │     │  │  └─ _elementpath.pyd
│  │  │  │     │  ├─ markupsafe
│  │  │  │     │  │  └─ _speedups.pyd
│  │  │  │     │  ├─ msvcp140.dll
│  │  │  │     │  ├─ private_rules
│  │  │  │     │  │  └─ refactorings
│  │  │  │     │  │     ├─ identity-comprehension.yaml
│  │  │  │     │  │     └─ list-literal.yaml
│  │  │  │     │  ├─ public_rules
│  │  │  │     │  │  ├─ google-python-style-guide.yaml
│  │  │  │     │  │  ├─ LICENSE
│  │  │  │     │  │  ├─ README.md
│  │  │  │     │  │  ├─ remove-debugging-statements.yaml
│  │  │  │     │  │  └─ use-fstring.yaml
│  │  │  │     │  ├─ pydantic
│  │  │  │     │  │  ├─ annotated_types.pyd
│  │  │  │     │  │  ├─ class_validators.pyd
│  │  │  │     │  │  ├─ color.pyd
│  │  │  │     │  │  ├─ config.pyd
│  │  │  │     │  │  ├─ dataclasses.pyd
│  │  │  │     │  │  ├─ datetime_parse.pyd
│  │  │  │     │  │  ├─ decorator.pyd
│  │  │  │     │  │  ├─ env_settings.pyd
│  │  │  │     │  │  ├─ errors.pyd
│  │  │  │     │  │  ├─ error_wrappers.pyd
│  │  │  │     │  │  ├─ fields.pyd
│  │  │  │     │  │  ├─ json.pyd
│  │  │  │     │  │  ├─ main.pyd
│  │  │  │     │  │  ├─ mypy.pyd
│  │  │  │     │  │  ├─ networks.pyd
│  │  │  │     │  │  ├─ parse.pyd
│  │  │  │     │  │  ├─ schema.pyd
│  │  │  │     │  │  ├─ tools.pyd
│  │  │  │     │  │  ├─ types.pyd
│  │  │  │     │  │  ├─ typing.pyd
│  │  │  │     │  │  ├─ utils.pyd
│  │  │  │     │  │  ├─ validators.pyd
│  │  │  │     │  │  └─ version.pyd
│  │  │  │     │  ├─ pyexpat.pyd
│  │  │  │     │  ├─ pysolvers.pyd
│  │  │  │     │  ├─ python3.dll
│  │  │  │     │  ├─ python310.dll
│  │  │  │     │  ├─ rules
│  │  │  │     │  │  ├─ java
│  │  │  │     │  │  │  └─ java-rules.yaml
│  │  │  │     │  │  ├─ javascript
│  │  │  │     │  │  │  ├─ assignment-operator.yaml
│  │  │  │     │  │  │  ├─ avoid-function-declarations-in-blocks.yaml
│  │  │  │     │  │  │  ├─ avoid-infinite-loops.yaml
│  │  │  │     │  │  │  ├─ avoid-jumping-in-finally.yaml
│  │  │  │     │  │  │  ├─ avoid-using-var.yaml
│  │  │  │     │  │  │  ├─ binary-operator-identity.yaml
│  │  │  │     │  │  │  ├─ combine-object-destructuring.yaml
│  │  │  │     │  │  │  ├─ de-morgan.yaml
│  │  │  │     │  │  │  ├─ dont-concatenate-string-literals.yaml
│  │  │  │     │  │  │  ├─ dont-negate-is-instanceof-operands.yaml
│  │  │  │     │  │  │  ├─ dont-reassign-caught-exceptions.yaml
│  │  │  │     │  │  │  ├─ dont-reassign-foreach-variables.yaml
│  │  │  │     │  │  │  ├─ dont-reassign-parameters.yaml
│  │  │  │     │  │  │  ├─ dont-self-assign-variables.yaml
│  │  │  │     │  │  │  ├─ dont-shadow-arguments.yaml
│  │  │  │     │  │  │  ├─ dont-use-with.yaml
│  │  │  │     │  │  │  ├─ dont-use-wrappers-for-builtins.yaml
│  │  │  │     │  │  │  ├─ flatten-nested-try.yaml
│  │  │  │     │  │  │  ├─ flip-comparison.yaml
│  │  │  │     │  │  │  ├─ generators-should-yield.yaml
│  │  │  │     │  │  │  ├─ inline-immediately-returned-variable.yaml
│  │  │  │     │  │  │  ├─ invert-ternary.yaml
│  │  │  │     │  │  │  ├─ max-min.yaml
│  │  │  │     │  │  │  ├─ merge-assign-operators.yaml
│  │  │  │     │  │  │  ├─ merge-else-if.yaml
│  │  │  │     │  │  │  ├─ merge_nested_ifs.yaml
│  │  │  │     │  │  │  ├─ misplaced-break-or-continue.yaml
│  │  │  │     │  │  │  ├─ no-eval.yaml
│  │  │  │     │  │  │  ├─ no-new-function.yaml
│  │  │  │     │  │  │  ├─ no-new-symbol.yaml
│  │  │  │     │  │  │  ├─ only-delete-object-properties.yaml
│  │  │  │     │  │  │  ├─ possible-incorrect-bitwise-operator.yaml
│  │  │  │     │  │  │  ├─ prefer-arrow-callback.yaml
│  │  │  │     │  │  │  ├─ remove-redundant-boolean.yaml
│  │  │  │     │  │  │  ├─ remove-redundant-if-statement.yaml
│  │  │  │     │  │  │  ├─ remove-redundant-slice-index.yaml
│  │  │  │     │  │  │  ├─ remove-unreachable-code.yaml
│  │  │  │     │  │  │  ├─ return-outside-function.yaml
│  │  │  │     │  │  │  ├─ simplify-ternary.yaml
│  │  │  │     │  │  │  ├─ throw-new-errors.yaml
│  │  │  │     │  │  │  ├─ use-array-literal.yaml
│  │  │  │     │  │  │  ├─ use-braces.yaml
│  │  │  │     │  │  │  ├─ use-object-destructuring.yaml
│  │  │  │     │  │  │  ├─ use-ternary-operator.yaml
│  │  │  │     │  │  │  ├─ while-guard-to-condition.yaml
│  │  │  │     │  │  │  ├─ wrap-immediately-invoked-function-expressions.yaml
│  │  │  │     │  │  │  └─ yield-outside-generator.yaml
│  │  │  │     │  │  └─ python
│  │  │  │     │  │     ├─ break-or-continue-outside-loop.yaml
│  │  │  │     │  │     ├─ dict-literal.yaml
│  │  │  │     │  │     ├─ merge-nested-ifs.yaml
│  │  │  │     │  │     ├─ no-complex-code-in-tests.yaml
│  │  │  │     │  │     ├─ or-if-exp-identity.yaml
│  │  │  │     │  │     ├─ pandas-chain-methods.yaml
│  │  │  │     │  │     ├─ raise-specific-error.yaml
│  │  │  │     │  │     ├─ remove-none-from-default-get.yaml
│  │  │  │     │  │     ├─ remove-redundant-path-exists.yaml
│  │  │  │     │  │     ├─ remove-unit-step-from-range.yaml
│  │  │  │     │  │     ├─ remove-zero-from-range.yaml
│  │  │  │     │  │     ├─ simplify-constant-sum.yaml
│  │  │  │     │  │     ├─ swap-if-expression.yaml
│  │  │  │     │  │     ├─ tuple-literal.yaml
│  │  │  │     │  │     ├─ use-iloc-for-indexing.yaml
│  │  │  │     │  │     ├─ use-isna.yaml
│  │  │  │     │  │     ├─ use-or-for-fallback.yaml
│  │  │  │     │  │     ├─ useless-else-on-loop.yaml
│  │  │  │     │  │     └─ while-guard-to-condition.yaml
│  │  │  │     │  ├─ select.pyd
│  │  │  │     │  ├─ sourcery.exe
│  │  │  │     │  ├─ sqlalchemy
│  │  │  │     │  │  ├─ cimmutabledict.pyd
│  │  │  │     │  │  ├─ cprocessors.pyd
│  │  │  │     │  │  └─ cresultproxy.pyd
│  │  │  │     │  ├─ sqlite3.dll
│  │  │  │     │  ├─ tree_sitter
│  │  │  │     │  │  └─ binding.pyd
│  │  │  │     │  ├─ ucrtbase.dll
│  │  │  │     │  ├─ ujson.pyd
│  │  │  │     │  ├─ unicodedata.pyd
│  │  │  │     │  ├─ vcruntime140.dll
│  │  │  │     │  ├─ vcruntime140_1.dll
│  │  │  │     │  ├─ wrapper.py
│  │  │  │     │  ├─ wrapt
│  │  │  │     │  │  └─ _wrappers.pyd
│  │  │  │     │  ├─ xxhash
│  │  │  │     │  │  └─ _xxhash.pyd
│  │  │  │     │  ├─ yaml
│  │  │  │     │  │  └─ _yaml.pyd
│  │  │  │     │  ├─ zstandard
│  │  │  │     │  │  ├─ backend_c.pyd
│  │  │  │     │  │  └─ _cffi.pyd
│  │  │  │     │  ├─ _asyncio.pyd
│  │  │  │     │  ├─ _bz2.pyd
│  │  │  │     │  ├─ _cffi_backend.pyd
│  │  │  │     │  ├─ _ctypes.pyd
│  │  │  │     │  ├─ _decimal.pyd
│  │  │  │     │  ├─ _elementtree.pyd
│  │  │  │     │  ├─ _hashlib.pyd
│  │  │  │     │  ├─ _lzma.pyd
│  │  │  │     │  ├─ _multiprocessing.pyd
│  │  │  │     │  ├─ _overlapped.pyd
│  │  │  │     │  ├─ _queue.pyd
│  │  │  │     │  ├─ _ruamel_yaml.pyd
│  │  │  │     │  ├─ _socket.pyd
│  │  │  │     │  ├─ _sqlite3.pyd
│  │  │  │     │  ├─ _ssl.pyd
│  │  │  │     │  ├─ _uuid.pyd
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     └─ wrapper.cpython-310.pyc
│  │  │  │     ├─ sourcery-1.14.0.dist-info
│  │  │  │     │  ├─ entry_points.txt
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ REQUESTED
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ tests
│  │  │  │     │  ├─ test_client.py
│  │  │  │     │  ├─ test_exceptions.py
│  │  │  │     │  ├─ test_package.py
│  │  │  │     │  ├─ test_parse.py
│  │  │  │     │  ├─ test_release.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ test_client.cpython-310.pyc
│  │  │  │     │     ├─ test_exceptions.cpython-310.pyc
│  │  │  │     │     ├─ test_package.cpython-310.pyc
│  │  │  │     │     ├─ test_parse.cpython-310.pyc
│  │  │  │     │     ├─ test_release.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ toml
│  │  │  │     │  ├─ decoder.py
│  │  │  │     │  ├─ encoder.py
│  │  │  │     │  ├─ ordered.py
│  │  │  │     │  ├─ tz.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ decoder.cpython-310.pyc
│  │  │  │     │     ├─ encoder.cpython-310.pyc
│  │  │  │     │     ├─ ordered.cpython-310.pyc
│  │  │  │     │     ├─ tz.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ toml-0.10.2.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ tomli
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ _parser.py
│  │  │  │     │  ├─ _re.py
│  │  │  │     │  ├─ _types.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ _parser.cpython-310.pyc
│  │  │  │     │     ├─ _re.cpython-310.pyc
│  │  │  │     │     ├─ _types.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ tomli-2.0.1.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ tomlkit
│  │  │  │     │  ├─ api.py
│  │  │  │     │  ├─ container.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ items.py
│  │  │  │     │  ├─ parser.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ source.py
│  │  │  │     │  ├─ toml_char.py
│  │  │  │     │  ├─ toml_document.py
│  │  │  │     │  ├─ toml_file.py
│  │  │  │     │  ├─ _compat.py
│  │  │  │     │  ├─ _types.py
│  │  │  │     │  ├─ _utils.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ api.cpython-310.pyc
│  │  │  │     │     ├─ container.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ items.cpython-310.pyc
│  │  │  │     │     ├─ parser.cpython-310.pyc
│  │  │  │     │     ├─ source.cpython-310.pyc
│  │  │  │     │     ├─ toml_char.cpython-310.pyc
│  │  │  │     │     ├─ toml_document.cpython-310.pyc
│  │  │  │     │     ├─ toml_file.cpython-310.pyc
│  │  │  │     │     ├─ _compat.cpython-310.pyc
│  │  │  │     │     ├─ _types.cpython-310.pyc
│  │  │  │     │     ├─ _utils.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ tomlkit-0.12.3.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ typing_extensions-4.8.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ LICENSE
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ typing_extensions.py
│  │  │  │     ├─ urllib3
│  │  │  │     │  ├─ connection.py
│  │  │  │     │  ├─ connectionpool.py
│  │  │  │     │  ├─ contrib
│  │  │  │     │  │  ├─ pyopenssl.py
│  │  │  │     │  │  ├─ socks.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ pyopenssl.cpython-310.pyc
│  │  │  │     │  │     ├─ socks.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ fields.py
│  │  │  │     │  ├─ filepost.py
│  │  │  │     │  ├─ poolmanager.py
│  │  │  │     │  ├─ py.typed
│  │  │  │     │  ├─ response.py
│  │  │  │     │  ├─ util
│  │  │  │     │  │  ├─ connection.py
│  │  │  │     │  │  ├─ proxy.py
│  │  │  │     │  │  ├─ request.py
│  │  │  │     │  │  ├─ response.py
│  │  │  │     │  │  ├─ retry.py
│  │  │  │     │  │  ├─ ssltransport.py
│  │  │  │     │  │  ├─ ssl_.py
│  │  │  │     │  │  ├─ ssl_match_hostname.py
│  │  │  │     │  │  ├─ timeout.py
│  │  │  │     │  │  ├─ url.py
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ wait.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ connection.cpython-310.pyc
│  │  │  │     │  │     ├─ proxy.cpython-310.pyc
│  │  │  │     │  │     ├─ request.cpython-310.pyc
│  │  │  │     │  │     ├─ response.cpython-310.pyc
│  │  │  │     │  │     ├─ retry.cpython-310.pyc
│  │  │  │     │  │     ├─ ssltransport.cpython-310.pyc
│  │  │  │     │  │     ├─ ssl_.cpython-310.pyc
│  │  │  │     │  │     ├─ ssl_match_hostname.cpython-310.pyc
│  │  │  │     │  │     ├─ timeout.cpython-310.pyc
│  │  │  │     │  │     ├─ url.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     ├─ wait.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ _base_connection.py
│  │  │  │     │  ├─ _collections.py
│  │  │  │     │  ├─ _request_methods.py
│  │  │  │     │  ├─ _version.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ connection.cpython-310.pyc
│  │  │  │     │     ├─ connectionpool.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ fields.cpython-310.pyc
│  │  │  │     │     ├─ filepost.cpython-310.pyc
│  │  │  │     │     ├─ poolmanager.cpython-310.pyc
│  │  │  │     │     ├─ response.cpython-310.pyc
│  │  │  │     │     ├─ _base_connection.cpython-310.pyc
│  │  │  │     │     ├─ _collections.cpython-310.pyc
│  │  │  │     │     ├─ _request_methods.cpython-310.pyc
│  │  │  │     │     ├─ _version.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ urllib3-2.1.0.dist-info
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ licenses
│  │  │  │     │  │  └─ LICENSE.txt
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  └─ WHEEL
│  │  │  │     ├─ win32
│  │  │  │     │  ├─ Demos
│  │  │  │     │  │  ├─ BackupRead_BackupWrite.py
│  │  │  │     │  │  ├─ BackupSeek_streamheaders.py
│  │  │  │     │  │  ├─ cerapi.py
│  │  │  │     │  │  ├─ CopyFileEx.py
│  │  │  │     │  │  ├─ CreateFileTransacted_MiniVersion.py
│  │  │  │     │  │  ├─ c_extension
│  │  │  │     │  │  │  ├─ setup.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ setup.cpython-310.pyc
│  │  │  │     │  │  ├─ dde
│  │  │  │     │  │  │  ├─ ddeclient.py
│  │  │  │     │  │  │  ├─ ddeserver.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ ddeclient.cpython-310.pyc
│  │  │  │     │  │  │     └─ ddeserver.cpython-310.pyc
│  │  │  │     │  │  ├─ desktopmanager.py
│  │  │  │     │  │  ├─ eventLogDemo.py
│  │  │  │     │  │  ├─ EvtFormatMessage.py
│  │  │  │     │  │  ├─ EvtSubscribe_pull.py
│  │  │  │     │  │  ├─ EvtSubscribe_push.py
│  │  │  │     │  │  ├─ FileSecurityTest.py
│  │  │  │     │  │  ├─ getfilever.py
│  │  │  │     │  │  ├─ GetSaveFileName.py
│  │  │  │     │  │  ├─ images
│  │  │  │     │  │  │  ├─ frowny.bmp
│  │  │  │     │  │  │  └─ smiley.bmp
│  │  │  │     │  │  ├─ mmapfile_demo.py
│  │  │  │     │  │  ├─ NetValidatePasswordPolicy.py
│  │  │  │     │  │  ├─ OpenEncryptedFileRaw.py
│  │  │  │     │  │  ├─ pipes
│  │  │  │     │  │  │  ├─ cat.py
│  │  │  │     │  │  │  ├─ runproc.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ cat.cpython-310.pyc
│  │  │  │     │  │  │     └─ runproc.cpython-310.pyc
│  │  │  │     │  │  ├─ print_desktop.py
│  │  │  │     │  │  ├─ rastest.py
│  │  │  │     │  │  ├─ RegCreateKeyTransacted.py
│  │  │  │     │  │  ├─ RegRestoreKey.py
│  │  │  │     │  │  ├─ security
│  │  │  │     │  │  │  ├─ account_rights.py
│  │  │  │     │  │  │  ├─ explicit_entries.py
│  │  │  │     │  │  │  ├─ GetTokenInformation.py
│  │  │  │     │  │  │  ├─ get_policy_info.py
│  │  │  │     │  │  │  ├─ list_rights.py
│  │  │  │     │  │  │  ├─ localized_names.py
│  │  │  │     │  │  │  ├─ lsaregevent.py
│  │  │  │     │  │  │  ├─ lsastore.py
│  │  │  │     │  │  │  ├─ query_information.py
│  │  │  │     │  │  │  ├─ regsave_sa.py
│  │  │  │     │  │  │  ├─ regsecurity.py
│  │  │  │     │  │  │  ├─ sa_inherit.py
│  │  │  │     │  │  │  ├─ security_enums.py
│  │  │  │     │  │  │  ├─ setkernelobjectsecurity.py
│  │  │  │     │  │  │  ├─ setnamedsecurityinfo.py
│  │  │  │     │  │  │  ├─ setsecurityinfo.py
│  │  │  │     │  │  │  ├─ setuserobjectsecurity.py
│  │  │  │     │  │  │  ├─ set_file_audit.py
│  │  │  │     │  │  │  ├─ set_file_owner.py
│  │  │  │     │  │  │  ├─ set_policy_info.py
│  │  │  │     │  │  │  ├─ sspi
│  │  │  │     │  │  │  │  ├─ fetch_url.py
│  │  │  │     │  │  │  │  ├─ simple_auth.py
│  │  │  │     │  │  │  │  ├─ socket_server.py
│  │  │  │     │  │  │  │  ├─ validate_password.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ fetch_url.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ simple_auth.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ socket_server.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ validate_password.cpython-310.pyc
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ account_rights.cpython-310.pyc
│  │  │  │     │  │  │     ├─ explicit_entries.cpython-310.pyc
│  │  │  │     │  │  │     ├─ GetTokenInformation.cpython-310.pyc
│  │  │  │     │  │  │     ├─ get_policy_info.cpython-310.pyc
│  │  │  │     │  │  │     ├─ list_rights.cpython-310.pyc
│  │  │  │     │  │  │     ├─ localized_names.cpython-310.pyc
│  │  │  │     │  │  │     ├─ lsaregevent.cpython-310.pyc
│  │  │  │     │  │  │     ├─ lsastore.cpython-310.pyc
│  │  │  │     │  │  │     ├─ query_information.cpython-310.pyc
│  │  │  │     │  │  │     ├─ regsave_sa.cpython-310.pyc
│  │  │  │     │  │  │     ├─ regsecurity.cpython-310.pyc
│  │  │  │     │  │  │     ├─ sa_inherit.cpython-310.pyc
│  │  │  │     │  │  │     ├─ security_enums.cpython-310.pyc
│  │  │  │     │  │  │     ├─ setkernelobjectsecurity.cpython-310.pyc
│  │  │  │     │  │  │     ├─ setnamedsecurityinfo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ setsecurityinfo.cpython-310.pyc
│  │  │  │     │  │  │     ├─ setuserobjectsecurity.cpython-310.pyc
│  │  │  │     │  │  │     ├─ set_file_audit.cpython-310.pyc
│  │  │  │     │  │  │     ├─ set_file_owner.cpython-310.pyc
│  │  │  │     │  │  │     └─ set_policy_info.cpython-310.pyc
│  │  │  │     │  │  ├─ service
│  │  │  │     │  │  │  ├─ nativePipeTestService.py
│  │  │  │     │  │  │  ├─ pipeTestService.py
│  │  │  │     │  │  │  ├─ pipeTestServiceClient.py
│  │  │  │     │  │  │  ├─ serviceEvents.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ nativePipeTestService.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pipeTestService.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pipeTestServiceClient.cpython-310.pyc
│  │  │  │     │  │  │     └─ serviceEvents.cpython-310.pyc
│  │  │  │     │  │  ├─ SystemParametersInfo.py
│  │  │  │     │  │  ├─ timer_demo.py
│  │  │  │     │  │  ├─ win32clipboardDemo.py
│  │  │  │     │  │  ├─ win32clipboard_bitmapdemo.py
│  │  │  │     │  │  ├─ win32comport_demo.py
│  │  │  │     │  │  ├─ win32console_demo.py
│  │  │  │     │  │  ├─ win32cred_demo.py
│  │  │  │     │  │  ├─ win32fileDemo.py
│  │  │  │     │  │  ├─ win32gui_demo.py
│  │  │  │     │  │  ├─ win32gui_devicenotify.py
│  │  │  │     │  │  ├─ win32gui_dialog.py
│  │  │  │     │  │  ├─ win32gui_menu.py
│  │  │  │     │  │  ├─ win32gui_taskbar.py
│  │  │  │     │  │  ├─ win32netdemo.py
│  │  │  │     │  │  ├─ win32rcparser_demo.py
│  │  │  │     │  │  ├─ win32servicedemo.py
│  │  │  │     │  │  ├─ win32ts_logoff_disconnected.py
│  │  │  │     │  │  ├─ win32wnet
│  │  │  │     │  │  │  ├─ testwnet.py
│  │  │  │     │  │  │  ├─ winnetwk.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ testwnet.cpython-310.pyc
│  │  │  │     │  │  │     └─ winnetwk.cpython-310.pyc
│  │  │  │     │  │  ├─ winprocess.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ BackupRead_BackupWrite.cpython-310.pyc
│  │  │  │     │  │     ├─ BackupSeek_streamheaders.cpython-310.pyc
│  │  │  │     │  │     ├─ cerapi.cpython-310.pyc
│  │  │  │     │  │     ├─ CopyFileEx.cpython-310.pyc
│  │  │  │     │  │     ├─ CreateFileTransacted_MiniVersion.cpython-310.pyc
│  │  │  │     │  │     ├─ desktopmanager.cpython-310.pyc
│  │  │  │     │  │     ├─ eventLogDemo.cpython-310.pyc
│  │  │  │     │  │     ├─ EvtFormatMessage.cpython-310.pyc
│  │  │  │     │  │     ├─ EvtSubscribe_pull.cpython-310.pyc
│  │  │  │     │  │     ├─ EvtSubscribe_push.cpython-310.pyc
│  │  │  │     │  │     ├─ FileSecurityTest.cpython-310.pyc
│  │  │  │     │  │     ├─ getfilever.cpython-310.pyc
│  │  │  │     │  │     ├─ GetSaveFileName.cpython-310.pyc
│  │  │  │     │  │     ├─ mmapfile_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ NetValidatePasswordPolicy.cpython-310.pyc
│  │  │  │     │  │     ├─ OpenEncryptedFileRaw.cpython-310.pyc
│  │  │  │     │  │     ├─ print_desktop.cpython-310.pyc
│  │  │  │     │  │     ├─ rastest.cpython-310.pyc
│  │  │  │     │  │     ├─ RegCreateKeyTransacted.cpython-310.pyc
│  │  │  │     │  │     ├─ RegRestoreKey.cpython-310.pyc
│  │  │  │     │  │     ├─ SystemParametersInfo.cpython-310.pyc
│  │  │  │     │  │     ├─ timer_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32clipboardDemo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32clipboard_bitmapdemo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32comport_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32console_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32cred_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32fileDemo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32gui_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32gui_devicenotify.cpython-310.pyc
│  │  │  │     │  │     ├─ win32gui_dialog.cpython-310.pyc
│  │  │  │     │  │     ├─ win32gui_menu.cpython-310.pyc
│  │  │  │     │  │     ├─ win32gui_taskbar.cpython-310.pyc
│  │  │  │     │  │     ├─ win32netdemo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32rcparser_demo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32servicedemo.cpython-310.pyc
│  │  │  │     │  │     ├─ win32ts_logoff_disconnected.cpython-310.pyc
│  │  │  │     │  │     └─ winprocess.cpython-310.pyc
│  │  │  │     │  ├─ include
│  │  │  │     │  │  └─ PyWinTypes.h
│  │  │  │     │  ├─ lib
│  │  │  │     │  │  ├─ afxres.py
│  │  │  │     │  │  ├─ commctrl.py
│  │  │  │     │  │  ├─ dbi.py
│  │  │  │     │  │  ├─ mmsystem.py
│  │  │  │     │  │  ├─ netbios.py
│  │  │  │     │  │  ├─ ntsecuritycon.py
│  │  │  │     │  │  ├─ pywin32_bootstrap.py
│  │  │  │     │  │  ├─ pywin32_testutil.py
│  │  │  │     │  │  ├─ pywintypes.py
│  │  │  │     │  │  ├─ rasutil.py
│  │  │  │     │  │  ├─ regcheck.py
│  │  │  │     │  │  ├─ regutil.py
│  │  │  │     │  │  ├─ sspi.py
│  │  │  │     │  │  ├─ sspicon.py
│  │  │  │     │  │  ├─ win2kras.py
│  │  │  │     │  │  ├─ win32con.py
│  │  │  │     │  │  ├─ win32cryptcon.py
│  │  │  │     │  │  ├─ win32evtlogutil.py
│  │  │  │     │  │  ├─ win32gui_struct.py
│  │  │  │     │  │  ├─ win32inetcon.py
│  │  │  │     │  │  ├─ win32netcon.py
│  │  │  │     │  │  ├─ win32pdhquery.py
│  │  │  │     │  │  ├─ win32pdhutil.py
│  │  │  │     │  │  ├─ win32rcparser.py
│  │  │  │     │  │  ├─ win32serviceutil.py
│  │  │  │     │  │  ├─ win32timezone.py
│  │  │  │     │  │  ├─ win32traceutil.py
│  │  │  │     │  │  ├─ win32verstamp.py
│  │  │  │     │  │  ├─ winerror.py
│  │  │  │     │  │  ├─ winioctlcon.py
│  │  │  │     │  │  ├─ winnt.py
│  │  │  │     │  │  ├─ winperf.py
│  │  │  │     │  │  ├─ winxptheme.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ afxres.cpython-310.pyc
│  │  │  │     │  │     ├─ commctrl.cpython-310.pyc
│  │  │  │     │  │     ├─ dbi.cpython-310.pyc
│  │  │  │     │  │     ├─ mmsystem.cpython-310.pyc
│  │  │  │     │  │     ├─ netbios.cpython-310.pyc
│  │  │  │     │  │     ├─ ntsecuritycon.cpython-310.pyc
│  │  │  │     │  │     ├─ pywin32_bootstrap.cpython-310.pyc
│  │  │  │     │  │     ├─ pywin32_testutil.cpython-310.pyc
│  │  │  │     │  │     ├─ pywintypes.cpython-310.pyc
│  │  │  │     │  │     ├─ rasutil.cpython-310.pyc
│  │  │  │     │  │     ├─ regcheck.cpython-310.pyc
│  │  │  │     │  │     ├─ regutil.cpython-310.pyc
│  │  │  │     │  │     ├─ sspi.cpython-310.pyc
│  │  │  │     │  │     ├─ sspicon.cpython-310.pyc
│  │  │  │     │  │     ├─ win2kras.cpython-310.pyc
│  │  │  │     │  │     ├─ win32con.cpython-310.pyc
│  │  │  │     │  │     ├─ win32cryptcon.cpython-310.pyc
│  │  │  │     │  │     ├─ win32evtlogutil.cpython-310.pyc
│  │  │  │     │  │     ├─ win32gui_struct.cpython-310.pyc
│  │  │  │     │  │     ├─ win32inetcon.cpython-310.pyc
│  │  │  │     │  │     ├─ win32netcon.cpython-310.pyc
│  │  │  │     │  │     ├─ win32pdhquery.cpython-310.pyc
│  │  │  │     │  │     ├─ win32pdhutil.cpython-310.pyc
│  │  │  │     │  │     ├─ win32rcparser.cpython-310.pyc
│  │  │  │     │  │     ├─ win32serviceutil.cpython-310.pyc
│  │  │  │     │  │     ├─ win32timezone.cpython-310.pyc
│  │  │  │     │  │     ├─ win32traceutil.cpython-310.pyc
│  │  │  │     │  │     ├─ win32verstamp.cpython-310.pyc
│  │  │  │     │  │     ├─ winerror.cpython-310.pyc
│  │  │  │     │  │     ├─ winioctlcon.cpython-310.pyc
│  │  │  │     │  │     ├─ winnt.cpython-310.pyc
│  │  │  │     │  │     ├─ winperf.cpython-310.pyc
│  │  │  │     │  │     └─ winxptheme.cpython-310.pyc
│  │  │  │     │  ├─ libs
│  │  │  │     │  │  └─ pywintypes.lib
│  │  │  │     │  ├─ license.txt
│  │  │  │     │  ├─ mmapfile.pyd
│  │  │  │     │  ├─ odbc.pyd
│  │  │  │     │  ├─ perfmon.pyd
│  │  │  │     │  ├─ perfmondata.dll
│  │  │  │     │  ├─ pythonservice.exe
│  │  │  │     │  ├─ scripts
│  │  │  │     │  │  ├─ backupEventLog.py
│  │  │  │     │  │  ├─ ce
│  │  │  │     │  │  │  ├─ pysynch.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ pysynch.cpython-310.pyc
│  │  │  │     │  │  ├─ ControlService.py
│  │  │  │     │  │  ├─ killProcName.py
│  │  │  │     │  │  ├─ rasutil.py
│  │  │  │     │  │  ├─ regsetup.py
│  │  │  │     │  │  ├─ setup_d.py
│  │  │  │     │  │  ├─ VersionStamp
│  │  │  │     │  │  │  ├─ BrandProject.py
│  │  │  │     │  │  │  ├─ bulkstamp.py
│  │  │  │     │  │  │  ├─ vssutil.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ BrandProject.cpython-310.pyc
│  │  │  │     │  │  │     ├─ bulkstamp.cpython-310.pyc
│  │  │  │     │  │  │     └─ vssutil.cpython-310.pyc
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ backupEventLog.cpython-310.pyc
│  │  │  │     │  │     ├─ ControlService.cpython-310.pyc
│  │  │  │     │  │     ├─ killProcName.cpython-310.pyc
│  │  │  │     │  │     ├─ rasutil.cpython-310.pyc
│  │  │  │     │  │     ├─ regsetup.cpython-310.pyc
│  │  │  │     │  │     └─ setup_d.cpython-310.pyc
│  │  │  │     │  ├─ servicemanager.pyd
│  │  │  │     │  ├─ test
│  │  │  │     │  │  ├─ handles.py
│  │  │  │     │  │  ├─ testall.py
│  │  │  │     │  │  ├─ test_clipboard.py
│  │  │  │     │  │  ├─ test_exceptions.py
│  │  │  │     │  │  ├─ test_odbc.py
│  │  │  │     │  │  ├─ test_pywintypes.py
│  │  │  │     │  │  ├─ test_security.py
│  │  │  │     │  │  ├─ test_sspi.py
│  │  │  │     │  │  ├─ test_win32api.py
│  │  │  │     │  │  ├─ test_win32crypt.py
│  │  │  │     │  │  ├─ test_win32event.py
│  │  │  │     │  │  ├─ test_win32file.py
│  │  │  │     │  │  ├─ test_win32gui.py
│  │  │  │     │  │  ├─ test_win32guistruct.py
│  │  │  │     │  │  ├─ test_win32inet.py
│  │  │  │     │  │  ├─ test_win32net.py
│  │  │  │     │  │  ├─ test_win32pipe.py
│  │  │  │     │  │  ├─ test_win32print.py
│  │  │  │     │  │  ├─ test_win32profile.py
│  │  │  │     │  │  ├─ test_win32rcparser.py
│  │  │  │     │  │  ├─ test_win32timezone.py
│  │  │  │     │  │  ├─ test_win32trace.py
│  │  │  │     │  │  ├─ test_win32wnet.py
│  │  │  │     │  │  ├─ win32rcparser
│  │  │  │     │  │  │  ├─ python.bmp
│  │  │  │     │  │  │  ├─ python.ico
│  │  │  │     │  │  │  ├─ test.h
│  │  │  │     │  │  │  └─ test.rc
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ handles.cpython-310.pyc
│  │  │  │     │  │     ├─ testall.cpython-310.pyc
│  │  │  │     │  │     ├─ test_clipboard.cpython-310.pyc
│  │  │  │     │  │     ├─ test_exceptions.cpython-310.pyc
│  │  │  │     │  │     ├─ test_odbc.cpython-310.pyc
│  │  │  │     │  │     ├─ test_pywintypes.cpython-310.pyc
│  │  │  │     │  │     ├─ test_security.cpython-310.pyc
│  │  │  │     │  │     ├─ test_sspi.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32api.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32crypt.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32event.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32file.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32gui.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32guistruct.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32inet.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32net.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32pipe.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32print.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32profile.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32rcparser.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32timezone.cpython-310.pyc
│  │  │  │     │  │     ├─ test_win32trace.cpython-310.pyc
│  │  │  │     │  │     └─ test_win32wnet.cpython-310.pyc
│  │  │  │     │  ├─ timer.pyd
│  │  │  │     │  ├─ win32api.pyd
│  │  │  │     │  ├─ win32clipboard.pyd
│  │  │  │     │  ├─ win32console.pyd
│  │  │  │     │  ├─ win32cred.pyd
│  │  │  │     │  ├─ win32crypt.pyd
│  │  │  │     │  ├─ win32event.pyd
│  │  │  │     │  ├─ win32evtlog.pyd
│  │  │  │     │  ├─ win32file.pyd
│  │  │  │     │  ├─ win32gui.pyd
│  │  │  │     │  ├─ win32help.pyd
│  │  │  │     │  ├─ win32inet.pyd
│  │  │  │     │  ├─ win32job.pyd
│  │  │  │     │  ├─ win32lz.pyd
│  │  │  │     │  ├─ win32net.pyd
│  │  │  │     │  ├─ win32pdh.pyd
│  │  │  │     │  ├─ win32pipe.pyd
│  │  │  │     │  ├─ win32print.pyd
│  │  │  │     │  ├─ win32process.pyd
│  │  │  │     │  ├─ win32profile.pyd
│  │  │  │     │  ├─ win32ras.pyd
│  │  │  │     │  ├─ win32security.pyd
│  │  │  │     │  ├─ win32service.pyd
│  │  │  │     │  ├─ win32trace.pyd
│  │  │  │     │  ├─ win32transaction.pyd
│  │  │  │     │  ├─ win32ts.pyd
│  │  │  │     │  ├─ win32wnet.pyd
│  │  │  │     │  ├─ winxpgui.pyd
│  │  │  │     │  ├─ _win32sysloader.pyd
│  │  │  │     │  └─ _winxptheme.pyd
│  │  │  │     ├─ win32com
│  │  │  │     │  ├─ client
│  │  │  │     │  │  ├─ build.py
│  │  │  │     │  │  ├─ CLSIDToClass.py
│  │  │  │     │  │  ├─ combrowse.py
│  │  │  │     │  │  ├─ connect.py
│  │  │  │     │  │  ├─ dynamic.py
│  │  │  │     │  │  ├─ gencache.py
│  │  │  │     │  │  ├─ genpy.py
│  │  │  │     │  │  ├─ makepy.py
│  │  │  │     │  │  ├─ selecttlb.py
│  │  │  │     │  │  ├─ tlbrowse.py
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ build.cpython-310.pyc
│  │  │  │     │  │     ├─ CLSIDToClass.cpython-310.pyc
│  │  │  │     │  │     ├─ combrowse.cpython-310.pyc
│  │  │  │     │  │     ├─ connect.cpython-310.pyc
│  │  │  │     │  │     ├─ dynamic.cpython-310.pyc
│  │  │  │     │  │     ├─ gencache.cpython-310.pyc
│  │  │  │     │  │     ├─ genpy.cpython-310.pyc
│  │  │  │     │  │     ├─ makepy.cpython-310.pyc
│  │  │  │     │  │     ├─ selecttlb.cpython-310.pyc
│  │  │  │     │  │     ├─ tlbrowse.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ demos
│  │  │  │     │  │  ├─ connect.py
│  │  │  │     │  │  ├─ dump_clipboard.py
│  │  │  │     │  │  ├─ eventsApartmentThreaded.py
│  │  │  │     │  │  ├─ eventsFreeThreaded.py
│  │  │  │     │  │  ├─ excelAddin.py
│  │  │  │     │  │  ├─ excelRTDServer.py
│  │  │  │     │  │  ├─ iebutton.py
│  │  │  │     │  │  ├─ ietoolbar.py
│  │  │  │     │  │  ├─ outlookAddin.py
│  │  │  │     │  │  ├─ trybag.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ connect.cpython-310.pyc
│  │  │  │     │  │     ├─ dump_clipboard.cpython-310.pyc
│  │  │  │     │  │     ├─ eventsApartmentThreaded.cpython-310.pyc
│  │  │  │     │  │     ├─ eventsFreeThreaded.cpython-310.pyc
│  │  │  │     │  │     ├─ excelAddin.cpython-310.pyc
│  │  │  │     │  │     ├─ excelRTDServer.cpython-310.pyc
│  │  │  │     │  │     ├─ iebutton.cpython-310.pyc
│  │  │  │     │  │     ├─ ietoolbar.cpython-310.pyc
│  │  │  │     │  │     ├─ outlookAddin.cpython-310.pyc
│  │  │  │     │  │     ├─ trybag.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ HTML
│  │  │  │     │  │  ├─ docindex.html
│  │  │  │     │  │  ├─ GeneratedSupport.html
│  │  │  │     │  │  ├─ image
│  │  │  │     │  │  │  ├─ blank.gif
│  │  │  │     │  │  │  ├─ BTN_HomePage.gif
│  │  │  │     │  │  │  ├─ BTN_ManualTop.gif
│  │  │  │     │  │  │  ├─ BTN_NextPage.gif
│  │  │  │     │  │  │  ├─ BTN_PrevPage.gif
│  │  │  │     │  │  │  ├─ pycom_blowing.gif
│  │  │  │     │  │  │  ├─ pythoncom.gif
│  │  │  │     │  │  │  └─ www_icon.gif
│  │  │  │     │  │  ├─ index.html
│  │  │  │     │  │  ├─ misc.html
│  │  │  │     │  │  ├─ package.html
│  │  │  │     │  │  ├─ PythonCOM.html
│  │  │  │     │  │  ├─ QuickStartClientCom.html
│  │  │  │     │  │  ├─ QuickStartServerCom.html
│  │  │  │     │  │  └─ variant.html
│  │  │  │     │  ├─ include
│  │  │  │     │  │  ├─ PythonCOM.h
│  │  │  │     │  │  ├─ PythonCOMRegister.h
│  │  │  │     │  │  └─ PythonCOMServer.h
│  │  │  │     │  ├─ libs
│  │  │  │     │  │  ├─ axscript.lib
│  │  │  │     │  │  └─ pythoncom.lib
│  │  │  │     │  ├─ License.txt
│  │  │  │     │  ├─ makegw
│  │  │  │     │  │  ├─ makegw.py
│  │  │  │     │  │  ├─ makegwenum.py
│  │  │  │     │  │  ├─ makegwparse.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ makegw.cpython-310.pyc
│  │  │  │     │  │     ├─ makegwenum.cpython-310.pyc
│  │  │  │     │  │     ├─ makegwparse.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ olectl.py
│  │  │  │     │  ├─ readme.html
│  │  │  │     │  ├─ server
│  │  │  │     │  │  ├─ connect.py
│  │  │  │     │  │  ├─ dispatcher.py
│  │  │  │     │  │  ├─ exception.py
│  │  │  │     │  │  ├─ factory.py
│  │  │  │     │  │  ├─ localserver.py
│  │  │  │     │  │  ├─ policy.py
│  │  │  │     │  │  ├─ register.py
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ connect.cpython-310.pyc
│  │  │  │     │  │     ├─ dispatcher.cpython-310.pyc
│  │  │  │     │  │     ├─ exception.cpython-310.pyc
│  │  │  │     │  │     ├─ factory.cpython-310.pyc
│  │  │  │     │  │     ├─ localserver.cpython-310.pyc
│  │  │  │     │  │     ├─ policy.cpython-310.pyc
│  │  │  │     │  │     ├─ register.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ servers
│  │  │  │     │  │  ├─ dictionary.py
│  │  │  │     │  │  ├─ interp.py
│  │  │  │     │  │  ├─ perfmon.py
│  │  │  │     │  │  ├─ PythonTools.py
│  │  │  │     │  │  ├─ test_pycomtest.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ dictionary.cpython-310.pyc
│  │  │  │     │  │     ├─ interp.cpython-310.pyc
│  │  │  │     │  │     ├─ perfmon.cpython-310.pyc
│  │  │  │     │  │     ├─ PythonTools.cpython-310.pyc
│  │  │  │     │  │     ├─ test_pycomtest.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ storagecon.py
│  │  │  │     │  ├─ test
│  │  │  │     │  │  ├─ daodump.py
│  │  │  │     │  │  ├─ errorSemantics.py
│  │  │  │     │  │  ├─ GenTestScripts.py
│  │  │  │     │  │  ├─ pippo.idl
│  │  │  │     │  │  ├─ pippo_server.py
│  │  │  │     │  │  ├─ policySemantics.py
│  │  │  │     │  │  ├─ readme.txt
│  │  │  │     │  │  ├─ testAccess.py
│  │  │  │     │  │  ├─ testADOEvents.py
│  │  │  │     │  │  ├─ testall.py
│  │  │  │     │  │  ├─ testArrays.py
│  │  │  │     │  │  ├─ testAXScript.py
│  │  │  │     │  │  ├─ testClipboard.py
│  │  │  │     │  │  ├─ testCollections.py
│  │  │  │     │  │  ├─ testConversionErrors.py
│  │  │  │     │  │  ├─ testDates.py
│  │  │  │     │  │  ├─ testDCOM.py
│  │  │  │     │  │  ├─ testDictionary.py
│  │  │  │     │  │  ├─ testDictionary.vbs
│  │  │  │     │  │  ├─ testDynamic.py
│  │  │  │     │  │  ├─ testExchange.py
│  │  │  │     │  │  ├─ testExplorer.py
│  │  │  │     │  │  ├─ testGatewayAddresses.py
│  │  │  │     │  │  ├─ testGIT.py
│  │  │  │     │  │  ├─ testInterp.vbs
│  │  │  │     │  │  ├─ testIterators.py
│  │  │  │     │  │  ├─ testmakepy.py
│  │  │  │     │  │  ├─ testMarshal.py
│  │  │  │     │  │  ├─ testMSOffice.py
│  │  │  │     │  │  ├─ testMSOfficeEvents.py
│  │  │  │     │  │  ├─ testNetscape.py
│  │  │  │     │  │  ├─ testPersist.py
│  │  │  │     │  │  ├─ testPippo.py
│  │  │  │     │  │  ├─ testPyComTest.py
│  │  │  │     │  │  ├─ Testpys.sct
│  │  │  │     │  │  ├─ testPyScriptlet.js
│  │  │  │     │  │  ├─ testROT.py
│  │  │  │     │  │  ├─ testServers.py
│  │  │  │     │  │  ├─ testShell.py
│  │  │  │     │  │  ├─ testStorage.py
│  │  │  │     │  │  ├─ testStreams.py
│  │  │  │     │  │  ├─ testvb.py
│  │  │  │     │  │  ├─ testvbscript_regexp.py
│  │  │  │     │  │  ├─ testWMI.py
│  │  │  │     │  │  ├─ testxslt.js
│  │  │  │     │  │  ├─ testxslt.py
│  │  │  │     │  │  ├─ testxslt.xsl
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ daodump.cpython-310.pyc
│  │  │  │     │  │     ├─ errorSemantics.cpython-310.pyc
│  │  │  │     │  │     ├─ GenTestScripts.cpython-310.pyc
│  │  │  │     │  │     ├─ pippo_server.cpython-310.pyc
│  │  │  │     │  │     ├─ policySemantics.cpython-310.pyc
│  │  │  │     │  │     ├─ testAccess.cpython-310.pyc
│  │  │  │     │  │     ├─ testADOEvents.cpython-310.pyc
│  │  │  │     │  │     ├─ testall.cpython-310.pyc
│  │  │  │     │  │     ├─ testArrays.cpython-310.pyc
│  │  │  │     │  │     ├─ testAXScript.cpython-310.pyc
│  │  │  │     │  │     ├─ testClipboard.cpython-310.pyc
│  │  │  │     │  │     ├─ testCollections.cpython-310.pyc
│  │  │  │     │  │     ├─ testConversionErrors.cpython-310.pyc
│  │  │  │     │  │     ├─ testDates.cpython-310.pyc
│  │  │  │     │  │     ├─ testDCOM.cpython-310.pyc
│  │  │  │     │  │     ├─ testDictionary.cpython-310.pyc
│  │  │  │     │  │     ├─ testDynamic.cpython-310.pyc
│  │  │  │     │  │     ├─ testExchange.cpython-310.pyc
│  │  │  │     │  │     ├─ testExplorer.cpython-310.pyc
│  │  │  │     │  │     ├─ testGatewayAddresses.cpython-310.pyc
│  │  │  │     │  │     ├─ testGIT.cpython-310.pyc
│  │  │  │     │  │     ├─ testIterators.cpython-310.pyc
│  │  │  │     │  │     ├─ testmakepy.cpython-310.pyc
│  │  │  │     │  │     ├─ testMarshal.cpython-310.pyc
│  │  │  │     │  │     ├─ testMSOffice.cpython-310.pyc
│  │  │  │     │  │     ├─ testMSOfficeEvents.cpython-310.pyc
│  │  │  │     │  │     ├─ testNetscape.cpython-310.pyc
│  │  │  │     │  │     ├─ testPersist.cpython-310.pyc
│  │  │  │     │  │     ├─ testPippo.cpython-310.pyc
│  │  │  │     │  │     ├─ testPyComTest.cpython-310.pyc
│  │  │  │     │  │     ├─ testROT.cpython-310.pyc
│  │  │  │     │  │     ├─ testServers.cpython-310.pyc
│  │  │  │     │  │     ├─ testShell.cpython-310.pyc
│  │  │  │     │  │     ├─ testStorage.cpython-310.pyc
│  │  │  │     │  │     ├─ testStreams.cpython-310.pyc
│  │  │  │     │  │     ├─ testvb.cpython-310.pyc
│  │  │  │     │  │     ├─ testvbscript_regexp.cpython-310.pyc
│  │  │  │     │  │     ├─ testWMI.cpython-310.pyc
│  │  │  │     │  │     ├─ testxslt.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ universal.py
│  │  │  │     │  ├─ util.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ olectl.cpython-310.pyc
│  │  │  │     │     ├─ storagecon.cpython-310.pyc
│  │  │  │     │     ├─ universal.cpython-310.pyc
│  │  │  │     │     ├─ util.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ win32comext
│  │  │  │     │  ├─ adsi
│  │  │  │     │  │  ├─ adsi.pyd
│  │  │  │     │  │  ├─ adsicon.py
│  │  │  │     │  │  ├─ demos
│  │  │  │     │  │  │  ├─ objectPicker.py
│  │  │  │     │  │  │  ├─ scp.py
│  │  │  │     │  │  │  ├─ search.py
│  │  │  │     │  │  │  ├─ test.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ objectPicker.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scp.cpython-310.pyc
│  │  │  │     │  │  │     ├─ search.cpython-310.pyc
│  │  │  │     │  │  │     └─ test.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ adsicon.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ authorization
│  │  │  │     │  │  ├─ authorization.pyd
│  │  │  │     │  │  ├─ demos
│  │  │  │     │  │  │  ├─ EditSecurity.py
│  │  │  │     │  │  │  ├─ EditServiceSecurity.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ EditSecurity.cpython-310.pyc
│  │  │  │     │  │  │     └─ EditServiceSecurity.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ axcontrol
│  │  │  │     │  │  ├─ axcontrol.pyd
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ axdebug
│  │  │  │     │  │  ├─ adb.py
│  │  │  │     │  │  ├─ codecontainer.py
│  │  │  │     │  │  ├─ contexts.py
│  │  │  │     │  │  ├─ debugger.py
│  │  │  │     │  │  ├─ documents.py
│  │  │  │     │  │  ├─ dump.py
│  │  │  │     │  │  ├─ expressions.py
│  │  │  │     │  │  ├─ gateways.py
│  │  │  │     │  │  ├─ stackframe.py
│  │  │  │     │  │  ├─ util.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ adb.cpython-310.pyc
│  │  │  │     │  │     ├─ codecontainer.cpython-310.pyc
│  │  │  │     │  │     ├─ contexts.cpython-310.pyc
│  │  │  │     │  │     ├─ debugger.cpython-310.pyc
│  │  │  │     │  │     ├─ documents.cpython-310.pyc
│  │  │  │     │  │     ├─ dump.cpython-310.pyc
│  │  │  │     │  │     ├─ expressions.cpython-310.pyc
│  │  │  │     │  │     ├─ gateways.cpython-310.pyc
│  │  │  │     │  │     ├─ stackframe.cpython-310.pyc
│  │  │  │     │  │     ├─ util.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ axscript
│  │  │  │     │  │  ├─ asputil.py
│  │  │  │     │  │  ├─ axscript.pyd
│  │  │  │     │  │  ├─ client
│  │  │  │     │  │  │  ├─ debug.py
│  │  │  │     │  │  │  ├─ error.py
│  │  │  │     │  │  │  ├─ framework.py
│  │  │  │     │  │  │  ├─ pydumper.py
│  │  │  │     │  │  │  ├─ pyscript.py
│  │  │  │     │  │  │  ├─ pyscript_rexec.py
│  │  │  │     │  │  │  ├─ scriptdispatch.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ debug.cpython-310.pyc
│  │  │  │     │  │  │     ├─ error.cpython-310.pyc
│  │  │  │     │  │  │     ├─ framework.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pydumper.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pyscript.cpython-310.pyc
│  │  │  │     │  │  │     ├─ pyscript_rexec.cpython-310.pyc
│  │  │  │     │  │  │     ├─ scriptdispatch.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ Demos
│  │  │  │     │  │  │  └─ client
│  │  │  │     │  │  │     ├─ asp
│  │  │  │     │  │  │     │  ├─ caps.asp
│  │  │  │     │  │  │     │  ├─ CreateObject.asp
│  │  │  │     │  │  │     │  ├─ interrupt
│  │  │  │     │  │  │     │  │  ├─ test.asp
│  │  │  │     │  │  │     │  │  ├─ test.html
│  │  │  │     │  │  │     │  │  ├─ test1.asp
│  │  │  │     │  │  │     │  │  └─ test1.html
│  │  │  │     │  │  │     │  └─ tut1.asp
│  │  │  │     │  │  │     ├─ ie
│  │  │  │     │  │  │     │  ├─ calc.htm
│  │  │  │     │  │  │     │  ├─ dbgtest.htm
│  │  │  │     │  │  │     │  ├─ demo.htm
│  │  │  │     │  │  │     │  ├─ demo_check.htm
│  │  │  │     │  │  │     │  ├─ demo_intro.htm
│  │  │  │     │  │  │     │  ├─ demo_menu.htm
│  │  │  │     │  │  │     │  ├─ docwrite.htm
│  │  │  │     │  │  │     │  ├─ foo2.htm
│  │  │  │     │  │  │     │  ├─ form.htm
│  │  │  │     │  │  │     │  ├─ marqueeDemo.htm
│  │  │  │     │  │  │     │  ├─ MarqueeText1.htm
│  │  │  │     │  │  │     │  ├─ mousetrack.htm
│  │  │  │     │  │  │     │  └─ pycom_blowing.gif
│  │  │  │     │  │  │     └─ wsh
│  │  │  │     │  │  │        ├─ blank.pys
│  │  │  │     │  │  │        ├─ excel.pys
│  │  │  │     │  │  │        ├─ registry.pys
│  │  │  │     │  │  │        └─ test.pys
│  │  │  │     │  │  ├─ server
│  │  │  │     │  │  │  ├─ axsite.py
│  │  │  │     │  │  │  ├─ error.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ axsite.cpython-310.pyc
│  │  │  │     │  │  │     ├─ error.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ test
│  │  │  │     │  │  │  ├─ debugTest.pys
│  │  │  │     │  │  │  ├─ debugTest.vbs
│  │  │  │     │  │  │  ├─ leakTest.py
│  │  │  │     │  │  │  ├─ testHost.py
│  │  │  │     │  │  │  ├─ testHost4Dbg.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ leakTest.cpython-310.pyc
│  │  │  │     │  │  │     ├─ testHost.cpython-310.pyc
│  │  │  │     │  │  │     └─ testHost4Dbg.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ asputil.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ bits
│  │  │  │     │  │  ├─ bits.pyd
│  │  │  │     │  │  ├─ test
│  │  │  │     │  │  │  ├─ show_all_jobs.py
│  │  │  │     │  │  │  ├─ test_bits.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ show_all_jobs.cpython-310.pyc
│  │  │  │     │  │  │     └─ test_bits.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ directsound
│  │  │  │     │  │  ├─ directsound.pyd
│  │  │  │     │  │  ├─ test
│  │  │  │     │  │  │  ├─ ds_record.py
│  │  │  │     │  │  │  ├─ ds_test.py
│  │  │  │     │  │  │  ├─ __init__.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ ds_record.cpython-310.pyc
│  │  │  │     │  │  │     ├─ ds_test.cpython-310.pyc
│  │  │  │     │  │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ ifilter
│  │  │  │     │  │  ├─ demo
│  │  │  │     │  │  │  ├─ filterDemo.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ filterDemo.cpython-310.pyc
│  │  │  │     │  │  ├─ ifilter.pyd
│  │  │  │     │  │  ├─ ifiltercon.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ ifiltercon.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ internet
│  │  │  │     │  │  ├─ inetcon.py
│  │  │  │     │  │  ├─ internet.pyd
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ inetcon.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ mapi
│  │  │  │     │  │  ├─ demos
│  │  │  │     │  │  │  ├─ mapisend.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ mapisend.cpython-310.pyc
│  │  │  │     │  │  ├─ emsabtags.py
│  │  │  │     │  │  ├─ exchange.pyd
│  │  │  │     │  │  ├─ mapi.pyd
│  │  │  │     │  │  ├─ mapitags.py
│  │  │  │     │  │  ├─ mapiutil.py
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ emsabtags.cpython-310.pyc
│  │  │  │     │  │     ├─ mapitags.cpython-310.pyc
│  │  │  │     │  │     ├─ mapiutil.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ propsys
│  │  │  │     │  │  ├─ propsys.pyd
│  │  │  │     │  │  ├─ pscon.py
│  │  │  │     │  │  ├─ test
│  │  │  │     │  │  │  ├─ testpropsys.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     └─ testpropsys.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ pscon.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  ├─ shell
│  │  │  │     │  │  ├─ demos
│  │  │  │     │  │  │  ├─ browse_for_folder.py
│  │  │  │     │  │  │  ├─ create_link.py
│  │  │  │     │  │  │  ├─ dump_link.py
│  │  │  │     │  │  │  ├─ explorer_browser.py
│  │  │  │     │  │  │  ├─ IActiveDesktop.py
│  │  │  │     │  │  │  ├─ IFileOperationProgressSink.py
│  │  │  │     │  │  │  ├─ IShellLinkDataList.py
│  │  │  │     │  │  │  ├─ ITransferAdviseSink.py
│  │  │  │     │  │  │  ├─ IUniformResourceLocator.py
│  │  │  │     │  │  │  ├─ servers
│  │  │  │     │  │  │  │  ├─ column_provider.py
│  │  │  │     │  │  │  │  ├─ context_menu.py
│  │  │  │     │  │  │  │  ├─ copy_hook.py
│  │  │  │     │  │  │  │  ├─ empty_volume_cache.py
│  │  │  │     │  │  │  │  ├─ folder_view.py
│  │  │  │     │  │  │  │  ├─ icon_handler.py
│  │  │  │     │  │  │  │  ├─ shell_view.py
│  │  │  │     │  │  │  │  └─ __pycache__
│  │  │  │     │  │  │  │     ├─ column_provider.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ context_menu.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ copy_hook.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ empty_volume_cache.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ folder_view.cpython-310.pyc
│  │  │  │     │  │  │  │     ├─ icon_handler.cpython-310.pyc
│  │  │  │     │  │  │  │     └─ shell_view.cpython-310.pyc
│  │  │  │     │  │  │  ├─ shellexecuteex.py
│  │  │  │     │  │  │  ├─ viewstate.py
│  │  │  │     │  │  │  ├─ walk_shell_folders.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ browse_for_folder.cpython-310.pyc
│  │  │  │     │  │  │     ├─ create_link.cpython-310.pyc
│  │  │  │     │  │  │     ├─ dump_link.cpython-310.pyc
│  │  │  │     │  │  │     ├─ explorer_browser.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IActiveDesktop.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IFileOperationProgressSink.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IShellLinkDataList.cpython-310.pyc
│  │  │  │     │  │  │     ├─ ITransferAdviseSink.cpython-310.pyc
│  │  │  │     │  │  │     ├─ IUniformResourceLocator.cpython-310.pyc
│  │  │  │     │  │  │     ├─ shellexecuteex.cpython-310.pyc
│  │  │  │     │  │  │     ├─ viewstate.cpython-310.pyc
│  │  │  │     │  │  │     └─ walk_shell_folders.cpython-310.pyc
│  │  │  │     │  │  ├─ shell.pyd
│  │  │  │     │  │  ├─ shellcon.py
│  │  │  │     │  │  ├─ test
│  │  │  │     │  │  │  ├─ testShellFolder.py
│  │  │  │     │  │  │  ├─ testShellItem.py
│  │  │  │     │  │  │  ├─ testSHFileOperation.py
│  │  │  │     │  │  │  └─ __pycache__
│  │  │  │     │  │  │     ├─ testShellFolder.cpython-310.pyc
│  │  │  │     │  │  │     ├─ testShellItem.cpython-310.pyc
│  │  │  │     │  │  │     └─ testSHFileOperation.cpython-310.pyc
│  │  │  │     │  │  ├─ __init__.py
│  │  │  │     │  │  └─ __pycache__
│  │  │  │     │  │     ├─ shellcon.cpython-310.pyc
│  │  │  │     │  │     └─ __init__.cpython-310.pyc
│  │  │  │     │  └─ taskscheduler
│  │  │  │     │     ├─ taskscheduler.pyd
│  │  │  │     │     ├─ test
│  │  │  │     │     │  ├─ test_addtask.py
│  │  │  │     │     │  ├─ test_addtask_1.py
│  │  │  │     │     │  ├─ test_addtask_2.py
│  │  │  │     │     │  ├─ test_localsystem.py
│  │  │  │     │     │  └─ __pycache__
│  │  │  │     │     │     ├─ test_addtask.cpython-310.pyc
│  │  │  │     │     │     ├─ test_addtask_1.cpython-310.pyc
│  │  │  │     │     │     ├─ test_addtask_2.cpython-310.pyc
│  │  │  │     │     │     └─ test_localsystem.cpython-310.pyc
│  │  │  │     │     ├─ __init__.py
│  │  │  │     │     └─ __pycache__
│  │  │  │     │        └─ __init__.cpython-310.pyc
│  │  │  │     ├─ yaml
│  │  │  │     │  ├─ composer.py
│  │  │  │     │  ├─ constructor.py
│  │  │  │     │  ├─ cyaml.py
│  │  │  │     │  ├─ dumper.py
│  │  │  │     │  ├─ emitter.py
│  │  │  │     │  ├─ error.py
│  │  │  │     │  ├─ events.py
│  │  │  │     │  ├─ loader.py
│  │  │  │     │  ├─ nodes.py
│  │  │  │     │  ├─ parser.py
│  │  │  │     │  ├─ reader.py
│  │  │  │     │  ├─ representer.py
│  │  │  │     │  ├─ resolver.py
│  │  │  │     │  ├─ scanner.py
│  │  │  │     │  ├─ serializer.py
│  │  │  │     │  ├─ tokens.py
│  │  │  │     │  ├─ _yaml.cp310-win_amd64.pyd
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ composer.cpython-310.pyc
│  │  │  │     │     ├─ constructor.cpython-310.pyc
│  │  │  │     │     ├─ cyaml.cpython-310.pyc
│  │  │  │     │     ├─ dumper.cpython-310.pyc
│  │  │  │     │     ├─ emitter.cpython-310.pyc
│  │  │  │     │     ├─ error.cpython-310.pyc
│  │  │  │     │     ├─ events.cpython-310.pyc
│  │  │  │     │     ├─ loader.cpython-310.pyc
│  │  │  │     │     ├─ nodes.cpython-310.pyc
│  │  │  │     │     ├─ parser.cpython-310.pyc
│  │  │  │     │     ├─ reader.cpython-310.pyc
│  │  │  │     │     ├─ representer.cpython-310.pyc
│  │  │  │     │     ├─ resolver.cpython-310.pyc
│  │  │  │     │     ├─ scanner.cpython-310.pyc
│  │  │  │     │     ├─ serializer.cpython-310.pyc
│  │  │  │     │     ├─ tokens.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ yarg
│  │  │  │     │  ├─ client.py
│  │  │  │     │  ├─ exceptions.py
│  │  │  │     │  ├─ package.py
│  │  │  │     │  ├─ parse.py
│  │  │  │     │  ├─ release.py
│  │  │  │     │  ├─ __about__.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ client.cpython-310.pyc
│  │  │  │     │     ├─ exceptions.cpython-310.pyc
│  │  │  │     │     ├─ package.cpython-310.pyc
│  │  │  │     │     ├─ parse.cpython-310.pyc
│  │  │  │     │     ├─ release.cpython-310.pyc
│  │  │  │     │     ├─ __about__.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ yarg-0.1.9.dist-info
│  │  │  │     │  ├─ DESCRIPTION.rst
│  │  │  │     │  ├─ INSTALLER
│  │  │  │     │  ├─ METADATA
│  │  │  │     │  ├─ metadata.json
│  │  │  │     │  ├─ RECORD
│  │  │  │     │  ├─ top_level.txt
│  │  │  │     │  ├─ WHEEL
│  │  │  │     │  └─ zip-safe
│  │  │  │     ├─ _black_version.py
│  │  │  │     ├─ _cffi_backend.cp310-win_amd64.pyd
│  │  │  │     ├─ _distutils_hack
│  │  │  │     │  ├─ override.py
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     ├─ override.cpython-310.pyc
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     ├─ _yaml
│  │  │  │     │  ├─ __init__.py
│  │  │  │     │  └─ __pycache__
│  │  │  │     │     └─ __init__.cpython-310.pyc
│  │  │  │     └─ __pycache__
│  │  │  │        ├─ docopt.cpython-310.pyc
│  │  │  │        ├─ mypy_extensions.cpython-310.pyc
│  │  │  │        ├─ pythoncom.cpython-310.pyc
│  │  │  │        ├─ six.cpython-310.pyc
│  │  │  │        ├─ typing_extensions.cpython-310.pyc
│  │  │  │        └─ _black_version.cpython-310.pyc
│  │  │  ├─ pyvenv.cfg
│  │  │  └─ Scripts
│  │  │     ├─ activate
│  │  │     ├─ activate-global-python-argcomplete
│  │  │     ├─ activate.bat
│  │  │     ├─ Activate.ps1
│  │  │     ├─ black.exe
│  │  │     ├─ blackd.exe
│  │  │     ├─ datamodel-codegen.exe
│  │  │     ├─ deactivate.bat
│  │  │     ├─ email_validator.exe
│  │  │     ├─ genson-script.py
│  │  │     ├─ genson.exe
│  │  │     ├─ httpx.exe
│  │  │     ├─ isort-identify-imports.exe
│  │  │     ├─ isort.exe
│  │  │     ├─ jsonschema.exe
│  │  │     ├─ normalizer.exe
│  │  │     ├─ pip.exe
│  │  │     ├─ pip3.10.exe
│  │  │     ├─ pip3.exe
│  │  │     ├─ pipreqs.exe
│  │  │     ├─ python-argcomplete-check-easy-install-script
│  │  │     ├─ python.exe
│  │  │     ├─ pythonw.exe
│  │  │     ├─ pywin32_postinstall.py
│  │  │     ├─ pywin32_testall.py
│  │  │     ├─ register-python-argcomplete
│  │  │     ├─ ruff.exe
│  │  │     ├─ sourcery.exe
│  │  │     └─ __pycache__
│  │  │        ├─ pywin32_postinstall.cpython-310.pyc
│  │  │        └─ pywin32_testall.cpython-310.pyc
│  │  ├─ .vscode
│  │  │  ├─ extensions.json
│  │  │  ├─ launch.json
│  │  │  ├─ settings.json
│  │  │  └─ tasks.json
│  │  ├─ archive
│  │  │  ├─ DaRT
│  │  │  │  ├─ .ruff_cache
│  │  │  │  │  ├─ 0.1.6
│  │  │  │  │  │  └─ 16513434275574315711
│  │  │  │  │  └─ CACHEDIR.TAG
│  │  │  │  ├─ dart_model.py
│  │  │  │  └─ __pycache__
│  │  │  │     └─ model_funcs.cpython-311.pyc
│  │  │  ├─ function_app_old.py
│  │  │  ├─ model_nsip_project.py
│  │  │  ├─ model_service_user.py
│  │  │  ├─ validation_nsip_project.py
│  │  │  └─ validation_service_user.py
│  │  ├─ config.yaml
│  │  ├─ deploy.sh
│  │  ├─ function_app.py
│  │  ├─ helper
│  │  │  ├─ datamodel-codegen.sh
│  │  │  └─ getfunctionurlsandsetkeyvaultsecrets.py
│  │  ├─ host.json
│  │  ├─ local.settings.json
│  │  ├─ requirements.txt
│  │  ├─ servicebus_funcs.py
│  │  ├─ set_environment.py
│  │  ├─ tests
│  │  │  ├─ config.yaml
│  │  │  ├─ config_test.ipynb
│  │  │  ├─ servicebus_funcs.py
│  │  │  ├─ set_environment.py
│  │  │  ├─ test.ipynb
│  │  │  ├─ validate_messages.py
│  │  │  ├─ validate_test.ipynb
│  │  │  ├─ var_funcs.py
│  │  │  └─ __pycache__
│  │  │     ├─ servicebus_funcs.cpython-311.pyc
│  │  │     ├─ set_environment.cpython-311.pyc
│  │  │     ├─ validate_messages.cpython-311.pyc
│  │  │     └─ var_funcs.cpython-311.pyc
│  │  ├─ validate_messages.py
│  │  ├─ var_funcs.py
│  │  ├─ __azurite_db_blob_extent__.json
│  │  ├─ __azurite_db_blob__.json
│  │  ├─ __blobstorage__
│  │  │  └─ 133dcd74-40d4-4248-b91e-ea4b76126ae6
│  │  └─ __pycache__
│  │     ├─ config.cpython-310.pyc
│  │     ├─ config.cpython-311.pyc
│  │     ├─ function_app.cpython-310.pyc
│  │     ├─ model_case_schedule.cpython-310.pyc
│  │     ├─ model_employee.cpython-310.pyc
│  │     ├─ model_interested_party.cpython-310.pyc
│  │     ├─ model_nsip.cpython-310.pyc
│  │     ├─ model_nsip_document.cpython-310.pyc
│  │     ├─ model_nsip_exam_timetable.cpython-310.pyc
│  │     ├─ model_nsip_exam_timetable_submission.cpython-310.pyc
│  │     ├─ model_nsip_project.cpython-310.pyc
│  │     ├─ model_nsip_project.cpython-311.pyc
│  │     ├─ model_nsip_project_update.cpython-310.pyc
│  │     ├─ model_nsip_representation.cpython-310.pyc
│  │     ├─ model_nsip_subscription.cpython-310.pyc
│  │     ├─ model_s51_advice.cpython-310.pyc
│  │     ├─ model_service_user.cpython-310.pyc
│  │     ├─ nsip_project.cpython-311.pyc
│  │     ├─ servicebus_funcs.cpython-310.pyc
│  │     ├─ servicebus_funcs.cpython-311.pyc
│  │     ├─ service_user.cpython-311.pyc
│  │     ├─ set_environment.cpython-310.pyc
│  │     ├─ set_environment.cpython-311.pyc
│  │     ├─ validate.cpython-310.pyc
│  │     ├─ validate.cpython-311.pyc
│  │     ├─ validate_messages.cpython-310.pyc
│  │     ├─ validation_nsip_project.cpython-310.pyc
│  │     ├─ validation_nsip_project.cpython-311.pyc
│  │     ├─ validation_service_user.cpython-310.pyc
│  │     ├─ var_funcs.cpython-310.pyc
│  │     └─ var_funcs.cpython-311.pyc
│  ├─ images
│  │  ├─ apim-function-apps.drawio.svg
│  │  ├─ copy_data_task.png
│  │  ├─ create_new_dataset.png
│  │  ├─ datalake_storage_gen2.png
│  │  ├─ edit-custom-connector.png
│  │  ├─ json_file_format.png
│  │  ├─ linkedService.png
│  │  ├─ logging_notebook.png
│  │  ├─ pagination.png
│  │  ├─ relative_url.png
│  │  ├─ service-user-architecture.drawio.svg
│  │  ├─ sink_dataset.png
│  │  ├─ source_dataset.png
│  │  ├─ swagger-inspector.png
│  │  ├─ swaggerhub.png
│  │  ├─ zendesk-built-in.jpg
│  │  ├─ zendesk-created-workflow.png
│  │  ├─ zendesk-custom.jpg
│  │  └─ zendesk-logo.png
│  ├─ infrastructure
│  │  ├─ .DS_Store
│  │  ├─ .terraform
│  │  │  └─ modules
│  │  │     ├─ azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ bastion_host.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ bastion_host_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ devops_agent_pool.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ devops_agent_pool_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ logic_app.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ logic_app_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ modules.json
│  │  │     ├─ odt_pe_backoffice_sb.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ odt_pe_backoffice_sb_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_data_lake.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_data_lake_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_ingestion.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_ingestion_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_management.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_management_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_monitoring.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_monitoring_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_network.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_network.subnets
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ main.tf
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ test
│  │  │     │  │  ├─ null_name.tf
│  │  │     │  │  ├─ README.md
│  │  │     │  │  └─ simple.tf
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_network_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_network_failover.subnets
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ main.tf
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ test
│  │  │     │  │  ├─ null_name.tf
│  │  │     │  │  ├─ README.md
│  │  │     │  │  └─ simple.tf
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_shir.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_shir_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_sql_server.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_sql_server_failover.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     ├─ synapse_workspace_private.azure_region
│  │  │     │  ├─ CHANGELOG.md
│  │  │     │  ├─ CONTRIBUTING.md
│  │  │     │  ├─ examples
│  │  │     │  │  └─ main
│  │  │     │  │     ├─ main.tf
│  │  │     │  │     └─ modules.tf
│  │  │     │  ├─ LICENSE
│  │  │     │  ├─ NOTICE
│  │  │     │  ├─ outputs.tf
│  │  │     │  ├─ README.md
│  │  │     │  ├─ REGIONS.md
│  │  │     │  ├─ regions.tf
│  │  │     │  ├─ terraform.tfvars.ci
│  │  │     │  ├─ variables.tf
│  │  │     │  └─ versions.tf
│  │  │     └─ synapse_workspace_private_failover.azure_region
│  │  │        ├─ CHANGELOG.md
│  │  │        ├─ CONTRIBUTING.md
│  │  │        ├─ examples
│  │  │        │  └─ main
│  │  │        │     ├─ main.tf
│  │  │        │     └─ modules.tf
│  │  │        ├─ LICENSE
│  │  │        ├─ NOTICE
│  │  │        ├─ outputs.tf
│  │  │        ├─ README.md
│  │  │        ├─ REGIONS.md
│  │  │        ├─ regions.tf
│  │  │        ├─ terraform.tfvars.ci
│  │  │        ├─ variables.tf
│  │  │        └─ versions.tf
│  │  ├─ .terraform.lock.hcl
│  │  ├─ configuration
│  │  │  ├─ data-lake
│  │  │  │  ├─ curated_table_definitions
│  │  │  │  │  ├─ employee.json
│  │  │  │  │  ├─ mipins_hr_measures.json
│  │  │  │  │  └─ nsip_relevant_reps.json
│  │  │  │  ├─ harmonised_table_definitions
│  │  │  │  │  ├─ casework_additional_fields_dim.json
│  │  │  │  │  ├─ casework_advert_details_dim.json
│  │  │  │  │  ├─ casework_all_appeals_additional_data_dim.json
│  │  │  │  │  ├─ casework_all_appeals_dim.json
│  │  │  │  │  ├─ casework_application_sub_type_case_name_dim.json
│  │  │  │  │  ├─ casework_case_dates_dim.json
│  │  │  │  │  ├─ casework_case_fact.json
│  │  │  │  │  ├─ casework_case_info_dim.json
│  │  │  │  │  ├─ casework_case_officer_additional_details_dim.json
│  │  │  │  │  ├─ casework_common_land_dim.json
│  │  │  │  │  ├─ casework_contacts_organisation_dim.json
│  │  │  │  │  ├─ casework_contact_information_dim.json
│  │  │  │  │  ├─ casework_decision_issue_dim.json
│  │  │  │  │  ├─ casework_enforcement_grounds_dim.json
│  │  │  │  │  ├─ casework_event_dim.json
│  │  │  │  │  ├─ casework_event_fact.json
│  │  │  │  │  ├─ casework_examination_timetable_dim.json
│  │  │  │  │  ├─ casework_hedgerow_dim.json
│  │  │  │  │  ├─ casework_high_hedges_dim.json
│  │  │  │  │  ├─ casework_inspector_cases_dim.json
│  │  │  │  │  ├─ casework_legacy_rights_of_way_dim.json
│  │  │  │  │  ├─ casework_local_planning_authority_dim.json
│  │  │  │  │  ├─ casework_local_planning_authority_fact.json
│  │  │  │  │  ├─ casework_local_plans_dim.json
│  │  │  │  │  ├─ casework_lpa_responsibility_dim.json
│  │  │  │  │  ├─ casework_nsip_advice_dim.json
│  │  │  │  │  ├─ casework_nsip_data_dim.json
│  │  │  │  │  ├─ casework_nsip_examination_timetable_dim.json
│  │  │  │  │  ├─ casework_nsip_redactions_dim.json
│  │  │  │  │  ├─ casework_nsip_relevant_representation_dim.json
│  │  │  │  │  ├─ casework_picaso_dim.json
│  │  │  │  │  ├─ casework_picasso_dim.json
│  │  │  │  │  ├─ casework_specialism_dim.json
│  │  │  │  │  ├─ casework_specialist_case_dates_dim.json
│  │  │  │  │  ├─ casework_specialist_case_string_dim.json
│  │  │  │  │  ├─ casework_specialist_coastal_access_dim.json
│  │  │  │  │  ├─ casework_specialist_environment_dim.json
│  │  │  │  │  ├─ casework_specialist_high_court_dim.json
│  │  │  │  │  ├─ casework_specialist_modifications_dim.json
│  │  │  │  │  ├─ casework_specialist_purchase_notice_dim.json
│  │  │  │  │  ├─ casework_specialist_recharge_dim.json
│  │  │  │  │  ├─ casework_special_circumstance_dim.json
│  │  │  │  │  ├─ casework_tpo_dim.json
│  │  │  │  │  ├─ checkmark_casemarking_dim.json
│  │  │  │  │  ├─ checkmark_casemarking_fact.json
│  │  │  │  │  ├─ checkmark_case_casemarking_bridge.json
│  │  │  │  │  ├─ checkmark_case_fact.json
│  │  │  │  │  ├─ checkmark_case_reading_case_bridge.json
│  │  │  │  │  ├─ checkmark_comments_case_bridge.json
│  │  │  │  │  ├─ checkmark_comments_dim.json
│  │  │  │  │  ├─ checkmark_comments_fact.json
│  │  │  │  │  ├─ checkmark_comment_state_reference_dim.json
│  │  │  │  │  ├─ checkmark_comment_type_reference_dim.json
│  │  │  │  │  ├─ checkmark_complexity_reference_dim.json
│  │  │  │  │  ├─ checkmark_conditions_reference_dim.json
│  │  │  │  │  ├─ checkmark_coverage_reference_dim.json
│  │  │  │  │  ├─ checkmark_documents_dim.json
│  │  │  │  │  ├─ checkmark_grounds_reference_dim.json
│  │  │  │  │  ├─ checkmark_inspector_manager_dim.json
│  │  │  │  │  ├─ checkmark_inspector_manager_fact.json
│  │  │  │  │  ├─ checkmark_inspector_manager_reading_case_bridge.json
│  │  │  │  │  ├─ checkmark_invalid_nullity_reference_dim.json
│  │  │  │  │  ├─ checkmark_level_reference_dim.json
│  │  │  │  │  ├─ checkmark_manager_type_reference_dim.json
│  │  │  │  │  ├─ checkmark_nsi_dim.json
│  │  │  │  │  ├─ checkmark_outcome_reference_dim.json
│  │  │  │  │  ├─ checkmark_presentation_accuracy_detail_reference_dim.json
│  │  │  │  │  ├─ checkmark_procedure_reference_dim.json
│  │  │  │  │  ├─ checkmark_reading_case_dim.json
│  │  │  │  │  ├─ checkmark_reading_case_fact.json
│  │  │  │  │  ├─ checkmark_source_reference_dim.json
│  │  │  │  │  ├─ checkmark_structure_reasoning_detail_reference_dim.json
│  │  │  │  │  ├─ date_dim.json
│  │  │  │  │  ├─ high_court_dim.json
│  │  │  │  │  ├─ hr_absence_dim.json
│  │  │  │  │  ├─ hr_contract_dim.json
│  │  │  │  │  ├─ hr_costcenter_dim.json
│  │  │  │  │  ├─ hr_disability_dim.json
│  │  │  │  │  ├─ hr_diversity_dim.json
│  │  │  │  │  ├─ hr_employeegroup_dim.json
│  │  │  │  │  ├─ hr_employee_dim.json
│  │  │  │  │  ├─ hr_employee_fact.json
│  │  │  │  │  ├─ hr_employee_hr_hierarchy_dim.json
│  │  │  │  │  ├─ hr_employee_leavers_dim.json
│  │  │  │  │  ├─ hr_historic_sap_hr.json
│  │  │  │  │  ├─ hr_leave_entitlement_dim.json
│  │  │  │  │  ├─ hr_organisation_unit_dim.json
│  │  │  │  │  ├─ hr_payband_dim.json
│  │  │  │  │  ├─ hr_payroll_area_dim.json
│  │  │  │  │  ├─ hr_personnel_area_dim.json
│  │  │  │  │  ├─ hr_personnel_sub_area_dim.json
│  │  │  │  │  ├─ hr_pins_location_dim.json
│  │  │  │  │  ├─ hr_position_dim.json
│  │  │  │  │  ├─ hr_record_fact.json
│  │  │  │  │  ├─ hr_religion_dim.json
│  │  │  │  │  ├─ hr_secure_info_fact.json
│  │  │  │  │  ├─ hr_specialism_dim.json
│  │  │  │  │  ├─ hr_sxo_dim.json
│  │  │  │  │  ├─ hr_work_schedule_dim.json
│  │  │  │  │  ├─ IMS
│  │  │  │  │  │  ├─ ims_attribute_dim.json
│  │  │  │  │  │  ├─ ims_dataflow_dim.json
│  │  │  │  │  │  ├─ ims_dpia_dim.json
│  │  │  │  │  │  ├─ ims_dsa_dim.json
│  │  │  │  │  │  ├─ ims_entity_dim.json
│  │  │  │  │  │  ├─ ims_information_asset_dim.json
│  │  │  │  │  │  ├─ ims_integration_dim.json
│  │  │  │  │  │  ├─ ims_masterdata_map_dim.json
│  │  │  │  │  │  └─ ims_ropa_dim.json
│  │  │  │  │  ├─ legacy_mwr_inspector_join.json
│  │  │  │  │  ├─ legacy_mwr_lines_dim.json
│  │  │  │  │  ├─ legacy_mwr_record_fact.json
│  │  │  │  │  ├─ legacy_mwr_status_dim.json
│  │  │  │  │  ├─ legacy_mwr_submission_date_dim.json
│  │  │  │  │  ├─ main_sourcesystem_fact.json
│  │  │  │  │  ├─ service_user_dim.json
│  │  │  │  │  ├─ timesheets_minutes_dim.json
│  │  │  │  │  ├─ timesheets_record_fact.json
│  │  │  │  │  ├─ timesheets_segment_type_reference_dim.json
│  │  │  │  │  ├─ timesheets_work_segment_dim.json
│  │  │  │  │  └─ timesheets_work_segment_lock_dim.json
│  │  │  │  ├─ orchestration
│  │  │  │  │  ├─ orchestration.json
│  │  │  │  │  └─ scheduling_outstanding_files_table.json
│  │  │  │  ├─ pins-odw-HR-table-list.json
│  │  │  │  ├─ pins-odw-mipins-table-list.json
│  │  │  │  ├─ pins-odw-source-to-standardised-table-list.json
│  │  │  │  ├─ pins-odw-standardised-to-harmonised-notebook-list.json
│  │  │  │  ├─ raw_logs
│  │  │  │  │  └─ datalabs_log_json
│  │  │  │  │     └─ fileshare_log_schema.json
│  │  │  │  └─ standardised_table_definitions
│  │  │  │     ├─ addresses.JSON
│  │  │  │     ├─ bis_pension_ernic_rates.json
│  │  │  │     ├─ CaseComment.json
│  │  │  │     ├─ CaseMarking.json
│  │  │  │     ├─ Casework_Adhoc
│  │  │  │     │  ├─ Calendar.json
│  │  │  │     │  ├─ Employee.json
│  │  │  │     │  ├─ ExaminationTimetable.json
│  │  │  │     │  ├─ Local_Plans.json
│  │  │  │     │  ├─ PicasoDataUnicode.json
│  │  │  │     │  ├─ Segment_Type_Reference.json
│  │  │  │     │  ├─ Specialist_Hedgerow.json
│  │  │  │     │  ├─ Specialist_HH.json
│  │  │  │     │  ├─ Specialist_TPO.json
│  │  │  │     │  ├─ WorkScheduleRule.json
│  │  │  │     │  ├─ Work_Segment.json
│  │  │  │     │  └─ Work_Segment_Lock.json
│  │  │  │     ├─ CommentStateReference.json
│  │  │  │     ├─ CommentTypeReference.json
│  │  │  │     ├─ ComplexityReference.json
│  │  │  │     ├─ ConditionsReference.json
│  │  │  │     ├─ CoverageReference.json
│  │  │  │     ├─ Documents.json
│  │  │  │     ├─ Example
│  │  │  │     │  └─ MOCK_DATA.json
│  │  │  │     ├─ GroundsReference.json
│  │  │  │     ├─ HighCourt.json
│  │  │  │     ├─ hist_sap_hr.json
│  │  │  │     ├─ Horizon
│  │  │  │     │  ├─ AddAdditionalData.json
│  │  │  │     │  ├─ AdditionalFields.json
│  │  │  │     │  ├─ AdvertDetails.json
│  │  │  │     │  ├─ AllAppeals.json
│  │  │  │     │  ├─ AppealsAdditionalData.json
│  │  │  │     │  ├─ AppSubTypeCaseName.json
│  │  │  │     │  ├─ CaseDates.json
│  │  │  │     │  ├─ CaseInfo.json
│  │  │  │     │  ├─ CaseInvolvement.json
│  │  │  │     │  ├─ CaseOfficerAdditionalDetails.json
│  │  │  │     │  ├─ CommonLand.json
│  │  │  │     │  ├─ Contacts_Organisation.json
│  │  │  │     │  ├─ DecisionIssues.json
│  │  │  │     │  ├─ DocumentCaseReference.json
│  │  │  │     │  ├─ DocumentCaseType.json
│  │  │  │     │  ├─ DocumentMetaData.json
│  │  │  │     │  ├─ DocumentTree.json
│  │  │  │     │  ├─ EnforcementGroundsForAppeal.json
│  │  │  │     │  ├─ Event.json
│  │  │  │     │  ├─ ExaminationTimetable.json
│  │  │  │     │  ├─ HorizonContactInformation.json
│  │  │  │     │  ├─ HorizonFolder.json
│  │  │  │     │  ├─ HZNRightOfWay.json
│  │  │  │     │  ├─ InspectorCases.json
│  │  │  │     │  ├─ Local_Planning_Authority.json
│  │  │  │     │  ├─ LPAResponsibility.json
│  │  │  │     │  ├─ NSIPAdvice.json
│  │  │  │     │  ├─ NSIPData.json
│  │  │  │     │  ├─ NSIPRedactions.json
│  │  │  │     │  ├─ NSIPReleventRepresentation.json
│  │  │  │     │  ├─ ProjectInfoInternal.json
│  │  │  │     │  ├─ ServiceUser.json
│  │  │  │     │  ├─ SpecialCircumstance.json
│  │  │  │     │  ├─ Specialism.json
│  │  │  │     │  ├─ SpecialistCaseDates.json
│  │  │  │     │  ├─ SpecialistCaseString.json
│  │  │  │     │  ├─ SpecialistCoastalAccess.json
│  │  │  │     │  ├─ SpecialistEnvironment.json
│  │  │  │     │  ├─ SpecialistHighCourt.json
│  │  │  │     │  ├─ SpecialistModifications.json
│  │  │  │     │  ├─ SpecialistPurchaseNotice.json
│  │  │  │     │  ├─ SpecialistRecharge.json
│  │  │  │     │  └─ VW_BIS_Inspector_Cases.json
│  │  │  │     ├─ HorizonVwBISEvent.json
│  │  │  │     ├─ HR_Absence_Data.json
│  │  │  │     ├─ HR_PC.json
│  │  │  │     ├─ IMS
│  │  │  │     │  ├─ IMS_bdc_attribute.json
│  │  │  │     │  ├─ IMS_bdc_entity.json
│  │  │  │     │  ├─ IMS_data_flow.json
│  │  │  │     │  ├─ IMS_data_sharing.json
│  │  │  │     │  ├─ IMS_dpia.json
│  │  │  │     │  ├─ IMS_information_assets.json
│  │  │  │     │  ├─ IMS_integration.json
│  │  │  │     │  ├─ IMS_master_data_map.json
│  │  │  │     │  └─ IMS_ropa.json
│  │  │  │     ├─ IMS_Attribute.json
│  │  │  │     ├─ IMS_DataFlow.json
│  │  │  │     ├─ IMS_DPIA.json
│  │  │  │     ├─ IMS_DSA.json
│  │  │  │     ├─ IMS_Entity.json
│  │  │  │     ├─ IMS_InformationAsset.json
│  │  │  │     ├─ IMS_Intergration.json
│  │  │  │     ├─ IMS_MasterDataMap.json
│  │  │  │     ├─ IMS_ROPA.json
│  │  │  │     ├─ InspectorManager.json
│  │  │  │     ├─ InvalidNullityReference.json
│  │  │  │     ├─ Leave_Entitlement.json
│  │  │  │     ├─ LegacyTimeSheets
│  │  │  │     │  ├─ MWR_Inspector_dim.json
│  │  │  │     │  ├─ MWR_Lines.json
│  │  │  │     │  ├─ MWR_Status.json
│  │  │  │     │  └─ MWR_Submisison_Date.json
│  │  │  │     ├─ LevelReference.json
│  │  │  │     ├─ ListedBuildings
│  │  │  │     │  ├─ listed_building.json
│  │  │  │     │  └─ listed_building_outline.json
│  │  │  │     ├─ Local_Planning_Authority.json
│  │  │  │     ├─ ManagerTypeReference.json
│  │  │  │     ├─ Nsi.json
│  │  │  │     ├─ NSIP
│  │  │  │     │  ├─ NSIPProject.json
│  │  │  │     │  ├─ nsip_exam_timetable.json
│  │  │  │     │  └─ nsip_s51_advice.json
│  │  │  │     ├─ OutcomeReference.json
│  │  │  │     ├─ PresentationAccuracyDetailReference.json
│  │  │  │     ├─ ProcedureReference.json
│  │  │  │     ├─ ReadingCase.json
│  │  │  │     ├─ ReadingStatusReference.json
│  │  │  │     ├─ ReadingTypeReference.json
│  │  │  │     ├─ SAPHR.JSON
│  │  │  │     ├─ SAP_email.json
│  │  │  │     ├─ SAP_Leavers.json
│  │  │  │     ├─ SourceReference.json
│  │  │  │     ├─ Specialisms.JSON
│  │  │  │     ├─ StructureReasoningDetailReference.json
│  │  │  │     ├─ Timesheets
│  │  │  │     │  ├─ Calendar.json
│  │  │  │     │  ├─ Employee.json
│  │  │  │     │  ├─ Local_Plans.json
│  │  │  │     │  ├─ Segment_Type_Reference.json
│  │  │  │     │  ├─ Specialist_Hedgerow.json
│  │  │  │     │  ├─ Specialist_HH.json
│  │  │  │     │  ├─ Specialist_TPO.json
│  │  │  │     │  ├─ Work_Segment.json
│  │  │  │     │  └─ Work_Segment_Lock.json
│  │  │  │     └─ WorkScheduleRule.json
│  │  │  ├─ data-lifecycle
│  │  │  │  └─ policies.json
│  │  │  ├─ devops-agents
│  │  │  │  ├─ build.pkr.hcl
│  │  │  │  ├─ sources.pkr.hcl
│  │  │  │  ├─ tools.sh
│  │  │  │  └─ variables.pkr.hcl
│  │  │  ├─ firewall-rules
│  │  │  │  └─ allowed_ip_addresses.yaml
│  │  │  ├─ README.md
│  │  │  └─ spark-pool
│  │  │     ├─ environment.yml
│  │  │     ├─ requirements-preview.txt
│  │  │     └─ requirements.txt
│  │  ├─ environments
│  │  │  ├─ dev.tfvars
│  │  │  ├─ prod.tfvars
│  │  │  └─ test.tfvars
│  │  ├─ locals.tf
│  │  ├─ modules
│  │  │  ├─ api-management
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ Demo_Conference_API.openapi+json.json
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ main.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variable.tf
│  │  │  ├─ bastion-host
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ bastion-host-nsg.tf
│  │  │  │  ├─ bastion-host.tf
│  │  │  │  ├─ bastion-vm-nsg.tf
│  │  │  │  ├─ bastion-vm.tf
│  │  │  │  ├─ key-vault-secrets.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ devops-agent-pool
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ agent-vmss.tf
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ outputs.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  ├─ resource-group.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ function-app
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ main.tf
│  │  │  │  ├─ output.tf
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ logic-app
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ api-connections.tf
│  │  │  │  ├─ api-custom-connector.tf
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ provider.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ region.tf
│  │  │  │  ├─ variable.tf
│  │  │  │  ├─ zendesk-created-workflow.tf
│  │  │  │  ├─ zendesk-swagger.json
│  │  │  │  ├─ zendesk-template.json
│  │  │  │  └─ zendesk-updated-workflow.tf
│  │  │  ├─ odt-backoffice-sb
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ odt-backoffice-topic-subscriptions.tf
│  │  │  │  ├─ odt-backofifce-private-endpoint.tf
│  │  │  │  ├─ outputs.tf
│  │  │  │  ├─ provider.tf
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ service-plan
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ main.tf
│  │  │  │  ├─ output.tf
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variable.tf
│  │  │  ├─ storage-account
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ main.tf
│  │  │  │  ├─ output.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-data-lake
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ data-lake-configuration.tf
│  │  │  │  ├─ data-lake-firewall.tf
│  │  │  │  ├─ data-lake-lifecycle-policy.tf
│  │  │  │  ├─ data-lake-private-endpoint.tf
│  │  │  │  ├─ data-lake-rbac.tf
│  │  │  │  ├─ data-lake.tf
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ key-vault-rbac.tf
│  │  │  │  ├─ key-vault-secrets.tf
│  │  │  │  ├─ key-vault.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ outputs.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-ingestion
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ outputs.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  ├─ service-bus-failover.tf
│  │  │  │  ├─ service-bus-namespace.tf
│  │  │  │  ├─ service-bus-rbac.tf
│  │  │  │  ├─ service-bus-subscriptions.tf
│  │  │  │  ├─ service-bus-topics.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-management
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ key-vault-private-endpoint.tf
│  │  │  │  ├─ key-vault-rbac.tf
│  │  │  │  ├─ key-vault.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ outputs.tf
│  │  │  │  ├─ purview.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-monitoring
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ alert-data-lake.tf
│  │  │  │  ├─ alert-groups.tf
│  │  │  │  ├─ alert-key-vault.tf
│  │  │  │  ├─ alert-service-health.tf
│  │  │  │  ├─ alert-synapse.tf
│  │  │  │  ├─ application-insights.tf
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ key-vault-secrets.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ log-analytics.tf
│  │  │  │  ├─ monitor-data-lake.tf
│  │  │  │  ├─ monitor-function-app.tf
│  │  │  │  ├─ monitor-key-vault.tf
│  │  │  │  ├─ monitor-network.tf
│  │  │  │  ├─ monitor-service-bus.tf
│  │  │  │  ├─ monitor-synapse-spark-pool.tf
│  │  │  │  ├─ monitor-synapse-sql-pool.tf
│  │  │  │  ├─ monitor-synapse.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-network
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ network-security.tf
│  │  │  │  ├─ network-watcher.tf
│  │  │  │  ├─ network.tf
│  │  │  │  ├─ outputs.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-shir
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ data.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  ├─ scripts
│  │  │  │  │  ├─ Deploy-Requirements.ps1
│  │  │  │  │  ├─ Initialize-IntegrationRuntime.ps1
│  │  │  │  │  └─ Install-OpenJDK.ps1
│  │  │  │  ├─ shir-vm-setup.tf
│  │  │  │  ├─ shir-vm.tf
│  │  │  │  ├─ storage-rbac.tf
│  │  │  │  ├─ storage.tf
│  │  │  │  ├─ synapse-shir.tf
│  │  │  │  └─ variables.tf
│  │  │  ├─ synapse-sql-server
│  │  │  │  ├─ .terraform.lock.hcl
│  │  │  │  ├─ key-vault-secrets.tf
│  │  │  │  ├─ locals.tf
│  │  │  │  ├─ random.tf
│  │  │  │  ├─ README.md
│  │  │  │  ├─ region.tf
│  │  │  │  ├─ sql-server-auditing.tf
│  │  │  │  ├─ sql-server-firewall.tf
│  │  │  │  ├─ sql-server.tf
│  │  │  │  ├─ storage-account-firewall.tf
│  │  │  │  ├─ storage-account-rbac.tf
│  │  │  │  ├─ storage-account.tf
│  │  │  │  ├─ synapse-private-endpoints.tf
│  │  │  │  └─ variables.tf
│  │  │  └─ synapse-workspace-private
│  │  │     ├─ .terraform.lock.hcl
│  │  │     ├─ data-lake-rbac.tf
│  │  │     ├─ key-vault-rbac.tf
│  │  │     ├─ key-vault-secrets.tf
│  │  │     ├─ locals.tf
│  │  │     ├─ outputs.tf
│  │  │     ├─ random.tf
│  │  │     ├─ README.md
│  │  │     ├─ region.tf
│  │  │     ├─ synapse-firewall.tf
│  │  │     ├─ synapse-private-endpoints.tf
│  │  │     ├─ synapse-rbac.tf
│  │  │     ├─ synapse-spark-pool.tf
│  │  │     ├─ synapse-sql-pool.tf
│  │  │     ├─ synapse-workspace.tf
│  │  │     └─ variables.tf
│  │  ├─ outputs.tf
│  │  ├─ provider.tf
│  │  ├─ README.md
│  │  ├─ region.tf
│  │  ├─ variables.tf
│  │  ├─ workload-agent-pool.tf
│  │  ├─ workload-api-manangement.tf
│  │  ├─ workload-data-lake.tf
│  │  ├─ workload-function-app.tf
│  │  ├─ workload-ingestion.tf
│  │  ├─ workload-logic-app.tf
│  │  ├─ workload-management.tf
│  │  ├─ workload-monitoring.tf
│  │  ├─ workload-network.tf
│  │  ├─ workload-odt-backoffice-sb.tf
│  │  ├─ workload-shir.tf
│  │  ├─ workload-sql-server.tf
│  │  └─ workload-synapse.tf
│  ├─ LICENSE
│  ├─ logicapp
│  │  ├─ custom-connectors
│  │  │  ├─ pins-la-custom-connector-zendesk.json
│  │  │  └─ zendesk-custom-connector.yaml
│  │  ├─ documentation.md
│  │  ├─ esb-to-odt-queue
│  │  │  ├─ connections.json
│  │  │  ├─ employee-publish-odt-stateless
│  │  │  │  └─ workflow.json
│  │  │  ├─ host.json
│  │  │  └─ parameters.json
│  │  ├─ logicapp-architecture.ipynb
│  │  ├─ logic_app_architecture_for_zendesk.png
│  │  └─ zendesk-to-esb
│  │     ├─ connections.json
│  │     ├─ host.json
│  │     ├─ zendesk-created
│  │     │  └─ workflow.json
│  │     └─ zendesk-updated
│  │        └─ workflow.json
│  ├─ pipelines
│  │  ├─ devops-agent-deploy.yaml
│  │  ├─ steps
│  │  │  ├─ azure-image-cleanup.yaml
│  │  │  ├─ azure-login.yaml
│  │  │  ├─ azure-private-endpoint-approval.yaml
│  │  │  ├─ azure-resource-lock.yaml
│  │  │  ├─ azure-resource-unlock.yaml
│  │  │  ├─ branch-set-source.yaml
│  │  │  ├─ branch-switch.yaml
│  │  │  ├─ checkov-validate.yaml
│  │  │  ├─ devops-agent-build.yaml
│  │  │  ├─ devops-agent-plan.yaml
│  │  │  ├─ download-secure-file.yaml
│  │  │  ├─ install-checkov.yaml
│  │  │  ├─ install-tflint.yaml
│  │  │  ├─ pause.yaml
│  │  │  ├─ synapse-parameters-override.yaml
│  │  │  ├─ synapse-sql-pool-check.yaml
│  │  │  ├─ synapse-sql-pool-pause.yaml
│  │  │  ├─ synapse-sql-pool-resume.yaml
│  │  │  ├─ terraform-apply.yaml
│  │  │  ├─ terraform-format.yaml
│  │  │  ├─ terraform-init.yaml
│  │  │  ├─ terraform-outputs-to-variables.yaml
│  │  │  ├─ terraform-outputs.yaml
│  │  │  ├─ terraform-plan.yaml
│  │  │  ├─ terraform-validate.yaml
│  │  │  ├─ tflint-validate.yaml
│  │  │  └─ verify-artifact.yaml
│  │  ├─ synapse-release.yaml
│  │  ├─ terraform-cd.yaml
│  │  └─ terraform-ci.yaml
│  ├─ README.md
│  ├─ scripts
│  │  ├─ ims_notebook.ipynb
│  │  ├─ listed-building-api.ipynb
│  │  ├─ odw-validation
│  │  │  ├─ .ruff_cache
│  │  │  │  ├─ 0.1.6
│  │  │  │  │  └─ 6215804850946707106
│  │  │  │  └─ CACHEDIR.TAG
│  │  │  ├─ json-schema.ipynb
│  │  │  ├─ model_nsip_exam_timetable.py
│  │  │  ├─ nsip-exam-timetable.py
│  │  │  ├─ tablefromjson.ipynb
│  │  │  └─ __pycache__
│  │  │     ├─ model_nsip_exam_timetable.cpython-310.pyc
│  │  │     └─ model_nsip_exam_timetable.cpython-311.pyc
│  │  ├─ zendesk-custom-fields.ipynb
│  │  └─ __pycache__
│  │     └─ model_nsip_exam_timetable.cpython-311.pyc
│  ├─ servicebus
│  │  ├─ receivefromsubscription.js
│  │  └─ sendtotopic.js
│  ├─ tests
│  │  └─ mock-data-employee.py
│  └─ workspace
│     ├─ credential
│     │  └─ WorkspaceSystemIdentity.json
│     ├─ dataflow
│     │  └─ Zendesk_POC.json
│     ├─ dataset
│     │  ├─ .DS_Store
│     │  ├─ AzureSqlTable1.json
│     │  ├─ AzureSqlTable2.json
│     │  ├─ a_ds_saphr_excel_binary_source.json
│     │  ├─ BISHighCourtEventDates.json
│     │  ├─ BIS_AddAdditionalData.json
│     │  ├─ BIS_AppealsAdditionalData_Parquet.json
│     │  ├─ BIS_HZN_AppealsAddtionalData.json
│     │  ├─ bkp_dst_odw_config.json
│     │  ├─ bkp_dst_odw_curated.json
│     │  ├─ bkp_dst_odw_harmonised.json
│     │  ├─ bkp_dst_odw_raw.json
│     │  ├─ bkp_dst_odw_standardised.json
│     │  ├─ bkp_src_odw_config.json
│     │  ├─ bkp_src_odw_curated.json
│     │  ├─ bkp_src_odw_harmonised.json
│     │  ├─ bkp_src_odw_raw.json
│     │  ├─ bkp_src_odw_standardised.json
│     │  ├─ b_ds_saphr_excel_binary_sink.json
│     │  ├─ CaseReference.json
│     │  ├─ CaseReferenceRaw.json
│     │  ├─ checkmark_case_marking.json
│     │  ├─ checkmark_comment_state_reference.json
│     │  ├─ checkmark_complexity_reference.json
│     │  ├─ checkmark_conditions_reference.json
│     │  ├─ checkmark_coverage_reference.json
│     │  ├─ checkmark_documents.json
│     │  ├─ checkmark_grounds_reference.json
│     │  ├─ checkmark_inspector_manager.json
│     │  ├─ checkmark_invalid_nullity_reference.json
│     │  ├─ checkmark_level_reference.json
│     │  ├─ checkmark_manager_type_reference.json
│     │  ├─ checkmark_nsi.json
│     │  ├─ Checkmark_outcome_reference.json
│     │  ├─ checkmark_presentation_accuracy_detail_reference.json
│     │  ├─ checkmark_procedure_reference.json
│     │  ├─ checkmark_reading_case.json
│     │  ├─ checkmark_reading_status_reference.json
│     │  ├─ checkmark_reading_type_reference.json
│     │  ├─ checkmark_source_reference.json
│     │  ├─ checkmark_structure_reasoning_detail_reference.json
│     │  ├─ Contacts_Organisation.json
│     │  ├─ Contacts_Organisation_LPA.json
│     │  ├─ CostCenter_Dim_NonPII.JSON
│     │  ├─ DestinationDataset_ahn.json
│     │  ├─ dim_Local_Planning_Authority.json
│     │  ├─ Document_Metadata.json
│     │  ├─ Doc_Folder.json
│     │  ├─ dst_miPINS_load_tables.json
│     │  ├─ dst_MiPINS_load_tables_raw_storage.json
│     │  ├─ dst_source_to_standardised_table_list.json
│     │  ├─ dst_standardised_to_harmonised_pipeline_list.json
│     │  ├─ dst_temp_employee_syn_curated.json
│     │  ├─ dst_temp_employee_syn_service_json_rest.json
│     │  ├─ dst_temp_employee_syn_service_json_storage.json
│     │  ├─ ds_hist_sap_hr.json
│     │  ├─ ds_hist_sap_hr_csv.json
│     │  ├─ ds_odw_mipins_config.json
│     │  ├─ ds_odw_mipins_curated.json
│     │  ├─ ds_odw_mipins_load_tables.json
│     │  ├─ ds_odw_mipins_tables.json
│     │  ├─ ds_odw_mipins_tables_csv.json
│     │  ├─ ds_SAP_HR.json
│     │  ├─ Dtree.json
│     │  ├─ ExaminationTimeTable.json
│     │  ├─ Folder_Entity.json
│     │  ├─ HighCourt.json
│     │  ├─ HighCourtDataSource.json
│     │  ├─ HorizonContactInfo.json
│     │  ├─ HorizonContactInformation.json
│     │  ├─ HorizonData_BIS_AllAppeals.json
│     │  ├─ HorizonVwBISEvent.json
│     │  ├─ Horizon_BIS_AllAppeals_Parquet.json
│     │  ├─ Horizon_Case_Involvement.json
│     │  ├─ Horizon_DocumentMetadata.json
│     │  ├─ Horizon_Folder_Entity.json
│     │  ├─ Horizon_Tables_Data.json
│     │  ├─ Horizon_TypeOfCaseCSV.json
│     │  ├─ Horizon_TypeOfCaseSQL.json
│     │  ├─ Horizon_vw_BIS_Event.json
│     │  ├─ Horizon_VW_BIS_Inspector_Cases.json
│     │  ├─ HZNSpecialCircumstance.json
│     │  ├─ HZNSpecialism.json
│     │  ├─ HZN_AddAdditionalData_Parquet.json
│     │  ├─ HZN_AdditionalFields.json
│     │  ├─ Hzn_AdvertDetails.json
│     │  ├─ HZN_AdvertDetails_Parquet.json
│     │  ├─ HZN_AppSubTypeCaseName.json
│     │  ├─ HZN_BIS_DecisionIssues.json
│     │  ├─ HZN_CaseDates.json
│     │  ├─ HZN_CaseInfo.json
│     │  ├─ HZN_CaseOfficerAddDetail.json
│     │  ├─ HZN_CommonLand.json
│     │  ├─ HZN_DecisionIssues_Parquet.json
│     │  ├─ HZN_EnforcementGroundsForAppeal.json
│     │  ├─ HZN_EnforcementGroundsForAppeal_Parquet.json
│     │  ├─ HZN_Event.json
│     │  ├─ HZN_InspectorCases.json
│     │  ├─ HZN_LPAResponsability_Parquet.json
│     │  ├─ HZN_LPARResponsability.json
│     │  ├─ HZN_NSIPRedactions.json
│     │  ├─ HZN_NSIP_Query.json
│     │  ├─ HZN_ProjInfoInternal.json
│     │  ├─ HZN_RightOfWay.json
│     │  ├─ HZN_Right_Of_Way.json
│     │  ├─ HZN_SpecCaseDates.json
│     │  ├─ HZN_SpecCaseString.json
│     │  ├─ HZN_SpecCoastalAccess.json
│     │  ├─ HZN_SpecEnvironment.json
│     │  ├─ HZN_SpecHighCourt.json
│     │  ├─ HZN_SpecMods.json
│     │  ├─ HZN_SpecPurchaseNotice.json
│     │  ├─ HZN_SpecRecharge.json
│     │  ├─ HZN_ViewData.json
│     │  ├─ IMSAttribute.json
│     │  ├─ IMSDataFlow.json
│     │  ├─ IMSDPIA.json
│     │  ├─ IMSDSA.json
│     │  ├─ IMSEntity.json
│     │  ├─ IMSInformationAsset.json
│     │  ├─ IMSIntergration.json
│     │  ├─ IMSMasterDataMap.json
│     │  ├─ IMSROPA.json
│     │  ├─ IMS_Attribute.json
│     │  ├─ IMS_DataFlow.json
│     │  ├─ IMS_DPIA.json
│     │  ├─ IMS_DSA.json
│     │  ├─ IMS_Entity.json
│     │  ├─ IMS_InformationAsset.json
│     │  ├─ IMS_Intergration.json
│     │  ├─ IMS_MasterDataMap.json
│     │  ├─ IMS_ROPA.json
│     │  ├─ Legacy_Timesheets_Data.json
│     │  ├─ ListedBuildingOutline.json
│     │  ├─ ListedBuildings.json
│     │  ├─ listed_building.json
│     │  ├─ listed_building_csv.json
│     │  ├─ listed_building_outline.json
│     │  ├─ listed_building_outline_csv.json
│     │  ├─ Live_InspectorDIM.json
│     │  ├─ Live_Inspector_dim.json
│     │  ├─ load_vw_horizon_event_dates.json
│     │  ├─ Local_Planning_Authority.json
│     │  ├─ mipins_checkmark_case_comment.json
│     │  ├─ mipins_checkmark_data.json
│     │  ├─ MiPINS_information_schema_columns.json
│     │  ├─ MWR_Lines.json
│     │  ├─ MWR_Status.json
│     │  ├─ MWR_Submission_Date.json
│     │  ├─ NSIPAdvice.json
│     │  ├─ NSIP_Advice.json
│     │  ├─ NSIP_Data.json
│     │  ├─ NSIP_ReleventRepresentation.json
│     │  ├─ SourceDataset_ahn.json
│     │  ├─ SpecialCircumstance_Parquet.json
│     │  ├─ Specialism_Parquet.json
│     │  ├─ Timesheets_Calendar.json
│     │  ├─ Timesheets_Data.json
│     │  ├─ Timesheets_Employee.json
│     │  ├─ Timesheets_Segment_Type_Reference.json
│     │  ├─ Timesheets_Work_Segment.json
│     │  ├─ Timesheets_Work_Segment_Lock.json
│     │  ├─ VW_Inspector_Cases.json
│     │  ├─ zendesk_api_created_24hours.json
│     │  ├─ zendesk_api_created_response_24hours.json
│     │  ├─ zendesk_api_historical_response.json
│     │  ├─ zendesk_api_historical_tickets.json
│     │  ├─ zendesk_api_updated_24hours.json
│     │  └─ zendesk_api_updated_response_24hours.json
│     ├─ integrationRuntime
│     │  ├─ AutoResolveIntegrationRuntime.json
│     │  ├─ PinsIntegrationRuntime.json
│     │  ├─ prdacpdb001shir.json
│     │  └─ preacpdb001shir.json
│     ├─ linkedService
│     │  ├─ AzureSqlDatabase1.json
│     │  ├─ HighCourtConnection.json
│     │  ├─ HighCourtLS.json
│     │  ├─ HighCourtRaw.json
│     │  ├─ ls_backup_destination.json
│     │  ├─ ls_backup_source.json
│     │  ├─ ls_datalab.json
│     │  ├─ ls_dsql.json
│     │  ├─ ls_ims_auth.json
│     │  ├─ ls_kv.json
│     │  ├─ ls_listed_building.json
│     │  ├─ ls_odw_sql_mipins.json
│     │  ├─ ls_servicebus.json
│     │  ├─ ls_shpt_mipins.json
│     │  ├─ ls_sql_hzn.json
│     │  ├─ ls_sql_mipins.json
│     │  ├─ ls_ssql_builtin.json
│     │  ├─ ls_storage.json
│     │  ├─ ls_storage_ar.json
│     │  ├─ ls_zendesk.json
│     │  ├─ ls_zendesk_2.json
│     │  ├─ ls_zendesk_custom.json
│     │  ├─ mipins_checkmark_data.json
│     │  ├─ pins-synw-odw-dev-uks-WorkspaceDefaultSqlServer.json
│     │  ├─ pins-synw-odw-dev-uks-WorkspaceDefaultStorage.json
│     │  ├─ pins-synw-odw-dev-ukw-WorkspaceDefaultSqlServer.json
│     │  ├─ pins-synw-odw-dev-ukw-WorkspaceDefaultStorage.json
│     │  ├─ SqlServer1.json
│     │  └─ sql_hzn_tables.json
│     ├─ managedVirtualNetwork
│     │  ├─ default
│     │  │  └─ managedPrivateEndpoint
│     │  │     ├─ AzureSqlDatabase639.json
│     │  │     ├─ synapse-sql-sqlServer--sql-odw-dev-uks.json
│     │  │     ├─ synapse-sql-sqlServer--sql-odw-dev-ukw.json
│     │  │     ├─ synapse-st-dfs--pinsstodwdevuks9h80mb.json
│     │  │     ├─ synapse-st-dfs--pinsstodwdevukwdvzrjm.json
│     │  │     ├─ synapse-ws-sql--pins-synw-odw-dev-uks.json
│     │  │     ├─ synapse-ws-sql--pins-synw-odw-dev-ukw.json
│     │  │     ├─ synapse-ws-sqlOnDemand--pins-synw-odw-dev-uks.json
│     │  │     └─ synapse-ws-sqlOnDemand--pins-synw-odw-dev-ukw.json
│     │  └─ default.json
│     ├─ notebook
│     │  ├─ adding_zendesk_to_service_user.json
│     │  ├─ Calendar.json
│     │  ├─ casework-views.json
│     │  ├─ casework_additional_fields_dim.json
│     │  ├─ casework_advert_details_dim.json
│     │  ├─ casework_all_appeals_additional_data_dim.json
│     │  ├─ casework_all_appeals_dim.json
│     │  ├─ casework_application_sub_type_case_name_dim.json
│     │  ├─ casework_case_dates_dim.json
│     │  ├─ casework_case_fact_legacy.json
│     │  ├─ casework_case_full_list.json
│     │  ├─ casework_case_info_dim.json
│     │  ├─ casework_case_officer_additional_details_dim.json
│     │  ├─ casework_common_land_dim.json
│     │  ├─ casework_contacts_organisation_dim.json
│     │  ├─ casework_contact_information_dim.json
│     │  ├─ casework_contact_information_dim_legacy.json
│     │  ├─ casework_decision_issue_dim.json
│     │  ├─ casework_enforcement_grounds_dim.json
│     │  ├─ casework_event_dim.json
│     │  ├─ casework_event_fact.json
│     │  ├─ casework_hedgerow_dim.json
│     │  ├─ casework_high_hedges_dim.json
│     │  ├─ casework_inspector_cases_dim.json
│     │  ├─ casework_legacy_rights_of_way_dim.json
│     │  ├─ casework_local_planning_authority_dim.json
│     │  ├─ casework_local_planning_authority_fact.json
│     │  ├─ casework_local_plans_dim.json
│     │  ├─ casework_lpa_resposibility_dim.json
│     │  ├─ casework_master.json
│     │  ├─ casework_nsip_advice_dim.json
│     │  ├─ casework_nsip_advice_dim_legacy.json
│     │  ├─ casework_nsip_data_dim.json
│     │  ├─ casework_nsip_data_dim_legacy.json
│     │  ├─ casework_nsip_examination_timetable_dim.json
│     │  ├─ casework_nsip_examination_timetable_dim_legacy.json
│     │  ├─ casework_nsip_redactions_dim.json
│     │  ├─ casework_nsip_relevant_representation_dim.json
│     │  ├─ casework_picaso_dim.json
│     │  ├─ casework_specialism_dim.json
│     │  ├─ casework_specialist_case_dates_dim.json
│     │  ├─ casework_specialist_case_string_dim.json
│     │  ├─ casework_specialist_coastal_access_dim.json
│     │  ├─ casework_specialist_environment_dim.json
│     │  ├─ casework_specialist_high_court_dim.json
│     │  ├─ casework_specialist_modifications_dim.json
│     │  ├─ casework_specialist_purchase_notice_dim.json
│     │  ├─ casework_specialist_recharge_dim.json
│     │  ├─ casework_special_circumstance_dim.json
│     │  ├─ casework_tpo_dim.json
│     │  ├─ checkmark_casemarking_dim.json
│     │  ├─ checkmark_casemarking_fact.json
│     │  ├─ checkmark_case_casemarking_bridge.json
│     │  ├─ checkmark_case_fact.json
│     │  ├─ checkmark_case_reading_case_bridge.json
│     │  ├─ checkmark_comments_case_bridge.json
│     │  ├─ checkmark_comments_dim.json
│     │  ├─ checkmark_comments_fact.json
│     │  ├─ checkmark_comment_state_reference_dim.json
│     │  ├─ checkmark_comment_type_reference_dim.json
│     │  ├─ checkmark_complexity_reference_dim.json
│     │  ├─ checkmark_conditions_reference_dim.json
│     │  ├─ checkmark_coverage_reference_dim.json
│     │  ├─ checkmark_documents_dim.json
│     │  ├─ checkmark_grounds_reference_dim.json
│     │  ├─ checkmark_inspector_manager_dim.json
│     │  ├─ checkmark_inspector_manager_fact.json
│     │  ├─ checkmark_inspector_manager_reading_case_bridge.json
│     │  ├─ checkmark_invalid_nullity_reference_dim.json
│     │  ├─ checkmark_level_reference_dim.json
│     │  ├─ checkmark_manager_type_reference_dim.json
│     │  ├─ checkmark_nsi_dim.json
│     │  ├─ checkmark_outcome_reference_dim.json
│     │  ├─ checkmark_presentation_accuracy_detail_reference_dim.json
│     │  ├─ checkmark_procedure_reference_dim.json
│     │  ├─ checkmark_reading_case.json
│     │  ├─ checkmark_reading_case_bridge.json
│     │  ├─ checkmark_reading_case_fact.json
│     │  ├─ checkmark_reading_status_reference_dim.json
│     │  ├─ checkmark_reading_type_reference_dim.json
│     │  ├─ checkmark_source_reference_dim.json
│     │  ├─ checkmark_structure_reasoning_detail_reference_dim.json
│     │  ├─ dart_cases_api.json
│     │  ├─ data-checks.json
│     │  ├─ data_validation_testing.json
│     │  ├─ data_validation_wip.json
│     │  ├─ delete-hr-harmonised.json
│     │  ├─ document_case_reference_dim.json
│     │  ├─ document_case_type_dim.json
│     │  ├─ document_metadata.json
│     │  ├─ document_meta_data.json
│     │  ├─ document_tree_dim.json
│     │  ├─ employee-publish.json
│     │  ├─ employee.json
│     │  ├─ examination_timetable.json
│     │  ├─ gather_data_quality_reports.json
│     │  ├─ high_court_dim.json
│     │  ├─ HIST_contract_dim.json
│     │  ├─ HIST_costcentre_dim.json
│     │  ├─ HIST_employeegroup_dim.json
│     │  ├─ HIST_employee_dim.json
│     │  ├─ HIST_employee_fact.json
│     │  ├─ HIST_Employee_HR_Hierarchy_Dim.json
│     │  ├─ HIST_HR_record_fact.json
│     │  ├─ HIST_initial_run_views.json
│     │  ├─ HIST_OrganisationUnit_Dim.json
│     │  ├─ HIST_payband_dim.json
│     │  ├─ HIST_payrollarea_dim.json
│     │  ├─ HIST_personnelarea_dim.json
│     │  ├─ HIST_personnelsubarea_dim.json
│     │  ├─ HIST_PINS_location_dim.json
│     │  ├─ HIST_position_dim.json
│     │  ├─ HIST_sap_hr_master.json
│     │  ├─ horizon_folder.json
│     │  ├─ hr_absence_dim.json
│     │  ├─ hr_contract_dim.json
│     │  ├─ hr_costcenter_dim.json
│     │  ├─ hr_disability_dim.json
│     │  ├─ hr_diversity_dim.json
│     │  ├─ hr_employeegroup_dim.json
│     │  ├─ hr_employee_dim.json
│     │  ├─ hr_employee_dim_for_leavers.json
│     │  ├─ hr_employee_fact.json
│     │  ├─ hr_employee_fact_for_leavers.json
│     │  ├─ hr_employee_hr_hierarchy_dim.json
│     │  ├─ hr_employee_leavers_dim.json
│     │  ├─ hr_leave_entitlement_dim.json
│     │  ├─ hr_organisation_unit_dim.json
│     │  ├─ hr_payband_dim.json
│     │  ├─ hr_payroll_area_dim.json
│     │  ├─ hr_personnel_area_dim.json
│     │  ├─ hr_personnel_sub_area_dim.json
│     │  ├─ hr_pins_location_dim.json
│     │  ├─ hr_position_dim.json
│     │  ├─ hr_record_fact.json
│     │  ├─ hr_record_fact_for_leavers.json
│     │  ├─ hr_religion_dim.json
│     │  ├─ hr_secure_info_fact.json
│     │  ├─ hr_specialism_dim.json
│     │  ├─ hr_sxo_dim.json
│     │  ├─ hr_work_schedule_dim.json
│     │  ├─ ims-master.json
│     │  ├─ ims-master_historic.json
│     │  ├─ ims_attribute_dim.json
│     │  ├─ ims_attribute_dim_historic.json
│     │  ├─ ims_dataflow_dim.json
│     │  ├─ ims_dataflow_dim_historic.json
│     │  ├─ ims_dpia_dim.json
│     │  ├─ ims_dpia_dim_historic.json
│     │  ├─ ims_dsa_dim.json
│     │  ├─ ims_dsa_dim_historic.json
│     │  ├─ ims_entity_dim.json
│     │  ├─ ims_entity_dim_historic.json
│     │  ├─ ims_information_asset_dim.json
│     │  ├─ ims_information_asset_dim_historic.json
│     │  ├─ ims_integration_dim.json
│     │  ├─ ims_integration_dim_historic.json
│     │  ├─ ims_masterdata_map_dim.json
│     │  ├─ ims_masterdata_map_dim_historic.json
│     │  ├─ ims_ropa_dim.json
│     │  ├─ ims_ropa_dim_historic.json
│     │  ├─ lake database query.json
│     │  ├─ leave.json
│     │  ├─ Leavers not in SAPHR.json
│     │  ├─ legacy_mrw_tables.json
│     │  ├─ legacy_service_user_dim.json
│     │  ├─ listed_building_dim.json
│     │  ├─ listed_building_outline_dim.json
│     │  ├─ main_sourcesystem_fact.json
│     │  ├─ master.json
│     │  ├─ mipins_high_court.json
│     │  ├─ mipins_hr_contract.json
│     │  ├─ mipins_hr_cost_centre.json
│     │  ├─ mipins_hr_employee_leavers.json
│     │  ├─ mipins_hr_fact_sickness.json
│     │  ├─ mipins_hr_measures.json
│     │  ├─ mipins_hr_measures_NEW.json
│     │  ├─ mipins_hr_measures_new_data_lookup.json
│     │  ├─ mipins_hr_measures_old_data_ingestion.json
│     │  ├─ mipins_hr_organisation_unit.json
│     │  ├─ mipins_hr_personnel_area.json
│     │  ├─ mipins_hr_personnel_sub_area.json
│     │  ├─ mipins_hr_protected_data.json
│     │  ├─ mipins_ims_masterdatamap.json
│     │  ├─ MiPINS_query.json
│     │  ├─ mipins_views.json
│     │  ├─ mipins_vw_fact_absence_all.json
│     │  ├─ Notebook 1.json
│     │  ├─ nsip-project-subscribe.json
│     │  ├─ nsip_applicant_service_user.json
│     │  ├─ nsip_data.json
│     │  ├─ nsip_relevant_reps.json
│     │  ├─ nsip_s51_advice.json
│     │  ├─ outstanding_files_add_entry.json
│     │  ├─ py_0_create_config_tables.json
│     │  ├─ py_0_log_copy_activity_output.json
│     │  ├─ py_0_log_notebook_output.json
│     │  ├─ py_0_source_to_raw_hr_functions.json
│     │  ├─ py_0_source_to_raw_hr_main.json
│     │  ├─ py_0_source_to_raw_hr_tests.json
│     │  ├─ py_1_initial_run_raw_to_standardised_scheduling.json
│     │  ├─ py_1_raw_to_standardised_hr_functions.json
│     │  ├─ py_1_raw_to_standardised_hr_main.json
│     │  ├─ py_1_raw_to_standardised_hr_tests.json
│     │  ├─ py_1_raw_to_standardised_scheduling.json
│     │  ├─ py_4_curated_tables.json
│     │  ├─ py_amend_tables.json
│     │  ├─ py_casework_raw_to_std.json
│     │  ├─ py_change_table.json
│     │  ├─ py_convert_json_to_csv_ims.json
│     │  ├─ py_convert_json_to_csv_listed_buildings.json
│     │  ├─ py_create_lake_databases.json
│     │  ├─ py_create_schema_from_raw.json
│     │  ├─ py_create_tables.json
│     │  ├─ py_create_tables_new.json
│     │  ├─ py_create_views_SAP_HR.json
│     │  ├─ py_daily_files_into_date_folders.json
│     │  ├─ py_delete_outstanding_files_entry.json
│     │  ├─ py_delete_rows_raw_to_std_outstanding_files.json
│     │  ├─ py_delete_table.json
│     │  ├─ py_delete_table_contents.json
│     │  ├─ py_delete_view.json
│     │  ├─ py_delta_table_cleanup.json
│     │  ├─ py_employee_harmonised_layer2_transform.json
│     │  ├─ py_fail_activity_logging.json
│     │  ├─ py_generate_schema_script.json
│     │  ├─ py_get_orchestration_entry.json
│     │  ├─ py_harmonised_and_hr_measures_monthly.json
│     │  ├─ py_HIST_all_hist_dates.json
│     │  ├─ py_hr_monthly_raw_to_std.json
│     │  ├─ py_inspector_address_harmonised_layer1_transform.json
│     │  ├─ py_inspector_harmonised_to_curated_load.json
│     │  ├─ py_inspector_raw_harmonised_layer1_transform.json
│     │  ├─ py_load_standardised_to_harmonised.json
│     │  ├─ py_logging_decorator.json
│     │  ├─ py_odw_curated_table_creation.json
│     │  ├─ py_odw_harmonised_table_creation.json
│     │  ├─ py_populate_HR_dimension_tables.json
│     │  ├─ py_populate_HR_dimension_tables_protected_data.json
│     │  ├─ py_process_raw_to_curated_table_for_reports.json
│     │  ├─ py_process_raw_to_standardised_delta_table.json
│     │  ├─ py_process_raw_to_standardised_validate.json
│     │  ├─ py_raw_to_std.json
│     │  ├─ py_reload_hr_leavers.json
│     │  ├─ py_reload_hr_record_fact.json
│     │  ├─ py_sap_hr_harmonised_layer1_transform.json
│     │  ├─ py_sb_to_raw.json
│     │  ├─ py_service_bus_json_to_csv.json
│     │  ├─ py_standardised_to_harmonised_data_conversions.json
│     │  ├─ py_temp_syn_employee_to_curated.json
│     │  ├─ py_testing_change_table_schema.json
│     │  ├─ py_utils_data_validation_final.json
│     │  ├─ py_utils_data_validation_functions.json
│     │  ├─ py_utils_get_function_metadata.json
│     │  ├─ py_utils_get_key_vault_secret.json
│     │  ├─ py_utils_get_standardised_column_names.json
│     │  ├─ py_utils_get_storage_account.json
│     │  ├─ py_versions.json
│     │  ├─ py_vw_SAP_HR_email_harmonised_layer1_transform.json
│     │  ├─ py_vw_SAP_HR_email_weekly_harmonised_layer1_transform.json
│     │  ├─ py_vw_SAP_PINS_email_harmonised_layer1_transform.json
│     │  ├─ sample_to_call_listed_buiding_API.json
│     │  ├─ sap-hr-master.json
│     │  ├─ sap-hr-master_full_reload.json
│     │  ├─ sap-hr-views-historic.json
│     │  ├─ sap-hr-views-leavers.json
│     │  ├─ sap-hr-views-saphr.json
│     │  ├─ sap-hr-views.json
│     │  ├─ service-user-publish-legacy-code.json
│     │  ├─ service-user-publish.json
│     │  ├─ service_user.json
│     │  ├─ service_user_dim.json
│     │  ├─ service_user_zendesk_dim.json
│     │  ├─ template_notebook.json
│     │  ├─ timesheets_master.json
│     │  ├─ timesheets_minutes_dim.json
│     │  ├─ timesheets_record_fact.json
│     │  ├─ timesheets_segment_type_reference_dim.json
│     │  ├─ timesheets_work_segment_dim.json
│     │  ├─ timesheets_work_segment_lock_dim.json
│     │  ├─ zendesk-subscribe.json
│     │  ├─ zendesk_get_created_tickets.json
│     │  ├─ zendesk_get_updated_tickets.json
│     │  ├─ zendesk_harmonised_export.json
│     │  ├─ zendesk_historical.json
│     │  ├─ zendesk_raw_inspect.json
│     │  ├─ zendesk_raw_to_standerdised.json
│     │  ├─ zendesk_read_me.json
│     │  ├─ zendesk_schema_validation.json
│     │  └─ zendesk_standardised_and_harmonised.json
│     ├─ pipeline
│     │  ├─ 0_Horizon_Data_Transfer_Raw.json
│     │  ├─ 0_Horizon_Document_Folder.json
│     │  ├─ 0_Horizon_Service_User.json
│     │  ├─ 0_Horizon_SQL_Tables_Raw_part1.json
│     │  ├─ 0_Horizon_SQL_Tables_Raw_part2.json
│     │  ├─ 0_Legacy_Timesheet_Data_Copy_RAW.json
│     │  ├─ 0_Listed_Buildings_API_to_RAW.json
│     │  ├─ 0_ODT_Data_Transfer.json
│     │  ├─ 0_pln_source_to_raw_fileshare.json
│     │  ├─ 0_pln_source_to_raw_fileshare_copy_activity.json
│     │  ├─ 0_pln_source_to_raw_MiPINS.json
│     │  ├─ 0_Raw_Case_Reference_Tables.json
│     │  ├─ 0_Raw_Checkmark_Data_part1.json
│     │  ├─ 0_Raw_Checkmark_Data_part2.json
│     │  ├─ 0_Raw_High_Court_Data_Copy.json
│     │  ├─ 0_Raw_Horizon_BIS_Event.json
│     │  ├─ 0_Raw_Horizon_Main.json
│     │  ├─ 0_Raw_Horizon_NSIP_Advice.json
│     │  ├─ 0_Raw_Horizon_NSIP_Data.json
│     │  ├─ 0_Raw_Horizon_NSIP_Relevant_Reps.json
│     │  ├─ 0_Raw_IMS.json
│     │  ├─ 0_Raw_IMS_Initial_load.json
│     │  ├─ 0_Timesheets_Data_Copy_RAW.json
│     │  ├─ 0_Zendesk_API_to_RAW.json
│     │  ├─ 0_Zendesk_API_to_RAW_historical_load.json
│     │  ├─ 0_ZenDesk_Data_Transfer.json
│     │  ├─ CopyPipeline_ahn.json
│     │  ├─ data_validation_test.json
│     │  ├─ pln_backup_odw_config.json
│     │  ├─ pln_backup_odw_curated.json
│     │  ├─ pln_backup_odw_harmonised.json
│     │  ├─ pln_backup_odw_raw.json
│     │  ├─ pln_backup_odw_standardised.json
│     │  ├─ pln_casework_deployment_clean_slate.json
│     │  ├─ pln_casework_harmonised_deployment.json
│     │  ├─ pln_casework_main.json
│     │  ├─ pln_casework_source_to_raw.json
│     │  ├─ pln_casework_source_to_raw_legacy.json
│     │  ├─ pln_copy_mipins.json
│     │  ├─ pln_copy_mipins_TEST.json
│     │  ├─ pln_fact_sickness.json
│     │  ├─ pln_high_court_main.json
│     │  ├─ pln_horizon_nsip_exam_timetable.json
│     │  ├─ pln_horizon_nsip_project.json
│     │  ├─ pln_horizon_nsip_s51_advice.json
│     │  ├─ pln_horizon_service_user.json
│     │  ├─ pln_hr_cube_objects.json
│     │  ├─ pln_hr_deployment_clean_slate.json
│     │  ├─ pln_hr_ingestion_harmonised_and_measures.json
│     │  ├─ pln_hr_ingestion_initial.json
│     │  ├─ pln_hr_main.json
│     │  ├─ pln_hr_measures_schedule.json
│     │  ├─ pln_ims_main.json
│     │  ├─ pln_initial_high_court.json
│     │  ├─ pln_listed_buildings_main.json
│     │  ├─ pln_load_employee_standardised_to_harmonised.json
│     │  ├─ pln_load_harmonised_to_curated.json
│     │  ├─ pln_load_raw_to_standardised.json
│     │  ├─ pln_load_standardised_to_harmonised.json
│     │  ├─ pln_migration_test.json
│     │  ├─ pln_mipins_raw_to_curated.json
│     │  ├─ pln_mipins_raw_to_curated_new_1.json
│     │  ├─ pln_mipins_raw_to_curated_new_2.json
│     │  ├─ pln_nisp_relevant_reps_clean_slate.json
│     │  ├─ pln_nsip_exam_timetable_clean_slate.json
│     │  ├─ pln_nsip_exam_timetable_main.json
│     │  ├─ pln_nsip_project_clean_slate.json
│     │  ├─ pln_nsip_project_main.json
│     │  ├─ pln_nsip_relevant_reps_main.json
│     │  ├─ pln_nsip_s51_advice_clean_slate.json
│     │  ├─ pln_nsip_s51_advice_main.json
│     │  ├─ pln_odw_master.json
│     │  ├─ pln_post_deployment.json
│     │  ├─ pln_raw_to_standardised_e2e.json
│     │  ├─ pln_service_bus_nsip_exam_timetable.json
│     │  ├─ pln_service_bus_nsip_project.json
│     │  ├─ pln_service_bus_nsip_s51_advice.json
│     │  ├─ pln_service_bus_service_user.json
│     │  ├─ pln_service_user_clean_slate.json
│     │  ├─ pln_service_user_main.json
│     │  ├─ pln_temp_employee_syn_raw_to_curated.json
│     │  ├─ pln_temp_eployee_syn_service_to_raw.json
│     │  ├─ pln_trigger_function_app.json
│     │  ├─ pln_zendesk_main.json
│     │  └─ pl_copy_sap_load_tables_to_raw_storage.json
│     ├─ publish_config.json
│     ├─ sparkConfiguration
│     │  ├─ Kat.json
│     │  ├─ MaxBuffer.json
│     │  ├─ maxFields.json
│     │  └─ NewConfig.json
│     ├─ sqlscript
│     │  ├─ add_user.json
│     │  ├─ Dart_API_testing.json
│     │  ├─ dart_query.json
│     │  ├─ dart_test.json
│     │  ├─ document_meta_data.json
│     │  ├─ Duplicates_in_Employee_Dim.json
│     │  ├─ Duplicates_in_Employee_Fact.json
│     │  ├─ hist_sap_hr.json
│     │  ├─ Horizon_Service_User_Data.json
│     │  ├─ hr_checking_duplicates.json
│     │  ├─ IMS InformationAsset.json
│     │  ├─ IMS_Attribute.json
│     │  ├─ IMS_Entity.json
│     │  ├─ IMS_Masterdata_Map.json
│     │  ├─ IMS_ROPA.json
│     │  ├─ mipins_high_court.json
│     │  ├─ mipins_hr_contract.json
│     │  ├─ mipins_hr_cost_centre.json
│     │  ├─ mipins_hr_employee_details.json
│     │  ├─ mipins_hr_employee_leavers.json
│     │  ├─ mipins_hr_fact_sickness.json
│     │  ├─ mipins_hr_organisational_unit.json
│     │  ├─ mipins_hr_personnel_area.json
│     │  ├─ mipins_hr_personnel_area_table.json
│     │  ├─ mipins_hr_personnel_sub_area.json
│     │  ├─ mipins_hr_protected_data.json
│     │  ├─ mipins_vw_fact_absence_all.json
│     │  ├─ miPINS_vw_mipins_high_court.json
│     │  ├─ miPINS_vw_mipins_listed_building.json
│     │  ├─ SQL script 1.json
│     │  ├─ Table without duplicates.json
│     │  ├─ vw_mipins_hr_gender.json
│     │  └─ vw_service_user.json
│     ├─ template-parameters-definition.json
│     └─ trigger
│        ├─ odt-to-odw.json
│        ├─ src_to_standardised_trigger.json
│        ├─ tr_backup_daily.json
│        ├─ tr_daily.json
│        └─ tr_weekly.json
├─ package-lock.json
├─ package.json
├─ pathlib.ipynb
├─ PINS.code-workspace
├─ pins_azure_architecture.png
├─ planning-swagger.json
├─ python-snippets
│  ├─ create-function-reference-table.ipynb
│  ├─ create-function-reference-table.py
│  ├─ dynamically-populate-function-args.py
│  ├─ function-args-unittest.py
│  └─ README.md
├─ questofpython
│  └─ challenge1.ipynb
├─ README.md
├─ requirements.txt
├─ service-user.json
├─ servicebus-test-py
├─ servicebus.code-workspace
├─ sql_parse.py
├─ synapse_sql_extract.ipynb
├─ synapse_sql_extract.sql
├─ table_keys.json
├─ table_mapping.json
├─ test_results_dict.json
├─ zendesk-data.ipynb
├─ zendesk.py
├─ zendesk_sample.json
├─ __azurite_db_blob_extent__.json
├─ __azurite_db_blob__.json
├─ __azurite_db_queue_extent__.json
├─ __azurite_db_queue__.json
├─ __azurite_db_table__.json
├─ __blobstorage__
│  └─ 49c6c808-710e-4bd4-a82f-02e575ced10e
├─ __pycache__
│  ├─ asyncio_test_funcs.cpython-311.pyc
│  └─ lasagna.cpython-310.pyc
└─ __queuestorage__

```