# -*- coding: utf-8 -*-
DESC = "ocr-2018-11-19"
INFO = {
  "InsuranceBillOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持病案首页、费用清单、结算单、医疗发票四种保险理赔单据的文本识别和结构化输出。"
  },
  "GeneralBasicOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "Scene",
        "desc": "保留字段。"
      },
      {
        "name": "LanguageType",
        "desc": "识别语言类型。\n支持自动识别语言类型，同时支持自选语言种类，默认中英文混合(zh)。\n可选值：\nzh\\auto\\jap\\kor\\\nspa\\fre\\ger\\por\\\nvie\\may\\rus\\ita\\\nhol\\swe\\fin\\dan\\\nnor\\hun\\tha\\lat\n可选值分别表示：\n中英文混合、自动识别、日语、韩语、\n西班牙语、法语、德语、葡萄牙语、\n越南语、马来语、俄语、意大利语、\n荷兰语、瑞典语、芬兰语、丹麦语、\n挪威语、匈牙利语、泰语、拉丁语系。"
      }
    ],
    "desc": "本接口支持多场景、任意版面下整图文字的识别。支持自动识别语言类型，同时支持自选语言种类（推荐），除中英文外，支持日语、韩语、西班牙语、法语、德语、葡萄牙语、越南语、马来语、俄语、意大利语、荷兰语、瑞典语、芬兰语、丹麦语、挪威语、匈牙利语、泰语等多种语言。应用场景包括：印刷文档识别、网络图片识别、广告图文字识别、街景店招识别、菜单识别、视频标题识别、头像文字识别等。"
  },
  "EnterpriseLicenseOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持智能化识别各类企业登记证书、许可证书、企业执照、三证合一类证书，结构化输出统一社会信用代码、公司名称、法定代表人、公司地址、注册资金、企业类型、经营范围等关键字段。"
  },
  "BusinessCardOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "Config",
        "desc": "可选字段，根据需要选择是否请求对应字段。\n目前支持的字段为：\nRetImageType-“PROPROCESS” 图像预处理，string 类型。\n图像预处理功能为，检测图片倾斜的角度，将原本倾斜的图片围绕中心点转正，最终输出一张正的名片抠图。\n\nSDK 设置方式参考：\nConfig = Json.stringify({\"RetImageType\":\"PROPROCESS\"})\nAPI 3.0 Explorer 设置方式参考：\nConfig = {\"RetImageType\":\"PROPROCESS\"}"
      }
    ],
    "desc": "本接口支持名片各字段的自动定位与识别，包含姓名、电话、手机号、邮箱、公司、部门、职位、网址、地址、QQ、微信、MSN等。"
  },
  "IDCardOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。\n建议图片存储于腾讯云，可保障更高的下载速度和稳定性。"
      },
      {
        "name": "CardSide",
        "desc": "FRONT：身份证有照片的一面（人像面），\nBACK：身份证有国徽的一面（国徽面），\n该参数如果不填，将为您自动判断身份证正反面。"
      },
      {
        "name": "Config",
        "desc": "以下可选字段均为bool 类型，默认false：\nCropIdCard，身份证照片裁剪（去掉证件外多余的边缘、自动矫正拍摄角度）\nCropPortrait，人像照片裁剪（自动抠取身份证头像区域）\nCopyWarn，复印件告警\nBorderCheckWarn，边框和框内遮挡告警\nReshootWarn，翻拍告警\nDetectPsWarn，PS检测告警\nTempIdWarn，临时身份证告警\nInvalidDateWarn，身份证有效日期不合法告警\nQuality，图片质量分数（评价图片的模糊程度）\n\nSDK 设置方式参考：\nConfig = Json.stringify({\"CropIdCard\":true,\"CropPortrait\":true})\nAPI 3.0 Explorer 设置方式参考：\nConfig = {\"CropIdCard\":true,\"CropPortrait\":true}"
      }
    ],
    "desc": "本接口支持中国大陆居民二代身份证正反面所有字段的识别，包括姓名、性别、民族、出生日期、住址、公民身份证号、签发机关、有效期限，识别准确度达到99%以上。\n\n另外，本接口还支持多种增值能力，满足不同场景的需求。如身份证照片、人像照片的裁剪功能，同时具备9种告警功能，如下表所示。\n\n<table style=\"width:650px\">\n      <thead>\n        <tr>\n       <th width=\"150\">增值能力</th>\n          <th width=\"500\">能力项</th>\n        </tr>\n      </thead>\n      <tbody>\n        <tr>\n          <td rowspan=\"2\">裁剪功能</td>\n          <td>身份证照片裁剪（去掉证件外多余的边缘、自动矫正拍摄角度）</td>\n        </tr>\n        <tr>\n          <td>人像照片裁剪（自动抠取身份证头像区域）</td>\n        </tr>\n        <tr>\n          <td rowspan=\"9\">告警功能</td>\n          <td>身份证有效日期不合法告警</td>\n        </tr>\n        <tr>\n          <td>身份证边框不完整告警</td>\n        </tr>\n        <tr>\n          <td>身份证复印件告警</td>\n        </tr>\n        <tr>\n          <td>身份证翻拍告警</td>\n        </tr>\n          <tr>\n          <td>身份证框内遮挡告警</td>\n        </tr>\n         <tr>\n          <td>临时身份证告警</td>\n        </tr>\n          <tr>\n          <td>身份证 PS 告警</td>\n        </tr>\n          <tr>\n          <td>图片模糊告警</td>\n        </tr>\n      </tbody>\n    </table>"
  },
  "PassportOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。\n建议图片存储于腾讯云，可保障更高的下载速度和稳定性。"
      },
      {
        "name": "Type",
        "desc": "默认填写CN\n支持中国大陆地区护照。"
      }
    ],
    "desc": "本接口支持中国大陆地区护照个人资料页多个字段的检测与识别。已支持字段包括英文姓名、中文姓名、国家码、护照号、出生地、出生日期、国籍英文、性别英文、有效期、签发地点英文、签发日期、持证人签名、护照机读码（MRZ码）等。"
  },
  "MLIDCardOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。( 中国地区之外不支持这个字段 )\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "RetImage",
        "desc": "是否返回图片"
      }
    ],
    "desc": "本接口支持马来西亚身份证识别，识别字段包括身份证号、姓名、性别、地址；具备身份证人像照片的裁剪功能和翻拍、复印件告警功能。\n本接口暂未完全对外开放，如需咨询，请[联系商务](https://cloud.tencent.com/about/connect)\n"
  },
  "QrcodeOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持条形码和二维码的识别（包括 DataMatrix 和 PDF417）。\n本接口暂未完全对外开放，如需咨询，请[联系商务](https://cloud.tencent.com/about/connect) "
  },
  "GeneralAccurateOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持图像整体文字的检测和识别，返回文字框位置与文字内容。相比通用印刷体识别接口，高精度版在英文、数字、小字、模糊字、倾斜文本行等困难场景下，准确率和召回率更高。"
  },
  "MixedInvoiceDetect": {
    "params": [
      {
        "name": "ReturnImage",
        "desc": "是否需要返回裁剪后的图片。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持多张、多类型票据的混合检测和自动分类，返回对应票据类型。目前已支持增值税发票、增值税发票（卷票）、定额发票、通用机打发票、购车发票、火车票、出租车发票、机票行程单、汽车票、轮船票、过路过桥费发票、酒店账单、客运限额发票、购物小票、完税证明共15种票据。"
  },
  "VinOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持图片内车辆识别代号（VIN）的检测和识别。"
  },
  "MLIDPassportOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "RetImage",
        "desc": "是否返回图片"
      }
    ],
    "desc": "本接口支持中国港澳台地区以及其他国家、地区的护照。识别字段包括护照ID、姓名、出生日期、性别、有效期、发行国、国籍；具备护照人像照片的裁剪功能和翻拍、复印件告警功能。\n本接口暂未完全对外开放，如需咨询，请[联系商务](https://cloud.tencent.com/about/connect)"
  },
  "VatRollInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持对增值税发票（卷票）的发票代码、发票号码、日期、校验码、合计金额（小写）等关键字段的识别。"
  },
  "QuotaInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持定额发票的发票号码、发票代码、金额(大小写)、发票消费类型、地区及是否有公司印章等关键字段的识别。"
  },
  "GeneralFastOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持图片中整体文字的检测和识别，返回文字框位置与文字内容。相比通用印刷体识别接口，识别速度更快、支持的 QPS 更高。"
  },
  "PropOwnerCertOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持房产证关键字段的识别，包括房地产权利人、共有情况、登记时间、规划用途、房屋性质、房屋坐落等。"
  },
  "BizLicenseOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持快速精准识别营业执照上的字段，包括注册号、公司名称、经营场所、主体类型、法定代表人、注册资金、组成形式、成立日期、营业期限和经营范围等字段。"
  },
  "GeneralHandwritingOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "Scene",
        "desc": "场景字段，默认不用填写。\n可选值:only_hw  表示只输出手写体识别结果，过滤印刷体。"
      }
    ],
    "desc": "本接口支持图片内手写体文字的检测和识别，针对手写字体无规则、字迹潦草、模糊等特点进行了识别能力的增强。"
  },
  "InvoiceGeneralOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持对通用机打发票的发票代码、发票号码、日期、购买方识别号、销售方识别号、校验码、小写金额等关键字段的识别。"
  },
  "VatInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持增值税专用发票、增值税普通发票、增值税电子发票全字段的内容检测和识别，包括发票代码、发票号码、开票日期、合计金额、校验码、税率、合计税额、价税合计、购买方识别号、复核、销售方识别号、开票人、密码区1、密码区2、密码区3、密码区4、发票名称、购买方名称、销售方名称、服务名称、备注、规格型号、数量、单价、金额、税额、收款人等字段。"
  },
  "WaybillOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持市面上主流版式电子运单的识别，包括收件人和寄件人的姓名、电话、地址以及运单号等字段。"
  },
  "FlightInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持机票行程单关键字段的识别，包括姓名、身份证件号码、航班号、票价 、合计、电子客票号码、填开日期等。"
  },
  "PermitOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持对卡式港澳台通行证的识别，包括签发地点、签发机关、有效期限、性别、出生日期、英文姓名、姓名、证件号等字段。"
  },
  "OrgCodeCertOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持组织机构代码证关键字段的识别，包括代码、有效期、地址、机构名称等。"
  },
  "FinanBillSliceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持常见银行票据的自动分类和识别。切片识别包括金融行业常见票据的重要切片字段识别，包括金额、账号、日期、凭证号码等。（金融票据切片：金融票据中待识别字段及其周围局部区域的裁剪图像。）"
  },
  "BusInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持识别公路汽车客票的发票代码、发票号码、日期、姓名、票价等字段。"
  },
  "TableOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持图片内表格文档的检测和识别，返回每个单元格的文字内容，支持将识别结果保存为 Excel 格式。"
  },
  "HmtResidentPermitOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "CardSide",
        "desc": "FRONT：有照片的一面（人像面），\nBACK：无照片的一面（国徽面），\n该参数如果不填或填错，将为您自动判断正反面。"
      }
    ],
    "desc": "港澳台居住证OCR支持港澳台居住证正反面全字段内容检测识别功能，包括姓名、性别、出生日期、地址、身份证ID、签发机关、有效期限、签发次数、通行证号码关键字段识别。可以应用于港澳台居住证信息有效性校验场景，例如银行开户、用户注册等场景。"
  },
  "ArithmeticOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持作业算式题目的自动识别，目前覆盖 K12 学力范围内的 14 种题型，包括加减乘除四则运算、分数四则运算、竖式四则运算、脱式计算等。"
  },
  "TollInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持对过路过桥费发票的发票代码、发票号码、日期、小写金额等关键字段的识别。"
  },
  "EstateCertOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持不动产权证关键字段的识别，包括使用期限、面积、用途、权利性质、权利类型、坐落、共有情况、权利人、权利其他状况等。\n\n\n"
  },
  "FinanBillOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持常见银行票据的自动分类和识别。整单识别包括支票（含现金支票、普通支票、转账支票），承兑汇票（含银行承兑汇票、商业承兑汇票）以及进账单等，适用于中国人民银行印发的 2010 版银行票据凭证版式（银发[2010]299 号）。"
  },
  "TrainTicketOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持火车票全字段的识别，包括编号、票价、姓名、座位号、出发时间、出发站、到达站、车次、席别、发票类型及序列号等。\n"
  },
  "TextDetect": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口通过检测图片中的文字信息特征，快速判断图片中有无文字并返回判断结果，帮助用户过滤无文字的图片。"
  },
  "GeneralEfficientOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持多场景、任意版面下整图文字的识别。相较于“通用印刷体识别”接口，精简版接口在准召率有一定损失的情况下，耗时更短。适用于对接口耗时较为敏感的客户。"
  },
  "TaxiInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持出租车发票关键字段的识别，包括发票号码、发票代码、金额、日期、上下车时间、里程、车牌号、发票类型及所属地区等字段。"
  },
  "ResidenceBookletOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持居民户口簿户主页及成员页关键字段的识别，包括姓名、户别、地址、籍贯、身份证号码等。"
  },
  "InstitutionOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持事业单位法人证书关键字段识别，包括注册号、有效期、住所、名称、法定代表人等。"
  },
  "EnglishOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持图像英文文字的检测和识别，返回文字框位置与文字内容。支持多场景、任意版面下的英文、字母、数字和常见字符的识别，同时覆盖英文印刷体和英文手写体识别。"
  },
  "VehicleRegCertOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持国内机动车登记证书主要字段的结构化识别，包括机动车所有人、身份证明名称、号码、车辆型号、车辆识别代号、发动机号、制造厂名称等。"
  },
  "BankCardOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 7M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 7M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持对中国大陆主流银行卡的卡号、银行信息、有效期等关键字段的检测与识别。"
  },
  "CarInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持机动车销售统一发票和二手车销售统一发票的识别，包括发票号码、发票代码、合计金额、合计税额等二十多个字段。"
  },
  "DutyPaidProofOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持对完税证明的税号、纳税人识别号、纳税人名称、金额合计大写、金额合计小写、填发日期、税务机关、填票人等关键字段的识别。"
  },
  "MainlandPermitOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "RetProfile",
        "desc": "是非返回头像。默认不返回。"
      }
    ],
    "desc": "智能识别并结构化港澳台居民来往内地通行证正面全部字段，包含中文姓名、英文姓名、性别、出生日期、签发机关、有效期限、证件号、签发地点、签发次数、证件类别。"
  },
  "FormulaOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持识别主流初高中数学符号和公式，返回公式的 Latex 格式文本。"
  },
  "LicensePlateOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持对中国大陆机动车车牌的自动定位和识别，返回地域编号和车牌号信息。"
  },
  "ShipInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "本接口支持识别轮船票的发票代码、发票号码、日期、姓名、票价等字段。"
  },
  "MixedInvoiceOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "Types",
        "desc": "需要识别的票据类型列表，为空或不填表示识别全部类型。\n0：出租车发票\n1：定额发票\n2：火车票\n3：增值税发票\n5：机票行程单\n8：通用机打发票\n9：汽车票\n10：轮船票\n11：增值税发票（卷票 ）\n12：购车发票\n13：过路过桥费发票"
      }
    ],
    "desc": "本接口支持多张、多类型票据的混合识别，系统自动实现分割、分类和识别，同时支持自选需要识别的票据类型。目前已支持增值税发票、增值税发票（卷票）、定额发票、通用机打发票、购车发票、火车票、出租车发票、机票行程单、汽车票、轮船票、过路过桥费发票共11种票据。"
  },
  "DriverLicenseOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。\n建议图片存储于腾讯云，可保障更高的下载速度和稳定性。"
      },
      {
        "name": "CardSide",
        "desc": "FRONT 为驾驶证主页正面（有红色印章的一面），\nBACK 为驾驶证副页正面（有档案编号的一面）。"
      }
    ],
    "desc": "本接口支持驾驶证主页和副页所有字段的自动定位与识别，重点字段的识别准确度达到99%以上。\n\n驾驶证主页：包括证号、姓名、性别、国籍、住址、出生日期、初次领证日期、准驾车型、有效期限。\n\n驾驶证副页：包括证号、姓名、档案编号、记录。\n\n另外，本接口还支持复印件、翻拍和PS告警功能。"
  },
  "EduPaperOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经Base64编码后不超过 3M。图片下载时间不超过 3 秒。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。\n支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。\n支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。\n图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的 Url 速度和稳定性可能受一定影响。"
      },
      {
        "name": "Config",
        "desc": "扩展配置信息。\n配置格式：{\"option1\":value1,\"option2\":value2}\n可配置信息：\n      参数名称  是否必选   类型   可选值  默认值  描述\n      task_type  否  Int32  [0,1]  1  用于选择任务类型: 0: 关闭版式分析与处理 1: 开启版式分析处理\n      is_structuralization 否 Bool false\\true true  用于选择是否结构化输出：false：返回包体返回通用输出 true：返回包体同时返回通用和结构化输出\n      if_readable_format 否 Bool false\\true false 是否按照版式整合通用文本/公式输出结果\n例子：\n{\"task_type\": 1,\"is_structuralization\": true,\"if_readable_format\": true}"
      }
    ],
    "desc": "本接口支持数学试题内容的识别和结构化输出，包括通用文本解析和小学/初中/高中数学公式解析能力（包括91种题型，180种符号）。"
  },
  "VehicleLicenseOCR": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的 Base64 值。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。\n图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 Url 地址。要求图片经Base64编码后不超过 7M，分辨率建议500*800以上，支持PNG、JPG、JPEG、BMP格式。建议卡片部分占据图片2/3以上。图片下载时间不超过 3 秒。\n建议图片存储于腾讯云，可保障更高的下载速度和稳定性。"
      },
      {
        "name": "CardSide",
        "desc": "FRONT 为行驶证主页正面（有红色印章的一面），\nBACK 为行驶证副页正面（有号码号牌的一面）。"
      }
    ],
    "desc": "本接口支持行驶证主页和副页所有字段的自动定位与识别。\n\n行驶证主页：车牌号码、车辆类型、所有人、住址、使用性质、品牌型号、识别代码、发动机号、注册日期、发证日期、发证单位。\n\n行驶证副页：号牌号码、档案编号、核定载人数、总质量、整备质量、核定载质量、外廓尺寸、准牵引总质量、备注、检验记录。\n\n另外，本接口还支持复印件、翻拍和PS告警功能。"
  }
}