import requests
response=requests.post("https://graph.facebook.com/104663191095947/feed?message=Hello Fans!&access_token=EAAIo4wKxn9kBAAzRexKZBQ91h85NpMoOnh0TbQ1VBR4f1C0wwg4pWgNOBZCI2zIZB21MLzfLqC08LE6akbI2a1zEI1TDsefvOwaQzI1X0RvfsF8HLkhTcZCYZC5ZCy0C9oL9Mqw1b5ZBSo2ULrp64Xfh66cAlSTgqrQNQWDZA2VRKEPBlAJT7CitajIFCUiEXHwBDuV4qZBfD9nPYSD8i6qMr"
)
print(response.json())



