# -*- coding: utf-8 -*-
DESC = "iai-2018-03-01"
INFO = {
  "DeletePersonFromGroup": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员ID"
      },
      {
        "name": "GroupId",
        "desc": "人员库ID"
      }
    ],
    "desc": "从某人员库中删除人员，此操作仅影响该人员库。若该人员仅存在于指定的人员库中，该人员将被删除，其所有的人脸信息也将被删除。"
  },
  "SearchFacesReturnsByGroup": {
    "params": [
      {
        "name": "GroupIds",
        "desc": "希望搜索的人员库列表，上限60个。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。\nUrl、Image必须提供一个，如果都提供，只使用 Url。\n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的Url速度和稳定性可能受一定影响。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "MaxFaceNum",
        "desc": "最多识别的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为10。\nMaxFaceNum用于，当输入的待识别图片包含多张人脸时，设定要搜索的人脸的数量。\n例：输入的Image或Url中的图片包含多张人脸，设MaxFaceNum=5，则会识别图片中面积最大的5张人脸。"
      },
      {
        "name": "MinFaceSize",
        "desc": "人脸长和宽的最小尺寸，单位为像素。默认为34。低于34将影响搜索精度。建议设置为80。"
      },
      {
        "name": "MaxPersonNumPerGroup",
        "desc": "被检测到的人脸，对应最多返回的最相似人员数目。默认值为5，最大值为10。  \n例，设MaxFaceNum为3，MaxPersonNum为5，则最多可能返回3*5=15个人员。"
      },
      {
        "name": "NeedPersonInfo",
        "desc": "是否返回人员具体信息。0 为关闭，1 为开启。默认为 0。其他非0非1值默认为0"
      },
      {
        "name": "QualityControl",
        "desc": "图片质量控制。 \n0: 不进行控制； \n1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； \n2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； \n3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； \n4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； \n默认 0。 \n若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。"
      },
      {
        "name": "FaceMatchThreshold",
        "desc": "出参Score中，只有大于等于FaceMatchThreshold值的结果才会返回。\n默认为0。\n取值范围[0.0,100.0) 。"
      }
    ],
    "desc": "用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopK 人员，按照**人员库的维度**以人员相似度从大到小顺序排列。\n\n支持一次性识别图片中的最多 10 张人脸，支持跨人员库（Group）搜索。\n\n单次搜索的人员库人脸总数量和人员库的算法模型版本（FaceModelVersion）相关。算法模型版本为2.0的人员库，单次搜索人员库人脸总数量不得超过 100 万张；算法模型版本为3.0的人员库，单次搜索人员库人脸总数量不得超过 300 万张。\n\n与[人员搜索](https://cloud.tencent.com/document/product/867/38881)及[人员搜索按库返回](https://cloud.tencent.com/document/product/867/38880)接口不同的是，本接口将该人员（Person）下的每个人脸（Face）都作为单独个体进行验证，而[人员搜索](https://cloud.tencent.com/document/product/867/38881)及[人员搜索按库返回](https://cloud.tencent.com/document/product/867/38880)接口 会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个Person下有4张 Face，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使搜索更加准确。\n\n本接口需与[人员库管理相关接口](https://cloud.tencent.com/document/product/867/32794)结合使用。\n\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。\n\n"
  },
  "CreateGroup": {
    "params": [
      {
        "name": "GroupName",
        "desc": "人员库名称，[1,60]个字符，可修改，不可重复。"
      },
      {
        "name": "GroupId",
        "desc": "人员库 ID，不可修改，不可重复。支持英文、数字、-%@#&_，长度限制64B。"
      },
      {
        "name": "GroupExDescriptions",
        "desc": "人员库自定义描述字段，用于描述人员库中人员属性，该人员库下所有人员将拥有此描述字段。 \n最多可以创建5个。 \n每个自定义描述字段支持[1,30]个字符。 \n在同一人员库中自定义描述字段不可重复。 \n例： 设置某人员库“自定义描述字段”为[\"学号\",\"工号\",\"手机号\"]， \n则该人员库下所有人员将拥有名为“学号”、“工号”、“手机号”的描述字段， \n可在对应人员描述字段中填写内容，登记该人员的学号、工号、手机号等信息。"
      },
      {
        "name": "Tag",
        "desc": "人员库信息备注，[0，40]个字符。"
      },
      {
        "name": "FaceModelVersion",
        "desc": "人脸识别服务所用的算法模型版本。目前入参支持 “2.0”和“3.0“ 两个输入。\n2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。 \n不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。"
      }
    ],
    "desc": "用于创建一个空的人员库，如果人员库已存在返回错误。\n可根据需要创建自定义描述字段，用于辅助描述该人员库下的人员信息。\n\n1个APPID下最多创建10万个人员库（Group）、最多包含5000万张人脸（Face）。\n\n不同算法模型版本（FaceModelVersion）的人员库（Group）最多可包含人脸（Face）数不同。算法模型版本为2.0的人员库最多包含100万张人脸，算法模型版本为3.0的人员库最多可包含300万张人脸。"
  },
  "GetCheckSimilarPersonJobIdList": {
    "params": [
      {
        "name": "Offset",
        "desc": "起始序号，默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认值为10，最大值为1000。"
      }
    ],
    "desc": "获取人员查重任务列表，按任务创建时间逆序（最新的在前面）。\n\n只保留最近1年的数据。"
  },
  "GetPersonBaseInfo": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员ID"
      }
    ],
    "desc": "获取指定人员的信息，包括姓名、性别、人脸等。"
  },
  "DetectLiveFace": {
    "params": [
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M（图片的宽高比请接近3:4，不符合宽高比的图片返回的分值不具备参考意义）。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。\nUrl、Image必须提供一个，如果都提供，只使用 Url。 \n（图片的宽高比请接近 3:4，不符合宽高比的图片返回的分值不具备参考意义） \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "FaceModelVersion",
        "desc": "人脸识别服务所用的算法模型版本。目前入参支持 “2.0”和“3.0“ 两个输入。  \n2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。 \n不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。"
      }
    ],
    "desc": "用于对用户上传的静态图片进行人脸活体检测。与动态活体检测的区别是：静态活体检测中，用户不需要通过唇语或摇头眨眼等动作来识别。\n\n静态活体检测适用于手机自拍的场景，或对防攻击要求不高的场景。如果对活体检测有更高安全性要求，请使用[人脸核身·云智慧眼](https://cloud.tencent.com/product/faceid)产品。\n\n>     \n- 图片的宽高比请接近3：4，不符合宽高比的图片返回的分值不具备参考意义。本接口适用于类手机自拍场景，非类手机自拍照返回的分值不具备参考意义。\n\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "CreateFace": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员ID。"
      },
      {
        "name": "Images",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。\n人员人脸总数量不可超过5张。\n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Urls",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。\nUrl、Image必须提供一个，如果都提供，只使用 Url。  \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n人员人脸总数量不可超过5张。\n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。"
      },
      {
        "name": "FaceMatchThreshold",
        "desc": "只有和该人员已有的人脸相似度超过FaceMatchThreshold值的人脸，才能增加人脸成功。 \n默认值60分。取值范围[0,100] 。"
      },
      {
        "name": "QualityControl",
        "desc": "图片质量控制。 \n0: 不进行控制； \n1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； \n2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； \n3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； \n4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； \n默认 0。 \n若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。"
      }
    ],
    "desc": "将一组人脸图片添加到一个人员中。一个人员最多允许包含 5 张图片。若该人员存在多个人员库中，所有人员库中该人员图片均会增加。\n\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "GetPersonListNum": {
    "params": [
      {
        "name": "GroupId",
        "desc": "人员库ID"
      }
    ],
    "desc": "获取指定人员库中人员数量。"
  },
  "GetPersonGroupInfo": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员ID"
      },
      {
        "name": "Offset",
        "desc": "起始序号，默认值为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认值为10，最大值为100"
      }
    ],
    "desc": "获取指定人员的信息，包括加入的人员库、描述内容等。"
  },
  "AnalyzeFace": {
    "params": [
      {
        "name": "Mode",
        "desc": "检测模式。0 为检测所有出现的人脸， 1 为检测面积最大的人脸。默认为 0。最多返回 10 张人脸的五官定位（人脸关键点）具体信息。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。\nUrl、Image必须提供一个，如果都提供，只使用 Url。  \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "FaceModelVersion",
        "desc": "人脸识别服务所用的算法模型版本。目前入参支持 “2.0”和“3.0“ 两个输入。  \n2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。  \n不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用最新版本。"
      }
    ],
    "desc": "对请求图片进行五官定位（也称人脸关键点定位），计算构成人脸轮廓的 90 个点，包括眉毛（左右各 8 点）、眼睛（左右各 8 点）、鼻子（13 点）、嘴巴（22 点）、脸型轮廓（21 点）、眼珠[或瞳孔]（2点）。\n\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "ModifyPersonBaseInfo": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员ID"
      },
      {
        "name": "PersonName",
        "desc": "需要修改的人员名称"
      },
      {
        "name": "Gender",
        "desc": "需要修改的人员性别"
      }
    ],
    "desc": "修改人员信息，包括名称、性别等。人员名称和性别修改会同步到包含该人员的所有人员库。"
  },
  "SearchFaces": {
    "params": [
      {
        "name": "GroupIds",
        "desc": "希望搜索的人员库列表，上限100个。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。\nUrl、Image必须提供一个，如果都提供，只使用 Url。  \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "MaxFaceNum",
        "desc": "最多识别的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为10。 \nMaxFaceNum用于，当输入的待识别图片包含多张人脸时，设定要搜索的人脸的数量。 \n例：输入的Image或Url中的图片包含多张人脸，设MaxFaceNum=5，则会识别图片中面积最大的5张人脸。"
      },
      {
        "name": "MinFaceSize",
        "desc": "人脸长和宽的最小尺寸，单位为像素。默认为34。低于34的人脸图片无法被识别。建议设置为80。"
      },
      {
        "name": "MaxPersonNum",
        "desc": "单张被识别的人脸返回的最相似人员数量。默认值为5，最大值为100。 \n例，设MaxFaceNum为1，MaxPersonNum为8，则返回Top8相似的人员信息。\n值越大，需要处理的时间越长。建议不要超过10。"
      },
      {
        "name": "NeedPersonInfo",
        "desc": "是否返回人员具体信息。0 为关闭，1 为开启。默认为 0。其他非0非1值默认为0"
      },
      {
        "name": "QualityControl",
        "desc": "图片质量控制。 \n0: 不进行控制； \n1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； \n2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； \n3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； \n4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； \n默认 0。 \n若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。"
      },
      {
        "name": "FaceMatchThreshold",
        "desc": "出参Score中，只有超过FaceMatchThreshold值的结果才会返回。默认为0。"
      }
    ],
    "desc": "用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopK 人员，识别结果按照相似度从大到小排序。\n\n支持一次性识别图片中的最多 10 张人脸，支持一次性跨 100 个人员库（Group）搜索。\n\n单次搜索的人员库人脸总数量和人员库的算法模型版本（FaceModelVersion）相关。算法模型版本为2.0的人员库，单次搜索人员库人脸总数量不得超过 100 万张；算法模型版本为3.0的人员库，单次搜索人员库人脸总数量不得超过 300 万张。\n\n与[人员搜索](https://cloud.tencent.com/document/product/867/38881)及[人员搜索按库返回](https://cloud.tencent.com/document/product/867/38880)接口不同的是，本接口将该人员（Person）下的每个人脸（Face）都作为单独个体进行验证，而人员搜索及人员搜索按库返回接口 会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个Person下有4张 Face，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使搜索更加准确。\n\n\n本接口需与[人员库管理相关接口](https://cloud.tencent.com/document/product/867/32794)结合使用。\n\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "CopyPerson": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员ID"
      },
      {
        "name": "GroupIds",
        "desc": "待加入的人员库列表"
      }
    ],
    "desc": "将已存在于某人员库的人员复制到其他人员库，该人员的描述信息不会被复制。单个人员最多只能同时存在100个人员库中。\n>     \n- 注：若该人员创建时算法模型版本为2.0，复制到非2.0算法模型版本的Group中时，复制操作将会失败。"
  },
  "CheckSimilarPerson": {
    "params": [
      {
        "name": "GroupIds",
        "desc": "待整理的人员库列表。 \n人员库总人数不可超过200万，人员库个数不可超过10个。"
      },
      {
        "name": "UniquePersonControl",
        "desc": "疑似同一人判断控制。  \n1：宽松的同一人要求； \n2：严格的同一人要求。  \n注： 要求越高，则疑似同一人的概率越小。"
      }
    ],
    "desc": "对指定的人员库进行人员查重，给出疑似相同人的信息。\n\n可以使用本接口对已有的单个人员库进行人员查重，避免同一人在单个人员库中拥有多个身份；也可以使用本接口对已有的多个人员库进行人员查重，查询同一人是否同时存在多个人员库中。\n\n不支持跨算法模型版本查重，且目前仅支持算法模型为3.0的人员库使用查重功能。\n\n>     \n- 若对完全相同的指定人员库进行查重操作，需等待上次操作完成才可。即，若两次请求输入的 GroupIds 相同，第一次请求若未完成，第二次请求将返回失败。\n\n>     \n- 查重的人员库状态为腾讯云开始进行查重任务的那一刻，即您可以理解为当您发起查重请求后，若您的查重任务需要排队，在排队期间您对人员库的增删操作均会会影响查重的结果。腾讯云将以开始进行查重任务的那一刻人员库的状态进行查重。查重任务开始后，您对人员库的任何操作均不影响查重任务的进行。但建议查重任务开始后，请不要对人员库中人员和人脸进行增删操作。"
  },
  "DeleteGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "人员库ID。"
      }
    ],
    "desc": "删除该人员库及包含的所有的人员。同时，人员对应的所有人脸信息将被删除。若某人员同时存在多个人员库中，该人员不会被删除，但属于该人员库中的自定义描述字段信息会被删除，属于其他人员库的自定义描述字段信息不受影响。\n"
  },
  "DeletePerson": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员ID"
      }
    ],
    "desc": "删除该人员信息，此操作会导致所有人员库均删除此人员。同时，该人员的所有人脸信息将被删除。"
  },
  "ModifyGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "人员库ID"
      },
      {
        "name": "GroupName",
        "desc": "人员库名称"
      },
      {
        "name": "GroupExDescriptionInfos",
        "desc": "需要修改的人员库自定义描述字段，key-value"
      },
      {
        "name": "Tag",
        "desc": "人员库信息备注"
      }
    ],
    "desc": "修改人员库名称、备注、自定义描述字段名称。"
  },
  "GetSimilarPersonResult": {
    "params": [
      {
        "name": "JobId",
        "desc": "查重任务ID，用于查询、获取查重的进度和结果。"
      }
    ],
    "desc": "获取人员查重接口（CheckSimilarPerson）结果。"
  },
  "CreatePerson": {
    "params": [
      {
        "name": "GroupId",
        "desc": "待加入的人员库ID。"
      },
      {
        "name": "PersonName",
        "desc": "人员名称。[1，60]个字符，可修改，可重复。"
      },
      {
        "name": "PersonId",
        "desc": "人员ID，单个腾讯云账号下不可修改，不可重复。支持英文、数字、-%@#&_，长度限制64B。"
      },
      {
        "name": "Gender",
        "desc": "0代表未填写，1代表男性，2代表女性。"
      },
      {
        "name": "PersonExDescriptionInfos",
        "desc": "人员描述字段内容，key-value。[0，60]个字符，可修改，可重复。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。\nUrl、Image必须提供一个，如果都提供，只使用 Url。  \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "UniquePersonControl",
        "desc": "此参数用于控制判断 Image 或 Url 中图片包含的人脸，是否在人员库中已有疑似的同一人。 \n如果判断为已有相同人在人员库中，则不会创建新的人员，返回疑似同一人的人员信息。 \n如果判断没有，则完成创建人员。 \n0: 不进行判断，无论是否有疑似同一人在库中均完成入库； \n1:较低的同一人判断要求（百一误识别率）； \n2: 一般的同一人判断要求（千一误识别率）； \n3: 较高的同一人判断要求（万一误识别率）； \n4: 很高的同一人判断要求（十万一误识别率）。 \n默认 0。  \n注： 要求越高，则疑似同一人的概率越小。不同要求对应的误识别率仅为参考值，您可以根据实际情况调整。"
      },
      {
        "name": "QualityControl",
        "desc": "图片质量控制。 \n0: 不进行控制； \n1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； \n2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； \n3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； \n4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； \n默认 0。 \n若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。"
      }
    ],
    "desc": "创建人员，添加人脸、姓名、性别及其他相关信息。\n\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "GetGroupInfo": {
    "params": [
      {
        "name": "GroupId",
        "desc": "人员库 ID。"
      }
    ],
    "desc": "获取人员库信息。"
  },
  "DetectFace": {
    "params": [
      {
        "name": "MaxFaceNum",
        "desc": "最多处理的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为120。 \n此参数用于控制处理待检测图片中的人脸个数，值越小，处理速度越快。"
      },
      {
        "name": "MinFaceSize",
        "desc": "人脸长和宽的最小尺寸，单位为像素。\n默认为34。建议不低于34。\n低于MinFaceSize值的人脸不会被检测。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。\nUrl、Image必须提供一个，如果都提供，只使用 Url。  \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "NeedFaceAttributes",
        "desc": "是否需要返回人脸属性信息（FaceAttributesInfo）。0 为不需要返回，1 为需要返回。默认为 0。 \n非 1 值均视为不需要返回，此时 FaceAttributesInfo 不具备参考意义。  \n最多返回面积最大的 5 张人脸属性信息，超过 5 张人脸（第 6 张及以后的人脸）的 FaceAttributesInfo 不具备参考意义。  \n提取人脸属性信息较为耗时，如不需要人脸属性信息，建议关闭此项功能，加快人脸检测速度。"
      },
      {
        "name": "NeedQualityDetection",
        "desc": "是否开启质量检测。0 为关闭，1 为开启。默认为 0。 \n非 1 值均视为不进行质量检测。\n最多返回面积最大的 30 张人脸质量分信息，超过 30 张人脸（第 31 张及以后的人脸）的 FaceQualityInfo不具备参考意义。  \n建议：人脸入库操作建议开启此功能。"
      },
      {
        "name": "FaceModelVersion",
        "desc": "人脸识别服务所用的算法模型版本。目前入参支持 “2.0”和“3.0“ 两个输入。  \n2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。 \n不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。"
      }
    ],
    "desc": "检测给定图片中的人脸（Face）的位置、相应的面部属性和人脸质量信息，位置包括 (x，y，w，h)，面部属性包括性别（gender）、年龄（age）、表情（expression）、魅力（beauty）、眼镜（glass）、发型（hair）、口罩（mask）和姿态 (pitch，roll，yaw)，人脸质量信息包括整体质量分（score）、模糊分（sharpness）、光照分（brightness）和五官遮挡分（completeness）。\n\n \n其中，人脸质量信息主要用于评价输入的人脸图片的质量。在使用人脸识别服务时，建议您对输入的人脸图片进行质量检测，提升后续业务处理的效果。该功能的应用场景包括：\n\n1） 人员库[创建人员](https://cloud.tencent.com/document/product/867/32793)/[增加人脸](https://cloud.tencent.com/document/product/867/32795)：保证人员人脸信息的质量，便于后续的业务处理。\n\n2） [人脸搜索](https://cloud.tencent.com/document/product/867/32798)：保证输入的图片质量，快速准确匹配到对应的人员。\n\n3） [人脸验证](https://cloud.tencent.com/document/product/867/32806)：保证人脸信息的质量，避免明明是本人却认证不通过的情况。\n\n4） [人脸融合](https://cloud.tencent.com/product/facefusion)：保证上传的人脸质量，人脸融合的效果更好。\n\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。\n\n"
  },
  "GetPersonList": {
    "params": [
      {
        "name": "GroupId",
        "desc": "人员库ID"
      },
      {
        "name": "Offset",
        "desc": "起始序号，默认值为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认值为10，最大值为1000"
      }
    ],
    "desc": "获取指定人员库中的人员列表。"
  },
  "VerifyPerson": {
    "params": [
      {
        "name": "Image",
        "desc": "图片 base64 数据。\n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。 图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。\n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "PersonId",
        "desc": "待验证的人员ID。人员ID具体信息请参考人员库管理相关接口。"
      },
      {
        "name": "QualityControl",
        "desc": "图片质量控制。 \n0: 不进行控制； \n1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； \n2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； \n3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； \n4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； \n默认 0。 \n若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。"
      }
    ],
    "desc": "给定一张人脸图片和一个 PersonId，判断图片中的人和 PersonId 对应的人是否为同一人。PersonId 请参考[人员库管理相关接口](https://cloud.tencent.com/document/product/867/32794)。\n本接口会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个Person下有4张 Face，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员验证（确定待识别的人脸图片是某人员）更加准确。\n\n 和人脸比对相关接口不同的是，人脸验证相关接口用于判断 “此人是否是此人”，“此人”的信息已存于人员库中，“此人”可能存在多张人脸图片；而人脸比对相关接口用于判断两张人脸的相似度。\n\n\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。\n- 仅支持算法模型版本（FaceModelVersion）为3.0的人员库。"
  },
  "ModifyPersonGroupInfo": {
    "params": [
      {
        "name": "GroupId",
        "desc": "人员库ID"
      },
      {
        "name": "PersonId",
        "desc": "人员ID"
      },
      {
        "name": "PersonExDescriptionInfos",
        "desc": "需要修改的人员描述字段内容，key-value"
      }
    ],
    "desc": "修改指定人员库人员描述内容。"
  },
  "VerifyFace": {
    "params": [
      {
        "name": "PersonId",
        "desc": "待验证的人员ID。人员ID具体信息请参考人员库管理相关接口。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。\n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。\nUrl、Image必须提供一个，如果都提供，只使用 Url。  \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。\n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "QualityControl",
        "desc": "图片质量控制。 \n0: 不进行控制； \n1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； \n2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； \n3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； \n4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； \n默认 0。 \n若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。"
      }
    ],
    "desc": "给定一张人脸图片和一个 PersonId，判断图片中的人和 PersonId 对应的人是否为同一人。PersonId 请参考[人员库管理相关接口](https://cloud.tencent.com/document/product/867/32794)。 \n\n与[人脸比对](https://cloud.tencent.com/document/product/867/32802)接口不同的是，人脸验证用于判断 “此人是否是此人”，“此人”的信息已存于人员库中，“此人”可能存在多张人脸图片；而[人脸比对](https://cloud.tencent.com/document/product/867/32802)用于判断两张人脸的相似度。\n\n与[人员验证](https://cloud.tencent.com/document/product/867/38879)接口不同的是，人脸验证将该人员（Person）下的每个人脸（Face）都作为单独个体进行验证，而[人员验证](https://cloud.tencent.com/document/product/867/38879)会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个 Person下有4张 Face，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员验证（确定待识别的人脸图片是某人员）更加准确。\n\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "SearchPersons": {
    "params": [
      {
        "name": "GroupIds",
        "desc": "希望搜索的人员库列表，上限100个。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。\n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。\nUrl、Image必须提供一个，如果都提供，只使用 Url。\n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的Url速度和稳定性可能受一定影响。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "MaxFaceNum",
        "desc": "最多识别的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为10。\nMaxFaceNum用于，当输入的待识别图片包含多张人脸时，设定要搜索的人脸的数量。\n例：输入的Image或Url中的图片包含多张人脸，设MaxFaceNum=5，则会识别图片中面积最大的5张人脸。"
      },
      {
        "name": "MinFaceSize",
        "desc": "人脸长和宽的最小尺寸，单位为像素。默认为34。低于34将影响搜索精度。建议设置为80。"
      },
      {
        "name": "MaxPersonNum",
        "desc": "单张被识别的人脸返回的最相似人员数量。默认值为5，最大值为100。\n例，设MaxFaceNum为1，MaxPersonNum为8，则返回Top8相似的人员信息。\n值越大，需要处理的时间越长。建议不要超过10。"
      },
      {
        "name": "QualityControl",
        "desc": "图片质量控制。 \n0: 不进行控制； \n1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； \n2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； \n3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； \n4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； \n默认 0。 \n若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。"
      },
      {
        "name": "FaceMatchThreshold",
        "desc": "出参Score中，只有大于等于FaceMatchThreshold值的结果才会返回。默认为0。取值范围[0.0,100.0) 。"
      },
      {
        "name": "NeedPersonInfo",
        "desc": "是否返回人员具体信息。0 为关闭，1 为开启。默认为 0。其他非0非1值默认为0"
      }
    ],
    "desc": "用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopK 人员，按照相似度从大到小排列。\n\n支持一次性识别图片中的最多 10 张人脸，支持一次性跨 100 个人员库（Group）搜索。\n\n单次搜索的人员库人脸总数量和人员库的算法模型版本（FaceModelVersion）相关。算法模型版本为2.0的人员库，单次搜索人员库人脸总数量不得超过 100 万张；算法模型版本为3.0的人员库，单次搜索人员库人脸总数量不得超过 300 万张。\n\n本接口会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个 Person 下有4张 Face ，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员搜索（确定待识别的人脸图片是某人）更加准确。而[人脸搜索](https://cloud.tencent.com/document/product/867/32798)及[人脸搜索按库返回接口](https://cloud.tencent.com/document/product/867/38882)将该人员（Person）下的每个人脸（Face）都作为单独个体进行搜索。\n\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。\n- 仅支持算法模型版本（FaceModelVersion）为3.0的人员库。"
  },
  "CompareFace": {
    "params": [
      {
        "name": "ImageA",
        "desc": "A 图片 base64 数据，base64 编码后大小不可超过5M。\n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "ImageB",
        "desc": "B 图片 base64 数据，base64 编码后大小不可超过5M。\n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "UrlA",
        "desc": "A 图片的 Url ，对应图片 base64 编码后大小不可超过5M。\nA 图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。\n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "UrlB",
        "desc": "B 图片的 Url ，对应图片 base64 编码后大小不可超过5M。\nB 图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。\n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "FaceModelVersion",
        "desc": "人脸识别服务所用的算法模型版本。目前入参支持 “2.0”和“3.0“ 两个输入。 \n2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。 \n不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。"
      },
      {
        "name": "QualityControl",
        "desc": "图片质量控制。 \n0: 不进行控制； \n1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； \n2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； \n3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； \n4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； \n默认 0。 \n若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。"
      }
    ],
    "desc": "对两张图片中的人脸进行相似度比对，返回人脸相似度分数。\n\n若您需要判断 “此人是否是某人”，即验证某张图片中的人是否是已知身份的某人，如常见的人脸登录场景，建议使用[人脸验证](https://cloud.tencent.com/document/product/867/32806)或[人员验证](https://cloud.tencent.com/document/product/867/38879)接口。\n\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "SearchPersonsReturnsByGroup": {
    "params": [
      {
        "name": "GroupIds",
        "desc": "希望搜索的人员库列表，上限60个。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。\nUrl、Image必须提供一个，如果都提供，只使用 Url。\n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的Url速度和稳定性可能受一定影响。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "MaxFaceNum",
        "desc": "最多识别的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为10。\nMaxFaceNum用于，当输入的待识别图片包含多张人脸时，设定要搜索的人脸的数量。\n例：输入的Image或Url中的图片包含多张人脸，设MaxFaceNum=5，则会识别图片中面积最大的5张人脸。"
      },
      {
        "name": "MinFaceSize",
        "desc": "人脸长和宽的最小尺寸，单位为像素。默认为34。低于34将影响搜索精度。建议设置为80。"
      },
      {
        "name": "MaxPersonNumPerGroup",
        "desc": "被检测到的人脸，对应最多返回的最相似人员数目。默认值为5，最大值为10。  \n例，设MaxFaceNum为3，MaxPersonNumPerGroup为5，GroupIds长度为3，则最多可能返回3*5*3=45个人员。"
      },
      {
        "name": "QualityControl",
        "desc": "图片质量控制。 \n0: 不进行控制； \n1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； \n2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； \n3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； \n4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； \n默认 0。 \n若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。"
      },
      {
        "name": "FaceMatchThreshold",
        "desc": "出参Score中，只有超过FaceMatchThreshold值的结果才会返回。默认为0。"
      },
      {
        "name": "NeedPersonInfo",
        "desc": "是否返回人员具体信息。0 为关闭，1 为开启。默认为 0。其他非0非1值默认为0"
      }
    ],
    "desc": "用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopK 人员，按照**人员库的维度**以人员相似度从大到小顺序排列。\n\n支持一次性识别图片中的最多 10 张人脸，支持跨人员库（Group）搜索。\n\n单次搜索的人员库人脸总数量和人员库的算法模型版本（FaceModelVersion）相关。算法模型版本为2.0的人员库，单次搜索人员库人脸总数量不得超过 100 万张；算法模型版本为3.0的人员库，单次搜索人员库人脸总数量不得超过 300 万张。\n\n本接口会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个 Person 下有4张 Face ，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员搜索（确定待识别的人脸图片是某人）更加准确。而[人脸搜索](https://cloud.tencent.com/document/product/867/32798)及[人脸搜索按库返回接口](https://cloud.tencent.com/document/product/867/38882)将该人员（Person）下的每个人脸（Face）都作为单独个体进行搜索。\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。\n- 仅支持算法模型版本（FaceModelVersion）为3.0的人员库。"
  },
  "GetGroupList": {
    "params": [
      {
        "name": "Offset",
        "desc": "起始序号，默认值为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认值为10，最大值为1000"
      }
    ],
    "desc": "获取人员库列表。"
  },
  "EstimateCheckSimilarPersonCostTime": {
    "params": [
      {
        "name": "GroupIds",
        "desc": "待整理的人员库列表。 \n人员库总人数不可超过200万，人员库个数不可超过10个。"
      }
    ],
    "desc": "获取若要开始一个人员查重任务，这个任务结束的预估时间。\n\n若EndTimestamp符合您预期，请您尽快发起人员查重请求，否则导致可能需要更多处理时间。\n\n若预估时间超过5小时，则无法使用人员查重功能。"
  },
  "DeleteFace": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员ID"
      },
      {
        "name": "FaceIds",
        "desc": "待删除的人脸ID列表"
      }
    ],
    "desc": "删除一个人员下的人脸图片。如果该人员只有一张人脸图片，则返回错误。"
  }
}