# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import Datastore
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

from pyVmomi.vim.cluster import VsanAttachToSrOperation
from pyVmomi.vim.cluster import VsanClusterCreateVmHealthTestResult
from pyVmomi.vim.cluster import VsanClusterFileServiceHealthSummary
from pyVmomi.vim.cluster import VsanClusterHclInfo
from pyVmomi.vim.cluster import VsanClusterHealthCheckInfo
from pyVmomi.vim.cluster import VsanClusterHealthConfigs
from pyVmomi.vim.cluster import VsanClusterHealthQuerySpec
from pyVmomi.vim.cluster import VsanClusterHealthSummary
from pyVmomi.vim.cluster import VsanClusterHealthSystemVersionResult
from pyVmomi.vim.cluster import VsanClusterNetworkLoadTestResult
from pyVmomi.vim.cluster import VsanClusterNetworkPerfTaskSpec
from pyVmomi.vim.cluster import VsanClusterTelemetryProxyConfig
from pyVmomi.vim.cluster import VsanClusterVmdkLoadTestResult
from pyVmomi.vim.cluster import VsanHistoricalHealthQuerySpec
from pyVmomi.vim.cluster import VsanObjectExtAttrs
from pyVmomi.vim.cluster import VsanStorageWorkloadType

from pyVmomi.vim.host import VsanSmartStatsHostSummary
from pyVmomi.vim.host import VsanVmdkLoadTestSpec

from pyVmomi.vim.vsan import VsanDiskModelInfo
from pyVmomi.vim.vsan import VsanHclDiskConstraint
from pyVmomi.vim.vsan import VsanHclQuerySpec
from pyVmomi.vim.vsan import VsanHclReleaseConstraint
from pyVmomi.vim.vsan import VsanHwToVcgInfoMappingSpec

class VsanVcClusterHealthSystem(ManagedObject):
   class VsanHealthLogLevelEnum(Enum):
      INFO: ClassVar['VsanHealthLogLevelEnum'] = 'INFO'
      WARNING: ClassVar['VsanHealthLogLevelEnum'] = 'WARNING'
      ERROR: ClassVar['VsanHealthLogLevelEnum'] = 'ERROR'
      DEBUG: ClassVar['VsanHealthLogLevelEnum'] = 'DEBUG'
      CRITICAL: ClassVar['VsanHealthLogLevelEnum'] = 'CRITICAL'
      VsanHealthLogLevelEnum_Unknown: ClassVar['VsanHealthLogLevelEnum'] = 'VsanHealthLogLevelEnum_Unknown'

   def QueryVerifyClusterHealthSystemVersions(self, cluster: ClusterComputeResource) -> VsanClusterHealthSystemVersionResult: ...
   def QueryFileServiceHealthSummary(self, cluster: ClusterComputeResource) -> Optional[VsanClusterFileServiceHealthSummary]: ...
   def QueryClusterCreateVmHealthTest(self, cluster: ClusterComputeResource, timeout: int, datastore: Optional[Datastore]) -> VsanClusterCreateVmHealthTestResult: ...
   def QueryClusterHealthSummary(self, cluster: Optional[ClusterComputeResource], vmCreateTimeout: Optional[int], objUuids: list[str], includeObjUuids: Optional[bool], fields: list[str], fetchFromCache: Optional[bool], perspective: Optional[str], hosts: list[HostSystem], spec: Optional[VsanClusterHealthQuerySpec]) -> VsanClusterHealthSummary: ...
   def QueryClusterHealthSummaryTask(self, cluster: ClusterComputeResource, hosts: list[HostSystem], includeDataProtectionHealth: Optional[bool], includeOnlineHealth: Optional[bool]) -> Task: ...
   def QueryVsanObjExtAttrs(self, cluster: ClusterComputeResource, uuids: list[str]) -> list[VsanObjectExtAttrs]: ...
   def QueryAllSupportedHealthChecks(self) -> list[VsanClusterHealthCheckInfo]: ...
   def QueryClusterNetworkPerfTest(self, cluster: ClusterComputeResource, multicast: bool, durationSec: Optional[int]) -> VsanClusterNetworkLoadTestResult: ...
   def QueryClusterNetworkPerfTask(self, cluster: ClusterComputeResource, spec: Optional[VsanClusterNetworkPerfTaskSpec]) -> Task: ...
   def RunVmdkLoadTest(self, cluster: ClusterComputeResource, runname: str, durationSec: Optional[int], specs: list[VsanVmdkLoadTestSpec], action: Optional[str]) -> Task: ...
   def QueryVsanClusterHealthConfig(self, cluster: ClusterComputeResource) -> VsanClusterHealthConfigs: ...
   def QueryVsanClusterHealthCheckInterval(self, cluster: ClusterComputeResource) -> int: ...
   def SetVsanClusterHealthCheckInterval(self, cluster: ClusterComputeResource, vsanClusterHealthCheckInterval: int) -> NoReturn: ...
   def GetVsanClusterSilentChecks(self, cluster: ClusterComputeResource) -> list[str]: ...
   def SetVsanClusterSilentChecks(self, cluster: ClusterComputeResource, addSilentChecks: list[str], removeSilentChecks: list[str]) -> bool: ...
   def SetVsanClusterTelemetryConfig(self, cluster: ClusterComputeResource, vsanClusterHealthConfig: VsanClusterHealthConfigs) -> NoReturn: ...
   def TestVsanClusterTelemetryProxy(self, proxyConfig: VsanClusterTelemetryProxyConfig) -> bool: ...
   def SendVsanTelemetry(self, cluster: ClusterComputeResource) -> NoReturn: ...
   def RepairClusterObjectsImmediate(self, cluster: ClusterComputeResource, uuids: list[str]) -> Task: ...
   def UpdateDefaultDSPolicyRecommendation(self, cluster: ClusterComputeResource) -> Task: ...
   def QueryClusterCreateVmHealthHistoryTest(self, cluster: ClusterComputeResource, count: Optional[int], datastore: Optional[Datastore]) -> list[VsanClusterCreateVmHealthTestResult]: ...
   def QueryClusterNetworkPerfHistoryTest(self, cluster: ClusterComputeResource, count: Optional[int], spec: Optional[VsanClusterNetworkPerfTaskSpec]) -> list[VsanClusterNetworkLoadTestResult]: ...
   def QueryClusterVmdkLoadHistoryTest(self, cluster: ClusterComputeResource, count: Optional[int], taskId: Optional[str]) -> list[VsanClusterVmdkLoadTestResult]: ...
   def QueryClusterVmdkWorkloadTypes(self) -> list[VsanStorageWorkloadType]: ...
   def QueryAttachToSrHistory(self, cluster: ClusterComputeResource, count: Optional[int], taskId: Optional[str]) -> list[VsanAttachToSrOperation]: ...
   def AttachVsanSupportBundleToSr(self, cluster: ClusterComputeResource, srNumber: str) -> Task: ...
   def GetClusterHclInfo(self, cluster: Optional[ClusterComputeResource], includeHostsResult: Optional[bool], includeVendorInfo: Optional[bool], esxRelease: Optional[str], querySpec: Optional[VsanHclQuerySpec]) -> VsanClusterHclInfo: ...
   def GetHclInfoForVsanEligibleDisks(self, querySpec: VsanHclQuerySpec) -> VsanClusterHclInfo: ...
   def DownloadHclFile(self, sha1sums: list[str]) -> Task: ...
   def GetClusterHclConstraints(self, cluster: ClusterComputeResource, release: str) -> VsanHclReleaseConstraint: ...
   def GetDiskHclConstraints(self, release: Optional[str], diskModels: list[VsanDiskModelInfo]) -> list[VsanHclDiskConstraint]: ...
   def GetClusterReleaseRecommendation(self, cluster: ClusterComputeResource, minor: list[str], major: list[str]) -> list[VsanHclReleaseConstraint]: ...
   def PurgeHclFiles(self, sha1sums: list[str]) -> NoReturn: ...
   def DownloadAndInstallVendorTool(self, cluster: ClusterComputeResource) -> Task: ...
   def UploadHclDb(self, db: str) -> bool: ...
   def UpdateHclDbFromWeb(self, url: Optional[str]) -> bool: ...
   def RebalanceCluster(self, cluster: ClusterComputeResource, targetHosts: list[HostSystem]) -> Task: ...
   def StopRebalanceCluster(self, cluster: ClusterComputeResource, targetHosts: list[HostSystem]) -> Task: ...
   def IsRebalanceRunning(self, cluster: ClusterComputeResource, targetHosts: list[HostSystem]) -> bool: ...
   def SetLogLevel(self, level: Optional[str]) -> NoReturn: ...
   def QuerySmartStatsSummary(self, cluster: ClusterComputeResource) -> list[VsanSmartStatsHostSummary]: ...
   def QueryVsanProxyConfig(self) -> VsanClusterTelemetryProxyConfig: ...
   def QueryClusterHistoricalHealth(self, spec: VsanHistoricalHealthQuerySpec) -> list[VsanClusterHealthSummary]: ...
   def SetVsanVcgMappingForHwDevices(self, spec: VsanHwToVcgInfoMappingSpec) -> bool: ...