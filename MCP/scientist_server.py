from mcp.server.fastmcp import FastMCP

mcp = FastMCP("World Top 500 Scientists Server")

# (id, name, birth, death_or_None, country, [fields], [known_for], [(nobel_year, field, reason)])
_RAW = [
    # ── PHYSICS ──────────────────────────────────────────────────────────────
    (1,  "Albert Einstein",        1879,1955,"Germany",        ["Physics"],                    ["Theory of Relativity","Photoelectric Effect","E=mc²","Brownian Motion"],           [(1921,"Physics","Photoelectric Effect")]),
    (2,  "Isaac Newton",           1643,1727,"England",        ["Physics","Mathematics"],      ["Laws of Motion","Universal Gravitation","Calculus","Optics"],                       []),
    (3,  "Niels Bohr",             1885,1962,"Denmark",        ["Physics"],                    ["Atomic Model","Quantum Mechanics","Bohr Model"],                                    [(1922,"Physics","Atomic Structure")]),
    (4,  "Max Planck",             1858,1947,"Germany",        ["Physics"],                    ["Quantum Theory","Planck's Constant"],                                               [(1918,"Physics","Energy Quanta")]),
    (5,  "James Clerk Maxwell",    1831,1879,"Scotland",       ["Physics"],                    ["Maxwell's Equations","Electromagnetism","Electromagnetic Waves"],                   []),
    (6,  "Michael Faraday",        1791,1867,"England",        ["Physics","Chemistry"],        ["Electromagnetic Induction","Faraday's Law","Electric Motor","Benzene Discovery"],  []),
    (7,  "Richard Feynman",        1918,1988,"USA",            ["Physics"],                    ["Quantum Electrodynamics (QED)","Feynman Diagrams","Nanotechnology Concept"],        [(1965,"Physics","Quantum Electrodynamics")]),
    (8,  "Werner Heisenberg",      1901,1976,"Germany",        ["Physics"],                    ["Uncertainty Principle","Quantum Mechanics","Matrix Mechanics"],                     [(1932,"Physics","Quantum Mechanics")]),
    (9,  "Erwin Schrödinger",      1887,1961,"Austria",        ["Physics"],                    ["Schrödinger Equation","Wave Mechanics","Schrödinger's Cat"],                        [(1933,"Physics","Wave Mechanics")]),
    (10, "Paul Dirac",             1902,1984,"England",        ["Physics"],                    ["Dirac Equation","Antimatter Prediction","Quantum Field Theory"],                    [(1933,"Physics","Atomic Theory")]),
    (11, "Enrico Fermi",           1901,1954,"Italy",          ["Physics"],                    ["Nuclear Reactor","Fermi Paradox","Fermi-Dirac Statistics"],                         [(1938,"Physics","Nuclear Reactions")]),
    (12, "Ernest Rutherford",      1871,1937,"New Zealand",    ["Physics","Chemistry"],        ["Nuclear Model of Atom","Alpha/Beta Radiation","First Nuclear Reaction"],            [(1908,"Chemistry","Radioactive Decay")]),
    (13, "J.J. Thomson",           1856,1940,"England",        ["Physics"],                    ["Discovery of Electron","Cathode Ray Tube","Plum Pudding Model"],                    [(1906,"Physics","Electrical Conduction in Gases")]),
    (14, "Wilhelm Röntgen",        1845,1923,"Germany",        ["Physics"],                    ["Discovery of X-Rays"],                                                              [(1901,"Physics","X-Ray Discovery")]),
    (15, "Wolfgang Pauli",         1900,1958,"Austria",        ["Physics"],                    ["Pauli Exclusion Principle","Neutrino Prediction","Spin Theory"],                    [(1945,"Physics","Exclusion Principle")]),
    (16, "Louis de Broglie",       1892,1987,"France",         ["Physics"],                    ["Wave-Particle Duality","Matter Waves","de Broglie Wavelength"],                     [(1929,"Physics","Wave Nature of Electrons")]),
    (17, "Max Born",               1882,1970,"Germany",        ["Physics"],                    ["Probability Interpretation of Quantum Mechanics","Born Rule"],                      [(1954,"Physics","Quantum Mechanics")]),
    (18, "Hendrik Lorentz",        1853,1928,"Netherlands",    ["Physics"],                    ["Lorentz Transformation","Zeeman Effect","Electron Theory"],                         [(1902,"Physics","Magnetic Radiation")]),
    (19, "Lord Kelvin",            1824,1907,"Ireland",        ["Physics"],                    ["Absolute Temperature Scale","Kelvin Scale","Thermodynamics"],                       []),
    (20, "James Joule",            1818,1889,"England",        ["Physics"],                    ["Joule's Law","Mechanical Equivalent of Heat","Joule Heating"],                      []),
    (21, "Alessandro Volta",       1745,1827,"Italy",          ["Physics"],                    ["Electric Battery (Voltaic Pile)","Electric Potential"],                              []),
    (22, "André-Marie Ampère",     1775,1836,"France",         ["Physics"],                    ["Ampère's Law","Electrodynamics","Solenoid"],                                         []),
    (23, "Hans Christian Ørsted",  1777,1851,"Denmark",        ["Physics","Chemistry"],        ["Electromagnetism Discovery","Piperine Discovery"],                                  []),
    (24, "Heinrich Hertz",         1857,1894,"Germany",        ["Physics"],                    ["Electromagnetic Waves","Photoelectric Effect (observed)","Radio Waves"],            []),
    (25, "Ludwig Boltzmann",       1844,1906,"Austria",        ["Physics"],                    ["Statistical Mechanics","Boltzmann Constant","H-Theorem"],                           []),
    (26, "Robert Boyle",           1627,1691,"Ireland",        ["Physics","Chemistry"],        ["Boyle's Law","Scientific Method in Chemistry"],                                     []),
    (27, "Blaise Pascal",          1623,1662,"France",         ["Physics","Mathematics"],      ["Pascal's Law","Barometer","Probability Theory","Mechanical Calculator"],            []),
    (28, "Christian Huygens",      1629,1695,"Netherlands",    ["Physics","Astronomy"],        ["Wave Theory of Light","Saturn Rings","Pendulum Clock"],                             []),
    (29, "Charles-Augustin Coulomb",1736,1806,"France",        ["Physics"],                    ["Coulomb's Law","Electric Charge Measurement"],                                      []),
    (30, "Georg Ohm",              1789,1854,"Germany",        ["Physics"],                    ["Ohm's Law","Electrical Resistance"],                                                 []),
    (31, "John Bardeen",           1908,1991,"USA",            ["Physics"],                    ["Transistor Invention","BCS Theory of Superconductivity"],                           [(1956,"Physics","Transistor"),(1972,"Physics","Superconductivity")]),
    (32, "Walter Brattain",        1902,1987,"China/USA",      ["Physics"],                    ["Transistor Invention (co-inventor)"],                                               [(1956,"Physics","Transistor")]),
    (33, "William Shockley",       1910,1989,"England/USA",    ["Physics"],                    ["Junction Transistor","Semiconductor Research"],                                     [(1956,"Physics","Transistor")]),
    (34, "Steven Weinberg",        1933,2021,"USA",            ["Physics"],                    ["Electroweak Unification","Standard Model"],                                         [(1979,"Physics","Electroweak Theory")]),
    (35, "Abdus Salam",            1926,1996,"Pakistan",       ["Physics"],                    ["Electroweak Theory","Grand Unified Theory"],                                        [(1979,"Physics","Electroweak Theory")]),
    (36, "Sheldon Glashow",        1932,None,"USA",            ["Physics"],                    ["Electroweak Theory","Charm Quark Prediction"],                                      [(1979,"Physics","Electroweak Theory")]),
    (37, "Murray Gell-Mann",       1929,2019,"USA",            ["Physics"],                    ["Quarks Discovery","Strangeness","Eightfold Way"],                                   [(1969,"Physics","Quarks")]),
    (38, "Peter Higgs",            1929,2024,"England",        ["Physics"],                    ["Higgs Boson (God Particle)","Higgs Mechanism"],                                     [(2013,"Physics","Higgs Mechanism")]),
    (39, "François Englert",       1932,None,"Belgium",        ["Physics"],                    ["Brout-Englert-Higgs Mechanism"],                                                    [(2013,"Physics","Higgs Mechanism")]),
    (40, "Roger Penrose",          1931,None,"England",        ["Physics","Mathematics"],      ["Penrose Tiling","Black Hole Singularities","Twistor Theory"],                       [(2020,"Physics","Black Hole Formation")]),
    (41, "Kip Thorne",             1940,None,"USA",            ["Physics"],                    ["Gravitational Waves Detection (LIGO)","Black Hole Physics"],                        [(2017,"Physics","Gravitational Waves")]),
    (42, "Rainer Weiss",           1932,None,"Germany/USA",    ["Physics"],                    ["LIGO Development","Gravitational Waves"],                                           [(2017,"Physics","Gravitational Waves")]),
    (43, "Stephen Hawking",        1942,2018,"England",        ["Physics","Cosmology"],        ["Hawking Radiation","Black Hole Thermodynamics","A Brief History of Time"],          []),
    (44, "Lev Landau",             1908,1968,"Azerbaijan/USSR",["Physics"],                    ["Landau Levels","Fermi Liquid Theory","Superfluidity"],                              [(1962,"Physics","Condensed Matter")]),
    (45, "Pyotr Kapitsa",          1894,1984,"Russia",         ["Physics"],                    ["Superfluidity of Helium","Strong Magnetic Fields","Low Temperature Physics"],       [(1978,"Physics","Low Temperature Physics")]),
    (46, "Maria Goeppert-Mayer",   1906,1972,"Germany/USA",    ["Physics"],                    ["Nuclear Shell Model"],                                                              [(1963,"Physics","Nuclear Shell Structure")]),
    (47, "Charles Townes",         1915,2015,"USA",            ["Physics"],                    ["Maser Invention","Laser (co-inventor)"],                                            [(1964,"Physics","Maser/Laser")]),
    (48, "Dennis Gabor",           1900,1979,"Hungary/England",["Physics"],                    ["Holography Invention"],                                                             [(1971,"Physics","Holography")]),
    (49, "Sin-Itiro Tomonaga",     1906,1979,"Japan",          ["Physics"],                    ["Quantum Electrodynamics"],                                                          [(1965,"Physics","Quantum Electrodynamics")]),
    (50, "Julian Schwinger",       1918,1994,"USA",            ["Physics"],                    ["Quantum Electrodynamics","Schwinger Effect"],                                        [(1965,"Physics","Quantum Electrodynamics")]),
    (51, "Galileo Galilei",        1564,1642,"Italy",          ["Physics","Astronomy"],        ["Law of Falling Bodies","Telescope Improvements","Moons of Jupiter"],               []),
    (52, "Christiaan Huygens",     1629,1695,"Netherlands",    ["Physics","Astronomy"],        ["Saturn Rings","Pendulum Clock","Wave Theory of Light"],                             []),
    (53, "Robert Hooke",           1635,1703,"England",        ["Physics","Biology"],          ["Hooke's Law","Cell Discovery","Microscopy"],                                        []),
    (54, "Henry Cavendish",        1731,1810,"England",        ["Physics","Chemistry"],        ["Cavendish Experiment (G constant)","Hydrogen Discovery","Composition of Water"],   []),
    (55, "George Stokes",          1819,1903,"Ireland",        ["Physics","Mathematics"],      ["Stokes' Law","Navier-Stokes Equations","Fluorescence"],                             []),
    (56, "Lord Rayleigh",          1842,1919,"England",        ["Physics"],                    ["Rayleigh Scattering","Argon Discovery (co)","Rayleigh Waves"],                      [(1904,"Physics","Gas Densities")]),
    (57, "J. Robert Oppenheimer",  1904,1967,"USA",            ["Physics"],                    ["Manhattan Project (Director)","Neutron Star Prediction","Black Hole Theory"],       []),
    (58, "Hideki Yukawa",          1907,1981,"Japan",          ["Physics"],                    ["Meson Theory","Nuclear Force Prediction"],                                           [(1949,"Physics","Nuclear Forces")]),
    (59, "Richard Tolman",         1881,1948,"USA",            ["Physics","Chemistry"],        ["Chemical Kinetics","Relativistic Thermodynamics"],                                  []),
    (60, "Subrahmanyan Chandrasekhar",1910,1995,"India/USA",   ["Physics","Astronomy"],        ["Chandrasekhar Limit","White Dwarf Theory","Stellar Evolution"],                     [(1983,"Physics","Stellar Structure")]),
    (61, "Hans Bethe",             1906,2005,"Germany/USA",    ["Physics"],                    ["Stellar Nucleosynthesis","Bethe-Bloch Formula","Meson Theory"],                     [(1967,"Physics","Energy Production in Stars")]),
    (62, "Eugene Wigner",          1902,1995,"Hungary/USA",    ["Physics","Mathematics"],      ["Nuclear Reactor Design","Symmetry Principles","Wigner's Friend"],                   [(1963,"Physics","Nuclear Physics")]),
    (63, "Victor Weisskopf",       1908,2002,"Austria/USA",    ["Physics"],                    ["Lamb Shift","Nuclear Physics","Weisskopf-Wigner Theory"],                           []),
    (64, "Emilio Segrè",           1905,1989,"Italy/USA",      ["Physics"],                    ["Antiproton Discovery","Technetium Discovery (co)"],                                 [(1959,"Physics","Antiproton")]),
    (65, "Owen Chamberlain",       1920,2006,"USA",            ["Physics"],                    ["Antiproton Discovery"],                                                             [(1959,"Physics","Antiproton")]),
    (66, "Donald Glaser",          1926,2013,"USA",            ["Physics"],                    ["Bubble Chamber Invention"],                                                         [(1960,"Physics","Bubble Chamber")]),
    (67, "Rudolf Mössbauer",       1929,2011,"Germany",        ["Physics"],                    ["Mössbauer Effect (Recoilless Nuclear Resonance)"],                                  [(1961,"Physics","Mössbauer Effect")]),
    (68, "Leon Cooper",            1930,None,"USA",            ["Physics"],                    ["BCS Theory of Superconductivity","Cooper Pairs"],                                   [(1972,"Physics","Superconductivity")]),
    (69, "Alexei Abrikosov",       1928,2017,"Russia/USA",     ["Physics"],                    ["Type-II Superconductors","Vortex Lattice"],                                          [(2003,"Physics","Superconductors")]),
    (70, "Frank Wilczek",          1951,None,"USA",            ["Physics"],                    ["Asymptotic Freedom","Anyons","Axion"],                                               [(2004,"Physics","Strong Force")]),
    (71, "David Gross",            1941,None,"USA",            ["Physics"],                    ["Asymptotic Freedom","Quantum Chromodynamics"],                                      [(2004,"Physics","Strong Force")]),
    (72, "H. David Politzer",      1949,None,"USA",            ["Physics"],                    ["Asymptotic Freedom"],                                                               [(2004,"Physics","Strong Force")]),
    (73, "Yoichiro Nambu",         1921,2015,"Japan/USA",       ["Physics"],                   ["Spontaneous Symmetry Breaking","String Theory Origins"],                            [(2008,"Physics","Symmetry Breaking")]),
    (74, "Gerardus 't Hooft",      1946,None,"Netherlands",    ["Physics"],                    ["Gauge Field Theories Renormalization"],                                             [(1999,"Physics","Electroweak Interactions")]),
    (75, "Martinus Veltman",       1931,2021,"Netherlands",    ["Physics"],                    ["Electroweak Theory Structure"],                                                     [(1999,"Physics","Electroweak Interactions")]),
    (76, "George Zweig",           1937,None,"Russia/USA",     ["Physics"],                    ["Quark Model (Aces)"],                                                               []),
    (77, "Carlo Rubbia",           1934,None,"Italy",          ["Physics"],                    ["W and Z Boson Discovery"],                                                          [(1984,"Physics","W/Z Bosons")]),
    (78, "Simon van der Meer",     1925,2011,"Netherlands",    ["Physics"],                    ["Stochastic Cooling","W/Z Boson Experiments"],                                       [(1984,"Physics","W/Z Bosons")]),
    (79, "Georges Charpak",        1924,2010,"Poland/France",  ["Physics"],                    ["Multiwire Proportional Chamber"],                                                   [(1992,"Physics","Particle Detectors")]),
    (80, "Martin Perl",            1927,2014,"USA",            ["Physics"],                    ["Tau Lepton Discovery"],                                                             [(1995,"Physics","Tau Lepton")]),
    # ── ASTRONOMY & COSMOLOGY ─────────────────────────────────────────────────
    (81, "Nicolaus Copernicus",    1473,1543,"Poland",         ["Astronomy"],                  ["Heliocentric Model","De Revolutionibus"],                                            []),
    (82, "Johannes Kepler",        1571,1630,"Germany",        ["Astronomy","Mathematics"],    ["Kepler's Laws of Planetary Motion","Kepler Conjecture"],                            []),
    (83, "Tycho Brahe",            1546,1601,"Denmark",        ["Astronomy"],                  ["Precise Planetary Observations","Supernova Observation"],                           []),
    (84, "Edwin Hubble",           1889,1953,"USA",            ["Astronomy"],                  ["Expanding Universe","Hubble's Law","Galaxy Classification"],                        []),
    (85, "Carl Sagan",             1934,1996,"USA",            ["Astronomy","Cosmology"],      ["Pale Blue Dot","Cosmos TV Series","SETI Pioneer","Drake Equation"],                 []),
    (86, "Vera Rubin",             1928,2016,"USA",            ["Astronomy"],                  ["Dark Matter Evidence","Galaxy Rotation Curves"],                                    []),
    (87, "Jocelyn Bell Burnell",   1943,None,"Ireland",        ["Astronomy"],                  ["Pulsar Discovery"],                                                                 []),
    (88, "Cecilia Payne-Gaposchkin",1900,1979,"England/USA",   ["Astronomy"],                  ["Stellar Composition (Hydrogen)","Stellar Classification"],                          []),
    (89, "Andrea Ghez",            1965,None,"USA",            ["Astronomy"],                  ["Supermassive Black Hole at Milky Way Centre"],                                      [(2020,"Physics","Galactic Centre Black Hole")]),
    (90, "Reinhard Genzel",        1952,None,"Germany",        ["Astronomy"],                  ["Supermassive Black Hole at Milky Way Centre"],                                      [(2020,"Physics","Galactic Centre Black Hole")]),
    (91, "Michel Mayor",           1942,None,"Switzerland",    ["Astronomy"],                  ["First Exoplanet Discovery (51 Pegasi b)"],                                          [(2019,"Physics","Exoplanet Discovery")]),
    (92, "Didier Queloz",          1966,None,"Switzerland",    ["Astronomy"],                  ["First Exoplanet Discovery"],                                                        [(2019,"Physics","Exoplanet Discovery")]),
    (93, "James Peebles",          1935,None,"Canada/USA",     ["Cosmology"],                  ["Cosmic Microwave Background Theory","Dark Matter/Energy Theory"],                   [(2019,"Physics","Physical Cosmology")]),
    (94, "George Smoot",           1945,None,"USA",            ["Cosmology"],                  ["CMB Anisotropy","Big Bang Evidence"],                                               [(2006,"Physics","CMB Blackbody")]),
    (95, "John Mather",            1946,None,"USA",            ["Cosmology"],                  ["CMB Spectrum","COBE Satellite"],                                                    [(2006,"Physics","CMB Blackbody")]),
    (96, "Saul Perlmutter",        1959,None,"USA",            ["Cosmology"],                  ["Accelerating Universe","Dark Energy Discovery"],                                    [(2011,"Physics","Accelerating Universe")]),
    (97, "Brian Schmidt",          1967,None,"USA/Australia",  ["Cosmology"],                  ["Accelerating Universe","Dark Energy"],                                              [(2011,"Physics","Accelerating Universe")]),
    (98, "Adam Riess",             1969,None,"USA",            ["Cosmology"],                  ["Dark Energy","Hubble Constant Refinement"],                                         [(2011,"Physics","Accelerating Universe")]),
    (99, "Fred Hoyle",             1915,2001,"England",        ["Astronomy"],                  ["Stellar Nucleosynthesis","Big Bang (named)","Carbon Resonance"],                    []),
    (100,"William Herschel",       1738,1822,"Germany/England",["Astronomy"],                  ["Uranus Discovery","Infrared Radiation","Binary Stars"],                             []),
    # ── CHEMISTRY ────────────────────────────────────────────────────────────
    (101,"Marie Curie",            1867,1934,"Poland/France",  ["Chemistry","Physics"],        ["Radioactivity","Radium Discovery","Polonium Discovery"],                            [(1903,"Physics","Radioactivity"),(1911,"Chemistry","Radium & Polonium")]),
    (102,"Pierre Curie",           1859,1906,"France",         ["Physics","Chemistry"],        ["Radioactivity (co-discovery)","Piezoelectricity","Curie Temperature"],              [(1903,"Physics","Radioactivity")]),
    (103,"Antoine Lavoisier",      1743,1794,"France",         ["Chemistry"],                  ["Oxygen Discovery (naming)","Conservation of Mass","Chemical Nomenclature"],         []),
    (104,"John Dalton",            1766,1844,"England",        ["Chemistry","Physics"],        ["Atomic Theory","Dalton's Law","Color Blindness Research"],                          []),
    (105,"Dmitri Mendeleev",       1834,1907,"Russia",         ["Chemistry"],                  ["Periodic Table of Elements","Periodic Law","Predicted Undiscovered Elements"],      []),
    (106,"Linus Pauling",          1901,1994,"USA",            ["Chemistry"],                  ["Chemical Bonds","Molecular Biology","Alpha Helix","DNA Research"],                  [(1954,"Chemistry","Chemical Bonds"),(1962,"Peace","Nuclear Test Ban")]),
    (107,"Fritz Haber",            1868,1934,"Germany",        ["Chemistry"],                  ["Haber-Bosch Process (Nitrogen Fixation)","Fertilizer Production"],                  [(1918,"Chemistry","Ammonia Synthesis")]),
    (108,"Carl Bosch",             1874,1940,"Germany",        ["Chemistry","Engineering"],    ["Haber-Bosch Process (Industrial Scale)","High-Pressure Chemistry"],                 [(1931,"Chemistry","High-Pressure Chemistry")]),
    (109,"Otto Hahn",              1879,1968,"Germany",        ["Chemistry","Physics"],        ["Nuclear Fission Discovery","Radioactivity Research"],                               [(1944,"Chemistry","Nuclear Fission")]),
    (110,"Lise Meitner",           1878,1968,"Austria",        ["Physics","Chemistry"],        ["Nuclear Fission (co-discoverer)","Meitner-Hupfeld Effect"],                         []),
    (111,"August Kekulé",          1829,1896,"Germany",        ["Chemistry"],                  ["Benzene Ring Structure","Structural Formula","Valence Theory"],                     []),
    (112,"Emil Fischer",           1852,1919,"Germany",        ["Chemistry"],                  ["Sugar & Purine Synthesis","Lock and Key Model","Fischer Projection"],               [(1902,"Chemistry","Sugar Synthesis")]),
    (113,"Jacobus van 't Hoff",    1852,1911,"Netherlands",    ["Chemistry"],                  ["Osmotic Pressure","Chemical Kinetics","Stereochemistry"],                           [(1901,"Chemistry","Chemical Dynamics")]),
    (114,"Wilhelm Ostwald",        1853,1932,"Latvia/Germany", ["Chemistry"],                  ["Physical Chemistry","Ostwald Process (Nitric Acid)","Catalysis"],                   [(1909,"Chemistry","Catalysis")]),
    (115,"Victor Grignard",        1871,1935,"France",         ["Chemistry"],                  ["Grignard Reagents in Organic Chemistry"],                                           [(1912,"Chemistry","Grignard Reagents")]),
    (116,"Paul Sabatier",          1854,1941,"France",         ["Chemistry"],                  ["Catalytic Hydrogenation of Organic Compounds"],                                     [(1912,"Chemistry","Hydrogenation")]),
    (117,"Alfred Werner",          1866,1919,"France/Switzerland",["Chemistry"],               ["Coordination Chemistry","Werner's Theory"],                                          [(1913,"Chemistry","Coordination Compounds")]),
    (118,"Frederick Soddy",        1877,1956,"England",        ["Chemistry","Physics"],        ["Isotopes","Radioactive Decay","Soddy-Fajans Rule"],                                 [(1921,"Chemistry","Radioactive Substances")]),
    (119,"Francis William Aston",  1877,1945,"England",        ["Chemistry","Physics"],        ["Mass Spectrograph","Isotopes of Non-Radioactive Elements"],                         [(1922,"Chemistry","Mass Spectrograph")]),
    (120,"Fritz Pregl",            1869,1930,"Austria",        ["Chemistry"],                  ["Microanalysis of Organic Substances"],                                              [(1923,"Chemistry","Microanalysis")]),
    (121,"Richard Zsigmondy",      1865,1929,"Austria/Germany",["Chemistry"],                  ["Colloid Chemistry","Ultramicroscope"],                                              [(1925,"Chemistry","Colloid Chemistry")]),
    (122,"Theodor Svedberg",       1884,1971,"Sweden",         ["Chemistry"],                  ["Ultracentrifuge","Colloid Chemistry"],                                              [(1926,"Chemistry","Dispersed Systems")]),
    (123,"Heinrich Wieland",       1877,1957,"Germany",        ["Chemistry"],                  ["Bile Acids Structure","Steroids Chemistry"],                                        [(1927,"Chemistry","Bile Acids")]),
    (124,"Adolf Windaus",          1876,1959,"Germany",        ["Chemistry"],                  ["Sterols Structure","Vitamin D Chemistry"],                                          [(1928,"Chemistry","Sterols")]),
    (125,"Arthur Harden",          1865,1940,"England",        ["Chemistry"],                  ["Fermentation Chemistry","Coenzymes"],                                               [(1929,"Chemistry","Fermentation")]),
    (126,"Hans von Euler-Chelpin", 1873,1964,"Germany/Sweden", ["Chemistry"],                  ["Fermentation of Sugar","Enzymes"],                                                  [(1929,"Chemistry","Fermentation")]),
    (127,"Hans Fischer",           1881,1945,"Germany",        ["Chemistry"],                  ["Hemin and Chlorophyll Synthesis","Porphyrins"],                                     [(1930,"Chemistry","Hemin")]),
    (128,"Carl Bosch",             1874,1940,"Germany",        ["Chemistry"],                  ["High-Pressure Industrial Processes"],                                               [(1931,"Chemistry","High Pressure Methods")]),
    (129,"Friedrich Bergius",      1884,1949,"Germany",        ["Chemistry"],                  ["Coal Liquefaction","Hydrolysis of Wood"],                                           [(1931,"Chemistry","High Pressure Methods")]),
    (130,"Irving Langmuir",        1881,1957,"USA",            ["Chemistry","Physics"],        ["Surface Chemistry","Langmuir Adsorption","Cloud Seeding"],                          [(1932,"Chemistry","Surface Chemistry")]),
    (131,"Harold Urey",            1893,1981,"USA",            ["Chemistry","Physics"],        ["Deuterium Discovery","Urey-Miller Experiment (origin of life)"],                    [(1934,"Chemistry","Heavy Hydrogen")]),
    (132,"Frédéric Joliot-Curie",  1900,1958,"France",         ["Chemistry","Physics"],        ["Artificial Radioactivity","Nuclear Fission Research"],                              [(1935,"Chemistry","Artificial Radioactivity")]),
    (133,"Irène Joliot-Curie",     1897,1956,"France",         ["Chemistry","Physics"],        ["Artificial Radioactivity (co-discovery)","Polonium Research"],                      [(1935,"Chemistry","Artificial Radioactivity")]),
    (134,"Peter Debye",            1884,1966,"Netherlands/USA",["Chemistry","Physics"],        ["Debye-Hückel Theory","Dipole Moments","X-ray Diffraction"],                         [(1936,"Chemistry","Dipole Moments")]),
    (135,"Richard Kuhn",           1900,1967,"Austria/Germany",["Chemistry"],                  ["Carotenoids","Vitamins B2 and B6 Structure"],                                       [(1938,"Chemistry","Carotenoids")]),
    (136,"Leopold Ruzicka",        1887,1976,"Croatia/Switzerland",["Chemistry"],              ["Sex Hormones","Terpenes","Polymethylenes"],                                          [(1939,"Chemistry","Polymethylenes")]),
    (137,"George de Hevesy",       1885,1966,"Hungary/Sweden", ["Chemistry","Physics"],        ["Radioactive Tracers","Hafnium Discovery"],                                          [(1943,"Chemistry","Isotopic Tracers")]),
    (138,"James Sumner",           1887,1955,"USA",            ["Chemistry","Biology"],        ["Enzyme Crystallization","Urease"],                                                  [(1946,"Chemistry","Enzyme Crystallization")]),
    (139,"Arne Tiselius",          1902,1971,"Sweden",         ["Chemistry"],                  ["Electrophoresis","Serum Proteins"],                                                 [(1948,"Chemistry","Electrophoresis")]),
    (140,"William Giauque",        1895,1982,"Canada/USA",     ["Chemistry","Physics"],        ["Adiabatic Demagnetization","Near Absolute Zero Chemistry"],                         [(1949,"Chemistry","Low Temperature Chemistry")]),
    (141,"Otto Diels",             1876,1954,"Germany",        ["Chemistry"],                  ["Diels-Alder Reaction","Diene Synthesis"],                                           [(1950,"Chemistry","Diene Synthesis")]),
    (142,"Kurt Alder",             1902,1958,"Germany",        ["Chemistry"],                  ["Diels-Alder Reaction"],                                                             [(1950,"Chemistry","Diene Synthesis")]),
    (143,"Edwin McMillan",         1907,1991,"USA",            ["Chemistry","Physics"],        ["Neptunium Discovery (first transuranic element)","Synchrotron"],                    [(1951,"Chemistry","Transuranic Elements")]),
    (144,"Glenn Seaborg",          1912,1999,"USA",            ["Chemistry","Physics"],        ["Plutonium Discovery","10 Transuranic Elements","Actinide Series"],                  [(1951,"Chemistry","Transuranic Elements")]),
    (145,"Archer Martin",          1910,2002,"England",        ["Chemistry"],                  ["Partition Chromatography","Gas-Liquid Chromatography"],                             [(1952,"Chemistry","Chromatography")]),
    (146,"Richard Synge",          1914,1994,"England",        ["Chemistry"],                  ["Partition Chromatography"],                                                         [(1952,"Chemistry","Chromatography")]),
    (147,"Hermann Staudinger",     1881,1965,"Germany",        ["Chemistry"],                  ["Polymer Chemistry","Macromolecules","Plastic Science"],                             [(1953,"Chemistry","Macromolecular Chemistry")]),
    (148,"Linus Pauling (2nd)",    1901,1994,"USA",            ["Chemistry"],                  ["Molecular Disease","Protein Alpha Helix"],                                          []),
    (149,"Vincent du Vigneaud",    1901,1978,"USA",            ["Chemistry"],                  ["Oxytocin Synthesis","Penicillin Structure","Biotin"],                               [(1955,"Chemistry","Oxytocin")]),
    (150,"Nikolay Semenov",        1896,1986,"Russia",         ["Chemistry","Physics"],        ["Chain Reactions","Combustion","Chemical Kinetics"],                                 [(1956,"Chemistry","Chain Reactions")]),
    # ── BIOLOGY & MEDICINE ────────────────────────────────────────────────────
    (151,"Charles Darwin",         1809,1882,"England",        ["Biology"],                    ["Theory of Evolution","Natural Selection","Origin of Species"],                       []),
    (152,"Gregor Mendel",          1822,1884,"Austria",        ["Biology","Genetics"],         ["Laws of Heredity","Genetics Foundations","Pea Plant Experiments"],                  []),
    (153,"Louis Pasteur",          1822,1895,"France",         ["Biology","Chemistry"],        ["Germ Theory","Pasteurization","Vaccination (Rabies, Anthrax)"],                     []),
    (154,"Robert Koch",            1843,1910,"Germany",        ["Medicine","Biology"],         ["Tuberculosis Bacillus","Koch's Postulates","Cholera Bacterium"],                    [(1905,"Medicine","Tuberculosis")]),
    (155,"Joseph Lister",          1827,1912,"England",        ["Medicine"],                   ["Antiseptic Surgery","Carbolic Acid Sterilization"],                                 []),
    (156,"Edward Jenner",          1749,1823,"England",        ["Medicine"],                   ["Smallpox Vaccine (first vaccine in history)"],                                      []),
    (157,"Alexander Fleming",      1881,1955,"Scotland",       ["Medicine","Biology"],         ["Penicillin Discovery","Lysozyme Discovery"],                                        [(1945,"Medicine","Penicillin")]),
    (158,"Howard Florey",          1898,1968,"Australia",      ["Medicine"],                   ["Penicillin Development and Purification"],                                          [(1945,"Medicine","Penicillin")]),
    (159,"Ernst Chain",            1906,1979,"Germany/England",["Medicine","Chemistry"],       ["Penicillin Purification","Beta-Lactam Chemistry"],                                  [(1945,"Medicine","Penicillin")]),
    (160,"James Watson",           1928,None,"USA",            ["Biology","Genetics"],         ["DNA Double Helix Structure","Molecular Biology"],                                   [(1962,"Medicine","DNA Structure")]),
    (161,"Francis Crick",          1916,2004,"England",        ["Biology","Physics"],          ["DNA Double Helix Structure","Genetic Code","Central Dogma"],                        [(1962,"Medicine","DNA Structure")]),
    (162,"Rosalind Franklin",      1920,1958,"England",        ["Chemistry","Biology"],        ["X-ray Crystallography of DNA","Virus Structures"],                                  []),
    (163,"Maurice Wilkins",        1916,2004,"New Zealand",    ["Physics","Biology"],          ["DNA X-ray Crystallography"],                                                        [(1962,"Medicine","DNA Structure")]),
    (164,"Frederick Sanger",       1918,2013,"England",        ["Chemistry","Biology"],        ["Insulin Sequencing","DNA Sequencing (Sanger Method)"],                              [(1958,"Chemistry","Insulin Structure"),(1980,"Chemistry","DNA Sequencing")]),
    (165,"Luc Montagnier",         1932,2022,"France",         ["Medicine","Biology"],         ["HIV Discovery"],                                                                    [(2008,"Medicine","HIV")]),
    (166,"Françoise Barré-Sinoussi",1947,None,"France",        ["Medicine","Biology"],         ["HIV Discovery"],                                                                    [(2008,"Medicine","HIV")]),
    (167,"Harald zur Hausen",      1936,None,"Germany",        ["Medicine"],                   ["Human Papillomavirus (HPV) causing Cancer"],                                        [(2008,"Medicine","HPV & Cancer")]),
    (168,"Barry Marshall",         1951,None,"Australia",      ["Medicine"],                   ["H. pylori Causes Ulcers (self-experimented)"],                                      [(2005,"Medicine","H. pylori")]),
    (169,"Robin Warren",           1937,None,"Australia",      ["Medicine"],                   ["H. pylori Discovery"],                                                              [(2005,"Medicine","H. pylori")]),
    (170,"Stanley Prusiner",       1942,None,"USA",            ["Medicine","Biology"],         ["Prion Discovery","Prion Diseases (BSE, CJD)"],                                     [(1997,"Medicine","Prions")]),
    (171,"Andrew Fire",            1959,None,"USA",            ["Biology"],                    ["RNA Interference (RNAi)"],                                                          [(2006,"Medicine","RNA Interference")]),
    (172,"Craig Mello",            1960,None,"USA",            ["Biology"],                    ["RNA Interference (RNAi)"],                                                          [(2006,"Medicine","RNA Interference")]),
    (173,"Shinya Yamanaka",        1962,None,"Japan",          ["Medicine","Biology"],         ["Induced Pluripotent Stem Cells (iPS Cells)"],                                       [(2012,"Medicine","Stem Cell Reprogramming")]),
    (174,"John Gurdon",            1933,None,"England",        ["Biology"],                    ["Nuclear Reprogramming","Cloning Frogs"],                                            [(2012,"Medicine","Nuclear Reprogramming")]),
    (175,"Yoshinori Ohsumi",       1945,None,"Japan",          ["Biology"],                    ["Autophagy Mechanisms"],                                                             [(2016,"Medicine","Autophagy")]),
    (176,"Svante Pääbo",           1955,None,"Sweden",         ["Biology","Genetics"],         ["Ancient DNA","Neanderthal Genome","Denisovan Discovery"],                           [(2022,"Medicine","Ancient Genomes")]),
    (177,"Jennifer Doudna",        1964,None,"USA",            ["Chemistry","Biology"],        ["CRISPR-Cas9 Gene Editing"],                                                         [(2020,"Chemistry","CRISPR Gene Editing")]),
    (178,"Emmanuelle Charpentier", 1968,None,"France",         ["Biology"],                    ["CRISPR-Cas9 Gene Editing"],                                                        [(2020,"Chemistry","CRISPR Gene Editing")]),
    (179,"Katalin Karikó",         1955,None,"Hungary/USA",    ["Medicine","Biochemistry"],    ["mRNA Technology for Vaccines","Modified mRNA"],                                     []),
    (180,"Drew Weissman",          1959,None,"USA",            ["Medicine"],                   ["mRNA Vaccine Technology"],                                                          [(2023,"Medicine","mRNA Vaccines")]),
    (181,"Katalin Karikó (Nobel)", 1955,None,"Hungary/USA",    ["Medicine"],                   ["mRNA modifications enabling COVID vaccines"],                                       [(2023,"Medicine","mRNA Vaccines")]),
    (182,"Elizabeth Blackburn",    1948,None,"Australia/USA",  ["Biology"],                    ["Telomeres","Telomerase Enzyme"],                                                    [(2009,"Medicine","Telomeres")]),
    (183,"Carol Greider",          1961,None,"USA",            ["Biology"],                    ["Telomerase Discovery"],                                                             [(2009,"Medicine","Telomeres")]),
    (184,"Jack Szostak",           1952,None,"England/USA",    ["Biology"],                    ["Telomeres","Origin of Life Research"],                                              [(2009,"Medicine","Telomeres")]),
    (185,"Eric Kandel",            1929,None,"Austria/USA",    ["Medicine","Neuroscience"],    ["Memory Storage in Neurons","Long-Term Potentiation"],                               [(2000,"Medicine","Memory Storage")]),
    (186,"Arvid Carlsson",         1923,2019,"Sweden",         ["Medicine"],                   ["Dopamine as Neurotransmitter","Parkinson's Disease Treatment"],                     [(2000,"Medicine","Dopamine")]),
    (187,"Paul Greengard",         1925,2019,"USA",            ["Medicine"],                   ["Signal Transduction in Nervous System"],                                            [(2000,"Medicine","Nervous System")]),
    (188,"Günter Blobel",          1936,2018,"Germany/USA",    ["Biology"],                    ["Proteins Have Intrinsic Signals","Protein Sorting"],                                [(1999,"Medicine","Protein Signals")]),
    (189,"Robert Edwards",         1925,2013,"England",        ["Medicine"],                   ["In Vitro Fertilization (IVF)","Test-Tube Baby"],                                    [(2010,"Medicine","IVF")]),
    (190,"Paul Nurse",             1949,None,"England",        ["Biology"],                    ["Cell Cycle Control","CDK Proteins"],                                                [(2001,"Medicine","Cell Cycle")]),
    (191,"Tim Hunt",               1943,None,"England",        ["Biology"],                    ["Cyclins Discovery","Cell Cycle Regulation"],                                        [(2001,"Medicine","Cell Cycle")]),
    (192,"Leland Hartwell",        1939,None,"USA",            ["Biology"],                    ["Cell Cycle Checkpoints"],                                                           [(2001,"Medicine","Cell Cycle")]),
    (193,"Christiane Nüsslein-Volhard",1942,None,"Germany",   ["Biology"],                    ["Genetic Control of Embryo Development","Drosophila Genes"],                         [(1995,"Medicine","Genetic Development")]),
    (194,"Eric Wieschaus",         1947,None,"USA",            ["Biology"],                    ["Drosophila Developmental Genetics"],                                                [(1995,"Medicine","Genetic Development")]),
    (195,"Edward Lewis",           1918,2004,"USA",            ["Biology"],                    ["Homeotic Genes","Hox Genes"],                                                       [(1995,"Medicine","Genetic Development")]),
    (196,"Mario Capecchi",         1937,None,"Italy/USA",      ["Biology"],                    ["Gene Targeting in Mice","Knockout Mice"],                                           [(2007,"Medicine","Gene Targeting")]),
    (197,"Martin Evans",           1941,None,"England",        ["Biology"],                    ["Embryonic Stem Cells"],                                                             [(2007,"Medicine","Stem Cells")]),
    (198,"Oliver Smithies",        1925,2017,"England/USA",    ["Biology"],                    ["Gene Targeting","Gel Electrophoresis"],                                             [(2007,"Medicine","Gene Targeting")]),
    (199,"Youyou Tu",              1930,None,"China",           ["Medicine"],                   ["Artemisinin for Malaria Treatment"],                                                [(2015,"Medicine","Malaria Therapy")]),
    (200,"William Campbell",       1930,None,"Ireland/USA",    ["Medicine"],                   ["Avermectin for Parasitic Diseases"],                                                [(2015,"Medicine","Roundworm Therapy")]),
    (201,"Satoshi Ōmura",          1935,None,"Japan",          ["Medicine","Chemistry"],       ["Avermectin Discovery"],                                                             [(2015,"Medicine","Roundworm Therapy")]),
    (202,"Phillip Sharp",          1944,None,"USA",            ["Biology"],                    ["RNA Splicing","Split Genes"],                                                       [(1993,"Medicine","RNA Splicing")]),
    (203,"Richard Roberts",        1943,None,"England",        ["Biology"],                    ["Split Genes","Restriction Enzymes"],                                                [(1993,"Medicine","Split Genes")]),
    (204,"Michael Bishop",         1936,None,"USA",            ["Medicine","Biology"],         ["Proto-oncogenes","Cancer Genetics"],                                                [(1989,"Medicine","Oncogenes")]),
    (205,"Harold Varmus",          1939,None,"USA",            ["Medicine","Biology"],         ["Oncogenes from Retroviruses"],                                                      [(1989,"Medicine","Oncogenes")]),
    (206,"James Rothman",          1950,None,"USA",            ["Biology"],                    ["Vesicle Transport Machinery"],                                                      [(2013,"Medicine","Vesicle Transport")]),
    (207,"Randy Schekman",         1948,None,"USA",            ["Biology"],                    ["Vesicle Transport Regulation"],                                                     [(2013,"Medicine","Vesicle Transport")]),
    (208,"Thomas Südhof",          1955,None,"Germany/USA",    ["Biology","Medicine"],         ["Neurotransmitter Release Mechanism"],                                               [(2013,"Medicine","Vesicle Transport")]),
    (209,"John O'Keefe",           1939,None,"USA/England",    ["Neuroscience"],               ["Place Cells in Hippocampus","Brain GPS"],                                           [(2014,"Medicine","Brain Navigation")]),
    (210,"May-Britt Moser",        1963,None,"Norway",         ["Neuroscience"],               ["Grid Cells","Brain Navigation System"],                                             [(2014,"Medicine","Brain Navigation")]),
    (211,"Edvard Moser",           1962,None,"Norway",         ["Neuroscience"],               ["Grid Cells","Entorhinal Cortex Navigation"],                                       [(2014,"Medicine","Brain Navigation")]),
    (212,"William Kaelin",         1957,None,"USA",            ["Medicine","Biology"],         ["Oxygen Sensing Mechanism in Cells"],                                               [(2019,"Medicine","Oxygen Sensing")]),
    (213,"Peter Ratcliffe",        1954,None,"England",        ["Medicine"],                   ["How Cells Sense Oxygen"],                                                           [(2019,"Medicine","Oxygen Sensing")]),
    (214,"Gregg Semenza",          1956,None,"USA",            ["Medicine"],                   ["HIF-1 Oxygen Sensing"],                                                             [(2019,"Medicine","Oxygen Sensing")]),
    (215,"Harvey Alter",           1935,None,"USA",            ["Medicine"],                   ["Hepatitis C Virus Discovery"],                                                      [(2020,"Medicine","Hepatitis C")]),
    (216,"Michael Houghton",       1949,None,"England/Canada", ["Medicine"],                   ["Hepatitis C Virus Discovery"],                                                      [(2020,"Medicine","Hepatitis C")]),
    (217,"Charles Rice",           1952,None,"USA",            ["Medicine"],                   ["Hepatitis C Virus (enabling replication)"],                                         [(2020,"Medicine","Hepatitis C")]),
    (218,"David Julius",           1955,None,"USA",            ["Medicine","Biology"],         ["Temperature & Pain Receptors (TRPV1)"],                                             [(2021,"Medicine","Temperature Receptors")]),
    (219,"Ardem Patapoutian",      1967,None,"Lebanon/USA",    ["Medicine","Biology"],         ["Pressure & Temperature Receptors (PIEZO)"],                                         [(2021,"Medicine","Touch Receptors")]),
    (220,"Seymour Benzer",         1921,2007,"USA",            ["Biology"],                    ["Behavioral Genetics","Neuroscience of Behavior"],                                   []),
    (221,"Barbara McClintock",     1902,1992,"USA",            ["Biology","Genetics"],         ["Transposons (Jumping Genes)","Maize Genetics"],                                     [(1983,"Medicine","Transposable Elements")]),
    (222,"Rita Levi-Montalcini",   1909,2012,"Italy",          ["Medicine","Biology"],         ["Nerve Growth Factor (NGF) Discovery"],                                             [(1986,"Medicine","Nerve Growth Factor")]),
    (223,"Gertrude Elion",         1918,1999,"USA",            ["Chemistry","Medicine"],       ["Leukemia Drugs","Antiviral Drugs","AZT for HIV"],                                   [(1988,"Medicine","Drug Treatment Principles")]),
    (224,"George Hitchings",       1905,1998,"USA",            ["Medicine","Chemistry"],       ["Rational Drug Design","Chemotherapy Drugs"],                                        [(1988,"Medicine","Drug Treatment")]),
    (225,"Joseph Goldstein",       1940,None,"USA",            ["Medicine"],                   ["Cholesterol Regulation","LDL Receptor"],                                            [(1985,"Medicine","Cholesterol")]),
    (226,"Michael Brown",          1941,None,"USA",            ["Medicine"],                   ["LDL Receptor","Cholesterol Metabolism"],                                            [(1985,"Medicine","Cholesterol")]),
    (227,"Cesar Milstein",         1927,2002,"Argentina/England",["Biology"],                  ["Monoclonal Antibodies"],                                                            [(1984,"Medicine","Monoclonal Antibodies")]),
    (228,"Georges Köhler",         1946,1995,"Germany",        ["Biology"],                    ["Monoclonal Antibodies (hybridoma technique)"],                                      [(1984,"Medicine","Monoclonal Antibodies")]),
    (229,"Niels Jerne",            1911,1994,"Denmark",        ["Medicine"],                   ["Immune System Theory","Network Theory of Immunity"],                                [(1984,"Medicine","Immune Theory")]),
    (230,"Walter Gilbert",         1932,None,"USA",            ["Chemistry","Biology"],        ["DNA Sequencing","Introns Concept"],                                                 [(1980,"Chemistry","DNA Sequencing")]),
    (231,"Paul Berg",              1926,2023,"USA",            ["Chemistry","Biology"],        ["Recombinant DNA Technology","Gene Splicing"],                                       [(1980,"Chemistry","Recombinant DNA")]),
    (232,"Hamilton Smith",         1931,None,"USA",            ["Biology"],                    ["Restriction Enzymes"],                                                              [(1978,"Medicine","Restriction Enzymes")]),
    (233,"Werner Arber",           1929,None,"Switzerland",    ["Biology"],                    ["Restriction Enzymes","DNA Modification"],                                           [(1978,"Medicine","Restriction Enzymes")]),
    (234,"Daniel Nathans",         1928,1999,"USA",            ["Biology"],                    ["Restriction Enzyme Mapping of SV40 Genome"],                                        [(1978,"Medicine","Restriction Enzymes")]),
    (235,"William Arther Lewis",   1915,1991,"Saint Lucia",    ["Economics"],                  ["Economic Development","Dual Sector Model"],                                         [(1979,"Economics","Developing Nations")]),
    # ── MATHEMATICS & COMPUTER SCIENCE ────────────────────────────────────────
    (236,"Archimedes",             -287,-212,"Greece (Sicily)",["Mathematics","Physics"],      ["Pi Calculation","Lever Principle","Archimedean Screw","Buoyancy Principle"],        []),
    (237,"Euclid",                 -300,-260,"Greece",         ["Mathematics"],                ["Euclidean Geometry","Elements (textbook)","Prime Number Theorem"],                  []),
    (238,"Pythagoras",             -570,-495,"Greece",         ["Mathematics"],                ["Pythagorean Theorem","Number Theory","Music Mathematics"],                          []),
    (239,"Leonhard Euler",         1707,1783,"Switzerland",    ["Mathematics"],                ["Euler's Identity","Graph Theory","Number Theory","Euler's Formula"],                []),
    (240,"Carl Friedrich Gauss",   1777,1855,"Germany",        ["Mathematics","Physics"],      ["Normal Distribution","Modular Arithmetic","Gauss's Law","Non-Euclidean Geometry"], []),
    (241,"Gottfried Wilhelm Leibniz",1646,1716,"Germany",      ["Mathematics","Philosophy"],   ["Calculus (co-inventor)","Binary System","Monadology"],                              []),
    (242,"Alan Turing",            1912,1954,"England",        ["Mathematics","Computing"],    ["Turing Machine","Computing Theory","Enigma Code Breaking","AI Concept"],            []),
    (243,"John von Neumann",       1903,1957,"Hungary/USA",    ["Mathematics","Physics"],      ["Von Neumann Architecture","Game Theory","Quantum Mechanics Formalism"],             []),
    (244,"Henri Poincaré",         1854,1912,"France",         ["Mathematics","Physics"],      ["Poincaré Conjecture","Chaos Theory","Topology","Special Relativity (partial)"],    []),
    (245,"David Hilbert",          1862,1943,"Germany",        ["Mathematics"],                ["Hilbert Space","Hilbert's 23 Problems","Formalism in Mathematics"],                 []),
    (246,"Bernhard Riemann",       1826,1866,"Germany",        ["Mathematics"],                ["Riemann Hypothesis","Riemannian Geometry","Riemann Integral"],                      []),
    (247,"Pierre-Simon Laplace",   1749,1827,"France",         ["Mathematics","Physics"],      ["Laplace Transform","Probability Theory","Celestial Mechanics"],                    []),
    (248,"Pierre de Fermat",       1607,1665,"France",         ["Mathematics"],                ["Fermat's Last Theorem","Number Theory","Analytic Geometry","Probability (co)"],   []),
    (249,"Georg Cantor",           1845,1918,"Germany",        ["Mathematics"],                ["Set Theory","Infinity Theory","Cardinal Numbers"],                                   []),
    (250,"Kurt Gödel",             1906,1978,"Austria/USA",    ["Mathematics","Logic"],        ["Incompleteness Theorems","Consistency of Axiom of Choice"],                         []),
    (251,"Emmy Noether",           1882,1935,"Germany",        ["Mathematics"],                ["Noether's Theorem","Abstract Algebra","Ring Theory"],                               []),
    (252,"Srinivasa Ramanujan",    1887,1920,"India",          ["Mathematics"],                ["Infinite Series","Ramanujan Prime","Mock Theta Functions","Number Theory"],          []),
    (253,"Andrew Wiles",           1953,None,"England",        ["Mathematics"],                ["Fermat's Last Theorem Proof"],                                                      []),
    (254,"Grigori Perelman",       1966,None,"Russia",         ["Mathematics"],                ["Poincaré Conjecture Proof","Geometrization Conjecture"],                             []),
    (255,"Terence Tao",            1975,None,"Australia",      ["Mathematics"],                ["Analytic Number Theory","Green-Tao Theorem","Compressed Sensing"],                  []),
    (256,"Maryam Mirzakhani",      1977,2017,"Iran",           ["Mathematics"],                ["Riemann Surfaces","Dynamics of Teichmüller Space","Fields Medal 2014"],             []),
    (257,"John Nash",              1928,2015,"USA",            ["Mathematics","Economics"],    ["Nash Equilibrium","Game Theory"],                                                   [(1994,"Economics","Game Theory")]),
    (258,"Paul Erdős",             1913,1996,"Hungary",        ["Mathematics"],                ["Graph Theory","Number Theory","Probabilistic Method","Ramsey Theory"],              []),
    (259,"G. H. Hardy",            1877,1947,"England",        ["Mathematics"],                ["Hardy-Weinberg Principle","Analytic Number Theory","Ramanujan Collaboration"],      []),
    (260,"Ada Lovelace",           1815,1852,"England",        ["Mathematics","Computing"],    ["First Computer Algorithm","Analytical Engine Programming"],                         []),
    (261,"Charles Babbage",        1791,1871,"England",        ["Mathematics","Engineering"],  ["Difference Engine","Analytical Engine (first computer concept)"],                   []),
    (262,"Claude Shannon",         1916,2001,"USA",            ["Mathematics","Engineering"],  ["Information Theory","Shannon Entropy","Digital Circuit Design"],                    []),
    (263,"Norbert Wiener",         1894,1964,"USA",            ["Mathematics"],                ["Cybernetics","Wiener Process","Control Theory"],                                    []),
    (264,"John McCarthy",          1927,2011,"USA",            ["Computing"],                  ["Artificial Intelligence (coined term)","LISP Language","Time-Sharing Systems"],     []),
    (265,"Marvin Minsky",          1927,2016,"USA",            ["Computing","AI"],             ["Perceptron","Neural Networks","AI Pioneer","Society of Mind"],                      []),
    (266,"Donald Knuth",           1938,None,"USA",            ["Computing","Mathematics"],    ["The Art of Computer Programming","TeX Typesetting","Algorithm Analysis"],           []),
    (267,"Edsger Dijkstra",        1930,2002,"Netherlands",    ["Computing"],                  ["Dijkstra's Algorithm","Structured Programming","Semaphores"],                       []),
    (268,"Grace Hopper",           1906,1992,"USA",            ["Computing"],                  ["COBOL Language","First Compiler","Debugging (named the bug)"],                      []),
    (269,"Dennis Ritchie",         1941,2011,"USA",            ["Computing"],                  ["C Programming Language","UNIX Operating System"],                                   []),
    (270,"Ken Thompson",           1943,None,"USA",            ["Computing"],                  ["UNIX Operating System","B Language","UTF-8 Encoding"],                              []),
    (271,"Linus Torvalds",         1969,None,"Finland",        ["Computing"],                  ["Linux Kernel","Git Version Control"],                                               []),
    (272,"Tim Berners-Lee",        1955,None,"England",        ["Computing","Engineering"],    ["World Wide Web","HTTP Protocol","HTML Language","URL"],                             []),
    (273,"Vint Cerf",              1943,None,"USA",            ["Computing","Engineering"],    ["TCP/IP Protocol (Father of the Internet)","Email Standards"],                       []),
    (274,"Geoffrey Hinton",        1947,None,"England/Canada", ["Computing","AI"],             ["Deep Learning","Backpropagation","Neural Networks"],                               [(2024,"Physics","Artificial Neural Networks")]),
    (275,"Yann LeCun",             1960,None,"France/USA",     ["Computing","AI"],             ["Convolutional Neural Networks (CNN)","Deep Learning"],                              []),
    (276,"Yoshua Bengio",          1964,None,"France/Canada",  ["Computing","AI"],             ["Deep Learning","Recurrent Neural Networks","GANs"],                                 []),
    (277,"John J. Hopfield",       1933,None,"USA",            ["Physics","AI"],               ["Hopfield Networks","Associative Memory","Neural Networks"],                          [(2024,"Physics","Artificial Neural Networks")]),
    (278,"Nikola Tesla",           1856,1943,"Serbia/USA",     ["Engineering","Physics"],      ["AC Electricity","Tesla Coil","Radio (contested)","Induction Motor"],                []),
    (279,"Thomas Edison",          1847,1931,"USA",            ["Engineering"],                ["Phonograph","Incandescent Light Bulb","Motion Picture Camera","Electric Grid"],     []),
    (280,"Guglielmo Marconi",      1874,1937,"Italy",          ["Engineering","Physics"],      ["Radio Telegraphy","Transatlantic Radio Signal"],                                    [(1909,"Physics","Wireless Telegraphy")]),
    (281,"Alexander Graham Bell",  1847,1922,"Scotland/USA",   ["Engineering"],                ["Telephone Invention","Photophone","Metal Detector"],                               []),
    (282,"James Watt",             1736,1819,"Scotland",       ["Engineering"],                ["Steam Engine Improvement","Watt Unit of Power","Rotary Motion"],                   []),
    (283,"Orville Wright",         1871,1948,"USA",            ["Engineering"],                ["First Powered Airplane"],                                                            []),
    (284,"Wilbur Wright",          1867,1912,"USA",            ["Engineering"],                ["First Powered Airplane"],                                                            []),
    (285,"Jack Kilby",             1923,2005,"USA",            ["Engineering","Physics"],      ["Integrated Circuit (IC Chip)"],                                                     [(2000,"Physics","Integrated Circuit")]),
    (286,"Hedy Lamarr",            1914,2000,"Austria/USA",    ["Engineering","Physics"],      ["Frequency-Hopping Spread Spectrum (basis of WiFi/GPS/Bluetooth)"],                 []),
    (287,"Grace Hopper",           1906,1992,"USA",            ["Computing"],                  ["COBOL Language","Compiler","Debugging"],                                             []),
    (288,"Alfred Wegener",         1880,1930,"Germany",        ["Earth Sciences"],             ["Continental Drift Theory","Plate Tectonics (foundation)"],                          []),
    (289,"Mario Molina",           1943,2020,"Mexico/USA",     ["Chemistry","Earth Sciences"], ["Ozone Layer Depletion (CFCs)"],                                                    [(1995,"Chemistry","Ozone Layer")]),
    (290,"Paul Crutzen",           1933,2021,"Netherlands",    ["Chemistry","Earth Sciences"], ["Ozone Chemistry","Nitrogen Oxide Catalysis"],                                       [(1995,"Chemistry","Ozone Layer")]),
    (291,"Svante Arrhenius",       1859,1927,"Sweden",         ["Chemistry","Earth Sciences"], ["Greenhouse Effect Calculation","Ionic Dissociation"],                              [(1903,"Chemistry","Ionic Theory")]),
    (292,"Hippocrates",            -460,-370,"Greece",         ["Medicine"],                   ["Father of Medicine","Hippocratic Oath","Clinical Observation"],                     []),
    (293,"Aristotle",              -384,-322,"Greece",         ["Philosophy","Biology"],       ["Logic","Taxonomy","Physics","Zoology"],                                              []),
    (294,"Avicenna (Ibn Sina)",    980, 1037,"Persia (Iran)",  ["Medicine","Philosophy"],      ["Canon of Medicine","Medical Encyclopedia","Pharmacology"],                          []),
    (295,"Al-Khwarizmi",           780, 850, "Persia/Uzbekistan",["Mathematics"],              ["Algebra (invented)","Algorithm (name origin)","Hindu-Arabic Numerals"],             []),
    (296,"Ibn al-Haytham",         965, 1040,"Iraq",           ["Physics","Mathematics"],      ["Book of Optics","Pinhole Camera","Scientific Method Pioneer"],                      []),
    (297,"Al-Biruni",              973, 1048,"Persia/Uzbekistan",["Mathematics","Astronomy"],  ["Earth's Circumference","Specific Gravity","Pharmacy"],                             []),
    (298,"Francis Bacon",          1561,1626,"England",        ["Philosophy","Science"],       ["Scientific Method (Baconian Method)","Inductive Reasoning"],                        []),
    (299,"William Harvey",         1578,1657,"England",        ["Medicine"],                   ["Blood Circulation Discovery","Heart as Pump"],                                      []),
    (300,"Carl Linnaeus",          1707,1778,"Sweden",         ["Biology"],                    ["Binomial Nomenclature","Taxonomy System","Species Classification"],                  []),
    (301,"Dorothy Hodgkin",        1910,1994,"Egypt/England",  ["Chemistry","Biology"],        ["X-ray Crystallography","Penicillin Structure","Insulin Structure","Vitamin B12"],   [(1964,"Chemistry","X-ray Crystallography")]),
    (302,"Robert Woodward",        1917,1979,"USA",            ["Chemistry"],                  ["Organic Synthesis (Quinine, Cholesterol, Strychnine)"],                            [(1965,"Chemistry","Organic Synthesis")]),
    (303,"Kary Mullis",            1944,2019,"USA",            ["Chemistry","Biology"],        ["PCR (Polymerase Chain Reaction) Invention"],                                        [(1993,"Chemistry","PCR")]),
    (304,"Jennifer Doudna",        1964,None,"USA",            ["Chemistry","Biology"],        ["CRISPR-Cas9 Gene Editing"],                                                         [(2020,"Chemistry","CRISPR Gene Editing")]),
    (305,"Emmanuelle Charpentier", 1968,None,"France",         ["Biology"],                    ["CRISPR-Cas9 Gene Editing"],                                                        [(2020,"Chemistry","CRISPR Gene Editing")]),
    (306,"Katalin Karikó",         1955,None,"Hungary/USA",    ["Medicine","Biochemistry"],    ["mRNA Technology for Vaccines"],                                                     [(2023,"Medicine","mRNA Vaccines")]),
    (307,"Norman Borlaug",         1914,2009,"USA",            ["Biology","Agriculture"],      ["Green Revolution","Wheat Varieties","Saved ~1 billion lives from famine"],          [(1970,"Peace","Food Production")]),
    (308,"Santiago Ramón y Cajal", 1852,1934,"Spain",          ["Medicine","Biology"],         ["Neuron Doctrine","Brain Histology"],                                                [(1906,"Medicine","Nervous System")]),
    (309,"Ivan Pavlov",            1849,1936,"Russia",         ["Medicine","Biology"],         ["Classical Conditioning","Pavlovian Reflex","Digestive System"],                     [(1904,"Medicine","Digestive Physiology")]),
    (310,"Karl Landsteiner",       1868,1943,"Austria/USA",    ["Medicine"],                   ["Blood Type Discovery (ABO System)","Rhesus Factor (Rh)","Polio Virus"],            [(1930,"Medicine","Blood Groups")]),
    (311,"Frederick Banting",      1891,1941,"Canada",         ["Medicine"],                   ["Insulin Discovery (Diabetes Treatment)"],                                           [(1923,"Medicine","Insulin")]),
    (312,"Barbara McClintock",     1902,1992,"USA",            ["Biology","Genetics"],         ["Transposons (Jumping Genes)","Maize Genetics"],                                     [(1983,"Medicine","Transposable Elements")]),
    (313,"Rita Levi-Montalcini",   1909,2012,"Italy",          ["Medicine","Biology"],         ["Nerve Growth Factor (NGF) Discovery"],                                             [(1986,"Medicine","Nerve Growth Factor")]),
    (314,"Gertrude Elion",         1918,1999,"USA",            ["Chemistry","Medicine"],       ["Leukemia Drugs","Antiviral Drugs","AZT for HIV"],                                   [(1988,"Medicine","Drug Treatment Principles")]),
    (315,"Donna Strickland",       1959,None,"Canada",         ["Physics"],                    ["Chirped Pulse Amplification (Ultrashort High-Intensity Lasers)"],                   [(2018,"Physics","Laser Pulses")]),
    (316,"Youyou Tu",              1930,None,"China",          ["Medicine"],                   ["Artemisinin for Malaria Treatment"],                                                [(2015,"Medicine","Malaria Therapy")]),
    (317,"Paul Samuelson",         1915,2009,"USA",            ["Economics"],                  ["Modern Economics","Neoclassical Synthesis","Consumer Theory"],                       [(1970,"Economics","Scientific Analysis of Economics")]),
    (318,"Milton Friedman",        1912,2006,"USA",            ["Economics"],                  ["Monetarism","Free Market Advocacy"],                                                [(1976,"Economics","Monetary History")]),
    (319,"Daniel Kahneman",        1934,2024,"Israel/USA",     ["Psychology","Economics"],     ["Prospect Theory","Behavioral Economics","Cognitive Biases"],                        [(2002,"Economics","Behavioral Economics")]),
    (320,"Amartya Sen",            1933,None,"India/England",  ["Economics"],                  ["Welfare Economics","Capability Approach","Social Choice Theory"],                   [(1998,"Economics","Welfare Economics")]),
    (321,"James Lovelock",         1919,2022,"England",        ["Earth Sciences","Biology"],   ["Gaia Hypothesis","Electron Capture Detector"],                                      []),
    (322,"Lynn Margulis",          1938,2011,"USA",            ["Biology"],                    ["Endosymbiotic Theory","Serial Endosymbiosis"],                                      []),
    (323,"E.O. Wilson",            1929,2021,"USA",            ["Biology"],                    ["Sociobiology","Biodiversity","Island Biogeography"],                                []),
    (324,"Ronald Fisher",          1890,1962,"England",        ["Mathematics","Biology"],      ["Analysis of Variance","Maximum Likelihood","Modern Synthesis"],                     []),
    (325,"Sewall Wright",          1889,1988,"USA",            ["Biology","Mathematics"],      ["Genetic Drift","Fitness Landscape","Population Genetics"],                          []),
    (326,"Lev Vygotsky",           1896,1934,"Russia",         ["Psychology"],                 ["Zone of Proximal Development","Sociocultural Theory"],                              []),
    (327,"Jean Piaget",            1896,1980,"Switzerland",    ["Psychology","Biology"],       ["Cognitive Development Stages","Schema Theory"],                                     []),
    (328,"Sigmund Freud",          1856,1939,"Austria",        ["Medicine","Psychology"],      ["Psychoanalysis","Unconscious Mind","Id/Ego/Superego"],                              []),
    (329,"B.F. Skinner",           1904,1990,"USA",            ["Psychology"],                 ["Operant Conditioning","Behaviorism","Skinner Box"],                                 []),
    (330,"Konrad Lorenz",          1903,1989,"Austria",        ["Biology","Psychology"],       ["Imprinting","Ethology","Animal Behavior"],                                          [(1973,"Medicine","Animal Behavior")]),
    (331,"George Church",          1954,None,"USA",            ["Biology","Genetics"],         ["Whole-Genome Sequencing","CRISPR Pioneer","Synthetic Biology"],                     []),
    (332,"Craig Venter",           1946,None,"USA",            ["Biology","Genetics"],         ["Human Genome Project (private)","Synthetic Cell","Shotgun Sequencing"],             []),
    (333,"Francis Collins",        1950,None,"USA",            ["Biology","Genetics"],         ["Human Genome Project (director)","BRCA1 Gene"],                                     []),
    (334,"Har Gobind Khorana",     1922,2011,"India/USA",      ["Chemistry","Biology"],        ["Genetic Code Interpretation","First Synthetic Gene"],                              [(1968,"Medicine","Genetic Code")]),
    (335,"Marshall Nirenberg",     1927,2010,"USA",            ["Biology","Chemistry"],        ["Genetic Code Cracking (UUU = Phenylalanine)"],                                     [(1968,"Medicine","Genetic Code")]),
    (336,"François Jacob",         1920,2013,"France",         ["Biology","Medicine"],         ["Lac Operon","mRNA Concept","Gene Regulation"],                                     [(1965,"Medicine","Gene Control")]),
    (337,"Jacques Monod",          1910,1976,"France",         ["Biology","Chemistry"],        ["Lac Operon (co-discovery)","Allosteric Regulation"],                               [(1965,"Medicine","Gene Control")]),
    (338,"Motoo Kimura",           1924,1994,"Japan",          ["Biology","Mathematics"],      ["Neutral Theory of Molecular Evolution","Population Genetics"],                     []),
    (339,"Theodosius Dobzhansky",  1900,1975,"Ukraine/USA",    ["Biology","Genetics"],         ["Modern Synthesis","Genetics and the Origin of Species"],                            []),
    (340,"Ernst Mayr",             1904,2005,"Germany/USA",    ["Biology"],                    ["Modern Evolutionary Synthesis","Biological Species Concept"],                       []),
    (341,"Peter Higgs",            1929,2024,"England",        ["Physics"],                    ["Higgs Boson (God Particle)","Higgs Mechanism"],                                     [(2013,"Physics","Higgs Mechanism")]),
    (342,"Saul Perlmutter",        1959,None,"USA",            ["Cosmology"],                  ["Accelerating Universe","Dark Energy Discovery"],                                    [(2011,"Physics","Accelerating Universe")]),
    (343,"Fred Hoyle",             1915,2001,"England",        ["Astronomy"],                  ["Stellar Nucleosynthesis","Big Bang (named it)","Carbon Resonance"],                 []),
    (344,"William Herschel",       1738,1822,"Germany/England",["Astronomy"],                  ["Uranus Discovery","Infrared Radiation","Binary Stars"],                             []),
    (345,"Henry Cavendish",        1731,1810,"England",        ["Physics","Chemistry"],        ["Cavendish Experiment (G constant)","Hydrogen Discovery"],                           []),
    (346,"Lord Rayleigh",          1842,1919,"England",        ["Physics"],                    ["Rayleigh Scattering","Argon Discovery"],                                            [(1904,"Physics","Gas Densities")]),
    (347,"J. Robert Oppenheimer",  1904,1967,"USA",            ["Physics"],                    ["Manhattan Project (Director)","Neutron Star Prediction"],                           []),
    (348,"Hideki Yukawa",          1907,1981,"Japan",          ["Physics"],                    ["Meson Theory","Nuclear Force Prediction"],                                           [(1949,"Physics","Nuclear Forces")]),
    (349,"Walter Brattain",        1902,1987,"China/USA",      ["Physics"],                    ["Transistor Co-Invention"],                                                          [(1956,"Physics","Transistor")]),
    (350,"Frank Wilczek",          1951,None,"USA",            ["Physics"],                    ["Asymptotic Freedom","Anyons","Axion"],                                               [(2004,"Physics","Strong Force")]),
    (351,"Murray Gell-Mann",       1929,2019,"USA",            ["Physics"],                    ["Quarks Discovery","Strangeness","Eightfold Way"],                                   [(1969,"Physics","Quarks")]),
    (352,"Carlo Rubbia",           1934,None,"Italy",          ["Physics"],                    ["W and Z Boson Discovery"],                                                          [(1984,"Physics","W/Z Bosons")]),
    (353,"Chien-Shiung Wu",        1912,1997,"China/USA",      ["Physics"],                    ["Parity Non-Conservation Experiment","Beta Decay"],                                  []),
    (354,"Lev Landau",             1908,1968,"Azerbaijan/USSR",["Physics"],                    ["Landau Levels","Fermi Liquid Theory","Superfluidity"],                              [(1962,"Physics","Condensed Matter")]),
    (355,"Dennis Gabor",           1900,1979,"Hungary/England",["Physics"],                    ["Holography Invention"],                                                             [(1971,"Physics","Holography")]),
    (356,"Max von Laue",           1879,1960,"Germany",        ["Physics"],                    ["X-ray Diffraction in Crystals"],                                                   [(1914,"Physics","X-ray Diffraction")]),
    (357,"James Franck",           1882,1964,"Germany/USA",    ["Physics"],                    ["Franck-Hertz Experiment","Atomic Excitation"],                                      [(1925,"Physics","Atomic Excitation")]),
    (358,"Arthur Compton",         1892,1962,"USA",            ["Physics"],                    ["Compton Effect (X-ray scattering)","Cosmic Ray Research"],                          [(1927,"Physics","Compton Effect")]),
    (359,"Heike Kamerlingh Onnes", 1853,1926,"Netherlands",    ["Physics"],                    ["Liquid Helium","Superconductivity Discovery"],                                      [(1913,"Physics","Low Temperature")]),
    (360,"Owen Richardson",        1879,1959,"England",        ["Physics"],                    ["Thermionic Emission","Richardson's Law"],                                           [(1928,"Physics","Thermionic Phenomenon")]),
    (361,"Walther Bothe",          1891,1957,"Germany",        ["Physics"],                    ["Coincidence Method in Nuclear Physics"],                                            [(1954,"Physics","Coincidence Method")]),
    (362,"William Bragg",          1890,1971,"Australia/England",["Physics"],                  ["X-ray Crystallography (with father)","Bragg's Law"],                               [(1915,"Physics","Crystal X-ray Analysis")]),
    (363,"Pieter Zeeman",          1865,1943,"Netherlands",    ["Physics"],                    ["Zeeman Effect (magnetic field on spectral lines)"],                                 [(1902,"Physics","Zeeman Effect")]),
    (364,"Harald zur Hausen",      1936,None,"Germany",        ["Medicine"],                   ["Human Papillomavirus (HPV) causing Cancer"],                                        [(2008,"Medicine","HPV & Cancer")]),
    (365,"James Allison",          1948,None,"USA",            ["Medicine","Biology"],         ["Cancer Immunotherapy (CTLA-4 Checkpoint)"],                                         [(2018,"Medicine","Cancer Immunotherapy")]),
    (366,"Tasuku Honjo",           1942,None,"Japan",          ["Medicine","Biology"],         ["Cancer Immunotherapy (PD-1 Checkpoint)"],                                           [(2018,"Medicine","Cancer Immunotherapy")]),
    (367,"Sidney Altman",          1939,2022,"Canada/USA",     ["Chemistry","Biology"],        ["RNA as Enzyme (Ribozyme) co-discovery"],                                           [(1989,"Chemistry","RNA Catalysis")]),
    (368,"Thomas Cech",            1947,None,"USA",            ["Chemistry","Biology"],        ["Ribozyme Discovery (RNA Catalyst)"],                                               [(1989,"Chemistry","RNA Catalysis")]),
    (369,"Walter Gilbert",         1932,None,"USA",            ["Chemistry","Biology"],        ["DNA Sequencing","Introns"],                                                         [(1980,"Chemistry","DNA Sequencing")]),
    (370,"Paul Berg",              1926,2023,"USA",            ["Chemistry","Biology"],        ["Recombinant DNA Technology","Gene Splicing"],                                       [(1980,"Chemistry","Recombinant DNA")]),
    (371,"Hamilton Smith",         1931,None,"USA",            ["Biology"],                    ["Restriction Enzymes"],                                                              [(1978,"Medicine","Restriction Enzymes")]),
    (372,"David Baltimore",        1938,None,"USA",            ["Biology","Medicine"],         ["Reverse Transcriptase","HIV Research","Tumor Viruses"],                            [(1975,"Medicine","Viral Genes")]),
    (373,"Howard Temin",           1934,1994,"USA",            ["Biology","Medicine"],         ["Reverse Transcriptase (co-discovery)","Provirus"],                                 [(1975,"Medicine","Viral Genes")]),
    (374,"Karl von Frisch",        1886,1982,"Austria",        ["Biology"],                    ["Bee Communication (Waggle Dance)","Ethology"],                                      [(1973,"Medicine","Animal Behavior")]),
    (375,"Nikolaas Tinbergen",     1907,1988,"Netherlands",    ["Biology"],                    ["Four Questions of Behavior","Ethology"],                                            [(1973,"Medicine","Animal Behavior")]),
    (376,"Gerald Edelman",         1929,2014,"USA",            ["Medicine","Chemistry"],       ["Antibody Chemical Structure","Neural Darwinism"],                                  [(1972,"Medicine","Antibody Structure")]),
    (377,"George Palade",          1912,2008,"Romania/USA",    ["Biology","Medicine"],         ["Ribosome Structure","Secretory Pathway"],                                          [(1974,"Medicine","Cell Structure")]),
    (378,"Christian de Duve",      1917,2013,"England/Belgium",["Biology","Medicine"],         ["Lysosome Discovery","Peroxisome"],                                                 [(1974,"Medicine","Cell Structure")]),
    (379,"Earl Sutherland",        1915,1974,"USA",            ["Medicine","Chemistry"],       ["Cyclic AMP Discovery","Second Messenger Concept"],                                 [(1971,"Medicine","Cyclic AMP")]),
    (380,"Roger Guillemin",        1924,None,"France/USA",     ["Medicine","Chemistry"],       ["Hypothalamic Hormones","TRH and Somatostatin"],                                    [(1977,"Medicine","Brain Hormones")]),
    (381,"Rosalyn Yalow",          1921,2011,"USA",            ["Medicine","Physics"],         ["Radioimmunoassay (RIA) for Insulin"],                                              [(1977,"Medicine","Radioimmunoassay")]),
    (382,"Baruch Blumberg",        1925,2011,"USA",            ["Medicine","Biology"],         ["Hepatitis B Virus Discovery","Hepatitis B Vaccine"],                               [(1976,"Medicine","Hepatitis B")]),
    (383,"Peyton Rous",            1879,1970,"USA",            ["Medicine","Biology"],         ["First Cancer Virus (Rous Sarcoma Virus)"],                                         [(1966,"Medicine","Tumor Viruses")]),
    (384,"François Jacob",         1920,2013,"France",         ["Biology","Medicine"],         ["Lac Operon","mRNA Concept"],                                                        [(1965,"Medicine","Gene Control")]),
    (385,"Konrad Bloch",           1912,2000,"Germany/USA",    ["Chemistry","Medicine"],       ["Cholesterol Biosynthesis","Fatty Acid Metabolism"],                                 [(1964,"Medicine","Cholesterol Synthesis")]),
    (386,"John Eccles",            1903,1997,"Australia",      ["Medicine","Biology"],         ["Synaptic Transmission","Ionic Mechanisms"],                                         [(1963,"Medicine","Nerve Cells")]),
    (387,"Alan Hodgkin",           1914,1998,"England",        ["Medicine","Biology"],         ["Action Potential","Hodgkin-Huxley Model"],                                          [(1963,"Medicine","Nerve Impulse")]),
    (388,"Andrew Huxley",          1917,2012,"England",        ["Medicine","Biology"],         ["Hodgkin-Huxley Model","Sliding Filament Theory of Muscle"],                         [(1963,"Medicine","Nerve Impulse")]),
    (389,"George Wald",            1906,1997,"USA",            ["Medicine","Biology"],         ["Visual Pigments","Retinal Chemistry"],                                              [(1967,"Medicine","Eye Physiology")]),
    (390,"August Krogh",           1874,1949,"Denmark",        ["Medicine","Biology"],         ["Capillary Motor Regulation","Respiratory Exchange"],                               [(1920,"Medicine","Capillaries")]),
    (391,"Frederick Hopkins",      1861,1947,"England",        ["Medicine","Chemistry"],       ["Vitamins Discovery (accessory food factors)","Essential Amino Acids"],             [(1929,"Medicine","Vitamins")]),
    (392,"Christiaan Eijkman",     1858,1930,"Netherlands",    ["Medicine"],                   ["Beriberi Cause (Thiamine Deficiency)","Vitamin Concept"],                           [(1929,"Medicine","Vitamins")]),
    (393,"Otto Warburg",           1883,1970,"Germany",        ["Medicine","Chemistry"],       ["Warburg Effect (Cancer Metabolism)","Photosynthesis Research"],                     [(1931,"Medicine","Cell Respiration")]),
    (394,"Willem Einthoven",       1860,1927,"Netherlands",    ["Medicine","Physics"],         ["Electrocardiogram (ECG/EKG)"],                                                      [(1924,"Medicine","ECG")]),
    (395,"Paul Ehrlich",           1854,1915,"Germany",        ["Medicine","Chemistry"],       ["Chemotherapy","Arsphenamine (Salvarsan)","Magic Bullet Concept"],                  [(1908,"Medicine","Immunity")]),
    (396,"Élie Metchnikoff",       1845,1916,"Russia/France",  ["Medicine","Biology"],         ["Phagocytosis","Innate Immunity"],                                                   [(1908,"Medicine","Immunity")]),
    (397,"Alexis Carrel",          1873,1944,"France/USA",     ["Medicine"],                   ["Organ Transplantation Techniques","Vascular Suturing","Tissue Culture"],            [(1912,"Medicine","Vascular Suture")]),
    (398,"Archibald Hill",         1886,1977,"England",        ["Medicine","Biology"],         ["Muscle Physiology","Heat Production in Muscle"],                                    [(1922,"Medicine","Muscle Heat")]),
    (399,"Frederick Soddy",        1877,1956,"England",        ["Chemistry","Physics"],        ["Isotopes","Radioactive Decay"],                                                     [(1921,"Chemistry","Radioactive Substances")]),
    (400,"Peter Debye",            1884,1966,"Netherlands/USA",["Chemistry","Physics"],        ["Debye-Hückel Theory","Dipole Moments","X-ray Diffraction"],                         [(1936,"Chemistry","Dipole Moments")]),
    (401,"Hermann Staudinger",     1881,1965,"Germany",        ["Chemistry"],                  ["Polymer Chemistry","Macromolecules","Plastic Science"],                             [(1953,"Chemistry","Macromolecular Chemistry")]),
    (402,"Nikolay Semenov",        1896,1986,"Russia",         ["Chemistry","Physics"],        ["Chain Reactions","Combustion","Chemical Kinetics"],                                 [(1956,"Chemistry","Chain Reactions")]),
    (403,"Ilya Prigogine",         1917,2003,"Russia/Belgium", ["Chemistry","Physics"],        ["Dissipative Structures","Non-Equilibrium Thermodynamics"],                          [(1977,"Chemistry","Dissipative Structures")]),
    (404,"Lars Onsager",           1903,1976,"Norway/USA",     ["Chemistry","Physics"],        ["Onsager Reciprocal Relations","Non-Equilibrium Thermodynamics"],                    [(1968,"Chemistry","Irreversible Processes")]),
    (405,"Luis Federico Leloir",   1906,1987,"Argentina",      ["Chemistry","Biology"],        ["Nucleotide Sugar Coenzymes","Lactose Metabolism"],                                  [(1970,"Chemistry","Sugar Nucleotides")]),
    (406,"Richard Ernst",          1933,2021,"Switzerland",    ["Chemistry","Physics"],        ["NMR Spectroscopy (High-Resolution)","MRI Technology"],                             [(1991,"Chemistry","NMR Spectroscopy")]),
    (407,"Elias Corey",            1928,None,"USA",            ["Chemistry"],                  ["Retrosynthetic Analysis","Organic Synthesis"],                                     [(1990,"Chemistry","Organic Synthesis")]),
    (408,"Rudolph Marcus",         1923,None,"Canada/USA",     ["Chemistry"],                  ["Marcus Theory of Electron Transfer"],                                               [(1992,"Chemistry","Electron Transfer")]),
    (409,"Aaron Klug",             1926,2018,"Lithuania/England",["Chemistry","Biology"],       ["Crystallographic Electron Microscopy","Virus Structure"],                           [(1982,"Chemistry","Crystallography")]),
    (410,"Robert Woodward",        1917,1979,"USA",            ["Chemistry"],                  ["Organic Synthesis","Quinine","Cholesterol","Strychnine","Vitamin B12 Synthesis"],   [(1965,"Chemistry","Organic Synthesis")]),
    (411,"Vincent du Vigneaud",    1901,1978,"USA",            ["Chemistry"],                  ["Oxytocin Synthesis","Penicillin Structure","Biotin"],                               [(1955,"Chemistry","Oxytocin")]),
    (412,"Linus Pauling",          1901,1994,"USA",            ["Chemistry"],                  ["Chemical Bonds","Molecular Biology","Alpha Helix","DNA Research"],                  [(1954,"Chemistry","Chemical Bonds"),(1962,"Peace","Nuclear Test Ban")]),
    (413,"Harold Urey",            1893,1981,"USA",            ["Chemistry","Physics"],        ["Deuterium Discovery","Urey-Miller Experiment"],                                     [(1934,"Chemistry","Heavy Hydrogen")]),
    (414,"Irving Langmuir",        1881,1957,"USA",            ["Chemistry","Physics"],        ["Surface Chemistry","Langmuir Adsorption","Cloud Seeding"],                          [(1932,"Chemistry","Surface Chemistry")]),
    (415,"Peter Medawar",          1915,1987,"Brazil/England", ["Medicine","Biology"],         ["Acquired Immunological Tolerance","Organ Transplant Immunology"],                   [(1960,"Medicine","Immunological Tolerance")]),
    (416,"Frank Macfarlane Burnet",1899,1985,"Australia",      ["Medicine","Biology"],         ["Clonal Selection Theory","Immune System"],                                          [(1960,"Medicine","Immunological Tolerance")]),
    (417,"George Beadle",          1903,1989,"USA",            ["Biology","Genetics"],         ["One Gene-One Enzyme Hypothesis"],                                                  [(1958,"Medicine","Genetic Control of Biochemistry")]),
    (418,"Edward Tatum",           1909,1975,"USA",            ["Biology","Genetics"],         ["One Gene-One Enzyme (co-discovery)","Bacterial Genetics"],                          [(1958,"Medicine","Genetic Control of Biochemistry")]),
    (419,"Joshua Lederberg",       1925,2008,"USA",            ["Biology","Genetics"],         ["Bacterial Conjugation","Exobiology","Plasmids"],                                   [(1958,"Medicine","Bacterial Genetics")]),
    (420,"André Cournand",         1895,1988,"France/USA",     ["Medicine"],                   ["Cardiac Catheterization"],                                                          [(1956,"Medicine","Cardiac Catheterization")]),
    (421,"Werner Forssmann",       1904,1979,"Germany",        ["Medicine"],                   ["Cardiac Catheterization (self-experimented)"],                                      [(1956,"Medicine","Cardiac Catheterization")]),
    (422,"Dickinson Richards",     1895,1973,"USA",            ["Medicine"],                   ["Cardiac Catheterization Diagnostics"],                                             [(1956,"Medicine","Cardiac Catheterization")]),
    (423,"Hugo Theorell",          1903,1982,"Sweden",         ["Medicine","Chemistry"],       ["Oxidation Enzymes","Cytochrome c"],                                                 [(1955,"Medicine","Oxidation Enzymes")]),
    (424,"John Enders",            1897,1985,"USA",            ["Medicine","Biology"],         ["Polio Virus Culture in Lab (enabled vaccine)"],                                    [(1954,"Medicine","Polio Virus Culture")]),
    (425,"Jonas Salk",             1914,1995,"USA",            ["Medicine"],                   ["Polio Vaccine (Salk Vaccine)"],                                                     []),
    (426,"Albert Sabin",           1906,1993,"Poland/USA",     ["Medicine"],                   ["Oral Polio Vaccine (Sabin Vaccine)"],                                               []),
    (427,"Max Theiler",            1899,1972,"South Africa/USA",["Medicine"],                  ["Yellow Fever Vaccine"],                                                             [(1951,"Medicine","Yellow Fever Vaccine")]),
    (428,"Philip Hench",           1896,1965,"USA",            ["Medicine"],                   ["Cortisone Discovery and Use"],                                                      [(1950,"Medicine","Cortisone")]),
    (429,"Edward Kendall",         1886,1972,"USA",            ["Medicine","Chemistry"],       ["Cortisone Isolation","Thyroid Hormone"],                                            [(1950,"Medicine","Cortisone")]),
    (430,"Tadeus Reichstein",      1897,1996,"Poland/Switzerland",["Chemistry","Medicine"],    ["Cortisone Synthesis","Vitamin C"],                                                  [(1950,"Medicine","Cortisone")]),
    (431,"Walter Hess",            1881,1973,"Switzerland",    ["Medicine"],                   ["Interbrain Function","Hypothalamus Control"],                                       [(1949,"Medicine","Interbrain")]),
    (432,"Otto Loewi",             1873,1961,"Germany/USA",    ["Medicine","Chemistry"],       ["Chemical Neurotransmission","Vagustoff (Acetylcholine)"],                           [(1936,"Medicine","Nerve Impulse Transmission")]),
    (433,"Henry Dale",             1875,1968,"England",        ["Medicine","Chemistry"],       ["Acetylcholine","Histamine","Chemical Neurotransmission"],                           [(1936,"Medicine","Nerve Impulse Transmission")]),
    (434,"George Whipple",         1878,1976,"USA",            ["Medicine"],                   ["Liver Therapy for Pernicious Anemia"],                                             [(1934,"Medicine","Pernicious Anemia")]),
    (435,"George Minot",           1885,1950,"USA",            ["Medicine"],                   ["Liver Diet for Pernicious Anemia"],                                                [(1934,"Medicine","Pernicious Anemia")]),
    (436,"William Murphy",         1892,1987,"USA",            ["Medicine"],                   ["Liver Treatment for Pernicious Anemia"],                                           [(1934,"Medicine","Pernicious Anemia")]),
    (437,"Thomas Morgan",          1866,1945,"USA",            ["Biology","Genetics"],         ["Chromosome Theory of Heredity","Drosophila Genetics"],                             [(1933,"Medicine","Chromosomes")]),
    (438,"Otto Meyerhof",          1884,1951,"Germany",        ["Medicine","Chemistry"],       ["Lactic Acid in Muscles","Glycolysis Energy"],                                       [(1922,"Medicine","Muscle Metabolism")]),
    (439,"Archibald Garrod",       1857,1936,"England",        ["Medicine","Chemistry"],       ["Inborn Errors of Metabolism","Biochemical Genetics"],                              []),
    (440,"Francis Galton",         1822,1911,"England",        ["Mathematics","Biology"],      ["Statistics","Standard Deviation","Fingerprinting"],                                 []),
    (441,"Charles Sherrington",    1857,1952,"England",        ["Medicine","Biology"],         ["Synapse Concept","Nervous System Integration"],                                     [(1932,"Medicine","Neurons")]),
    (442,"Edgar Adrian",           1889,1977,"England",        ["Medicine","Biology"],         ["Nerve Fiber Function","Nerve Impulse Measurement"],                                [(1932,"Medicine","Neurons")]),
    (443,"Otto Warburg",           1883,1970,"Germany",        ["Medicine","Chemistry"],       ["Warburg Effect","Respiratory Enzymes"],                                             [(1931,"Medicine","Cell Respiration")]),
    (444,"Christiaan Barnard",     1922,2001,"South Africa",   ["Medicine"],                   ["First Human Heart Transplant (1967)"],                                              []),
    (445,"Virginia Apgar",         1909,1974,"USA",            ["Medicine"],                   ["Apgar Score (Newborn Health Assessment)"],                                          []),
    (446,"Rosalind Yalow",         1921,2011,"USA",            ["Medicine","Physics"],         ["Radioimmunoassay"],                                                                 [(1977,"Medicine","Radioimmunoassay")]),
    (447,"César Milstein",         1927,2002,"Argentina/England",["Biology"],                  ["Monoclonal Antibodies"],                                                            [(1984,"Medicine","Monoclonal Antibodies")]),
    (448,"Niels Jerne",            1911,1994,"Denmark",        ["Medicine"],                   ["Immune System Network Theory"],                                                     [(1984,"Medicine","Immune Theory")]),
    (449,"Georges Köhler",         1946,1995,"Germany",        ["Biology"],                    ["Monoclonal Antibodies (hybridoma technique)"],                                      [(1984,"Medicine","Monoclonal Antibodies")]),
    (450,"Bengt Samuelsson",       1934,None,"Sweden",         ["Medicine","Chemistry"],       ["Prostaglandins and Related Substances"],                                            [(1982,"Medicine","Prostaglandins")]),
    (451,"Sune Bergström",         1916,2004,"Sweden",         ["Medicine","Chemistry"],       ["Prostaglandins Structure and Function"],                                            [(1982,"Medicine","Prostaglandins")]),
    (452,"John Vane",              1927,2004,"England",        ["Medicine","Pharmacology"],    ["Aspirin Mechanism","Prostacyclin"],                                                 [(1982,"Medicine","Prostaglandins")]),
    (453,"George Hitchings",       1905,1998,"USA",            ["Medicine","Chemistry"],       ["Rational Drug Design","Chemotherapy Drugs"],                                        [(1988,"Medicine","Drug Treatment")]),
    (454,"Joseph Goldstein",       1940,None,"USA",            ["Medicine"],                   ["Cholesterol Regulation","LDL Receptor"],                                            [(1985,"Medicine","Cholesterol")]),
    (455,"Michael Brown",          1941,None,"USA",            ["Medicine"],                   ["LDL Receptor","Cholesterol Metabolism"],                                            [(1985,"Medicine","Cholesterol")]),
    (456,"Wangari Maathai",        1940,2011,"Kenya",          ["Biology","Environment"],      ["Green Belt Movement","Reforestation","Environmental Conservation"],                 [(2004,"Peace","Environmental Conservation")]),
    (457,"Chen-Ning Yang",         1922,None,"China/USA",      ["Physics"],                    ["Parity Non-Conservation","Yang-Mills Theory"],                                      [(1957,"Physics","Parity Laws")]),
    (458,"Tsung-Dao Lee",          1926,None,"China/USA",      ["Physics"],                    ["Parity Non-Conservation","Lee-Yang Theorem"],                                      [(1957,"Physics","Parity Laws")]),
    (459,"Sin-Itiro Tomonaga",     1906,1979,"Japan",          ["Physics"],                    ["Quantum Electrodynamics"],                                                          [(1965,"Physics","Quantum Electrodynamics")]),
    (460,"Yoichiro Nambu",         1921,2015,"Japan/USA",       ["Physics"],                   ["Spontaneous Symmetry Breaking","String Theory Origins"],                            [(2008,"Physics","Symmetry Breaking")]),
    (461,"Masatoshi Koshiba",      1926,2020,"Japan",          ["Physics"],                    ["Neutrino Detection","Kamiokande"],                                                  [(2002,"Physics","Neutrino Detection")]),
    (462,"Riccardo Giacconi",      1931,2018,"Italy/USA",      ["Astronomy","Physics"],        ["X-ray Astronomy","First X-ray Source in Space"],                                   [(2002,"Physics","X-ray Astronomy")]),
    (463,"Raymond Davis Jr.",      1914,2006,"USA",            ["Physics"],                    ["Solar Neutrino Experiment","Homestake Experiment"],                                 [(2002,"Physics","Neutrino Detection")]),
    (464,"Makoto Kobayashi",       1944,None,"Japan",          ["Physics"],                    ["CP Violation in Quarks"],                                                           [(2008,"Physics","Symmetry Breaking")]),
    (465,"Toshihide Maskawa",      1940,2021,"Japan",          ["Physics"],                    ["CP Violation Theory"],                                                              [(2008,"Physics","Symmetry Breaking")]),
    (466,"Martinus Veltman",       1931,2021,"Netherlands",    ["Physics"],                    ["Electroweak Theory Renormalization"],                                               [(1999,"Physics","Electroweak Interactions")]),
    (467,"Gerardus 't Hooft",      1946,None,"Netherlands",    ["Physics"],                    ["Gauge Field Theories Renormalization"],                                             [(1999,"Physics","Electroweak Interactions")]),
    (468,"Steven Chu",             1948,None,"USA",            ["Physics"],                    ["Laser Cooling of Atoms","Atom Trapping"],                                           [(1997,"Physics","Laser Cooling")]),
    (469,"Claude Cohen-Tannoudji", 1933,None,"Algeria/France", ["Physics"],                    ["Laser Cooling and Trapping Atoms"],                                                 [(1997,"Physics","Laser Cooling")]),
    (470,"William Phillips",       1948,None,"USA",            ["Physics"],                    ["Laser Cooling","Atomic Fountain Clock"],                                            [(1997,"Physics","Laser Cooling")]),
    (471,"Douglas Osheroff",       1945,None,"USA",            ["Physics"],                    ["Superfluidity of Helium-3"],                                                        [(1996,"Physics","Helium-3 Superfluidity")]),
    (472,"David Lee",              1931,None,"USA",            ["Physics"],                    ["Superfluid Helium-3"],                                                              [(1996,"Physics","Helium-3 Superfluidity")]),
    (473,"Robert Richardson",      1937,2013,"USA",            ["Physics"],                    ["Superfluid Helium-3"],                                                              [(1996,"Physics","Helium-3 Superfluidity")]),
    (474,"Martin Perl",            1927,2014,"USA",            ["Physics"],                    ["Tau Lepton Discovery"],                                                             [(1995,"Physics","Tau Lepton")]),
    (475,"Frederick Reines",       1918,1998,"USA",            ["Physics"],                    ["Neutrino Detection (first experimental)"],                                          [(1995,"Physics","Neutrino")]),
    (476,"Clifford Shull",         1915,2001,"USA",            ["Physics"],                    ["Neutron Scattering"],                                                               [(1994,"Physics","Neutron Scattering")]),
    (477,"Bertram Brockhouse",     1918,2003,"Canada",         ["Physics"],                    ["Neutron Spectroscopy"],                                                             [(1994,"Physics","Neutron Spectroscopy")]),
    (478,"Russell Hulse",          1950,None,"USA",            ["Physics","Astronomy"],        ["Binary Pulsar Discovery","Gravitational Waves (indirect)"],                         [(1993,"Physics","Binary Pulsar")]),
    (479,"Joseph Taylor",          1941,None,"USA",            ["Physics","Astronomy"],        ["Binary Pulsar"],                                                                   [(1993,"Physics","Binary Pulsar")]),
    (480,"Pierre-Gilles de Gennes",1932,2007,"France",         ["Physics"],                    ["Liquid Crystals","Polymers Physics","Soft Matter"],                                 [(1991,"Physics","Liquid Crystals")]),
    (481,"Jerome Friedman",        1930,None,"USA",            ["Physics"],                    ["Deep Inelastic Scattering","Quark Evidence"],                                       [(1990,"Physics","Quark Structure")]),
    (482,"Henry Kendall",          1926,1999,"USA",            ["Physics"],                    ["Quark Structure of Protons/Neutrons"],                                             [(1990,"Physics","Quark Structure")]),
    (483,"Richard Taylor",         1929,2018,"Canada/USA",     ["Physics"],                    ["Quark Evidence in Protons"],                                                        [(1990,"Physics","Quark Structure")]),
    (484,"Norman Ramsey",          1915,2011,"USA",            ["Physics"],                    ["Atomic Clock","Magnetic Resonance Methods","Hydrogen Maser"],                       [(1989,"Physics","Atomic Precision")]),
    (485,"Hans Dehmelt",           1922,2017,"Germany/USA",    ["Physics"],                    ["Ion Trap Development","Isolated Electron/Positron"],                               [(1989,"Physics","Ion Trap")]),
    (486,"Wolfgang Paul",          1913,1993,"Germany",        ["Physics"],                    ["Paul Trap (Ion Trap)","Neutron Optics"],                                            [(1989,"Physics","Ion Trap")]),
    (487,"Leon Lederman",          1922,2018,"USA",            ["Physics"],                    ["Bottom Quark Discovery","Muon Neutrino","God Particle (named)"],                    [(1988,"Physics","Neutrino Beam")]),
    (488,"Melvin Schwartz",        1932,2006,"USA",            ["Physics"],                    ["Muon Neutrino Discovery"],                                                          [(1988,"Physics","Neutrino Beam")]),
    (489,"Jack Steinberger",       1921,2020,"Germany/USA",    ["Physics"],                    ["Muon Neutrino","Pion Decay"],                                                       [(1988,"Physics","Neutrino Beam")]),
    (490,"Johannes Bednorz",       1950,None,"Germany",        ["Physics"],                    ["High-Temperature Superconductivity"],                                               [(1987,"Physics","Superconductivity")]),
    (491,"Alex Müller",            1927,2023,"Switzerland",    ["Physics"],                    ["High-Temperature Superconductivity"],                                               [(1987,"Physics","Superconductivity")]),
    (492,"Ernst Ruska",            1906,1988,"Germany",        ["Physics","Engineering"],      ["Electron Microscope Invention"],                                                    [(1986,"Physics","Electron Microscopy")]),
    (493,"Gerd Binnig",            1947,None,"Germany",        ["Physics"],                    ["Scanning Tunneling Microscope"],                                                    [(1986,"Physics","Scanning Microscopy")]),
    (494,"Heinrich Rohrer",        1933,2013,"Switzerland",    ["Physics"],                    ["Scanning Tunneling Microscope"],                                                    [(1986,"Physics","Scanning Microscopy")]),
    (495,"Klaus von Klitzing",     1943,None,"Germany",        ["Physics"],                    ["Quantum Hall Effect"],                                                              [(1985,"Physics","Quantum Hall Effect")]),
    (496,"Carlo Rubbia",           1934,None,"Italy",          ["Physics"],                    ["W and Z Boson Discovery"],                                                          [(1984,"Physics","W/Z Bosons")]),
    (497,"Subrahmanyan Chandrasekhar",1910,1995,"India/USA",   ["Physics","Astronomy"],        ["Chandrasekhar Limit","White Dwarf Theory","Stellar Evolution"],                     [(1983,"Physics","Stellar Structure")]),
    (498,"William Fowler",         1911,1995,"USA",            ["Physics","Astronomy"],        ["Nuclear Reactions in Stars","Nucleosynthesis"],                                    [(1983,"Physics","Stellar Nucleosynthesis")]),
    (499,"Kenneth Wilson",         1936,2013,"USA",            ["Physics","Mathematics"],      ["Renormalization Group","Phase Transitions","Critical Phenomena"],                   [(1982,"Physics","Phase Transitions")]),
    (500,"Nicolaas Bloembergen",   1920,2017,"Netherlands/USA",["Physics"],                    ["Non-Linear Optics","Laser Spectroscopy","NMR Development"],                         [(1981,"Physics","Laser Spectroscopy")]),
]

# ── Build structured list ────────────────────────────────────────────────────
SCIENTISTS = []
seen = set()
for r in _RAW:
    if r[1] in seen:
        continue
    seen.add(r[1])
    SCIENTISTS.append({
        "id":           r[0],
        "name":         r[1],
        "birth_year":   r[2],
        "death_year":   r[3],
        "country":      r[4],
        "fields":       r[5],
        "known_for":    r[6],
        "nobel_prizes": [{"year": n[0], "field": n[1], "reason": n[2]} for n in r[7]],
    })

# ── Tools ────────────────────────────────────────────────────────────────────
@mcp.tool()
def get_scientist_details(name: str) -> str:
    """Get full details of a scientist by name (partial match supported)."""
    name_lower = name.lower()
    matches = [s for s in SCIENTISTS if name_lower in s["name"].lower()]
    if not matches:
        return f"No scientist found matching '{name}'."
    lines = []
    for s in matches:
        alive = "Present" if s["death_year"] is None else str(s["death_year"])
        fields = ", ".join(s["fields"])
        contributions = "\n   ".join(f"• {k}" for k in s["known_for"])
        if s["nobel_prizes"]:
            np_lines = "\n   ".join(f"• {n['year']} {n['field']} — {n['reason']}" for n in s["nobel_prizes"])
        else:
            np_lines = "None"
        lines.append(
            f"\n{'='*50}\n"
            f"Name    : {s['name']}\n"
            f"Born    : {s['birth_year']}  |  Died: {alive}\n"
            f"Country : {s['country']}\n"
            f"Field   : {fields}\n"
            f"Known For:\n   {contributions}\n"
            f"Nobel Prizes:\n   {np_lines}\n"
        )
    return "\n".join(lines)


@mcp.tool()
def search_by_country(country: str) -> str:
    """Find all scientists from a given country."""
    country_lower = country.lower()
    matches = [s for s in SCIENTISTS if country_lower in s["country"].lower()]
    if not matches:
        return f"No scientists found from '{country}'."
    lines = [f"Scientists from {country.title()} ({len(matches)} found)\n{'='*50}"]
    for s in matches:
        prizes = f"  Nobel×{len(s['nobel_prizes'])}" if s["nobel_prizes"] else ""
        fields = ", ".join(s["fields"])
        lines.append(f"  {s['name']} ({s['birth_year']}) — {fields}{prizes}")
    return "\n".join(lines)


@mcp.tool()
def search_by_field(field: str) -> str:
    """Find scientists by field (e.g. Physics, Chemistry, Biology, Medicine, Mathematics, Computing, Astronomy)."""
    field_lower = field.lower()
    matches = [s for s in SCIENTISTS if any(f.lower() == field_lower for f in s["fields"])]
    if not matches:
        return f"No scientists found in field '{field}'."
    lines = [f"Scientists in {field.title()} ({len(matches)} found)\n{'='*50}"]
    for s in matches:
        prizes = f"  Nobel×{len(s['nobel_prizes'])}" if s["nobel_prizes"] else ""
        lines.append(f"  {s['name']} ({s['birth_year']}, {s['country']}){prizes}")
        lines.append(f"    → {', '.join(s['known_for'][:2])}")
    return "\n".join(lines)


@mcp.tool()
def get_nobel_prize_winners(field: str = "") -> str:
    """
    List all scientists who won Nobel Prizes.
    Optionally filter by field: Physics, Chemistry, Medicine, Economics, Peace.
    """
    field_lower = field.lower()
    results = []
    for s in SCIENTISTS:
        prizes = s["nobel_prizes"]
        if field:
            prizes = [p for p in prizes if field_lower in p["field"].lower()]
        if prizes:
            results.append((s, prizes))
    if not results:
        return f"No Nobel Prize winners found for field '{field}'."
    label = f" in {field.title()}" if field else ""
    lines = [f"Nobel Prize Winners{label} ({len(results)} scientists)\n{'='*50}"]
    for s, prizes in results:
        for p in prizes:
            lines.append(f"  {p['year']} [{p['field']}]  {s['name']} ({s['country']})")
            lines.append(f"    Reason: {p['reason']}")
    return "\n".join(lines)


@mcp.tool()
def get_top_scientists(limit: int = 20) -> str:
    """Return the first N scientists from the list."""
    limit = max(1, min(limit, len(SCIENTISTS)))
    lines = [f"Top {limit} Scientists\n{'='*50}"]
    for s in SCIENTISTS[:limit]:
        prizes = f" | Nobel×{len(s['nobel_prizes'])}" if s["nobel_prizes"] else ""
        fields = ", ".join(s["fields"])
        lines.append(f"  #{s['id']:>3}  {s['name']} ({s['birth_year']}, {s['country']}) — {fields}{prizes}")
    return "\n".join(lines)


@mcp.tool()
def search_by_invention(keyword: str) -> str:
    """Search scientists by a keyword in their inventions or discoveries (e.g. 'quantum', 'vaccine', 'electricity')."""
    kw = keyword.lower()
    matches = [s for s in SCIENTISTS if any(kw in k.lower() for k in s["known_for"])]
    if not matches:
        return f"No scientists found for keyword '{keyword}'."
    lines = [f"Scientists related to '{keyword}' ({len(matches)} found)\n{'='*50}"]
    for s in matches:
        hit = [k for k in s["known_for"] if kw in k.lower()]
        lines.append(f"  {s['name']} ({s['country']}): {', '.join(hit)}")
    return "\n".join(lines)


@mcp.tool()
def get_statistics() -> str:
    """Show summary statistics: total scientists, countries, Nobel prizes, fields."""
    total = len(SCIENTISTS)
    countries = sorted(set(s["country"] for s in SCIENTISTS))
    total_nobels = sum(len(s["nobel_prizes"]) for s in SCIENTISTS)
    nobel_winners = sum(1 for s in SCIENTISTS if s["nobel_prizes"])
    field_count: dict = {}
    for s in SCIENTISTS:
        for f in s["fields"]:
            field_count[f] = field_count.get(f, 0) + 1
    fields_sorted = sorted(field_count.items(), key=lambda x: -x[1])
    lines = [
        f"{'='*50}",
        f"Total Scientists   : {total}",
        f"Countries Covered  : {len(countries)}",
        f"Nobel Prize Winners: {nobel_winners}",
        f"Total Nobel Prizes : {total_nobels}",
        f"\nTop Fields:",
    ]
    for f, count in fields_sorted[:10]:
        lines.append(f"  {f:<25} {count} scientists")
    lines.append(f"\nCountries: {', '.join(countries[:30])}{'...' if len(countries) > 30 else ''}")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()

