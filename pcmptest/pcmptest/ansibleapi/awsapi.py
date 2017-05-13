#!/usr/bin/env python

import boto
#import boto.ec2.instance

def get_instance():
    conn = boto.connect_ec2('AKIAJCMEDAFNQ6DT45YA', '2skv7tVklHCB0m5or0ylgBsyIVYeiSs+lb1b/eKt')
    reservations = conn.get_all_instances()
#    conn.run_instances(image_id, min_count, max_count, key_name, security_groups, user_data, addressing_type, instance_type, placement, kernel_id, ramdisk_id, monitoring_enabled, subnet_id, block_device_map, disable_api_termination, instance_initiated_shutdown_behavior, private_ip_address, placement_group, client_token, security_group_ids, additional_info, instance_profile_name, instance_profile_arn, tenancy, ebs_optimized, network_interfaces, dry_run)
#    for i in len(reservations):
#    instance = reservations[1].instances[0]
    instance = reservations[0].instances[0]
    ipaddr = instance.ip_address
    print(type(instance))
    print(instance)
    print(ipaddr)


if __name__ == '__main__':
    get_instance()


