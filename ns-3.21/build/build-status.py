#! /usr/bin/env python

# Programs that are runnable.
ns3_runnable_programs = ['build/src/aodv/examples/ns3.21-aodv-debug', 'build/src/bridge/examples/ns3.21-csma-bridge-debug', 'build/src/bridge/examples/ns3.21-csma-bridge-one-hop-debug', 'build/src/buildings/examples/ns3.21-buildings-pathloss-profiler-debug', 'build/src/config-store/examples/ns3.21-config-store-save-debug', 'build/src/core/examples/ns3.21-main-callback-debug', 'build/src/core/examples/ns3.21-sample-simulator-debug', 'build/src/core/examples/ns3.21-main-ptr-debug', 'build/src/core/examples/ns3.21-main-random-variable-debug', 'build/src/core/examples/ns3.21-main-random-variable-stream-debug', 'build/src/core/examples/ns3.21-sample-random-variable-debug', 'build/src/core/examples/ns3.21-sample-random-variable-stream-debug', 'build/src/core/examples/ns3.21-command-line-example-debug', 'build/src/core/examples/ns3.21-hash-example-debug', 'build/src/core/examples/ns3.21-main-test-sync-debug', 'build/src/csma/examples/ns3.21-csma-one-subnet-debug', 'build/src/csma/examples/ns3.21-csma-broadcast-debug', 'build/src/csma/examples/ns3.21-csma-packet-socket-debug', 'build/src/csma/examples/ns3.21-csma-multicast-debug', 'build/src/csma/examples/ns3.21-csma-raw-ip-socket-debug', 'build/src/csma/examples/ns3.21-csma-ping-debug', 'build/src/csma-layout/examples/ns3.21-csma-star-debug', 'build/src/dsdv/examples/ns3.21-dsdv-manet-debug', 'build/src/dsr/examples/ns3.21-dsr-debug', 'build/src/emu/examples/ns3.21-emu-udp-echo-debug', 'build/src/emu/examples/ns3.21-emu-ping-debug', 'build/src/energy/examples/ns3.21-li-ion-energy-source-debug', 'build/src/fd-net-device/examples/ns3.21-dummy-network-debug', 'build/src/fd-net-device/examples/ns3.21-fd2fd-onoff-debug', 'build/src/fd-net-device/examples/ns3.21-realtime-dummy-network-debug', 'build/src/fd-net-device/examples/ns3.21-realtime-fd2fd-onoff-debug', 'build/src/fd-net-device/examples/ns3.21-fd-emu-ping-debug', 'build/src/fd-net-device/examples/ns3.21-fd-emu-udp-echo-debug', 'build/src/fd-net-device/examples/ns3.21-fd-emu-onoff-debug', 'build/src/fd-net-device/examples/ns3.21-fd-tap-ping-debug', 'build/src/fd-net-device/examples/ns3.21-fd-tap-ping6-debug', 'build/src/internet/examples/ns3.21-main-simple-debug', 'build/src/internet/examples/ns3.21-codel-vs-droptail-basic-test-debug', 'build/src/internet/examples/ns3.21-codel-vs-droptail-asymmetric-debug', 'build/src/lr-wpan/examples/ns3.21-lr-wpan-packet-print-debug', 'build/src/lr-wpan/examples/ns3.21-lr-wpan-phy-test-debug', 'build/src/lr-wpan/examples/ns3.21-lr-wpan-data-debug', 'build/src/lr-wpan/examples/ns3.21-lr-wpan-error-model-plot-debug', 'build/src/lr-wpan/examples/ns3.21-lr-wpan-error-distance-plot-debug', 'build/src/lte/examples/ns3.21-lena-cqi-threshold-debug', 'build/src/lte/examples/ns3.21-lena-dual-stripe-debug', 'build/src/lte/examples/ns3.21-lena-fading-debug', 'build/src/lte/examples/ns3.21-lena-intercell-interference-debug', 'build/src/lte/examples/ns3.21-lena-pathloss-traces-debug', 'build/src/lte/examples/ns3.21-lena-profiling-debug', 'build/src/lte/examples/ns3.21-lena-rem-debug', 'build/src/lte/examples/ns3.21-lena-rem-sector-antenna-debug', 'build/src/lte/examples/ns3.21-lena-rlc-traces-debug', 'build/src/lte/examples/ns3.21-lena-simple-debug', 'build/src/lte/examples/ns3.21-lena-simple-epc-debug', 'build/src/lte/examples/ns3.21-lena-x2-handover-debug', 'build/src/lte/examples/ns3.21-lena-x2-handover-measures-debug', 'build/src/lte/examples/ns3.21-lena-simple-epc-emu-debug', 'build/src/lte/examples/ns3.21-lena-frequency-reuse-debug', 'build/src/lte/examples/ns3.21-lena-distributed-ffr-debug', 'build/src/lte/examples/ns3.21-lena-uplink-power-control-debug', 'build/src/mesh/examples/ns3.21-mesh-debug', 'build/src/mobility/examples/ns3.21-main-grid-topology-debug', 'build/src/mobility/examples/ns3.21-main-random-topology-debug', 'build/src/mobility/examples/ns3.21-main-random-walk-debug', 'build/src/mobility/examples/ns3.21-mobility-trace-example-debug', 'build/src/mobility/examples/ns3.21-ns2-mobility-trace-debug', 'build/src/mobility/examples/ns3.21-bonnmotion-ns2-example-debug', 'build/src/mpi/examples/ns3.21-simple-distributed-debug', 'build/src/mpi/examples/ns3.21-third-distributed-debug', 'build/src/mpi/examples/ns3.21-nms-p2p-nix-distributed-debug', 'build/src/mpi/examples/ns3.21-simple-distributed-empty-node-debug', 'build/src/netanim/examples/ns3.21-dumbbell-animation-debug', 'build/src/netanim/examples/ns3.21-grid-animation-debug', 'build/src/netanim/examples/ns3.21-star-animation-debug', 'build/src/netanim/examples/ns3.21-wireless-animation-debug', 'build/src/netanim/examples/ns3.21-uan-animation-debug', 'build/src/netanim/examples/ns3.21-dynamic_linknode-debug', 'build/src/netanim/examples/ns3.21-resources_demo-debug', 'build/src/network/examples/ns3.21-main-packet-header-debug', 'build/src/network/examples/ns3.21-main-packet-tag-debug', 'build/src/network/examples/ns3.21-red-tests-debug', 'build/src/network/examples/ns3.21-droptail_vs_red-debug', 'build/src/network/examples/ns3.21-packet-socket-apps-debug', 'build/src/nix-vector-routing/examples/ns3.21-nix-simple-debug', 'build/src/nix-vector-routing/examples/ns3.21-nms-p2p-nix-debug', 'build/src/olsr/examples/ns3.21-simple-point-to-point-olsr-debug', 'build/src/olsr/examples/ns3.21-olsr-hna-debug', 'build/src/point-to-point/examples/ns3.21-main-attribute-value-debug', 'build/src/propagation/examples/ns3.21-main-propagation-loss-debug', 'build/src/propagation/examples/ns3.21-jakes-propagation-model-example-debug', 'build/src/sixlowpan/examples/ns3.21-example-sixlowpan-debug', 'build/src/sixlowpan/examples/ns3.21-example-ping-lr-wpan-debug', 'build/src/spectrum/examples/ns3.21-adhoc-aloha-ideal-phy-debug', 'build/src/spectrum/examples/ns3.21-adhoc-aloha-ideal-phy-matrix-propagation-loss-model-debug', 'build/src/spectrum/examples/ns3.21-adhoc-aloha-ideal-phy-with-microwave-oven-debug', 'build/src/stats/examples/ns3.21-gnuplot-example-debug', 'build/src/stats/examples/ns3.21-double-probe-example-debug', 'build/src/stats/examples/ns3.21-gnuplot-aggregator-example-debug', 'build/src/stats/examples/ns3.21-gnuplot-helper-example-debug', 'build/src/stats/examples/ns3.21-file-aggregator-example-debug', 'build/src/stats/examples/ns3.21-file-helper-example-debug', 'build/src/tap-bridge/examples/ns3.21-tap-csma-debug', 'build/src/tap-bridge/examples/ns3.21-tap-csma-virtual-machine-debug', 'build/src/tap-bridge/examples/ns3.21-tap-wifi-virtual-machine-debug', 'build/src/tap-bridge/examples/ns3.21-tap-wifi-dumbbell-debug', 'build/src/topology-read/examples/ns3.21-topology-read-debug', 'build/src/uan/examples/ns3.21-uan-cw-example-debug', 'build/src/uan/examples/ns3.21-uan-rc-example-debug', 'build/src/virtual-net-device/examples/ns3.21-virtual-net-device-debug', 'build/src/wave/examples/ns3.21-wave-simple-80211p-debug', 'build/src/wifi/examples/ns3.21-wifi-phy-test-debug', 'build/src/wimax/examples/ns3.21-wimax-ipv4-debug', 'build/src/wimax/examples/ns3.21-wimax-multicast-debug', 'build/src/wimax/examples/ns3.21-wimax-simple-debug', 'build/src/wrab/examples/ns3.21-wrab-example-debug', 'build/src/wran/examples/ns3.21-wran-ipv4-debug', 'build/src/wran/examples/ns3.21-wran-multicast-debug', 'build/src/wran/examples/ns3.21-wran-simple-debug', 'build/examples/matrix-topology/ns3.21-matrix-topology-debug', 'build/examples/tcp/ns3.21-tcp-large-transfer-debug', 'build/examples/tcp/ns3.21-tcp-nsc-lfn-debug', 'build/examples/tcp/ns3.21-tcp-nsc-zoo-debug', 'build/examples/tcp/ns3.21-tcp-star-server-debug', 'build/examples/tcp/ns3.21-star-debug', 'build/examples/tcp/ns3.21-tcp-bulk-send-debug', 'build/examples/tcp/ns3.21-tcp-nsc-comparison-debug', 'build/examples/tcp/ns3.21-tcp-variants-comparison-debug', 'build/examples/udp/ns3.21-udp-echo-debug', 'build/examples/energy/ns3.21-energy-model-example-debug', 'build/examples/energy/ns3.21-energy-model-with-harvesting-example-debug', 'build/examples/naming/ns3.21-object-names-debug', 'build/examples/tutorial/ns3.21-hello-simulator-debug', 'build/examples/tutorial/ns3.21-first-debug', 'build/examples/tutorial/ns3.21-second-debug', 'build/examples/tutorial/ns3.21-third-debug', 'build/examples/tutorial/ns3.21-fourth-debug', 'build/examples/tutorial/ns3.21-fifth-debug', 'build/examples/tutorial/ns3.21-sixth-debug', 'build/examples/tutorial/ns3.21-seventh-debug', 'build/examples/error-model/ns3.21-simple-error-model-debug', 'build/examples/ipv6/ns3.21-icmpv6-redirect-debug', 'build/examples/ipv6/ns3.21-ping6-debug', 'build/examples/ipv6/ns3.21-radvd-debug', 'build/examples/ipv6/ns3.21-radvd-two-prefix-debug', 'build/examples/ipv6/ns3.21-test-ipv6-debug', 'build/examples/ipv6/ns3.21-fragmentation-ipv6-debug', 'build/examples/ipv6/ns3.21-fragmentation-ipv6-two-MTU-debug', 'build/examples/ipv6/ns3.21-loose-routing-ipv6-debug', 'build/examples/ipv6/ns3.21-wsn-ping6-debug', 'build/examples/wireless/ns3.21-mixed-wireless-debug', 'build/examples/wireless/ns3.21-wifi-adhoc-debug', 'build/examples/wireless/ns3.21-wifi-clear-channel-cmu-debug', 'build/examples/wireless/ns3.21-wifi-ap-debug', 'build/examples/wireless/ns3.21-wifi-wired-bridging-debug', 'build/examples/wireless/ns3.21-simple-wifi-frame-aggregation-debug', 'build/examples/wireless/ns3.21-multirate-debug', 'build/examples/wireless/ns3.21-wifi-simple-adhoc-debug', 'build/examples/wireless/ns3.21-wifi-simple-adhoc-grid-debug', 'build/examples/wireless/ns3.21-wifi-simple-infra-debug', 'build/examples/wireless/ns3.21-wifi-simple-interference-debug', 'build/examples/wireless/ns3.21-wifi-blockack-debug', 'build/examples/wireless/ns3.21-ofdm-validation-debug', 'build/examples/wireless/ns3.21-wifi-hidden-terminal-debug', 'build/examples/wireless/ns3.21-ht-wifi-network-debug', 'build/examples/socket/ns3.21-socket-bound-static-routing-debug', 'build/examples/socket/ns3.21-socket-bound-tcp-static-routing-debug', 'build/examples/socket/ns3.21-socket-options-ipv4-debug', 'build/examples/socket/ns3.21-socket-options-ipv6-debug', 'build/examples/realtime/ns3.21-realtime-udp-echo-debug', 'build/examples/routing/ns3.21-dynamic-global-routing-debug', 'build/examples/routing/ns3.21-static-routing-slash32-debug', 'build/examples/routing/ns3.21-global-routing-slash32-debug', 'build/examples/routing/ns3.21-global-injection-slash32-debug', 'build/examples/routing/ns3.21-simple-global-routing-debug', 'build/examples/routing/ns3.21-simple-alternate-routing-debug', 'build/examples/routing/ns3.21-mixed-global-routing-debug', 'build/examples/routing/ns3.21-simple-routing-ping6-debug', 'build/examples/routing/ns3.21-manet-routing-compare-debug', 'build/examples/routing/ns3.21-ripng-simple-network-debug', 'build/examples/stats/ns3.21-wifi-example-sim-debug', 'build/examples/udp-client-server/ns3.21-udp-client-server-debug', 'build/examples/udp-client-server/ns3.21-udp-trace-client-server-debug', 'build/scratch/subdir/ns3.21-subdir-debug', 'build/scratch/ns3.21-scratch-simulator-debug', 'build/scratch/ns3.21-wran-debug', 'build/scratch/ns3.21-wran_wifi-debug']

# Scripts that are runnable.
ns3_runnable_scripts = ['csma-bridge.py', 'sample-simulator.py', 'wifi-olsr-flowmon.py', 'tap-csma-virtual-machine.py', 'tap-wifi-virtual-machine.py', 'first.py', 'mixed-wireless.py', 'wifi-ap.py', 'realtime-udp-echo.py', 'simple-routing-ping6.py']

