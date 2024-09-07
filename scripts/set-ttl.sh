#!/bin/bash
#!/usr/bin/env bash

iptables -t mangle -I POSTROUTING -j TTL --ttl-set 64
iptables -t mangle -I PREROUTING -j TTL --ttl-set 64
ip6tables -t mangle -I POSTROUTING -j TTL --ttl-set 64
ip6tables -t mangle -I PREROUTING -j TTL --ttl-set 64