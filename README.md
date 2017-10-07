# Social Shared Count

Check how many times your url was shared on Facebook and VK. For Facebook it returns _"an aggregation of shares, likes, and comments for the URL. This number is approximate"_. We are not sure this method would be supported as even now it may be found in [outdated documentation only](https://developers.facebook.com/docs/graph-api/reference/v2.8/url).

You need a [Facebook user token](https://developers.facebook.com/tools/accesstoken/) to count shares on Facebook. If no token provided, shares for VK only will be calculated.

The script can separately get shares for url with parameters, e.g. for _example.com_ you can also count:
* _example.com/?res=1_
* _example.com/?res=2_
* _example.com/?res=3_
* etc.

The command line arguments syntax is as follows: url [parameter] [max number of url with parameters (not included)] [FB token], e.g.:
_python3 count_shares.py https://example.com res 4 EAAaVWRTd..._