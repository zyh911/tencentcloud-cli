# -*- coding: utf-8 -*-
DESC = "monitor-2018-07-24"
INFO = {
  "DescribeProductEventList": {
    "params": [
      {
        "name": "Module",
        "desc": "接口模块名，固定值\"monitor\""
      },
      {
        "name": "ProductName",
        "desc": "产品类型过滤，比如\"cvm\"表示云服务器"
      },
      {
        "name": "EventName",
        "desc": "事件名称过滤，比如\"guest_reboot\"表示机器重启"
      },
      {
        "name": "InstanceId",
        "desc": "影响对象，比如ins-19708ino"
      },
      {
        "name": "Dimensions",
        "desc": "维度过滤，比如外网IP:10.0.0.1"
      },
      {
        "name": "RegionList",
        "desc": "地域过滤，比如gz"
      },
      {
        "name": "Type",
        "desc": "事件类型过滤，取值范围[\"status_change\",\"abnormal\"]，分别表示状态变更、异常事件"
      },
      {
        "name": "Status",
        "desc": "事件状态过滤，取值范围[\"recover\",\"alarm\",\"-\"]，分别表示已恢复、未恢复、无状态"
      },
      {
        "name": "Project",
        "desc": "项目ID过滤"
      },
      {
        "name": "IsAlarmConfig",
        "desc": "告警状态配置过滤，1表示已配置，0表示未配置"
      },
      {
        "name": "TimeOrder",
        "desc": "按更新时间排序，ASC表示升序，DESC表示降序，默认DESC"
      },
      {
        "name": "StartTime",
        "desc": "起始时间，默认一天前的时间戳"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，默认当前时间戳"
      },
      {
        "name": "Offset",
        "desc": "页偏移量，默认0"
      },
      {
        "name": "Limit",
        "desc": "每页返回的数量，默认20"
      }
    ],
    "desc": "分页获取产品事件的列表"
  },
  "DescribeAccidentEventList": {
    "params": [
      {
        "name": "Module",
        "desc": "接口模块名，当前接口取值monitor"
      },
      {
        "name": "StartTime",
        "desc": "起始时间，默认一天前的时间戳"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，默认当前时间戳"
      },
      {
        "name": "Limit",
        "desc": "分页参数，每页返回的数量，取值1~100，默认20"
      },
      {
        "name": "Offset",
        "desc": "分页参数，页偏移量，从0开始计数，默认0"
      },
      {
        "name": "UpdateTimeOrder",
        "desc": "根据UpdateTime排序的规则，取值asc或desc"
      },
      {
        "name": "OccurTimeOrder",
        "desc": "根据OccurTime排序的规则，取值asc或desc（优先根据UpdateTimeOrder排序）"
      },
      {
        "name": "AccidentType",
        "desc": "根据事件类型过滤，1表示服务问题，2表示其他订阅"
      },
      {
        "name": "AccidentEvent",
        "desc": "根据事件过滤，1表示云服务器存储问题，2表示云服务器网络连接问题，3表示云服务器运行异常，202表示运营商网络抖动"
      },
      {
        "name": "AccidentStatus",
        "desc": "根据事件状态过滤，0表示已恢复，1表示未恢复"
      },
      {
        "name": "AccidentRegion",
        "desc": "根据事件地域过滤，gz表示广州，sh表示上海等"
      },
      {
        "name": "AffectResource",
        "desc": "根据影响资源过滤，比如ins-19a06bka"
      }
    ],
    "desc": "获取平台事件列表"
  },
  "UnBindingPolicyObject": {
    "params": [
      {
        "name": "Module",
        "desc": "固定值，为\"monitor\""
      },
      {
        "name": "GroupId",
        "desc": "策略组id"
      },
      {
        "name": "UniqueId",
        "desc": "待删除对象实例的唯一id列表"
      },
      {
        "name": "InstanceGroupId",
        "desc": "实例分组id, 如果按实例分组删除的话UniqueId参数是无效的"
      }
    ],
    "desc": "删除策略的关联对象"
  },
  "BindingPolicyObject": {
    "params": [
      {
        "name": "GroupId",
        "desc": "策略分组Id"
      },
      {
        "name": "Module",
        "desc": "必填。固定值\"monitor\""
      },
      {
        "name": "InstanceGroupId",
        "desc": "实例分组ID"
      },
      {
        "name": "Dimensions",
        "desc": "需要绑定的对象维度信息"
      }
    ],
    "desc": "将告警策略绑定到特定对象"
  },
  "ModifyAlarmReceivers": {
    "params": [
      {
        "name": "GroupId",
        "desc": "需要修改接收人的策略组Id"
      },
      {
        "name": "Module",
        "desc": "必填。固定为“monitor”"
      },
      {
        "name": "ReceiverInfos",
        "desc": "新接收人信息, 没有填写则删除所有接收人"
      }
    ],
    "desc": "修改告警接收人"
  },
  "DescribeBindingPolicyObjectList": {
    "params": [
      {
        "name": "Module",
        "desc": "固定值，为\"monitor\""
      },
      {
        "name": "GroupId",
        "desc": "策略组id"
      },
      {
        "name": "Limit",
        "desc": "分页参数，每页返回的数量，取值1~100，默认20"
      },
      {
        "name": "Offset",
        "desc": "分页参数，页偏移量，从0开始计数，默认0"
      },
      {
        "name": "Dimensions",
        "desc": "筛选对象的维度信息"
      }
    ],
    "desc": "获取已绑定对象列表"
  },
  "SendCustomAlarmMsg": {
    "params": [
      {
        "name": "Module",
        "desc": "接口模块名，当前取值monitor"
      },
      {
        "name": "PolicyId",
        "desc": "消息策略ID，在云监控自定义消息页面配置"
      },
      {
        "name": "Msg",
        "desc": "用户想要发送的自定义消息内容"
      }
    ],
    "desc": "发送自定义消息告警"
  },
  "DeletePolicyGroup": {
    "params": [
      {
        "name": "Module",
        "desc": "固定值，为\"monitor\""
      },
      {
        "name": "GroupId",
        "desc": "策略组id"
      }
    ],
    "desc": "删除告警策略组"
  },
  "DescribeBaseMetrics": {
    "params": [
      {
        "name": "Namespace",
        "desc": "业务命名空间"
      },
      {
        "name": "MetricName",
        "desc": "指标名"
      }
    ],
    "desc": "获取基础指标详情"
  },
  "DescribePolicyGroupInfo": {
    "params": [
      {
        "name": "Module",
        "desc": "固定值，为\"monitor\""
      },
      {
        "name": "GroupId",
        "desc": "策略组id"
      }
    ],
    "desc": "获取基础策略组详情"
  },
  "DescribePolicyGroupList": {
    "params": [
      {
        "name": "Module",
        "desc": "固定值，为\"monitor\""
      },
      {
        "name": "Limit",
        "desc": "分页参数，每页返回的数量，取值1~100"
      },
      {
        "name": "Offset",
        "desc": "分页参数，页偏移量，从0开始计数"
      },
      {
        "name": "Like",
        "desc": "按策略名搜索"
      },
      {
        "name": "InstanceGroupId",
        "desc": "实例分组id"
      },
      {
        "name": "UpdateTimeOrder",
        "desc": "按更新时间排序, asc 或者 desc"
      },
      {
        "name": "ProjectIds",
        "desc": "项目id列表"
      },
      {
        "name": "ViewNames",
        "desc": "告警策略类型列表"
      },
      {
        "name": "FilterUnuseReceiver",
        "desc": "是否过滤无接收人策略组, 1表示过滤, 0表示不过滤"
      },
      {
        "name": "Receivers",
        "desc": "过滤条件, 接收组列表"
      },
      {
        "name": "ReceiverUserList",
        "desc": "过滤条件, 接收人列表"
      },
      {
        "name": "Dimensions",
        "desc": "维度组合字段(json字符串), 例如[[{\"name\":\"unInstanceId\",\"value\":\"ins-6e4b2aaa\"}]]"
      },
      {
        "name": "ConditionTempGroupId",
        "desc": "模板策略组id, 多个id用逗号分隔"
      },
      {
        "name": "ReceiverType",
        "desc": "过滤条件, 接收人或者接收组, user表示接收人, group表示接收组"
      }
    ],
    "desc": "获取基础策略告警组列表"
  },
  "DescribeBasicAlarmList": {
    "params": [
      {
        "name": "Module",
        "desc": "接口模块名，当前取值monitor"
      },
      {
        "name": "StartTime",
        "desc": "起始时间，默认一天前的时间戳"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，默认当前时间戳"
      },
      {
        "name": "Limit",
        "desc": "分页参数，每页返回的数量，取值1~100，默认20"
      },
      {
        "name": "Offset",
        "desc": "分页参数，页偏移量，从0开始计数，默认0"
      },
      {
        "name": "OccurTimeOrder",
        "desc": "根据发生时间排序，取值ASC或DESC"
      },
      {
        "name": "ProjectIds",
        "desc": "根据项目ID过滤"
      },
      {
        "name": "ViewNames",
        "desc": "根据策略类型过滤"
      },
      {
        "name": "AlarmStatus",
        "desc": "根据告警状态过滤"
      },
      {
        "name": "ObjLike",
        "desc": "根据告警对象过滤"
      },
      {
        "name": "InstanceGroupIds",
        "desc": "根据实例组ID过滤"
      }
    ],
    "desc": "获取基础告警列表"
  },
  "GetMonitorData": {
    "params": [
      {
        "name": "Namespace",
        "desc": "命名空间，每个云产品会有一个命名空间"
      },
      {
        "name": "MetricName",
        "desc": "指标名称，各个云产品的详细指标说明请参阅各个产品[监控接口](https://cloud.tencent.com/document/product/248/30384)文档"
      },
      {
        "name": "Instances",
        "desc": "实例对象的维度组合"
      },
      {
        "name": "Period",
        "desc": "监控统计周期。默认为取值为300，单位为s"
      },
      {
        "name": "StartTime",
        "desc": "起始时间，如2018-09-22T19:51:23+08:00"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，默认为当前时间。 EndTime不能小于StartTime"
      }
    ],
    "desc": "获取云产品的监控数据。传入产品的命名空间、对象维度描述和监控指标即可获得相应的监控数据。\n接口调用频率限制为：20次/秒，1200次/分钟。\n若您需要调用的指标、对象较多，可能存在因限频出现拉取失败的情况，建议尽量将请求按时间维度均摊。"
  },
  "PutMonitorData": {
    "params": [
      {
        "name": "Metrics",
        "desc": "一组指标和数据"
      },
      {
        "name": "AnnounceIp",
        "desc": "上报时自行指定的 IP"
      },
      {
        "name": "AnnounceTimestamp",
        "desc": "上报时自行指定的时间戳"
      },
      {
        "name": "AnnounceInstance",
        "desc": "上报时自行指定的 IP 或 产品实例ID"
      }
    ],
    "desc": "默认接口请求频率限制：50次/秒。\n默认单租户指标上限：100个。\n单次上报最多 30 个指标/值对，请求返回错误时，请求中所有的指标/值均不会被保存。\n\n上报的时间戳为期望保存的时间戳，建议构造整数分钟时刻的时间戳。\n时间戳时间范围必须为当前时间到 300 秒前之间。\n同一 IP 指标对的数据需按分钟先后顺序上报。"
  },
  "CreatePolicyGroup": {
    "params": [
      {
        "name": "GroupName",
        "desc": "组策略名称"
      },
      {
        "name": "Module",
        "desc": "固定值，为\"monitor\""
      },
      {
        "name": "ViewName",
        "desc": "策略组所属视图的名称，若通过模版创建，可不传入"
      },
      {
        "name": "ProjectId",
        "desc": "策略组所属项目Id，会进行鉴权操作"
      },
      {
        "name": "ConditionTempGroupId",
        "desc": "模版策略组Id, 通过模版创建时才需要传"
      },
      {
        "name": "IsShielded",
        "desc": "是否屏蔽策略组，0表示不屏蔽，1表示屏蔽。不填默认为0"
      },
      {
        "name": "Remark",
        "desc": "策略组的备注信息"
      },
      {
        "name": "InsertTime",
        "desc": "插入时间，戳格式为Unix时间戳，不填则按后台处理时间填充"
      },
      {
        "name": "Conditions",
        "desc": "策略组中的阈值告警规则"
      },
      {
        "name": "EventConditions",
        "desc": "策略组中的时间告警规则"
      },
      {
        "name": "BackEndCall",
        "desc": "是否为后端调用。当且仅当值为1时，后台拉取策略模版中的规则填充入Conditions以及EventConditions字段"
      },
      {
        "name": "IsUnionRule",
        "desc": "指标告警规则的且或关系，0表示或规则(满足任意规则就告警)，1表示且规则(满足所有规则才告警)"
      }
    ],
    "desc": "增加策略组"
  },
  "UnBindingAllPolicyObject": {
    "params": [
      {
        "name": "Module",
        "desc": "固定值，为\"monitor\""
      },
      {
        "name": "GroupId",
        "desc": "策略组id"
      }
    ],
    "desc": "删除全部的关联对象"
  },
  "DescribePolicyConditionList": {
    "params": [
      {
        "name": "Module",
        "desc": "固定值，为\"monitor\""
      }
    ],
    "desc": "获取基础告警策略条件"
  }
}