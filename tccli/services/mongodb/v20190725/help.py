# -*- coding: utf-8 -*-
DESC = "mongodb-2019-07-25"
INFO = {
  "AssignProject": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID"
      }
    ],
    "desc": "本接口(AssignProject)用于指定云数据库实例的所属项目。\n"
  },
  "ModifyDBInstanceSpec": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      },
      {
        "name": "Memory",
        "desc": "实例配置变更后的内存大小，单位：GB。内存和磁盘必须同时升配或同时降配"
      },
      {
        "name": "Volume",
        "desc": "实例配置变更后的硬盘大小，单位：GB。内存和磁盘必须同时升配或同时降配。降配时，新的磁盘参数必须大于已用磁盘容量的1.2倍"
      },
      {
        "name": "OplogSize",
        "desc": "实例配置变更后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%"
      }
    ],
    "desc": "本接口(ModifyDBInstanceSpec)用于调整MongoDB云数据库实例配置。接口支持的售卖规格，可从查询云数据库的售卖规格（DescribeSpecInfo）获取。"
  },
  "OfflineIsolatedDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      }
    ],
    "desc": "本接口(OfflineIsolatedInstances)用于立即下线隔离状态的云数据库实例。进行操作的实例状态必须为隔离状态。"
  },
  "CreateDBInstance": {
    "params": [
      {
        "name": "NodeNum",
        "desc": "每个副本集内节点个数，当前副本集节点数固定为3，分片从节点数可选，具体参照查询云数据库的售卖规格返回参数"
      },
      {
        "name": "Memory",
        "desc": "实例内存大小，单位：GB"
      },
      {
        "name": "Volume",
        "desc": "实例硬盘大小，单位：GB"
      },
      {
        "name": "MongoVersion",
        "desc": "版本号，具体支持的售卖版本请参照查询云数据库的售卖规格（DescribeSpecInfo）返回结果。参数与版本对应关系是MONGO_3_WT：MongoDB 3.2 WiredTiger存储引擎版本，MONGO_3_ROCKS：MongoDB 3.2 RocksDB存储引擎版本，MONGO_36_WT：MongoDB 3.6 WiredTiger存储引擎版本"
      },
      {
        "name": "GoodsNum",
        "desc": "实例数量, 最小值1，最大值为10"
      },
      {
        "name": "Zone",
        "desc": "实例所属区域名称，格式如：ap-guangzhou-2"
      },
      {
        "name": "Period",
        "desc": "实例时长，单位：月，可选值包括 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]"
      },
      {
        "name": "MachineCode",
        "desc": "机器类型，HIO：高IO型；HIO10G：高IO万兆型"
      },
      {
        "name": "ClusterType",
        "desc": "实例类型，REPLSET-副本集，SHARD-分片集群"
      },
      {
        "name": "ReplicateSetNum",
        "desc": "副本集个数，创建副本集实例时，该参数必须设置为1；创建分片实例时，具体参照查询云数据库的售卖规格返回参数"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，不设置为默认项目"
      },
      {
        "name": "VpcId",
        "desc": "私有网络 ID，如果不传则默认选择基础网络，请使用 查询私有网络列表"
      },
      {
        "name": "SubnetId",
        "desc": "私有网络下的子网 ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用 查询子网列表"
      },
      {
        "name": "Password",
        "desc": "实例密码，不设置该参数则需要在创建完成后通过设置密码接口初始化实例密码。密码必须是8-16位字符，且至少包含字母、数字和字符 !@#%^*() 中的两种"
      },
      {
        "name": "Tags",
        "desc": "实例标签信息"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "自动续费标记，可选值为：0 - 不自动续费；1 - 自动续费。默认为不自动续费"
      }
    ],
    "desc": "本接口(CreateDBInstance)用于创建包年包月的MongoDB云数据库实例。接口支持的售卖规格，可从查询云数据库的售卖规格（DescribeSpecInfo）获取。"
  },
  "DescribeClientConnections": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      }
    ],
    "desc": "本接口(DescribeClientConnections)用于查询实例客户端连接信息，包括连接IP和连接数量。目前只支持3.2版本的MongoDB实例。"
  },
  "CreateDBInstanceHour": {
    "params": [
      {
        "name": "Memory",
        "desc": "实例内存大小，单位：GB"
      },
      {
        "name": "Volume",
        "desc": "实例硬盘大小，单位：GB"
      },
      {
        "name": "ReplicateSetNum",
        "desc": "副本集个数，创建副本集实例时，该参数必须设置为1；创建分片实例时，具体参照查询云数据库的售卖规格返回参数"
      },
      {
        "name": "NodeNum",
        "desc": "每个副本集内节点个数，当前副本集节点数固定为3，分片从节点数可选，具体参照查询云数据库的售卖规格返回参数"
      },
      {
        "name": "MongoVersion",
        "desc": "版本号，具体支持的售卖版本请参照查询云数据库的售卖规格（DescribeSpecInfo）返回结果。参数与版本对应关系是MONGO_3_WT：MongoDB 3.2 WiredTiger存储引擎版本，MONGO_3_ROCKS：MongoDB 3.2 RocksDB存储引擎版本，MONGO_36_WT：MongoDB 3.6 WiredTiger存储引擎版本"
      },
      {
        "name": "MachineCode",
        "desc": "机器类型，HIO：高IO型；HIO10G：高IO万兆"
      },
      {
        "name": "GoodsNum",
        "desc": "实例数量，最小值1，最大值为10"
      },
      {
        "name": "Zone",
        "desc": "可用区信息，格式如：ap-guangzhou-2"
      },
      {
        "name": "ClusterType",
        "desc": "实例类型，REPLSET-副本集，SHARD-分片集群"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID，如果不设置该参数则默认选择基础网络"
      },
      {
        "name": "SubnetId",
        "desc": "私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填"
      },
      {
        "name": "Password",
        "desc": "实例密码，不设置该参数则需要在创建完成后通过设置密码接口初始化实例密码。密码必须是8-16位字符，且至少包含字母、数字和字符 !@#%^*() 中的两种"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，不设置为默认项目"
      },
      {
        "name": "Tags",
        "desc": "实例标签信息"
      }
    ],
    "desc": "本接口(CreateDBInstanceHour)用于创建按量计费的MongoDB云数据库实例。"
  },
  "RenameInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      },
      {
        "name": "NewName",
        "desc": "实例名称"
      }
    ],
    "desc": "本接口(RenameInstance)用于修改云数据库实例的名称。"
  },
  "DescribeSpecInfo": {
    "params": [
      {
        "name": "Zone",
        "desc": "待查询可用区"
      }
    ],
    "desc": "本接口(DescribeSpecInfo)用于查询实例的售卖规格。"
  },
  "DescribeDBBackups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      }
    ],
    "desc": "本接口（DescribeDBBackups）用于查询实例备份列表，目前只支持7天内的备份查询。"
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      },
      {
        "name": "InstanceType",
        "desc": "实例类型，取值范围：0-所有实例,1-正式实例，2-临时实例, 3-只读实例，-1-正式实例+只读+灾备实例"
      },
      {
        "name": "ClusterType",
        "desc": "集群类型，取值范围：0-副本集实例，1-分片实例，-1-所有实例"
      },
      {
        "name": "Status",
        "desc": "实例状态，取值范围：0-待初始化，1-流程执行中，2-实例有效，-2-实例已过期"
      },
      {
        "name": "VpcId",
        "desc": "私有网络的ID，基础网络则不传该参数"
      },
      {
        "name": "SubnetId",
        "desc": "私有网络的子网ID，基础网络则不传该参数。入参设置该参数的同时，必须设置相应的VpcId"
      },
      {
        "name": "PayMode",
        "desc": "付费类型，取值范围：0-按量计费，1-包年包月，-1-按量计费+包年包月"
      },
      {
        "name": "Limit",
        "desc": "单次请求返回的数量，最小值为1，最大值为100，默认值为20"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认值为0"
      },
      {
        "name": "OrderBy",
        "desc": "返回结果集排序的字段，目前支持：\"ProjectId\", \"InstanceName\", \"CreateTime\"，默认为升序排序"
      },
      {
        "name": "OrderByType",
        "desc": "返回结果集排序方式，目前支持：\"ASC\"或者\"DESC\""
      },
      {
        "name": "ProjectIds",
        "desc": "项目 ID"
      },
      {
        "name": "SearchKey",
        "desc": "搜索关键词，支持实例Id、实例名称、完整IP"
      }
    ],
    "desc": "本接口(DescribeDBInstances)用于查询云数据库实例列表，支持通过项目ID、实例ID、实例状态等过滤条件来筛选实例。支持查询主实例、灾备实例和只读实例信息列表。"
  },
  "IsolateDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      }
    ],
    "desc": "本接口(IsolateDBInstance)用于隔离MongoDB云数据库按量计费实例。隔离后实例保留在回收站中，不能再写入数据。隔离一定时间后，实例会彻底删除，回收站保存时间请参考按量计费的服务条款。在隔离中的按量计费实例无法恢复，请谨慎操作。"
  },
  "DescribeBackupAccess": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同"
      },
      {
        "name": "BackupName",
        "desc": "需要获取下载授权的备份文件名"
      }
    ],
    "desc": "本接口（DescribeBackupAccess）用于获取备份文件的下载授权，具体的备份文件信息可通过查询实例备份列表（DescribeDBBackups）接口获取"
  }
}