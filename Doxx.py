import base64
exec(base64.b64decode(b'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBzb2NrZXQKaW1wb3J0IHdob2lzCmltcG9ydCB0aW1lCmltcG9ydCBvcwppbXBvcnQgc3VicHJvY2VzcwoKIyBNYXN1a2thbiBBUEkgS2V5IEh1bnRlci5pbyBBbmRhCkhVTlRFUl9BUElfS0VZID0gIjRhYzcwNjg5NDc4NDkzYzk2NDc1MDFkZGJiMTBjZjZhMWY1ZjlmYmEiCgojIEFOU0kgRXNjYXBlIENvZGVzIHVudHVrIHdhcm5hCldISVRFID0gIlwwMzNbOTdtIgpHUkVFTiA9ICJcMDMzWzkybSIKUkVTRVQgPSAiXDAzM1swbSIKCiMgRnVuZ3NpIHVudHVrIG1lbWJlcnNpaGthbiBsYXlhcgpkZWYgY2xlYXJfc2NyZWVuKCk6CiAgICBvcy5zeXN0ZW0oJ2NscycgaWYgb3MubmFtZSA9PSAnbnQnIGVsc2UgJ2NsZWFyJykKCiMgRnVuZ3NpIHVudHVrIG1lbWFpbmthbiBmaWxlIE1QMyBkZW5nYW4gbXB2IGRhbGFtIG1vZGUgbG9vcApkZWYgcGxheV9tcDMoKToKICAgIHRyeToKICAgICAgICAjIE1lbmphbGFua2FuIG1wdiBkaSBiYWNrZ3JvdW5kIGRlbmdhbiBwYXJhbWV0ZXIgLS1sb29wPWluZiBhZ2FyIGZpbGUgZGlwdXRhciBzZWNhcmEgdGVydXMtbWVuZXJ1cwogICAgICAgIHN1YnByb2Nlc3MuUG9wZW4oWyJtcHYiLCAiLS1sb29wPWluZiIsICJQLm1wMyJdLCBzdGRvdXQ9c3VicHJvY2Vzcy5QSVBFLCBzdGRlcnI9c3VicHJvY2Vzcy5QSVBFKQogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIHByaW50KGYiWy1dIEVycm9yIHBsYXlpbmcgTVAzIGZpbGU6IHtlfSIpCgojIE1lbmFtYmFoa2FuIEhlYWRlciBUb29sCmRlZiBwcmludF9oZWFkZXIoKToKICAgIHByaW50KGYie0dSRUVOfVxueyc9JyAqIDQwfSIpCiAgICBwcmludCgiICIgKiAxMCArICJPU0lOVCBXRUJTSVRFIEJZIElORkVSTkFMWFBMT0lUIiArICIgIiAqIDEwKQogICAgcHJpbnQoZiJ7Jz0nICogNDB9IikKICAgIHByaW50KCIgIiAqIDEwICsgIklORkVSTkFMWFBMT0lUIFRPT0xTIiArICIgIiAqIDEwKQogICAgcHJpbnQoZiJ7Jz0nICogNDB9IikKICAgIHByaW50KGYiQXV0aG9yOiBJTkZFUk5BTFhQTE9JVCIubGp1c3QoNDApKQogICAgcHJpbnQoZiJJbnN0YWdyYW06IGluZmVybmFseHBsb2l0Ii5sanVzdCg0MCkpCiAgICBwcmludChmIlRpa1RvazogcmVueHBsb2l0MSIubGp1c3QoNDApKQogICAgcHJpbnQoZiJ7Jz0nICogNDB9e1JFU0VUfSIpCgpkZWYgbG9hZGluZ19hbmltYXRpb24oKToKICAgIGZvciBfIGluIHJhbmdlKDMpOgogICAgICAgIHByaW50KGYie0dSRUVOfUxvYWRpbmciLCBlbmQ9IiIpCiAgICAgICAgZm9yIF8gaW4gcmFuZ2UoMyk6CiAgICAgICAgICAgIHRpbWUuc2xlZXAoMC41KQogICAgICAgICAgICBwcmludCgiLiIsIGVuZD0iIiwgZmx1c2g9VHJ1ZSkKICAgICAgICBwcmludCgiXG4iLCBlbmQ9IiIsIGZsdXNoPVRydWUpCgpkZWYgZ2V0X2h0dHBfaGVhZGVycyh1cmwpOgogICAgdHJ5OgogICAgICAgIHJlc3BvbnNlID0gcmVxdWVzdHMuZ2V0KHVybCkKICAgICAgICBwcmludChmIntHUkVFTn1cbnsnPScqNDB9IikKICAgICAgICBwcmludChmIlsrXSBIVFRQIEhlYWRlcnMgZm9yIHt1cmx9OiIpCiAgICAgICAgZm9yIGtleSwgdmFsdWUgaW4gcmVzcG9uc2UuaGVhZGVycy5pdGVtcygpOgogICAgICAgICAgICBwcmludChmIiAge1dISVRFfXtrZXl9OiB7dmFsdWV9IikKICAgICAgICBwcmludChmInsnPScqNDB9e1JFU0VUfSIpCiAgICBleGNlcHQgcmVxdWVzdHMuZXhjZXB0aW9ucy5SZXF1ZXN0RXhjZXB0aW9uIGFzIGU6CiAgICAgICAgcHJpbnQoZiJ7R1JFRU59Wy1dIEVycm9yIGZldGNoaW5nIEhUVFAgaGVhZGVyczoge2V9e1JFU0VUfSIpCgpkZWYgZ2V0X3dob2lzX2luZm8oZG9tYWluKToKICAgIHRyeToKICAgICAgICB3ID0gd2hvaXMud2hvaXMoZG9tYWluKQogICAgICAgIHByaW50KGYie0dSRUVOfVxueyc9Jyo0MH0iKQogICAgICAgIHByaW50KGYiWytdIFdIT0lTIEluZm9ybWF0aW9uIGZvciB7ZG9tYWlufToiKQogICAgICAgIHByaW50KGYiICBEb21haW4gTmFtZToge1dISVRFfXt3LmRvbWFpbl9uYW1lfSIpCiAgICAgICAgcHJpbnQoZiIgIFJlZ2lzdHJhcjoge1dISVRFfXt3LnJlZ2lzdHJhcn0iKQogICAgICAgIHByaW50KGYiICBDcmVhdGlvbiBEYXRlOiB7V0hJVEV9e3cuY3JlYXRpb25fZGF0ZX0iKQogICAgICAgIHByaW50KGYiICBFeHBpcmF0aW9uIERhdGU6IHtXSElURX17dy5leHBpcmF0aW9uX2RhdGV9IikKICAgICAgICBwcmludChmIiAgTmFtZSBTZXJ2ZXJzOiB7V0hJVEV9eycsICcuam9pbih3Lm5hbWVfc2VydmVycyl9IikKICAgICAgICBwcmludChmInsnPScqNDB9e1JFU0VUfSIpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgcHJpbnQoZiJ7R1JFRU59Wy1dIEVycm9yIGZldGNoaW5nIFdIT0lTIGluZm9ybWF0aW9uOiB7ZX17UkVTRVR9IikKCmRlZiBmaW5kX3N1YmRvbWFpbnMoZG9tYWluKToKICAgIHN1YmRvbWFpbnMgPSBbInd3dyIsICJtYWlsIiwgImZ0cCIsICJ0ZXN0IiwgImFkbWluIiwgImJsb2ciXQogICAgcHJpbnQoZiJ7R1JFRU59XG57Jz0nKjQwfSIpCiAgICBwcmludChmIlsrXSBTZWFyY2hpbmcgZm9yIHN1YmRvbWFpbnMgZm9yIHtkb21haW59Li4uIikKICAgIGZvciBzdWIgaW4gc3ViZG9tYWluczoKICAgICAgICBzdWJkb21haW4gPSBmIntzdWJ9Lntkb21haW59IgogICAgICAgIHRyeToKICAgICAgICAgICAgaXAgPSBzb2NrZXQuZ2V0aG9zdGJ5bmFtZShzdWJkb21haW4pCiAgICAgICAgICAgIHByaW50KGYiICBGb3VuZDoge1dISVRFfXtzdWJkb21haW59ICh7aXB9KXtSRVNFVH0iKQogICAgICAgIGV4Y2VwdCBzb2NrZXQuZ2FpZXJyb3I6CiAgICAgICAgICAgIHBhc3MKICAgIHByaW50KGYie0dSRUVOfXsnPScqNDB9e1JFU0VUfSIpCgpkZWYgZ2V0X2lwX2luZm8oaXApOgogICAgdHJ5OgogICAgICAgIHJlc3BvbnNlID0gcmVxdWVzdHMuZ2V0KGYiaHR0cDovL2lwLWFwaS5jb20vanNvbi97aXB9IikKICAgICAgICBkYXRhID0gcmVzcG9uc2UuanNvbigpCiAgICAgICAgcHJpbnQoZiJ7R1JFRU59XG57Jz0nKjQwfSIpCiAgICAgICAgcHJpbnQoZiJbK10gSVAgSW5mb3JtYXRpb24gZm9yIHtpcH06IikKICAgICAgICBwcmludChmIiAgQ291bnRyeToge1dISVRFfXtkYXRhWydjb3VudHJ5J119IikKICAgICAgICBwcmludChmIiAgUmVnaW9uOiB7V0hJVEV9e2RhdGFbJ3JlZ2lvbk5hbWUnXX0iKQogICAgICAgIHByaW50KGYiICBDaXR5OiB7V0hJVEV9e2RhdGFbJ2NpdHknXX0iKQogICAgICAgIHByaW50KGYiICBJU1A6IHtXSElURX17ZGF0YVsnaXNwJ119IikKICAgICAgICBwcmludChmInsnPScqNDB9e1JFU0VUfSIpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgcHJpbnQoZiJ7R1JFRU59Wy1dIEVycm9yIGZldGNoaW5nIElQIGluZm9ybWF0aW9uOiB7ZX17UkVTRVR9IikKCmRlZiBmaW5kX2VtYWlscyhkb21haW4pOgogICAgaWYgbm90IEhVTlRFUl9BUElfS0VZOgogICAgICAgIHByaW50KGYie0dSRUVOfVxuWy1dIEh1bnRlci5pbyBBUEkga2V5IGlzIG1pc3NpbmcuIENhbm5vdCBmZXRjaCBlbWFpbCBhZGRyZXNzZXMue1JFU0VUfSIpCiAgICAgICAgcmV0dXJuCiAgICAKICAgIHVybCA9IGYiaHR0cHM6Ly9hcGkuaHVudGVyLmlvL3YyL2RvbWFpbi1zZWFyY2g/ZG9tYWluPXtkb21haW59JmFwaV9rZXk9e0hVTlRFUl9BUElfS0VZfSIKICAgIHRyeToKICAgICAgICByZXNwb25zZSA9IHJlcXVlc3RzLmdldCh1cmwpCiAgICAgICAgZGF0YSA9IHJlc3BvbnNlLmpzb24oKQogICAgICAgIGlmICdkYXRhJyBpbiBkYXRhIGFuZCAnZW1haWxzJyBpbiBkYXRhWydkYXRhJ106CiAgICAgICAgICAgIGVtYWlscyA9IGRhdGFbJ2RhdGEnXVsnZW1haWxzJ10KICAgICAgICAgICAgcHJpbnQoZiJ7R1JFRU59XG57Jz0nKjQwfSIpCiAgICAgICAgICAgIHByaW50KGYiWytdIEVtYWlscyBmb3VuZCBmb3Ige2RvbWFpbn06IikKICAgICAgICAgICAgZm9yIGVtYWlsIGluIGVtYWlsczoKICAgICAgICAgICAgICAgIHByaW50KGYiICB7V0hJVEV9e2VtYWlsWyd2YWx1ZSddfSAtIHtlbWFpbFsndHlwZSddfXtSRVNFVH0iKQogICAgICAgICAgICBwcmludChmInsnPScqNDB9e1JFU0VUfSIpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgcHJpbnQoZiJ7R1JFRU59XG5bLV0gTm8gZW1haWxzIGZvdW5kIG9yIEFQSSBsaW1pdCByZWFjaGVkLntSRVNFVH0iKQogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIHByaW50KGYie0dSRUVOfVstXSBFcnJvciBmZXRjaGluZyBlbWFpbCBhZGRyZXNzZXM6IHtlfXtSRVNFVH0iKQoKZGVmIG1haW4oKToKICAgIGNsZWFyX3NjcmVlbigpICAjIEJlcnNpaGthbiBsYXlhciBzZWJlbHVtIG1lbXVsYWkKICAgIHByaW50X2hlYWRlcigpCiAgICBsb2FkaW5nX2FuaW1hdGlvbigpCiAgICBwcmludChmIntHUkVFTn1bIE9TSU5UIFRvb2wgZm9yIFdlYnNpdGUgSW52ZXN0aWdhdGlvbiBde1JFU0VUfSIpCiAgICAKICAgIHRhcmdldCA9IGlucHV0KGYie1dISVRFfUVudGVyIGEgd2Vic2l0ZSAoZS5nLiwgZXhhbXBsZS5jb20pOiB7UkVTRVR9Iikuc3RyaXAoKQogICAgCiAgICAjIFJlbW92ZSAiaHR0cDovLyIgb3IgImh0dHBzOi8vIiBpZiBwcm92aWRlZAogICAgaWYgdGFyZ2V0LnN0YXJ0c3dpdGgoImh0dHA6Ly8iKSBvciB0YXJnZXQuc3RhcnRzd2l0aCgiaHR0cHM6Ly8iKToKICAgICAgICB0YXJnZXQgPSB0YXJnZXQuc3BsaXQoIjovLyIpWzFdCgogICAgIyBHZXQgSFRUUCBoZWFkZXJzCiAgICBnZXRfaHR0cF9oZWFkZXJzKGYiaHR0cDovL3t0YXJnZXR9IikKCiAgICAjIEdldCBXSE9JUyBpbmZvcm1hdGlvbgogICAgZ2V0X3dob2lzX2luZm8odGFyZ2V0KQoKICAgICMgRmluZCBzdWJkb21haW5zCiAgICBmaW5kX3N1YmRvbWFpbnModGFyZ2V0KQoKICAgICMgR2V0IElQIGluZm9ybWF0aW9uCiAgICB0cnk6CiAgICAgICAgaXAgPSBzb2NrZXQuZ2V0aG9zdGJ5bmFtZSh0YXJnZXQpCiAgICAgICAgcHJpbnQoZiJ7R1JFRU59XG5bK10gSVAgQWRkcmVzcyBmb3Ige3RhcmdldH06IHtXSElURX17aXB9e1JFU0VUfSIpCiAgICAgICAgZ2V0X2lwX2luZm8oaXApCiAgICBleGNlcHQgc29ja2V0LmdhaWVycm9yOgogICAgICAgIHByaW50KGYie0dSRUVOfVstXSBFcnJvciByZXNvbHZpbmcgSVAgYWRkcmVzcy57UkVTRVR9IikKCiAgICAjIEZpbmQgZW1haWxzCiAgICBmaW5kX2VtYWlscyh0YXJnZXQpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgcGxheV9tcDMoKSAgIyBNZW11bGFpIHBlbXV0YXJhbiBNUDMgZGFsYW0gbG9vcCBkaSBiYWNrZ3JvdW5kCiAgICBtYWluKCk='))