@'

\# Architecture



\## Overview



This project demonstrates Docker networking, service discovery, network isolation,

and reverse proxy routing using four manually configured Ubuntu containers.



\## Architecture



```text

&#x20;                        Windows Host

&#x20;                             |

&#x20;                       localhost:8080

&#x20;                             |

&#x20;                             v

&#x20;                    +------------------+

&#x20;                    |  Nginx Reverse   |

&#x20;                    |      Proxy       |

&#x20;                    +--------+---------+

&#x20;                             |

&#x20;                   proxy-network

&#x20;                    /                 \\

&#x20;                   /                   \\

&#x20;                  v                     v

&#x20;         +----------------+     +----------------+

&#x20;         |    Frontend    |     |    Backend     |

&#x20;         |  Nginx :80     |     |  Flask :5000   |

&#x20;         +----------------+     +--------+-------+

&#x20;                                         |

&#x20;                                  proxy-network-2

&#x20;                                         |

&#x20;                                         v

&#x20;                                 +---------------+

&#x20;                                 |  PostgreSQL   |

&#x20;                                 |     :5432     |

&#x20;                                 +---------------+



Only Nginx exposes a published host port.

Frontend, backend, and PostgreSQL use internal container ports.

'@



\## Networks



\### proxy-network



Connects:



\- nginx-container

\- frontend-container

\- backend-container



Subnet:



```text

172.19.0.0/16

