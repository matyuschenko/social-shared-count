# Social Shared Count

Check how many times your url was shared on Facebook and VK. For Facebook it returns _"an aggregation of shares, likes, and comments for the URL. This number is approximate"_. We are not sure this method would be supported as even now it may be found in [outdated documentation only](https://developers.facebook.com/docs/graph-api/reference/v2.8/url).

You need a [Facebook user token](https://developers.facebook.com/tools/accesstoken/) to run this script. Put it in a _TOKEN_ file next to the script.

The script can separately get shares for url with parameters, e.g. for _example.com_ you can also count:
* _example.com/?res=1_
* _example.com/?res=2_
* _example.com/?res=3_
* etc.

If you provide human-readable explanation for your parameters in a separate file _param_names.txt_, they may be indicated in result.
