"""Utilities for Meraki SDK."""

import meraki


def _org_name_to_id(org_name):
    """Translate Org Name to Org Id."""
    return [org['id'] for org in get_meraki_orgs() if org['name'] == org_name][0]


def _switchname_to_serial(org_name, sw_name):
    """Translate Switch Name to Switch Serial."""
    return [sw['serial'] for sw in get_meraki_devices(org_name) if sw['name'] == sw_name][0]


def _netname_to_id(org_name, net_name):
    """Translate Network Name to Network ID."""
    return [net['id'] for net in get_meraki_networks_by_org(org_name) if net['name'] == net_name][0]


def get_meraki_orgs():
    """Query the Meraki Dashboard API for a list of defined organizations."""
    dashboard = meraki.DashboardAPI(suppress_logging=True)
    return dashboard.organizations.getOrganizations()


def get_meraki_org_admins(org_name):
    """Query the Meraki Dashboard API for the admins of a organization."""
    dashboard = meraki.DashboardAPI(suppress_logging=True)
    return dashboard.organizations.getOrganizationAdmins(_org_name_to_id(org_name))


def get_meraki_devices(org_name):
    """Query the Meraki Dashboard API for a list of devices in the given organization."""
    dashboard = meraki.DashboardAPI(suppress_logging=True)
    return dashboard.organizations.getOrganizationDevices(organizationId=_org_name_to_id(org_name))


def get_meraki_networks_by_org(org_name):
    """Query the Meraki Dashboard API for a list of Networks."""
    dashboard = meraki.DashboardAPI(suppress_logging=True)
    return dashboard.organizations.getOrganizationNetworks(_org_name_to_id(org_name))


def get_meraki_switchports(org_name, device_name):
    """Query the Meraki Dashboard API for a list of Networks."""
    dashboard = meraki.DashboardAPI(suppress_logging=True)
    return dashboard.switch.getDeviceSwitchPorts(_switchname_to_serial(org_name, device_name))


def get_meraki_firewall_performance(org_name, device_name):
    """Query Meraki with a firewall to return device performance."""
    dashboard = meraki.DashboardAPI(suppress_logging=True)
    return dashboard.appliance.getDeviceAppliancePerformance(_switchname_to_serial(org_name, device_name))


def get_meraki_network_ssids(org_name, net_name):
    """Query Meraki for a Networks SSIDs."""
    dashboard = meraki.DashboardAPI(suppress_logging=True)
    return dashboard.wireless.getNetworkWirelessSsids(_netname_to_id(org_name, net_name))


def get_meraki_camera_recent(org_name, device_name):
    """Query Meraki Recent Cameras"""
    dashboard = meraki.DashboardAPI(suppress_logging=True)
    return dashboard.camera.getDeviceCameraAnalyticsRecent(_switchname_to_serial(org_name, device_name))
