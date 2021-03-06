# -*- coding: utf-8 -*-
import os
import json
import tccli.options_define as OptionsDefine
import tccli.format_output as FormatOutput
from tccli.nice_command import NiceCommand
import tccli.error_msg as ErrorMsg
import tccli.help_template as HelpTemplate
from tccli import __version__
from tccli.utils import Utils
from tccli.configure import Configure
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.cpdp.v20190820 import cpdp_client as cpdp_client_v20190820
from tencentcloud.cpdp.v20190820 import models as models_v20190820
from tccli.services.cpdp import v20190820
from tccli.services.cpdp.v20190820 import help as v20190820_help


def doBindAcct(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindAcct", g_param[OptionsDefine.Version])
        return

    param = {
        "MidasAppId": argv.get("--MidasAppId"),
        "SubAppId": argv.get("--SubAppId"),
        "BindType": Utils.try_to_json(argv, "--BindType"),
        "SettleAcctNo": argv.get("--SettleAcctNo"),
        "SettleAcctName": argv.get("--SettleAcctName"),
        "SettleAcctType": Utils.try_to_json(argv, "--SettleAcctType"),
        "IdType": argv.get("--IdType"),
        "IdCode": argv.get("--IdCode"),
        "AcctBranchName": argv.get("--AcctBranchName"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),
        "Mobile": argv.get("--Mobile"),
        "CnapsBranchId": argv.get("--CnapsBranchId"),
        "EiconBankBranchId": argv.get("--EiconBankBranchId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindAcctRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindAcct(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindRelateAcctSmallAmount(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindRelateAcctSmallAmount", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "TranNetMemberCode": argv.get("--TranNetMemberCode"),
        "MemberName": argv.get("--MemberName"),
        "MemberGlobalType": argv.get("--MemberGlobalType"),
        "MemberGlobalId": argv.get("--MemberGlobalId"),
        "MemberAcctNo": argv.get("--MemberAcctNo"),
        "BankType": argv.get("--BankType"),
        "AcctOpenBranchName": argv.get("--AcctOpenBranchName"),
        "Mobile": argv.get("--Mobile"),
        "CnapsBranchId": argv.get("--CnapsBranchId"),
        "EiconBankBranchId": argv.get("--EiconBankBranchId"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindRelateAcctSmallAmountRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindRelateAcctSmallAmount(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doApplyWithdrawal(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ApplyWithdrawal", g_param[OptionsDefine.Version])
        return

    param = {
        "MidasAppId": argv.get("--MidasAppId"),
        "SubAppId": argv.get("--SubAppId"),
        "SettleAcctNo": argv.get("--SettleAcctNo"),
        "SettleAcctName": argv.get("--SettleAcctName"),
        "CurrencyType": argv.get("--CurrencyType"),
        "CurrencyUnit": Utils.try_to_json(argv, "--CurrencyUnit"),
        "CurrencyAmt": argv.get("--CurrencyAmt"),
        "TranWebName": argv.get("--TranWebName"),
        "IdType": argv.get("--IdType"),
        "IdCode": argv.get("--IdCode"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ApplyWithdrawalRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ApplyWithdrawal(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doWithdrawCashMembership(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("WithdrawCashMembership", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "TranWebName": argv.get("--TranWebName"),
        "MemberGlobalType": argv.get("--MemberGlobalType"),
        "MemberGlobalId": argv.get("--MemberGlobalId"),
        "TranNetMemberCode": argv.get("--TranNetMemberCode"),
        "MemberName": argv.get("--MemberName"),
        "TakeCashAcctNo": argv.get("--TakeCashAcctNo"),
        "OutAmtAcctName": argv.get("--OutAmtAcctName"),
        "Ccy": argv.get("--Ccy"),
        "CashAmt": argv.get("--CashAmt"),
        "Remark": argv.get("--Remark"),
        "ReservedMsg": argv.get("--ReservedMsg"),
        "WebSign": argv.get("--WebSign"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.WithdrawCashMembershipRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.WithdrawCashMembership(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyMntMbrBindRelateAcctBankCode(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyMntMbrBindRelateAcctBankCode", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "SubAcctNo": argv.get("--SubAcctNo"),
        "MemberBindAcctNo": argv.get("--MemberBindAcctNo"),
        "AcctOpenBranchName": argv.get("--AcctOpenBranchName"),
        "CnapsBranchId": argv.get("--CnapsBranchId"),
        "EiconBankBranchId": argv.get("--EiconBankBranchId"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyMntMbrBindRelateAcctBankCodeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyMntMbrBindRelateAcctBankCode(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryMemberBind(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryMemberBind", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "QueryFlag": argv.get("--QueryFlag"),
        "PageNum": argv.get("--PageNum"),
        "SubAcctNo": argv.get("--SubAcctNo"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryMemberBindRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryMemberBind(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateCustAcctId(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateCustAcctId", g_param[OptionsDefine.Version])
        return

    param = {
        "FunctionFlag": argv.get("--FunctionFlag"),
        "FundSummaryAcctNo": argv.get("--FundSummaryAcctNo"),
        "TranNetMemberCode": argv.get("--TranNetMemberCode"),
        "MemberProperty": argv.get("--MemberProperty"),
        "Mobile": argv.get("--Mobile"),
        "MrchCode": argv.get("--MrchCode"),
        "SelfBusiness": Utils.try_to_json(argv, "--SelfBusiness"),
        "ContactName": argv.get("--ContactName"),
        "SubAcctName": argv.get("--SubAcctName"),
        "SubAcctShortName": argv.get("--SubAcctShortName"),
        "SubAcctType": Utils.try_to_json(argv, "--SubAcctType"),
        "UserNickname": argv.get("--UserNickname"),
        "Email": argv.get("--Email"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateCustAcctIdRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateCustAcctId(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCloseOrder(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CloseOrder", g_param[OptionsDefine.Version])
        return

    param = {
        "MidasAppId": argv.get("--MidasAppId"),
        "UserId": argv.get("--UserId"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),
        "OutTradeNo": argv.get("--OutTradeNo"),
        "TransactionId": argv.get("--TransactionId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CloseOrderRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CloseOrder(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryMerchantInfoForManagement(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryMerchantInfoForManagement", g_param[OptionsDefine.Version])
        return

    param = {
        "InvoicePlatformId": Utils.try_to_json(argv, "--InvoicePlatformId"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Profile": argv.get("--Profile"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryMerchantInfoForManagementRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryMerchantInfoForManagement(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doReviseMbrProperty(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ReviseMbrProperty", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "SubAcctNo": argv.get("--SubAcctNo"),
        "MemberProperty": argv.get("--MemberProperty"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ReviseMbrPropertyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ReviseMbrProperty(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryBalance(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryBalance", g_param[OptionsDefine.Version])
        return

    param = {
        "MidasAppId": argv.get("--MidasAppId"),
        "SubAppId": argv.get("--SubAppId"),
        "QueryFlag": argv.get("--QueryFlag"),
        "PageOffset": argv.get("--PageOffset"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryBalanceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryBalance(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindRelateAcctUnionPay(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindRelateAcctUnionPay", g_param[OptionsDefine.Version])
        return

    param = {
        "TranNetMemberCode": argv.get("--TranNetMemberCode"),
        "MemberName": argv.get("--MemberName"),
        "MemberGlobalType": argv.get("--MemberGlobalType"),
        "MemberGlobalId": argv.get("--MemberGlobalId"),
        "MemberAcctNo": argv.get("--MemberAcctNo"),
        "BankType": argv.get("--BankType"),
        "AcctOpenBranchName": argv.get("--AcctOpenBranchName"),
        "Mobile": argv.get("--Mobile"),
        "MrchCode": argv.get("--MrchCode"),
        "CnapsBranchId": argv.get("--CnapsBranchId"),
        "EiconBankBranchId": argv.get("--EiconBankBranchId"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindRelateAcctUnionPayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindRelateAcctUnionPay(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnbindRelateAcct(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnbindRelateAcct", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "FunctionFlag": argv.get("--FunctionFlag"),
        "TranNetMemberCode": argv.get("--TranNetMemberCode"),
        "MemberAcctNo": argv.get("--MemberAcctNo"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnbindRelateAcctRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnbindRelateAcct(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryBankTransactionDetails(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryBankTransactionDetails", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "FunctionFlag": argv.get("--FunctionFlag"),
        "SubAcctNo": argv.get("--SubAcctNo"),
        "QueryFlag": argv.get("--QueryFlag"),
        "PageNum": argv.get("--PageNum"),
        "StartDate": argv.get("--StartDate"),
        "EndDate": argv.get("--EndDate"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryBankTransactionDetailsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryBankTransactionDetails(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryMemberTransaction(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryMemberTransaction", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "FunctionFlag": argv.get("--FunctionFlag"),
        "OutSubAcctNo": argv.get("--OutSubAcctNo"),
        "OutMemberCode": argv.get("--OutMemberCode"),
        "OutSubAcctName": argv.get("--OutSubAcctName"),
        "InSubAcctNo": argv.get("--InSubAcctNo"),
        "InMemberCode": argv.get("--InMemberCode"),
        "InSubAcctName": argv.get("--InSubAcctName"),
        "TranAmt": argv.get("--TranAmt"),
        "TranFee": argv.get("--TranFee"),
        "TranType": argv.get("--TranType"),
        "Ccy": argv.get("--Ccy"),
        "OrderNo": argv.get("--OrderNo"),
        "OrderContent": argv.get("--OrderContent"),
        "Remark": argv.get("--Remark"),
        "ReservedMsg": argv.get("--ReservedMsg"),
        "WebSign": argv.get("--WebSign"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryMemberTransactionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryMemberTransaction(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryCommonTransferRecharge(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryCommonTransferRecharge", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "FunctionFlag": argv.get("--FunctionFlag"),
        "StartDate": argv.get("--StartDate"),
        "EndDate": argv.get("--EndDate"),
        "PageNum": argv.get("--PageNum"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryCommonTransferRechargeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryCommonTransferRecharge(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDownloadBill(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DownloadBill", g_param[OptionsDefine.Version])
        return

    param = {
        "StateDate": argv.get("--StateDate"),
        "MidasAppId": argv.get("--MidasAppId"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DownloadBillRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DownloadBill(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryAcctBinding(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryAcctBinding", g_param[OptionsDefine.Version])
        return

    param = {
        "MidasAppId": argv.get("--MidasAppId"),
        "SubAppId": argv.get("--SubAppId"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryAcctBindingRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryAcctBinding(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryOrder(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryOrder", g_param[OptionsDefine.Version])
        return

    param = {
        "MidasAppId": argv.get("--MidasAppId"),
        "UserId": argv.get("--UserId"),
        "Type": argv.get("--Type"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),
        "Count": Utils.try_to_json(argv, "--Count"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "StartTime": argv.get("--StartTime"),
        "EndTime": argv.get("--EndTime"),
        "OutTradeNo": argv.get("--OutTradeNo"),
        "TransactionId": argv.get("--TransactionId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryOrderRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryOrder(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateInvoice(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateInvoice", g_param[OptionsDefine.Version])
        return

    param = {
        "InvoicePlatformId": Utils.try_to_json(argv, "--InvoicePlatformId"),
        "TitleType": Utils.try_to_json(argv, "--TitleType"),
        "BuyerTitle": argv.get("--BuyerTitle"),
        "OrderId": argv.get("--OrderId"),
        "AmountHasTax": Utils.try_to_json(argv, "--AmountHasTax"),
        "TaxAmount": Utils.try_to_json(argv, "--TaxAmount"),
        "AmountWithoutTax": Utils.try_to_json(argv, "--AmountWithoutTax"),
        "SellerTaxpayerNum": argv.get("--SellerTaxpayerNum"),
        "SellerName": argv.get("--SellerName"),
        "SellerAddress": argv.get("--SellerAddress"),
        "SellerPhone": argv.get("--SellerPhone"),
        "SellerBankName": argv.get("--SellerBankName"),
        "SellerBankAccount": argv.get("--SellerBankAccount"),
        "BuyerTaxpayerNum": argv.get("--BuyerTaxpayerNum"),
        "BuyerAddress": argv.get("--BuyerAddress"),
        "BuyerBankName": argv.get("--BuyerBankName"),
        "BuyerBankAccount": argv.get("--BuyerBankAccount"),
        "BuyerPhone": argv.get("--BuyerPhone"),
        "BuyerEmail": argv.get("--BuyerEmail"),
        "TakerPhone": argv.get("--TakerPhone"),
        "InvoiceType": Utils.try_to_json(argv, "--InvoiceType"),
        "CallbackUrl": argv.get("--CallbackUrl"),
        "Drawer": argv.get("--Drawer"),
        "Payee": argv.get("--Payee"),
        "Checker": argv.get("--Checker"),
        "TerminalCode": argv.get("--TerminalCode"),
        "LevyMethod": argv.get("--LevyMethod"),
        "Deduction": Utils.try_to_json(argv, "--Deduction"),
        "Remark": argv.get("--Remark"),
        "Items": Utils.try_to_json(argv, "--Items"),
        "Profile": argv.get("--Profile"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateInvoiceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateInvoice(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryCustAcctIdBalance(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryCustAcctIdBalance", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "QueryFlag": argv.get("--QueryFlag"),
        "PageNum": argv.get("--PageNum"),
        "SubAcctNo": argv.get("--SubAcctNo"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryCustAcctIdBalanceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryCustAcctIdBalance(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryRefund(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryRefund", g_param[OptionsDefine.Version])
        return

    param = {
        "UserId": argv.get("--UserId"),
        "RefundId": argv.get("--RefundId"),
        "MidasAppId": argv.get("--MidasAppId"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryRefundRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryRefund(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRegisterBillSupportWithdraw(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RegisterBillSupportWithdraw", g_param[OptionsDefine.Version])
        return

    param = {
        "TranNetMemberCode": argv.get("--TranNetMemberCode"),
        "OrderNo": argv.get("--OrderNo"),
        "SuspendAmt": argv.get("--SuspendAmt"),
        "TranFee": argv.get("--TranFee"),
        "MrchCode": argv.get("--MrchCode"),
        "Remark": argv.get("--Remark"),
        "ReservedMsgOne": argv.get("--ReservedMsgOne"),
        "ReservedMsgTwo": argv.get("--ReservedMsgTwo"),
        "ReservedMsgThree": argv.get("--ReservedMsgThree"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RegisterBillSupportWithdrawRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RegisterBillSupportWithdraw(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryBankClear(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryBankClear", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "FunctionFlag": argv.get("--FunctionFlag"),
        "PageNum": argv.get("--PageNum"),
        "StartDate": argv.get("--StartDate"),
        "EndDate": argv.get("--EndDate"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryBankClearRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryBankClear(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQuerySingleTransactionStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QuerySingleTransactionStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "FunctionFlag": argv.get("--FunctionFlag"),
        "TranNetSeqNo": argv.get("--TranNetSeqNo"),
        "SubAcctNo": argv.get("--SubAcctNo"),
        "TranDate": argv.get("--TranDate"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QuerySingleTransactionStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QuerySingleTransactionStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnBindAcct(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnBindAcct", g_param[OptionsDefine.Version])
        return

    param = {
        "MidasAppId": argv.get("--MidasAppId"),
        "SubAppId": argv.get("--SubAppId"),
        "SettleAcctNo": argv.get("--SettleAcctNo"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnBindAcctRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnBindAcct(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBindRelateAccReUnionPay(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BindRelateAccReUnionPay", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "TranNetMemberCode": argv.get("--TranNetMemberCode"),
        "MemberAcctNo": argv.get("--MemberAcctNo"),
        "MessageCheckCode": argv.get("--MessageCheckCode"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BindRelateAccReUnionPayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BindRelateAccReUnionPay(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateRedInvoice(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateRedInvoice", g_param[OptionsDefine.Version])
        return

    param = {
        "InvoicePlatformId": Utils.try_to_json(argv, "--InvoicePlatformId"),
        "Invoices": Utils.try_to_json(argv, "--Invoices"),
        "Profile": argv.get("--Profile"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateRedInvoiceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateRedInvoice(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCheckAmount(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CheckAmount", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "TranNetMemberCode": argv.get("--TranNetMemberCode"),
        "TakeCashAcctNo": argv.get("--TakeCashAcctNo"),
        "AuthAmt": argv.get("--AuthAmt"),
        "Ccy": argv.get("--Ccy"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CheckAmountRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CheckAmount(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRevResigterBillSupportWithdraw(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RevResigterBillSupportWithdraw", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "TranNetMemberCode": argv.get("--TranNetMemberCode"),
        "OldOrderNo": argv.get("--OldOrderNo"),
        "CancelAmt": argv.get("--CancelAmt"),
        "TranFee": argv.get("--TranFee"),
        "Remark": argv.get("--Remark"),
        "ReservedMsgOne": argv.get("--ReservedMsgOne"),
        "ReservedMsgTwo": argv.get("--ReservedMsgTwo"),
        "ReservedMsgThree": argv.get("--ReservedMsgThree"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RevResigterBillSupportWithdrawRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RevResigterBillSupportWithdraw(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRevokeMemberRechargeThirdPay(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RevokeMemberRechargeThirdPay", g_param[OptionsDefine.Version])
        return

    param = {
        "OldFillFrontSeqNo": argv.get("--OldFillFrontSeqNo"),
        "OldFillPayChannelType": argv.get("--OldFillPayChannelType"),
        "OldPayChannelTranSeqNo": argv.get("--OldPayChannelTranSeqNo"),
        "OldFillEjzbOrderNo": argv.get("--OldFillEjzbOrderNo"),
        "ApplyCancelMemberAmt": argv.get("--ApplyCancelMemberAmt"),
        "ApplyCancelCommission": argv.get("--ApplyCancelCommission"),
        "MrchCode": argv.get("--MrchCode"),
        "Remark": argv.get("--Remark"),
        "ReservedMsgOne": argv.get("--ReservedMsgOne"),
        "ReservedMsgTwo": argv.get("--ReservedMsgTwo"),
        "ReservedMsgThree": argv.get("--ReservedMsgThree"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RevokeMemberRechargeThirdPayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RevokeMemberRechargeThirdPay(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRefund(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("Refund", g_param[OptionsDefine.Version])
        return

    param = {
        "UserId": argv.get("--UserId"),
        "RefundId": argv.get("--RefundId"),
        "MidasAppId": argv.get("--MidasAppId"),
        "TotalRefundAmt": Utils.try_to_json(argv, "--TotalRefundAmt"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),
        "OutTradeNo": argv.get("--OutTradeNo"),
        "MchRefundAmt": Utils.try_to_json(argv, "--MchRefundAmt"),
        "TransactionId": argv.get("--TransactionId"),
        "PlatformRefundAmt": Utils.try_to_json(argv, "--PlatformRefundAmt"),
        "SubOrderRefundList": Utils.try_to_json(argv, "--SubOrderRefundList"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RefundRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.Refund(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQuerySmallAmountTransfer(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QuerySmallAmountTransfer", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "OldTranSeqNo": argv.get("--OldTranSeqNo"),
        "TranDate": argv.get("--TranDate"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QuerySmallAmountTransferRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QuerySmallAmountTransfer(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRechargeMemberThirdPay(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RechargeMemberThirdPay", g_param[OptionsDefine.Version])
        return

    param = {
        "TranNetMemberCode": argv.get("--TranNetMemberCode"),
        "MemberFillAmt": argv.get("--MemberFillAmt"),
        "Commission": argv.get("--Commission"),
        "Ccy": argv.get("--Ccy"),
        "PayChannelType": argv.get("--PayChannelType"),
        "PayChannelAssignMerNo": argv.get("--PayChannelAssignMerNo"),
        "PayChannelTranSeqNo": argv.get("--PayChannelTranSeqNo"),
        "EjzbOrderNo": argv.get("--EjzbOrderNo"),
        "MrchCode": argv.get("--MrchCode"),
        "EjzbOrderContent": argv.get("--EjzbOrderContent"),
        "Remark": argv.get("--Remark"),
        "ReservedMsgOne": argv.get("--ReservedMsgOne"),
        "ReservedMsgTwo": argv.get("--ReservedMsgTwo"),
        "ReservedMsgThree": argv.get("--ReservedMsgThree"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RechargeMemberThirdPayRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RechargeMemberThirdPay(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryInvoice(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryInvoice", g_param[OptionsDefine.Version])
        return

    param = {
        "InvoicePlatformId": Utils.try_to_json(argv, "--InvoicePlatformId"),
        "OrderId": argv.get("--OrderId"),
        "OrderSn": argv.get("--OrderSn"),
        "IsRed": Utils.try_to_json(argv, "--IsRed"),
        "Profile": argv.get("--Profile"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryInvoiceRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryInvoice(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateMerchant(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateMerchant", g_param[OptionsDefine.Version])
        return

    param = {
        "InvoicePlatformId": Utils.try_to_json(argv, "--InvoicePlatformId"),
        "TaxpayerName": argv.get("--TaxpayerName"),
        "TaxpayerNum": argv.get("--TaxpayerNum"),
        "LegalPersonName": argv.get("--LegalPersonName"),
        "ContactsName": argv.get("--ContactsName"),
        "Phone": argv.get("--Phone"),
        "Address": argv.get("--Address"),
        "RegionCode": Utils.try_to_json(argv, "--RegionCode"),
        "CityName": argv.get("--CityName"),
        "Drawer": argv.get("--Drawer"),
        "TaxRegistrationCertificate": argv.get("--TaxRegistrationCertificate"),
        "Email": argv.get("--Email"),
        "BusinessMobile": argv.get("--BusinessMobile"),
        "BankName": argv.get("--BankName"),
        "BankAccount": argv.get("--BankAccount"),
        "Reviewer": argv.get("--Reviewer"),
        "Payee": argv.get("--Payee"),
        "RegisterCode": argv.get("--RegisterCode"),
        "State": argv.get("--State"),
        "CallbackUrl": argv.get("--CallbackUrl"),
        "Profile": argv.get("--Profile"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateMerchantRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateMerchant(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAcct(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateAcct", g_param[OptionsDefine.Version])
        return

    param = {
        "MidasAppId": argv.get("--MidasAppId"),
        "SubMchId": argv.get("--SubMchId"),
        "SubMchName": argv.get("--SubMchName"),
        "Address": argv.get("--Address"),
        "Contact": argv.get("--Contact"),
        "Mobile": argv.get("--Mobile"),
        "Email": argv.get("--Email"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),
        "SubMchType": argv.get("--SubMchType"),
        "ShortName": argv.get("--ShortName"),
        "SubMerchantMemberType": argv.get("--SubMerchantMemberType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAcctRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateAcct(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doUnifiedOrder(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("UnifiedOrder", g_param[OptionsDefine.Version])
        return

    param = {
        "CurrencyType": argv.get("--CurrencyType"),
        "MidasAppId": argv.get("--MidasAppId"),
        "OutTradeNo": argv.get("--OutTradeNo"),
        "ProductDetail": argv.get("--ProductDetail"),
        "ProductId": argv.get("--ProductId"),
        "ProductName": argv.get("--ProductName"),
        "TotalAmt": Utils.try_to_json(argv, "--TotalAmt"),
        "UserId": argv.get("--UserId"),
        "RealChannel": argv.get("--RealChannel"),
        "OriginalAmt": Utils.try_to_json(argv, "--OriginalAmt"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),
        "CallbackUrl": argv.get("--CallbackUrl"),
        "Channel": argv.get("--Channel"),
        "Metadata": argv.get("--Metadata"),
        "Quantity": Utils.try_to_json(argv, "--Quantity"),
        "SubAppId": argv.get("--SubAppId"),
        "SubOrderList": Utils.try_to_json(argv, "--SubOrderList"),
        "TotalMchIncome": Utils.try_to_json(argv, "--TotalMchIncome"),
        "TotalPlatformIncome": Utils.try_to_json(argv, "--TotalPlatformIncome"),
        "WxOpenId": argv.get("--WxOpenId"),
        "WxSubOpenId": argv.get("--WxSubOpenId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.UnifiedOrderRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.UnifiedOrder(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRevRegisterBillSupportWithdraw(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RevRegisterBillSupportWithdraw", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "TranNetMemberCode": argv.get("--TranNetMemberCode"),
        "OldOrderNo": argv.get("--OldOrderNo"),
        "CancelAmt": argv.get("--CancelAmt"),
        "TranFee": argv.get("--TranFee"),
        "Remark": argv.get("--Remark"),
        "ReservedMsgOne": argv.get("--ReservedMsgOne"),
        "ReservedMsgTwo": argv.get("--ReservedMsgTwo"),
        "ReservedMsgThree": argv.get("--ReservedMsgThree"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RevRegisterBillSupportWithdrawRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RevRegisterBillSupportWithdraw(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryInvoiceForManagement(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryInvoiceForManagement", g_param[OptionsDefine.Version])
        return

    param = {
        "InvoicePlatformId": Utils.try_to_json(argv, "--InvoicePlatformId"),
        "InvoiceStatus": Utils.try_to_json(argv, "--InvoiceStatus"),
        "RedInvoiceStatus": Utils.try_to_json(argv, "--RedInvoiceStatus"),
        "BeginTime": argv.get("--BeginTime"),
        "EndTime": argv.get("--EndTime"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "OrderId": argv.get("--OrderId"),
        "InvoiceId": argv.get("--InvoiceId"),
        "OrderSn": argv.get("--OrderSn"),
        "InvoiceSn": argv.get("--InvoiceSn"),
        "InvoiceCode": argv.get("--InvoiceCode"),
        "Profile": argv.get("--Profile"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryInvoiceForManagementRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryInvoiceForManagement(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryBankWithdrawCashDetails(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryBankWithdrawCashDetails", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "FunctionFlag": argv.get("--FunctionFlag"),
        "SubAcctNo": argv.get("--SubAcctNo"),
        "QueryFlag": argv.get("--QueryFlag"),
        "PageNum": argv.get("--PageNum"),
        "BeginDate": argv.get("--BeginDate"),
        "EndDate": argv.get("--EndDate"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryBankWithdrawCashDetailsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryBankWithdrawCashDetails(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryReconciliationDocument(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryReconciliationDocument", g_param[OptionsDefine.Version])
        return

    param = {
        "MrchCode": argv.get("--MrchCode"),
        "FileType": argv.get("--FileType"),
        "FileDate": argv.get("--FileDate"),
        "ReservedMsg": argv.get("--ReservedMsg"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryReconciliationDocumentRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryReconciliationDocument(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCheckAcct(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CheckAcct", g_param[OptionsDefine.Version])
        return

    param = {
        "MidasAppId": argv.get("--MidasAppId"),
        "SubAppId": argv.get("--SubAppId"),
        "BindType": Utils.try_to_json(argv, "--BindType"),
        "SettleAcctNo": argv.get("--SettleAcctNo"),
        "MidasSecretId": argv.get("--MidasSecretId"),
        "MidasSignature": argv.get("--MidasSignature"),
        "CheckCode": argv.get("--CheckCode"),
        "CurrencyType": argv.get("--CurrencyType"),
        "CurrencyUnit": Utils.try_to_json(argv, "--CurrencyUnit"),
        "CurrencyAmt": argv.get("--CurrencyAmt"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.CpdpClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CheckAcctRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CheckAcct(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20190820": cpdp_client_v20190820,

}

MODELS_MAP = {
    "v20190820": models_v20190820,

}

ACTION_MAP = {
    "BindAcct": doBindAcct,
    "BindRelateAcctSmallAmount": doBindRelateAcctSmallAmount,
    "ApplyWithdrawal": doApplyWithdrawal,
    "WithdrawCashMembership": doWithdrawCashMembership,
    "ModifyMntMbrBindRelateAcctBankCode": doModifyMntMbrBindRelateAcctBankCode,
    "QueryMemberBind": doQueryMemberBind,
    "CreateCustAcctId": doCreateCustAcctId,
    "CloseOrder": doCloseOrder,
    "QueryMerchantInfoForManagement": doQueryMerchantInfoForManagement,
    "ReviseMbrProperty": doReviseMbrProperty,
    "QueryBalance": doQueryBalance,
    "BindRelateAcctUnionPay": doBindRelateAcctUnionPay,
    "UnbindRelateAcct": doUnbindRelateAcct,
    "QueryBankTransactionDetails": doQueryBankTransactionDetails,
    "QueryMemberTransaction": doQueryMemberTransaction,
    "QueryCommonTransferRecharge": doQueryCommonTransferRecharge,
    "DownloadBill": doDownloadBill,
    "QueryAcctBinding": doQueryAcctBinding,
    "QueryOrder": doQueryOrder,
    "CreateInvoice": doCreateInvoice,
    "QueryCustAcctIdBalance": doQueryCustAcctIdBalance,
    "QueryRefund": doQueryRefund,
    "RegisterBillSupportWithdraw": doRegisterBillSupportWithdraw,
    "QueryBankClear": doQueryBankClear,
    "QuerySingleTransactionStatus": doQuerySingleTransactionStatus,
    "UnBindAcct": doUnBindAcct,
    "BindRelateAccReUnionPay": doBindRelateAccReUnionPay,
    "CreateRedInvoice": doCreateRedInvoice,
    "CheckAmount": doCheckAmount,
    "RevResigterBillSupportWithdraw": doRevResigterBillSupportWithdraw,
    "RevokeMemberRechargeThirdPay": doRevokeMemberRechargeThirdPay,
    "Refund": doRefund,
    "QuerySmallAmountTransfer": doQuerySmallAmountTransfer,
    "RechargeMemberThirdPay": doRechargeMemberThirdPay,
    "QueryInvoice": doQueryInvoice,
    "CreateMerchant": doCreateMerchant,
    "CreateAcct": doCreateAcct,
    "UnifiedOrder": doUnifiedOrder,
    "RevRegisterBillSupportWithdraw": doRevRegisterBillSupportWithdraw,
    "QueryInvoiceForManagement": doQueryInvoiceForManagement,
    "QueryBankWithdrawCashDetails": doQueryBankWithdrawCashDetails,
    "QueryReconciliationDocument": doQueryReconciliationDocument,
    "CheckAcct": doCheckAcct,

}

AVAILABLE_VERSION_LIST = [
    v20190820.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20190820.version.replace('-', ''): {"help": v20190820_help.INFO,"desc": v20190820_help.DESC},

}


def cpdp_action(argv, arglist):
    if "help" in argv:
        versions = sorted(AVAILABLE_VERSIONS.keys())
        opt_v = "--" + OptionsDefine.Version
        version = versions[-1]
        if opt_v in argv:
            version = 'v' + argv[opt_v].replace('-', '')
        if version not in versions:
            print("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
            return
        action_str = ""
        docs = AVAILABLE_VERSIONS[version]["help"]
        desc = AVAILABLE_VERSIONS[version]["desc"]
        for action, info in docs.items():
            action_str += "        %s\n" % action
            action_str += Utils.split_str("        ", info["desc"], 120)
        helpstr = HelpTemplate.SERVICE % {"name": "cpdp", "desc": desc, "actions": action_str}
        print(helpstr)
    else:
        print(ErrorMsg.FEW_ARG)


def version_merge():
    help_merge = {}
    for v in AVAILABLE_VERSIONS:
        for action in AVAILABLE_VERSIONS[v]["help"]:
            if action not in help_merge:
                help_merge[action] = {}
            help_merge[action]["cb"] = ACTION_MAP[action]
            help_merge[action]["params"] = []
            for param in AVAILABLE_VERSIONS[v]["help"][action]["params"]:
                if param["name"] not in help_merge[action]["params"]:
                    help_merge[action]["params"].append(param["name"])
    return help_merge


def register_arg(command):
    cmd = NiceCommand("cpdp", cpdp_action)
    command.reg_cmd(cmd)
    cmd.reg_opt("help", "bool")
    cmd.reg_opt(OptionsDefine.Version, "string")
    help_merge = version_merge()

    for actionName, action in help_merge.items():
        c = NiceCommand(actionName, action["cb"])
        cmd.reg_cmd(c)
        c.reg_opt("help", "bool")
        for param in action["params"]:
            c.reg_opt("--" + param, "string")

        for opt in OptionsDefine.ACTION_GLOBAL_OPT:
            stropt = "--" + opt
            c.reg_opt(stropt, "string")


def parse_global_arg(argv):
    params = {}
    for opt in OptionsDefine.ACTION_GLOBAL_OPT:
        stropt = "--" + opt
        if stropt in argv:
            params[opt] = argv[stropt]
        else:
            params[opt] = None
    if params[OptionsDefine.Version]:
        params[OptionsDefine.Version] = "v" + params[OptionsDefine.Version].replace('-', '')

    config_handle = Configure()
    profile = config_handle.profile
    if ("--" + OptionsDefine.Profile) in argv:
        profile = argv[("--" + OptionsDefine.Profile)]

    is_conexist, conf_path = config_handle._profile_existed(profile + "." + config_handle.configure)
    is_creexist, cred_path = config_handle._profile_existed(profile + "." + config_handle.credential)
    config = {}
    cred = {}
    if is_conexist:
        config = config_handle._load_json_msg(conf_path)
    if is_creexist:
        cred = config_handle._load_json_msg(cred_path)
    if os.environ.get(OptionsDefine.ENV_SECRET_ID):
        cred[OptionsDefine.SecretId] = os.environ.get(OptionsDefine.ENV_SECRET_ID)
    if os.environ.get(OptionsDefine.ENV_SECRET_KEY):
        cred[OptionsDefine.SecretKey] = os.environ.get(OptionsDefine.ENV_SECRET_KEY)
    if os.environ.get(OptionsDefine.ENV_REGION):
        config[OptionsDefine.Region] = os.environ.get(OptionsDefine.ENV_REGION)

    for param in params.keys():
        if param == OptionsDefine.Version:
            continue
        if params[param] is None:
            if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId]:
                if param in cred:
                    params[param] = cred[param]
                else:
                    raise Exception("%s is invalid" % param)
            else:
                if param in config:
                    params[param] = config[param]
                elif param == OptionsDefine.Region:
                    raise Exception("%s is invalid" % OptionsDefine.Region)
    try:
        if params[OptionsDefine.Version] is None:
            version = config["cpdp"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["cpdp"][OptionsDefine.Endpoint]
    except Exception as err:
        raise Exception("config file:%s error, %s" % (conf_path, str(err)))
    versions = sorted(AVAILABLE_VERSIONS.keys())
    if params[OptionsDefine.Version] not in versions:
        raise Exception("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
    return params


def show_help(action, version):
    docs = AVAILABLE_VERSIONS[version]["help"][action]
    desc = AVAILABLE_VERSIONS[version]["desc"]
    docstr = ""
    for param in docs["params"]:
        docstr += "        %s\n" % ("--" + param["name"])
        docstr += Utils.split_str("        ", param["desc"], 120)

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "cpdp", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["cpdp"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
