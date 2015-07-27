newrecord("bid-east.bilinmedia.net") do |query, answer|
        ips = ["54.164.24.124", "54.164.74.39", "52.4.61.247", "52.6.219.62", "54.175.155.105", "54.175.115.108", "54.175.108.13", "54.175.100.98"]
        ips = ips.randomize([1, 1, 1, 1, 1, 1, 1, 1])
        answer.shuffle false
        answer.ttl 30
        answer.content ips[0]
        answer.content ips[1]
        answer.content ips[2]
        answer.content ips[3]
        answer.content ips[4]
        answer.content ips[5]
        answer.content ips[6]
        answer.content ips[7]
    end



module Pdns
        newrecord("ads.bilinmedia.net") do |query, answer|
                country_, region_ = country(query[:remoteip])
                answer.qclass query[:qclass]
                answer.qtype :A
                case country_
                        when "US"
                                case region_
                                        when "WI","IL","TN","MS","ID","KY","AL","OH","WV","VA","NC","SC","GA","FL","NY","PA","ME","VT","NH","MA","RI","CT","NJ","DE","MD","DC"
                                                # using east ip
                                                answer.ttl 300
                                                answer.content "54.165.40.127"
                                        else
                                                # using west ip
                                                answer.ttl 300
                                                answer.content "54.67.109.162"
                                end
                        else
                        # using west ip
                        answer.ttl 300
                        answer.content "54.67.109.162"
                end
        end
end