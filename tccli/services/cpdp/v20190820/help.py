# -*- coding: utf-8 -*-
DESC = "cpdp-2019-08-20"
INFO = {
  "BindAcct": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "BindType",
        "desc": "1 – 小额转账验证\n2 – 短信验证\n每个结算账户每天只能使用一次小额转账验证"
      },
      {
        "name": "SettleAcctNo",
        "desc": "用于提现\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "SettleAcctName",
        "desc": "结算账户户名\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "SettleAcctType",
        "desc": "1 – 本行账户\n2 – 他行账户"
      },
      {
        "name": "IdType",
        "desc": "证件类型，见《证件类型》表"
      },
      {
        "name": "IdCode",
        "desc": "证件号码\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "AcctBranchName",
        "desc": "开户行名称"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "Mobile",
        "desc": "用于短信验证\nBindType==2时必填\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "CnapsBranchId",
        "desc": "超级网银行号和大小额行号\n二选一"
      },
      {
        "name": "EiconBankBranchId",
        "desc": "超级网银行号和大小额行号\n二选一"
      }
    ],
    "desc": "商户绑定提现银行卡，每个商户只能绑定一张提现银行卡"
  },
  "BindRelateAcctSmallAmount": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）"
      },
      {
        "name": "MemberName",
        "desc": "STRING(150)，见证子账户的户名（首次绑定的情况下，此字段即为待绑定的提现账户的户名。非首次绑定的情况下，须注意带绑定的提现账户的户名须与留存在后台系统的会员户名一致）"
      },
      {
        "name": "MemberGlobalType",
        "desc": "STRING(5)，会员证件类型（详情见“常见问题”）"
      },
      {
        "name": "MemberGlobalId",
        "desc": "STRING(32)，会员证件号码"
      },
      {
        "name": "MemberAcctNo",
        "desc": "STRING(50)，会员的待绑定账户的账号（提现的银行卡）"
      },
      {
        "name": "BankType",
        "desc": "STRING(10)，会员的待绑定账户的本他行类型（1: 本行; 2: 他行）"
      },
      {
        "name": "AcctOpenBranchName",
        "desc": "STRING(150)，会员的待绑定账户的开户行名称"
      },
      {
        "name": "Mobile",
        "desc": "STRING(30)，会员的手机号（手机号须由长度为11位的数字构成）"
      },
      {
        "name": "CnapsBranchId",
        "desc": "STRING(20)，会员的待绑定账户的开户行的联行号（本他行类型为他行的情况下，此字段和下一个字段至少一个不为空）"
      },
      {
        "name": "EiconBankBranchId",
        "desc": "STRING(20)，会员的待绑定账户的开户行的超级网银行号（本他行类型为他行的情况下，此字段和上一个字段至少一个不为空）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，转账方式（1: 往账鉴权(默认值); 2: 来账鉴权）"
      }
    ],
    "desc": "会员绑定提现账户-小额鉴权。会员申请绑定提现账户，绑定后从会员子账户中提现到绑定账户。\n转账鉴权有两种形式：往账鉴权和来账鉴权。\n往账鉴权：该接口发起成功后，银行会向提现账户转入小于等于0.5元的随机金额，并短信通知客户查看，客户查看后，需将收到的金额大小，在电商平台页面上回填，并通知银行。银行验证通过后，完成提现账户绑定。\n来账鉴权：该接口发起成功后，银行以短信通知客户查看，客户查看后，需通过待绑定的账户往市场的监管账户转入短信上指定的金额。银行检索到该笔指定金额的来账是源自待绑定账户，则绑定成功。平安银行的账户，即BankType送1时，大小额行号和超级网银号都不用送。"
  },
  "ApplyWithdrawal": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "SettleAcctNo",
        "desc": "用于提现\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "SettleAcctName",
        "desc": "结算账户户名\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "CurrencyType",
        "desc": "币种 RMB"
      },
      {
        "name": "CurrencyUnit",
        "desc": "单位，1：元，2：角，3：分"
      },
      {
        "name": "CurrencyAmt",
        "desc": "金额"
      },
      {
        "name": "TranWebName",
        "desc": "交易网名称"
      },
      {
        "name": "IdType",
        "desc": "会员证件类型"
      },
      {
        "name": "IdCode",
        "desc": "会员证件号码\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      }
    ],
    "desc": "商户提现"
  },
  "ModifyMntMbrBindRelateAcctBankCode": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子账户的账号"
      },
      {
        "name": "MemberBindAcctNo",
        "desc": "STRING(50)，会员绑定账号"
      },
      {
        "name": "AcctOpenBranchName",
        "desc": "STRING(150)，开户行名称（若大小额行号不填则送超级网银号对应的银行名称，若填大小额行号则送大小额行号对应的银行名称）"
      },
      {
        "name": "CnapsBranchId",
        "desc": "STRING(20)，大小额行号（CnapsBranchId和EiconBankBranchId两者二选一必填）"
      },
      {
        "name": "EiconBankBranchId",
        "desc": "STRING(20)，超级网银行号"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "维护会员绑定提现账户联行号。此接口可以支持市场修改会员的提现账户的开户行信息，具体包括开户行行名、开户行的银行联行号（大小额联行号）和超级网银行号。"
  },
  "QueryMemberBind": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "QueryFlag",
        "desc": "STRING(4)，查询标志（1: 全部会员; 2: 单个会员; 3: 单个会员的证件信息）"
      },
      {
        "name": "PageNum",
        "desc": "STRING (10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子账户的账号（若SelectFlag为2或3时，子账户账号必输）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "会员绑定信息查询。查询标志为“单个会员”的情况下，返回该会员的有效的绑定账户信息。\n查询标志为“全部会员”的情况下，返回市场下的全部的有效的绑定账户信息。查询标志为“单个会员的证件信息”的情况下，返回市场下的指定的会员的留存在电商见证宝系统的证件信息。"
  },
  "ReviseMbrProperty": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子账户的账号"
      },
      {
        "name": "MemberProperty",
        "desc": "STRING(10)，会员属性（00-普通子账号; SH-商户子账户。暂时只支持00-普通子账号改为SH-商户子账户）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "修改会员属性-普通商户子账户。修改会员的会员属性。"
  },
  "QueryOrder": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主 MidasAppId"
      },
      {
        "name": "UserId",
        "desc": "用户ID，长度不小于5位， 仅支持字母和数字的组合"
      },
      {
        "name": "Type",
        "desc": "type=by_order根据订单号 查订单；\ntype=by_user根据用户id 查订单 。"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "Count",
        "desc": "每页返回的记录数。根据用户 号码查询订单列表时需要传。 用于分页展示。Type=by_order时必填"
      },
      {
        "name": "Offset",
        "desc": "记录数偏移量，默认从0开 始。根据用户号码查询订单列 表时需要传。用于分页展示。Type=by_order时必填"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间，Unix时间戳。Type=by_order时必填"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间，Unix时间戳。Type=by_order时必填"
      },
      {
        "name": "OutTradeNo",
        "desc": "业务订单号，OutTradeNo与 TransactionId不能同时为 空，都传优先使用 OutTradeNo"
      },
      {
        "name": "TransactionId",
        "desc": "聚鑫订单号，OutTradeNo与 TransactionId不能同时为 空，都传优先使用 OutTradeNo"
      }
    ],
    "desc": "根据订单号，或者用户Id，查询支付订单状态 "
  },
  "QueryMerchantInfoForManagement": {
    "params": [
      {
        "name": "InvoicePlatformId",
        "desc": "开票平台ID"
      },
      {
        "name": "Offset",
        "desc": "页码"
      },
      {
        "name": "Limit",
        "desc": "页大小"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox。"
      }
    ],
    "desc": "智慧零售-查询管理端商户"
  },
  "CreateCustAcctId": {
    "params": [
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1: 开户; 3: 销户）"
      },
      {
        "name": "FundSummaryAcctNo",
        "desc": "STRING(50)，资金汇总账号（即收单资金归集入账的账号）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码（平台端的用户ID，需要保证唯一性，可数字字母混合，如HY_120）"
      },
      {
        "name": "MemberProperty",
        "desc": "STRING(10)，会员属性（00-普通子账户(默认); SH-商户子账户）"
      },
      {
        "name": "Mobile",
        "desc": "STRING(30)，手机号码"
      },
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "SelfBusiness",
        "desc": "String(2)，是否为自营业务（0位非自营，1为自营）"
      },
      {
        "name": "ContactName",
        "desc": "String(64)，联系人"
      },
      {
        "name": "SubAcctName",
        "desc": "String(64)，子账户名称"
      },
      {
        "name": "SubAcctShortName",
        "desc": "String(64)，子账户简称"
      },
      {
        "name": "SubAcctType",
        "desc": "String(4)，子账户类型（0: 个人子账户; 1: 企业子账户）"
      },
      {
        "name": "UserNickname",
        "desc": "STRING(150)，用户昵称"
      },
      {
        "name": "Email",
        "desc": "STRING(150)，邮箱"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "会员子账户开立。会员在银行注册，并开立会员子账户，交易网会员代码即会员在平台端系统的会员编号。\n平台需保存银行返回的子账户账号，后续交易接口都会用到。会员属性字段为预留扩展字段，当前必须送默认值。"
  },
  "QueryBalance": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "QueryFlag",
        "desc": "2：普通会员子账号\n3：功能子账号"
      },
      {
        "name": "PageOffset",
        "desc": "起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      }
    ],
    "desc": "子商户余额查询"
  },
  "BindRelateAcctUnionPay": {
    "params": [
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”（右侧）进行分隔）"
      },
      {
        "name": "MemberName",
        "desc": "STRING(150)，见证子账户的户名（首次绑定的情况下，此字段即为待绑定的提现账户的户名。非首次绑定的情况下，须注意带绑定的提现账户的户名须与留存在后台系统的会员户名一致）"
      },
      {
        "name": "MemberGlobalType",
        "desc": "STRING(5)，会员证件类型（详情见“常见问题”）"
      },
      {
        "name": "MemberGlobalId",
        "desc": "STRING(32)，会员证件号码"
      },
      {
        "name": "MemberAcctNo",
        "desc": "STRING(50)，会员的待绑定账户的账号（提现的银行卡）"
      },
      {
        "name": "BankType",
        "desc": "STRING(10)，会员的待绑定账户的本他行类型（1: 本行; 2: 他行）"
      },
      {
        "name": "AcctOpenBranchName",
        "desc": "STRING(150)，会员的待绑定账户的开户行名称（若大小额行号不填则送超级网银号对应的银行名称，若填大小额行号则送大小额行号对应的银行名称）"
      },
      {
        "name": "Mobile",
        "desc": "STRING(30)，会员的手机号（手机号须由长度为11位的数字构成）"
      },
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "CnapsBranchId",
        "desc": "STRING(20)，会员的待绑定账户的开户行的联行号（本他行类型为他行的情况下，此字段和下一个字段至少一个不为空）"
      },
      {
        "name": "EiconBankBranchId",
        "desc": "STRING(20)，会员的待绑定账户的开户行的超级网银行号（本他行类型为他行的情况下，此字段和上一个字段至少一个不为空）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "会员绑定提现账户-银联鉴权。用于会员申请绑定提现账户，申请后银行前往银联验证卡信息：姓名、证件、卡号、银行预留手机是否相符，相符则发送给会员手机动态验证码并返回成功，不相符则返回失败。\n平台接收到银行返回成功后，进入输入动态验证码的页面，有效期120秒，若120秒未输入，客户可点击重新发送动态验证码，这个步骤重新调用该接口即可。\n平安银行的账户，大小额行号和超级网银号都不用送。\n超级网银号：单笔转账金额不超过5万，不限制笔数，只用选XX银行，不用具体到支行，可实时知道对方是否收款成功。\n大小额联行号：单笔转账可超过5万，需具体到支行，不能实时知道对方是否收款成功。金额超过5万的，在工作日的8点30-17点间才会成功。"
  },
  "WithdrawCashMembership": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "TranWebName",
        "desc": "STRING(150)，交易网名称（市场名称）"
      },
      {
        "name": "MemberGlobalType",
        "desc": "STRING(5)，会员证件类型（详情见“常见问题”）"
      },
      {
        "name": "MemberGlobalId",
        "desc": "STRING(32)，会员证件号码"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码"
      },
      {
        "name": "MemberName",
        "desc": "STRING(150)，会员名称"
      },
      {
        "name": "TakeCashAcctNo",
        "desc": "STRING(50)，提现账号（银行卡）"
      },
      {
        "name": "OutAmtAcctName",
        "desc": "STRING(150)，出金账户名称（银行卡户名）"
      },
      {
        "name": "Ccy",
        "desc": "STRING(3)，币种（默认为RMB）"
      },
      {
        "name": "CashAmt",
        "desc": "STRING(20)，可提现金额"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注（建议可送订单号，可在对账文件的备注字段获取到）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      },
      {
        "name": "WebSign",
        "desc": "STRING(300)，网银签名"
      }
    ],
    "desc": "会员提现-不验证。此接口受理会员发起的提现申请。会员子账户的可提现余额、可用余额会减少，市场的资金汇总账户(监管账户)会减少相应的发生金额，提现到会员申请的收款账户。\t\t"
  },
  "QueryBankTransactionDetails": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1: 当日; 2: 历史）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子帐户的帐号"
      },
      {
        "name": "QueryFlag",
        "desc": "STRING(4)，查询标志（1: 全部; 2: 转出; 3: 转入 ）"
      },
      {
        "name": "PageNum",
        "desc": "STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）"
      },
      {
        "name": "StartDate",
        "desc": "STRING(8)，开始日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）"
      },
      {
        "name": "EndDate",
        "desc": "STRING(8)，终止日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "查询银行时间段内交易明细。查询时间段的会员成功交易。"
  },
  "QueryMemberTransaction": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1: 下单预支付; 2: 确认并付款; 3: 退款; 6: 直接支付T+1; 9: 直接支付T+0）"
      },
      {
        "name": "OutSubAcctNo",
        "desc": "STRING(50)，转出方的见证子账户的账号（付款方）"
      },
      {
        "name": "OutMemberCode",
        "desc": "STRING(32)，转出方的交易网会员代码"
      },
      {
        "name": "OutSubAcctName",
        "desc": "STRING(150)，转出方的见证子账户的户名（户名是绑卡时上送的账户名称，如果未绑卡，就送OpenCustAcctId接口上送的用户昵称UserNickname）"
      },
      {
        "name": "InSubAcctNo",
        "desc": "STRING(50)，转入方的见证子账户的账号（收款方）"
      },
      {
        "name": "InMemberCode",
        "desc": "STRING(32)，转入方的交易网会员代码"
      },
      {
        "name": "InSubAcctName",
        "desc": "STRING(150)，转入方的见证子账户的户名（户名是绑卡时上送的账户名称，如果未绑卡，就送OpenCustAcctId接口上送的用户昵称UserNickname）"
      },
      {
        "name": "TranAmt",
        "desc": "STRING(20)，交易金额"
      },
      {
        "name": "TranFee",
        "desc": "STRING(20)，交易费用（平台收取交易费用）"
      },
      {
        "name": "TranType",
        "desc": "STRING(20)，交易类型（01: 普通交易）"
      },
      {
        "name": "Ccy",
        "desc": "STRING(3)，币种（默认: RMB）"
      },
      {
        "name": "OrderNo",
        "desc": "STRING(50)，订单号（功能标志为1,2,3时必输）"
      },
      {
        "name": "OrderContent",
        "desc": "STRING(500)，订单内容"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注（建议可送订单号，可在对账文件的备注字段获取到）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域（若需短信验证码则此项必输短信指令号）"
      },
      {
        "name": "WebSign",
        "desc": "STRING(300)，网银签名（若需短信验证码则此项必输）"
      }
    ],
    "desc": "会员间交易-不验证。此接口可以实现会员间的余额的交易，实现资金在会员之间流动。"
  },
  "QueryInvoiceForManagement": {
    "params": [
      {
        "name": "InvoicePlatformId",
        "desc": "开票平台ID"
      },
      {
        "name": "InvoiceStatus",
        "desc": "开票状态"
      },
      {
        "name": "RedInvoiceStatus",
        "desc": "红冲状态"
      },
      {
        "name": "BeginTime",
        "desc": "开始时间"
      },
      {
        "name": "EndTime",
        "desc": "结束时间"
      },
      {
        "name": "Offset",
        "desc": "页码"
      },
      {
        "name": "Limit",
        "desc": "页大小"
      },
      {
        "name": "OrderId",
        "desc": "订单号"
      },
      {
        "name": "InvoiceId",
        "desc": "发票ID"
      },
      {
        "name": "OrderSn",
        "desc": "业务开票号"
      },
      {
        "name": "InvoiceSn",
        "desc": "发票号码"
      },
      {
        "name": "InvoiceCode",
        "desc": "发票代码"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填 sandbox。"
      }
    ],
    "desc": "智慧零售-查询管理端发票"
  },
  "QueryCommonTransferRecharge": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1为查询当日数据，0查询历史数据）"
      },
      {
        "name": "StartDate",
        "desc": "STRING(8)，开始日期（格式：20190101）"
      },
      {
        "name": "EndDate",
        "desc": "STRING(8)，终止日期（格式：20190101）"
      },
      {
        "name": "PageNum",
        "desc": "STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "查询普通转账充值明细。接口用于查询会员主动转账进资金汇总账户的明细情况。若会员使用绑定账号转入，则直接入账到会员子账户。若未使用绑定账号转入，则系统无法自动清分到对应子账户，则转入挂账子账户由平台自行清分。若是 “见证+收单充值”T0充值记录时备注Note为“见证+收单充值,订单号” 此接口可以查到T0到账的“见证+收单充值”充值记录。"
  },
  "DownloadBill": {
    "params": [
      {
        "name": "StateDate",
        "desc": "请求下载对账单日期"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的MidasAppId"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的SecretId"
      },
      {
        "name": "MidasSignature",
        "desc": "使用聚鑫安全密钥计算的签名"
      }
    ],
    "desc": "账单下载接口，根据本接口返回的URL地址，在D+1日下载对账单。注意，本接口返回的URL地址有时效，请尽快下载。URL超时时效后，请重新调用本接口再次获取。"
  },
  "QueryAcctBinding": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "MidasSecretId",
        "desc": "由平台客服提供的计费密钥Id"
      },
      {
        "name": "MidasSignature",
        "desc": "计费签名"
      }
    ],
    "desc": "聚鑫-查询子账户绑定银行卡"
  },
  "CloseOrder": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "UserId",
        "desc": "用户ID，长度不小于5位， 仅支持字母和数字的组合"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "OutTradeNo",
        "desc": "业务订单号，OutTradeNo ， TransactionId二选一，不能都为空,优先使用 OutTradeNo"
      },
      {
        "name": "TransactionId",
        "desc": "聚鑫订单号，OutTradeNo ， TransactionId二选一，不能都为空,优先使用 OutTradeNo"
      }
    ],
    "desc": "通过此接口关闭此前已创建的订单，关闭后，用户将无法继续付款。仅能关闭创建后未支付的订单"
  },
  "CreateInvoice": {
    "params": [
      {
        "name": "InvoicePlatformId",
        "desc": "开票平台ID。0：高灯"
      },
      {
        "name": "TitleType",
        "desc": "抬头类型：1：个人/政府事业单位；2：企业"
      },
      {
        "name": "BuyerTitle",
        "desc": "购方名称"
      },
      {
        "name": "OrderId",
        "desc": "业务开票号"
      },
      {
        "name": "AmountHasTax",
        "desc": "含税总金额（单位为分）"
      },
      {
        "name": "TaxAmount",
        "desc": "总税额（单位为分）"
      },
      {
        "name": "AmountWithoutTax",
        "desc": "不含税总金额（单位为分）"
      },
      {
        "name": "SellerTaxpayerNum",
        "desc": "销方纳税人识别号"
      },
      {
        "name": "SellerName",
        "desc": "销方名称。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "SellerAddress",
        "desc": "销方地址。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "SellerPhone",
        "desc": "销方电话。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "SellerBankName",
        "desc": "销方银行名称。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "SellerBankAccount",
        "desc": "销方银行账号。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "BuyerTaxpayerNum",
        "desc": "购方纳税人识别号（购方票面信息）,若抬头类型为2时，必传"
      },
      {
        "name": "BuyerAddress",
        "desc": "购方地址。开具专用发票时必填"
      },
      {
        "name": "BuyerBankName",
        "desc": "购方银行名称。开具专用发票时必填"
      },
      {
        "name": "BuyerBankAccount",
        "desc": "购方银行账号。开具专用发票时必填"
      },
      {
        "name": "BuyerPhone",
        "desc": "购方电话。开具专用发票时必填"
      },
      {
        "name": "BuyerEmail",
        "desc": "收票人邮箱。若填入，会收到发票推送邮件"
      },
      {
        "name": "TakerPhone",
        "desc": "收票人手机号。若填入，会收到发票推送短信"
      },
      {
        "name": "InvoiceType",
        "desc": "开票类型：\n1：增值税专用发票；\n2：增值税普通发票；\n3：增值税电子发票；\n4：增值税卷式发票；\n5：区块链电子发票。\n若该字段不填，或值不为1-5，则认为开具”增值税电子发票”"
      },
      {
        "name": "CallbackUrl",
        "desc": "发票结果回传地址"
      },
      {
        "name": "Drawer",
        "desc": "开票人姓名。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "Payee",
        "desc": "收款人姓名。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "Checker",
        "desc": "复核人姓名。（不填默认读取商户注册时输入的信息）"
      },
      {
        "name": "TerminalCode",
        "desc": "税盘号"
      },
      {
        "name": "LevyMethod",
        "desc": "征收方式。开具差额征税发票时必填2。开具普通征税发票时为空"
      },
      {
        "name": "Deduction",
        "desc": "差额征税扣除额（单位为分）"
      },
      {
        "name": "Remark",
        "desc": "备注（票面信息）"
      },
      {
        "name": "Items",
        "desc": "项目商品明细"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox。"
      }
    ],
    "desc": "智慧零售-发票开具"
  },
  "QueryCustAcctIdBalance": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "QueryFlag",
        "desc": "STRING(4)，查询标志（2: 普通会员子账号; 3: 功能子账号）"
      },
      {
        "name": "PageNum",
        "desc": "STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子账户的账号（若SelectFlag为2时，子账号必输）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "查询银行子账户余额。查询会员子账户以及平台的功能子账户的余额。"
  },
  "QueryRefund": {
    "params": [
      {
        "name": "UserId",
        "desc": "用户ID，长度不小于5位，仅支持字母和数字的组合。"
      },
      {
        "name": "RefundId",
        "desc": "退款订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合。"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      }
    ],
    "desc": "提交退款申请后，通过调用该接口查询退款状态。退款可能有一定延时，用微信零钱支付的退款约20分钟内到账，银行卡支付的退款约3个工作日后到账。"
  },
  "RegisterBillSupportWithdraw": {
    "params": [
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码"
      },
      {
        "name": "OrderNo",
        "desc": "STRING(50)，订单号"
      },
      {
        "name": "SuspendAmt",
        "desc": "STRING(20)，挂账金额（包含交易费用）"
      },
      {
        "name": "TranFee",
        "desc": "STRING(20)，交易费用（暂未使用，默认传0.0）"
      },
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注"
      },
      {
        "name": "ReservedMsgOne",
        "desc": "STRING(300)，保留域1"
      },
      {
        "name": "ReservedMsgTwo",
        "desc": "STRING(300)，保留域2"
      },
      {
        "name": "ReservedMsgThree",
        "desc": "STRING(300)，保留域3"
      }
    ],
    "desc": "登记挂账(支持撤销)。此接口可实现把不明来账或自有资金等已登记在挂账子账户下的资金调整到普通会员子账户。即通过申请调用此接口，将会减少挂账子账户的资金，调增指定的普通会员子账户的可提现余额及可用余额。此接口不支持把挂账子账户资金清分到功能子账户。"
  },
  "QueryBankClear": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1: 全部; 2: 指定时间段）"
      },
      {
        "name": "PageNum",
        "desc": "STRING (10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）"
      },
      {
        "name": "StartDate",
        "desc": "STRING(8)，开始日期（若是指定时间段查询，则必输，当查询全部时，不起作用。格式: 20190101）"
      },
      {
        "name": "EndDate",
        "desc": "STRING(8)，终止日期（若是指定时间段查询，则必输，当查询全部时，不起作用。格式：20190101）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "查询银行在途清算结果。查询时间段内交易网的在途清算结果。"
  },
  "QuerySingleTransactionStatus": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（2: 会员间交易; 3: 提现; 4: 充值）"
      },
      {
        "name": "TranNetSeqNo",
        "desc": "STRING(52)，交易网流水号（提现，充值或会员交易请求时的CnsmrSeqNo值）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子帐户的帐号（未启用）"
      },
      {
        "name": "TranDate",
        "desc": "STRING(8)，交易日期（未启用）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "查询银行单笔交易状态。查询单笔交易的状态。"
  },
  "UnBindAcct": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "SettleAcctNo",
        "desc": "用于提现\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      }
    ],
    "desc": "商户解除绑定的提现银行卡"
  },
  "BindRelateAccReUnionPay": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”（右侧）进行分隔）"
      },
      {
        "name": "MemberAcctNo",
        "desc": "STRING(50)，会员的待绑定账户的账号（即 BindRelateAcctUnionPay接口中的“会员的待绑定账户的账号”）"
      },
      {
        "name": "MessageCheckCode",
        "desc": "STRING(20)，短信验证码（即 BindRelateAcctUnionPay接口中的手机所接收到的短信验证码）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "会员绑定提现账户-回填银联鉴权短信码。用于会员填写动态验证码后，发往银行进行验证，验证成功则完成绑定。"
  },
  "CreateRedInvoice": {
    "params": [
      {
        "name": "InvoicePlatformId",
        "desc": "开票平台ID"
      },
      {
        "name": "Invoices",
        "desc": "红冲明细"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填 sandbox。"
      }
    ],
    "desc": "智慧零售-发票红冲"
  },
  "CheckAmount": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）"
      },
      {
        "name": "TakeCashAcctNo",
        "desc": "STRING(50)，会员的待绑定账户的账号（即 BindRelateAcctSmallAmount接口中的“会员的待绑定账户的账号”）"
      },
      {
        "name": "AuthAmt",
        "desc": "STRING(20)，鉴权验证金额（即 BindRelateAcctSmallAmount接口中的“会员的待绑定账户收到的验证金额。原小额转账鉴权方式为来账鉴权的情况下此字段须赋值为0.00）"
      },
      {
        "name": "Ccy",
        "desc": "STRING(3)，币种（默认为RMB）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，原小额转账方式（1: 往账鉴权，此为默认值; 2: 来账鉴权）"
      }
    ],
    "desc": "验证鉴权金额。此接口可受理BindRelateAcctSmallAmount接口发起的转账金额（往账鉴权方式）的验证处理。若所回填的验证金额验证通过，则会绑定原申请中的银行账户作为提现账户。通过此接口也可以查得BindRelateAcctSmallAmount接口发起的来账鉴权方式的申请的当前状态。"
  },
  "RevResigterBillSupportWithdraw": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码"
      },
      {
        "name": "OldOrderNo",
        "desc": "STRING(30)，原订单号（RegisterBillSupportWithdraw接口中的订单号）"
      },
      {
        "name": "CancelAmt",
        "desc": "STRING(20)，撤销金额（支持部分撤销，不能大于原订单可用金额，包含交易费用）"
      },
      {
        "name": "TranFee",
        "desc": "STRING(20)，交易费用（暂未使用，默认传0.0）"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注"
      },
      {
        "name": "ReservedMsgOne",
        "desc": "STRING(300)，保留域1"
      },
      {
        "name": "ReservedMsgTwo",
        "desc": "STRING(300)，保留域2"
      },
      {
        "name": "ReservedMsgThree",
        "desc": "STRING(300)，保留域3"
      }
    ],
    "desc": "登记挂账撤销。此接口可以实现把RegisterBillSupportWithdraw接口完成的登记挂账进行撤销，即调减普通会员子账户的可提现和可用余额，调增挂账子账户的可用余额。"
  },
  "RevokeMemberRechargeThirdPay": {
    "params": [
      {
        "name": "OldFillFrontSeqNo",
        "desc": "STRING(52)，原充值的前置流水号"
      },
      {
        "name": "OldFillPayChannelType",
        "desc": "STRING(20)，原充值的支付渠道类型"
      },
      {
        "name": "OldPayChannelTranSeqNo",
        "desc": "STRING(52)，原充值的支付渠道交易流水号"
      },
      {
        "name": "OldFillEjzbOrderNo",
        "desc": "STRING(52)，原充值的电商见证宝订单号"
      },
      {
        "name": "ApplyCancelMemberAmt",
        "desc": "STRING(20)，申请撤销的会员金额"
      },
      {
        "name": "ApplyCancelCommission",
        "desc": "STRING(20)，申请撤销的手续费金额"
      },
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注"
      },
      {
        "name": "ReservedMsgOne",
        "desc": "STRING(300)，保留域1"
      },
      {
        "name": "ReservedMsgTwo",
        "desc": "STRING(300)，保留域2"
      },
      {
        "name": "ReservedMsgThree",
        "desc": "STRING(300)，保留域3"
      }
    ],
    "desc": "撤销会员在途充值(经第三方支付渠道)"
  },
  "Refund": {
    "params": [
      {
        "name": "UserId",
        "desc": "用户ID，长度不小于5位， 仅支持字母和数字的组合"
      },
      {
        "name": "RefundId",
        "desc": "退款订单号，仅支持数字、 字母、下划线（_）、横杠字 符（-）、点（.）的组合"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "TotalRefundAmt",
        "desc": "退款金额，单位：分。备注：当该字段为空或者为0 时，系统会默认使用订单当 实付金额作为退款金额"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "OutTradeNo",
        "desc": "商品订单，仅支持数字、字 母、下划线（_）、横杠字符 （-）、点（.）的组合。  OutTradeNo ,TransactionId 二选一,不能都为空,优先使用 OutTradeNo"
      },
      {
        "name": "MchRefundAmt",
        "desc": "结算应收金额，单位：分"
      },
      {
        "name": "TransactionId",
        "desc": "调用下单接口获取的聚鑫交 易订单。  OutTradeNo ,TransactionId 二选一,不能都为空,优先使用 OutTradeNo"
      },
      {
        "name": "PlatformRefundAmt",
        "desc": "平台应收金额，单位：分"
      },
      {
        "name": "SubOrderRefundList",
        "desc": "支持多个子订单批量退款单 个子订单退款支持传 SubOutTradeNo ，也支持传 SubOutTradeNoList ，都传的时候以 SubOutTradeNoList 为准。  如果传了子单退款细节，外 部不需要再传退款金额，平 台应退，商户应退金额，我 们可以直接根据子单退款算出来总和。"
      }
    ],
    "desc": "如交易订单需退款，可以通过本接口将支付款全部或部分退还给付款方，聚鑫将在收到退款请求并且验证成功之后，按照退款规则将支付款按原路退回到支付帐号。最长支持1年的订单退款。在订单包含多个子订单的情况下，如果使用本接口传入OutTradeNo或TransactionId退款，则只支持全单退款；如果需要部分退款，请通过传入子订单的方式来指定部分金额退款。 "
  },
  "QuerySmallAmountTransfer": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "OldTranSeqNo",
        "desc": "STRING(52)，原交易流水号（小额鉴权交易请求时的CnsmrSeqNo值）"
      },
      {
        "name": "TranDate",
        "desc": "STRING(8)，交易日期（格式：20190101）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "查询小额鉴权转账结果。查询小额往账鉴权的转账状态。"
  },
  "RechargeMemberThirdPay": {
    "params": [
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会代码"
      },
      {
        "name": "MemberFillAmt",
        "desc": "STRING(20)，会员充值金额"
      },
      {
        "name": "Commission",
        "desc": "STRING(20)，手续费金额"
      },
      {
        "name": "Ccy",
        "desc": "STRING(3)，币种。如RMB"
      },
      {
        "name": "PayChannelType",
        "desc": "STRING(20)，支付渠道类型。\n0001-微信\n0002-支付宝\n0003-京东支付"
      },
      {
        "name": "PayChannelAssignMerNo",
        "desc": "STRING(50)，支付渠道所分配的商户号"
      },
      {
        "name": "PayChannelTranSeqNo",
        "desc": "STRING(52)，支付渠道交易流水号"
      },
      {
        "name": "EjzbOrderNo",
        "desc": "STRING(52)，电商见证宝订单号"
      },
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号"
      },
      {
        "name": "EjzbOrderContent",
        "desc": "STRING(500)，电商见证宝订单内容"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注"
      },
      {
        "name": "ReservedMsgOne",
        "desc": "STRING(300)，保留域1"
      },
      {
        "name": "ReservedMsgTwo",
        "desc": "STRING(300)，保留域2"
      },
      {
        "name": "ReservedMsgThree",
        "desc": "STRING(300)，保留域3"
      }
    ],
    "desc": "见证宝-会员在途充值(经第三方支付渠道)"
  },
  "QueryInvoice": {
    "params": [
      {
        "name": "InvoicePlatformId",
        "desc": "开票平台ID"
      },
      {
        "name": "OrderId",
        "desc": "订单号"
      },
      {
        "name": "OrderSn",
        "desc": "业务开票号"
      },
      {
        "name": "IsRed",
        "desc": "发票种类：\n0：蓝票\n1：红票【该字段默认为0， 如果需要查询红票信息，本字段必须传1，否则可能查询不到需要的发票信息】。"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填sandbox。"
      }
    ],
    "desc": "智慧零售-发票查询"
  },
  "CreateMerchant": {
    "params": [
      {
        "name": "InvoicePlatformId",
        "desc": "开票平台ID"
      },
      {
        "name": "TaxpayerName",
        "desc": "企业名称"
      },
      {
        "name": "TaxpayerNum",
        "desc": "销方纳税人识别号"
      },
      {
        "name": "LegalPersonName",
        "desc": "注册企业法人代表名称"
      },
      {
        "name": "ContactsName",
        "desc": "联系人"
      },
      {
        "name": "Phone",
        "desc": "联系人手机号"
      },
      {
        "name": "Address",
        "desc": "不包含省市名称的地址"
      },
      {
        "name": "RegionCode",
        "desc": "地区编码"
      },
      {
        "name": "CityName",
        "desc": "市（地区）名称"
      },
      {
        "name": "Drawer",
        "desc": "开票人"
      },
      {
        "name": "TaxRegistrationCertificate",
        "desc": "税务登记证图片（Base64）字符串，需小于 3M"
      },
      {
        "name": "Email",
        "desc": "联系人邮箱地址"
      },
      {
        "name": "BusinessMobile",
        "desc": "企业电话"
      },
      {
        "name": "BankName",
        "desc": "银行名称"
      },
      {
        "name": "BankAccount",
        "desc": "银行账号"
      },
      {
        "name": "Reviewer",
        "desc": "复核人"
      },
      {
        "name": "Payee",
        "desc": "收款人"
      },
      {
        "name": "RegisterCode",
        "desc": "注册邀请码"
      },
      {
        "name": "State",
        "desc": "不填默认为1，有效状态\n0：表示无效；\n1:表示有效；\n2:表示禁止开蓝票；\n3:表示禁止冲红。"
      },
      {
        "name": "CallbackUrl",
        "desc": "接收推送的消息地址"
      },
      {
        "name": "Profile",
        "desc": "接入环境。沙箱环境填 sandbox。"
      }
    ],
    "desc": "智慧零售-商户注册"
  },
  "CreateAcct": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫平台分配的支付MidasAppId"
      },
      {
        "name": "SubMchId",
        "desc": "业务平台的子商户ID，唯一"
      },
      {
        "name": "SubMchName",
        "desc": "子商户名称"
      },
      {
        "name": "Address",
        "desc": "子商户地址"
      },
      {
        "name": "Contact",
        "desc": "子商户联系人\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "Mobile",
        "desc": "联系人手机号\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "Email",
        "desc": "邮箱 \n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "SubMchType",
        "desc": "子商户类型：\n个人: personal\n企业：enterprise\n缺省： enterprise"
      },
      {
        "name": "ShortName",
        "desc": "不填则默认子商户名称"
      },
      {
        "name": "SubMerchantMemberType",
        "desc": "子商户会员类型：\ngeneral:普通子账户\nmerchant:商户子账户\n缺省： general"
      }
    ],
    "desc": "子商户入驻聚鑫平台"
  },
  "UnifiedOrder": {
    "params": [
      {
        "name": "CurrencyType",
        "desc": "ISO 货币代码，CNY"
      },
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "OutTradeNo",
        "desc": "支付订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合"
      },
      {
        "name": "ProductDetail",
        "desc": "商品详情，需要URL编码"
      },
      {
        "name": "ProductId",
        "desc": "商品ID，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合"
      },
      {
        "name": "ProductName",
        "desc": "商品名称，需要URL编码"
      },
      {
        "name": "TotalAmt",
        "desc": "支付金额，单位： 分"
      },
      {
        "name": "UserId",
        "desc": "用户ID，长度不小于5位，仅支持字母和数字的组合"
      },
      {
        "name": "RealChannel",
        "desc": "银行真实渠道.如:bank_pingan"
      },
      {
        "name": "OriginalAmt",
        "desc": "原始金额"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "CallbackUrl",
        "desc": "Web端回调地址"
      },
      {
        "name": "Channel",
        "desc": "指定支付渠道：  wechat：微信支付  qqwallet：QQ钱包 \n bank：网银支付  只有一个渠道时需要指定"
      },
      {
        "name": "Metadata",
        "desc": "透传字段，支付成功回调透传给应用，用于业务透传自定义内容"
      },
      {
        "name": "Quantity",
        "desc": "购买数量，不传默认为1"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "SubOrderList",
        "desc": "子订单信息列表，格式：子订单号、子应用ID、金额。 压缩后最长不可超过65535字节(去除空格，换行，制表符等无意义字符)\n注：接入银行或其他支付渠道服务商模式下，必传"
      },
      {
        "name": "TotalMchIncome",
        "desc": "结算应收金额，单位：分"
      },
      {
        "name": "TotalPlatformIncome",
        "desc": "平台应收金额，单位：分"
      },
      {
        "name": "WxOpenId",
        "desc": "微信公众号/小程序支付时为必选，需要传微信下的openid"
      },
      {
        "name": "WxSubOpenId",
        "desc": "在服务商模式下，微信公众号/小程序支付时wx_sub_openid和wx_openid二选一"
      }
    ],
    "desc": "应用需要先调用本接口生成支付订单号，并将应答的PayInfo透传给聚鑫SDK，拉起客户端（包括微信公众号/微信小程序/客户端App）支付。"
  },
  "RevRegisterBillSupportWithdraw": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码"
      },
      {
        "name": "OldOrderNo",
        "desc": "STRING(30)，原订单号（RegisterBillSupportWithdraw接口中的订单号）"
      },
      {
        "name": "CancelAmt",
        "desc": "STRING(20)，撤销金额（支持部分撤销，不能大于原订单可用金额，包含交易费用）"
      },
      {
        "name": "TranFee",
        "desc": "STRING(20)，交易费用（暂未使用，默认传0.0）"
      },
      {
        "name": "Remark",
        "desc": "STRING(300)，备注"
      },
      {
        "name": "ReservedMsgOne",
        "desc": "STRING(300)，保留域1"
      },
      {
        "name": "ReservedMsgTwo",
        "desc": "STRING(300)，保留域2"
      },
      {
        "name": "ReservedMsgThree",
        "desc": "STRING(300)，保留域3"
      }
    ],
    "desc": "登记挂账撤销。此接口可以实现把RegisterBillSupportWithdraw接口完成的登记挂账进行撤销，即调减普通会员子账户的可提现和可用余额，调增挂账子账户的可用余额。"
  },
  "UnbindRelateAcct": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1: 解绑）"
      },
      {
        "name": "TranNetMemberCode",
        "desc": "STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）"
      },
      {
        "name": "MemberAcctNo",
        "desc": "STRING(50)，待解绑的提现账户的账号（提现账号）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "会员解绑提现账户。此接口可以支持会员解除名下的绑定账户关系。"
  },
  "QueryBankWithdrawCashDetails": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号（签约客户号）"
      },
      {
        "name": "FunctionFlag",
        "desc": "STRING(2)，功能标志（1: 当日; 2: 历史）"
      },
      {
        "name": "SubAcctNo",
        "desc": "STRING(50)，见证子帐户的帐号"
      },
      {
        "name": "QueryFlag",
        "desc": "STRING(4)，查询标志（2: 提现; 3: 清分）"
      },
      {
        "name": "PageNum",
        "desc": "STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）"
      },
      {
        "name": "BeginDate",
        "desc": "STRING(8)，开始日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）"
      },
      {
        "name": "EndDate",
        "desc": "STRING(8)，结束日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "查询银行时间段内清分提现明细。查询银行时间段内清分提现明细接口：若为“见证+收单退款”“见证+收单充值”记录时备注Note为“见证+收单充值,订单号”“见证+收单退款,订单号”，此接口可以查到T0/T1的充值明细和退款记录。查询标志：充值记录仍用3清分选项查询，退款记录同提现用2选项查询。"
  },
  "QueryReconciliationDocument": {
    "params": [
      {
        "name": "MrchCode",
        "desc": "String(22)，商户号"
      },
      {
        "name": "FileType",
        "desc": "STRING(10)，文件类型（充值文件-CZ; 提现文件-TX; 交易文件-JY; 余额文件-YE; 合约文件-HY）"
      },
      {
        "name": "FileDate",
        "desc": "STRING(8)，文件日期（格式：20190101）"
      },
      {
        "name": "ReservedMsg",
        "desc": "STRING(1027)，保留域"
      }
    ],
    "desc": "查询对账文件信息。平台调用该接口获取需下载对账文件的文件名称以及密钥。 平台获取到信息后， 可以再调用OPENAPI的文件下载功能。"
  },
  "CheckAcct": {
    "params": [
      {
        "name": "MidasAppId",
        "desc": "聚鑫分配的支付主MidasAppId"
      },
      {
        "name": "SubAppId",
        "desc": "聚鑫计费SubAppId，代表子商户"
      },
      {
        "name": "BindType",
        "desc": "1：小额鉴权\n2：短信校验鉴权"
      },
      {
        "name": "SettleAcctNo",
        "desc": "结算账户账号\n<敏感信息>加密详见《商户端接口敏感信息加密说明》"
      },
      {
        "name": "MidasSecretId",
        "desc": "聚鑫分配的安全ID"
      },
      {
        "name": "MidasSignature",
        "desc": "按照聚鑫安全密钥计算的签名"
      },
      {
        "name": "CheckCode",
        "desc": "短信验证码\nBindType==2必填"
      },
      {
        "name": "CurrencyType",
        "desc": "币种 RMB\nBindType==1必填"
      },
      {
        "name": "CurrencyUnit",
        "desc": "单位\n1：元，2：角，3：分\nBindType==1必填"
      },
      {
        "name": "CurrencyAmt",
        "desc": "金额\nBindType==1必填"
      }
    ],
    "desc": "商户绑定提现银行卡的验证接口"
  }
}