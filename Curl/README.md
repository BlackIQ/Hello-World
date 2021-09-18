# Curl

cURL is a computer software project providing a library (libcurl) and command-line tool (curl) for transferring data using various network protocols. The name stands for "Client URL", which was first released in 1997.

cURL was first released in 1997. It was originally named httpget and then became urlget before adopting the current name of cURL. The original author and lead developer is the Swedish developer Daniel Stenberg, who created cURL because he wanted to automate the fetching of currency exchange rates for IRC users.

cURL is a command-line tool for getting or sending data including files using URL syntax. Since cURL uses libcurl, it supports every protocol libcurl supports.

cURL supports HTTPS and performs SSL certificate verification by default when a secure protocol is specified such as HTTPS. When cURL connects to a remote server via HTTPS, it will obtain the remote server certificate, then check against its CA certificate store the validity of the remote server to ensure the remote server is the one it claims to be. Some cURL packages are bundled with CA certificate store file. There are several options to specify a CA certificate such as --cacert and --capath. The --cacert option can be used to specify the location of the CA certificate store file. In the Windows platform, if a CA certificate file is not specified, cURL will look for a CA certificate file name “curl-ca-bundle.crt” in the following order:

- Directory where the cURL program is located.
- Current working directory.
- Windows system directory.
- Windows directory.
- Directories specified in the %PATH% environment variables.

cURL will return an error message if the remote server is using a self-signed certificate, or if the remote server certificate is not signed by a CA listed in the CA cert file. -k or --insecure option can be used to skip certificate verification. Alternatively, if the remote server is trusted, the remote server CA certificate can be added to the CA certificate store file.

## Refrences

- [cURL](https://curl.se)
- [Wikipedia](https://en.wikipedia.org/wiki/CURL)