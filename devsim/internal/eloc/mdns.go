/*
Copyright © 2022 Ci4Rail GmbH
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package eloc

import (
	"net"

	"github.com/hashicorp/mdns"
)

func (e *Eloc) startMdns(statusServerPort int, mdnsOnLo bool) error {
	info := []string{"My awesome service"}

	var ips []net.IP
	ips = nil
	if mdnsOnLo {
		ips = []net.IP{[]byte{127, 0, 0, 1}}
	}
	service, err := mdns.NewMDNSService(e.deviceID+"-eloc", "_io4edge-eloc._tcp", "", "", statusServerPort, ips, info)

	if err != nil {
		return err
	}
	e.statusServerMdnsService = service

	// Create the mDNS server
	server, err := mdns.NewServer(&mdns.Config{Zone: service})
	if err != nil {
		return err
	}
	e.statusServerMdnsServer = server
	return nil
}
