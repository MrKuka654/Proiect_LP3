def cauta_ruta_directa(routes, plecare, destinatie):
    for route in routes:
        statii = route["statii"]

        if plecare in statii and destinatie in statii:
            index_start = statii.index(plecare)
            index_stop = statii.index(destinatie)

            if index_start < index_stop:
                nr_statii = index_stop - index_start
                timp_total = nr_statii * route["timp_intre_statii"]

                return {
                    "linie": route["linie"],
                    "traseu": statii[index_start:index_stop + 1],
                    "durata": timp_total,
                    "cost": route["cost"]
                }

    return None


def cauta_ruta_cu_schimbare(routes, plecare, destinatie):
    for route1 in routes:
        if plecare in route1["statii"]:

            for route2 in routes:
                if destinatie in route2["statii"] and route1 != route2:

                    statii_comune = set(route1["statii"]) & set(route2["statii"])

                    for statie_schimb in statii_comune:

                        statii1 = route1["statii"]
                        statii2 = route2["statii"]

                        i_start = statii1.index(plecare)
                        i_mid1 = statii1.index(statie_schimb)
                        i_mid2 = statii2.index(statie_schimb)
                        i_stop = statii2.index(destinatie)

                        if i_start < i_mid1 and i_mid2 < i_stop:

                            timp1 = (i_mid1 - i_start) * route1["timp_intre_statii"]
                            timp2 = (i_stop - i_mid2) * route2["timp_intre_statii"]

                            return {
                                "linie1": route1["linie"],
                                "traseu1": statii1[i_start:i_mid1 + 1],
                                "schimbare_la": statie_schimb,
                                "linie2": route2["linie"],
                                "traseu2": statii2[i_mid2:i_stop + 1],
                                "durata": timp1 + timp2,
                                "cost": route1["cost"] + route2["cost"]
                            }

    return None