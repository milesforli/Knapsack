function FindProxyForURL(url, host)
{
// variable strings to return
var proxy_yes = "PROXY 106.14.14.109:8888";
var proxy_no = "DIRECT";
var resolved_ip = dnsResolve(host);
 
// If a specific URL needs to bypass the proxy then send traffic direct.
if (shExpMatch(url, "*.imtt.qq.com*")) { return proxy_yes; }
if (shExpMatch(url, "*.tbs.qq.com*")) { return proxy_yes; }
if (shExpMatch(url, "*.wx.qq.com*")) { return proxy_yes; }
if (shExpMatch(url, "*.weixin.qq.com*")) { return proxy_yes; }
if (shExpMatch(url, "*.qpic.cn*")) { return proxy_yes; }
if (shExpMatch(url, "*.qlogo.cn*")) { return proxy_yes; }
// if (isInNet(resolved_ip, "10.0.0.0",  "255.0.0.0")) { return proxy_no; }
elsereturn "DIRECT";
}
