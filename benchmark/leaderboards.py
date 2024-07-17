_LEADERBOARDS = {
    "Caco2_Wang": [
        "old", # old or new format (incl dataset description)
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE"],
        "incr", # increasing or descending order
        [
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.276
            ],
            [
                "BaseBoosting", "Andrew Li", "andrew@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC", 
                "https://github.com/Oloren-AI/OCE-TDC/blob/main/Report.pdf", "365,713", 0.285
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.287
            ],
            [
                "MolMapNet-D", "Shen Wan Xiang", "wanxiang.shen@u.nus.edu", "https://github.com/shenwanxiang/bidd-molmap/tree\
                    /master/misc/tdc_leaderboard_submission/Caco2_Wang-MolMapNet-D.ipynb", 
                    "https://www.nature.com/articles/s42256-021-00301-6", "407,617", 0.287
            ],
            [
                "XGBoost", "Andrew Li", "andrew@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC/blob/main/submission.ipynb", 
                "https://github.com/Oloren-AI/OCE-TDC/blob/main/Report.pdf", "12", 0.289
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies", 
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.297
            ],
            [
                "Basic ML", "Nilavo Boral", "nilavoboral@gmail.com", "https://github.com/NilavoBoral/Therapeutics-Data-Commons", 
                "https://www.biorxiv.org/content/10.1101/2022.06.29.115436v1", "N/A", 0.321
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.330
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu","https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.335
            ],
            [
                "Euclia ML model", "Euclia", "euclia@euclia.io", "https://github.com/euclia/public-models", 
                "https://github.com/euclia/public-models", "50", 0.341
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.344
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.393
            ]
        ], # meta info: model, contact_name, contact_email, GH, repo, .. other .., value to rank by
        [
            [
                0.276,
                0.005
            ],
            [
                0.285,
                0.005
            ],
            [
                0.287,
                0.005
            ],
            [
                0.287,
                0.005
            ],
            [
                0.289,
                0.011
            ],
            [
                0.297,
                0.008
            ],
            [
                0.321,
                0.005
            ],
            [
                0.330,
                0.024
            ],
            [
                0.335,
                0.033
            ],
            [
                0.341,
                0.004
            ],
            [
                0.344,
                0.015
            ],
            [
                0.393,
                0.024
            ],
        ], # metrics (val, std)
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.Caco2_Wang ", "cm/s", "906", "Regression", "MAE", "Scaffold"]
    ],
    "Bioavailability_Ma": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUROC"],
        "desc",
        [
            [
                "HistGradientBoostingClassifier (DeepMol)", "DeepMol Team", "jcapels96@gmail.com", 
                "https://github.com/BioSystemsUM/deepmol_case_studies", "https://doi.org/10.1101/2024.05.27.595849",
                "N/A", 0.753
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC", 
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.748
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.746
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.742
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.730
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.706
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.672
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.671
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", 
                "https://github.com/chemprop/chemprop", "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A",
                0.667
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", 
                "https://pubmed.ncbi.nlm.nih.gov/31408336/", "300,806", 0.632
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", 
                "https://ieeexplore.ieee.org/document/9412489", "480,193", 0.632
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies", 
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.617
            ],
        ],
        [
            [
                0.753,
                0
            ],
            [
                0.748,
                0.033
            ],
            [
                0.746,
                0.030
            ],
            [
                0.742,
                0.010
            ],
            [
                0.730,
                0.010
            ],
            [
                0.706,
                0.031
            ],
            [
                0.672,
                0.021
            ],
            [
                0.671,
                0.026
            ],
            [
                0.667,
                0.068
            ],
            [
                0.632,
                0.036
            ],
            [
                0.617,
                0.009
            ],
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.Bioavailability_Ma" , "%", "640", "Binary", "AUROC", "Scaffold"],
    ],
    "Lipophilicity_AstraZeneca": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE"],
        "incr",
        [
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.467
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.470
            ],
            [
                "BaseBoosting KyQVZ6b2", "David Huang", "david@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC/tree/main", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6350b9d186473a47d31a8492", "N/A", 0.479
            ],
            [
                "Innoplexus ADME", "Rohit Yadav", "rohit.yadav@ics.innoplexus.com", 
                "https://github.com/Innoplexus-opensource/ics-therapeutics-data-commons/tree/main", 
                "https://github.com/Innoplexus-opensource/ics-therapeutics-data-commons/blob/main/Innoplexus_ADME_Model_report.pdf",
                "N/A", 0.499
            ],
            [
                "CMPNN", "Devansh Amin", "devanshamin97@gmail.com", "https://github.com/devanshamin/LitGNN", 
                "https://www.ijcai.org/Proceedings/2020/392", "3.0 M", 0.515
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.525
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", 
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.535
            ],
            [
                "StackingRegressor (DeepMol)", "DeepMol Team", "jcapels96@gmail.com", 
                "https://github.com/BioSystemsUM/deepmol_case_studies", "https://doi.org/10.1101/2024.05.27.595849",
                "N/A", 0.538
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.539
            ],
            [
                "GCN", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1609.02907",
                "191,810", 0.541
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.547
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", 
                "https://ieeexplore.ieee.org/document/9412489", "480,193", 0.563
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", 
                "https://pubmed.ncbi.nlm.nih.gov/31408336/", "300,806", 0.572
            ],
        ],
        [
            [
                0.467,
                0.006
            ],
            [
                0.470,
                0.009
            ],
            [
                0.479,
                0.007
            ],
            [
                0.499,
                0.003
            ],
            [
                0.515,
                0.038
            ],
            [
                0.525,
                0.003
            ],
            [
                0.535,
                0.012
            ],
            [
                0.538,
                0.001
            ],
            [
                0.539,
                0.002
            ],
            [
                0.541,
                0.011
            ],
            [
                0.547,
                0.024
            ],
            [
                0.563,
                0.023
            ],
            [
                0.572,
                0.007
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.Lipophilicity_AstraZeneca", "log-ratio", "4,200", "Regression", "MAE", "Scaffold"]
    ],
    "Solubility_AqSolDB": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE" ],
        "incr",
        [
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.761
            ],
            [
                "Innoplexus ADME", "Rohit Yadav", "rohit.yadav@ics.innoplexus.com", "https://github.com/Innoplexus-opensource/\
                    ics-therapeutics-data-commons/tree/main", "https://github.com/Innoplexus-opensource/ics-therapeutics-data\
                        -commons/blob/main/Innoplexus_ADME_Model_report.pdf", "N/A", 0.771
            ],
            [
                "DeepMol (AutoML) ", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.775
            ],
            [
                "AttentiveFP ", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://pubmed.ncbi.nlm.nih.gov/31408336/", "300,806", 0.776
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.789
            ],
            [
                " MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.792
            ],
            [
                "CMPNN", "Devansh Amin", "devanshamin97@gmail.com", "https://github.com/devanshamin/LitGNN", 
                "https://www.ijcai.org/Proceedings/2020/392", "3.0 M", 0.796
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.827
            ],
            [
                "Basic ML", "Nilavo Boral", "nilavoboral@gmail.com", "https://github.com/NilavoBoral/Therapeutics-Data-Commons", 
                "https://www.biorxiv.org/content/10.1101/2022.06.29.115436v1", "N/A", 0.828
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.829
            ]
            
        ],
        [
            [
                0.761,
                0.025
            ],
            [
                0.771,
                0.005
            ],
            [
                0.775,
                0.006
            ],
            [
                0.776,
                0.008
            ],
            [
                0.789,
                0.003
            ],
            [
                0.792,
                0.002
            ],
            [
                0.796,
                0.038
            ],
            [
                0.827,
                0.047
            ],
            [
                0.828,
                0.002
            ],
            [
                0.829,
                0.022
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.Solubility_AqSolDB ", "log mol/L", "9,982", "Regression", "MAE", "Scaffold"]
    ],
    "HIA_Hou": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUROC" ],
        "desc",
        [
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.990
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.989
            ],
            [
                "RFStacker", "Andrew Li", "andrew@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC/blob/main/submission.ipynb", 
                "https://github.com/Oloren-AI/OCE-TDC/blob/main/Report.pdf", "1,858,225", 0.988
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", "https://arxiv.org/abs/2310.00174",
                "N/A", 0.986
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.981
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.981
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.978
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.975
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://pubmed.ncbi.nlm.nih.gov/31408336/", "300,806", 0.974
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu". 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", "https://doi.org/10.1093/bioinformatics/btaa1005",
                "633,409", 0.972
            ]
        ],
        [
            [
                0.990,
                0.002
            ],
            [
                0.989,
                0.001
            ],
            [
                0.988,
                0.002
            ],
            [
                0.986,
                0.000
            ],
            [
                0.981,
                0.009
            ],
            [
                0.981,
                0.002
            ],
            [
                0.978,
                0.006
            ],
            [
                0.975,
                0.004
            ],
            [
                0.974,
                0.007
            ],
            [
                0.972,
                0.008
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.HIA_Hou ", "%", "578", "Regression", "AUROC", "Scaffold"]
    ],
    "Pgp_Broccatelli": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUROC" ],
        "desc",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.938
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.935
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.930
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC", 
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.929
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.929
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", 
                "https://github.com/F-LIDM/CFA4DD", "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3",
                "N/A", 0.928
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.923
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.922
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", "https://doi.org/10.1093/bioinformatics/btaa1005",
                "633,409", 0.918
            ],
            [
                "CNN (DeepPurpose)", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "226,625", 0.908
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://ieeexplore.ieee.org/document/9412489", "480,193", 0.902
            ],
        ],
        [
            [
                0.938,
                0.002
            ],
            [
                0.935,
                0.006
            ],
            [
                0.930,
                0.002
            ],
            [
                0.929,
                0.010
            ],
            [
                0.929,
                0.006
            ],
            [
                0.928,
                0.008
            ],
            [
                0.923,
                0.005
            ],
            [
                0.922,
                0.0
            ],
            [
                0.918,
                0.007
            ],
            [
                0.908,
                0.012
            ],
            [
                0.902,
                0.020
            ]
        ]
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.Pgp_Broccatelli ", "%", "1,212", "Binary", "AUROC", "Scaffold"]
    ],
    "BBB_Martins": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUROC" ],
        "desc",
        [
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.920
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", "https://arxiv.org/abs/2310.00174",
                "N/A", 0.916
            ],
            [
                "Lantern RADR Ensemble", "Rick Fontenot", "rick@lanternpharma.com", "https://github.com/lanternpharma/tdc-bbb-martins",
                "https://github.com/lanternpharma/tdc-bbb-martins/blob/main/Lantern_TDC_BBBmartins.pdf", "N/A", 0.915
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.913
            ],
            [
                "Lantern RADR Deep Neural Network", "Rick Fontenot", "rick@lanternpharma.com", 
                "https://github.com/lanternpharma/tdc-bbb-martins", 
                "https://github.com/lanternpharma/tdc-bbb-martins/blob/main/Lantern_TDC_BBBmartins.pdf", "N/A", 0.912
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark",
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.910
            ],
            [
                "Lantern RADR Random Forest", "Rick Fontenot", "rick@lanternpharma.com", 
                "https://github.com/lanternpharma/tdc-bbb-martins", 
                "https://github.com/lanternpharma/tdc-bbb-martins/blob/main/Lantern_TDC_BBBmartins.pdf", "319", 0.908
            ],
            [
                "Lantern RADR SVM", "Rick Fontenot", "rick@lanternpharma.com", "https://github.com/lanternpharma/tdc-bbb-martins",
                "https://github.com/lanternpharma/tdc-bbb-martins/blob/main/Lantern_TDC_BBBmartins.pdf", "241", 0.905
            ],
            [
                "Lantern RADR Logistic Regression", "Rick Fontenot", "rick@lanternpharma.com", 
                "https://github.com/lanternpharma/tdc-bbb-martins", 
                "https://github.com/lanternpharma/tdc-bbb-martins/blob/main/Lantern_TDC_BBBmartins.pdf","456", 0.903
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC",
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.901
            ],
        ],
        [
            [
                0.920,
                0.006
            ],
            [
                0.916,
                0.001
            ],
            [
                0.915,
                0.002
            ],
            [
                0.913,
                0.001
            ],
            [
                0.912,
                0.003
            ],
            [
                0.910,
                0.024
            ],
            [
                0.908,
                0.002
            ],
            [
                0.905,
                0.007
            ],
            [
                0.903,
                0.002
            ],
            [
                0.901,
                0.007
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.BBB_Martins ", "%", "1,975", "Binary", "AUROC", "Scaffold"]
    ],
    "PPBR_AZ": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE"],
        "incr",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 7.526
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 7.660
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 7.788
            ],
            [
                "BaseBoosting KyQVZ6b2", "David Huang", "david@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC/tree/main", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6350b9d186473a47d31a8492", "N/A", 7.914
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 7.99
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 8.288
            ],
            [
                "Innoplexus ADME", "Rohit Yadav", "rohit.yadav@ics.innoplexus.com", 
                "https://github.com/Innoplexus-opensource/ics-therapeutics-data-commons/tree/main", 
                "https://github.com/Innoplexus-opensource/ics-therapeutics-data-commons/blob/main/Innoplexus_ADME_Model_report.pdf",
                "N/A", 8.582
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 8.680
            ],
            [
                "Basic ML", "Nilavo Boral", "nilavoboral@gmail.com", "https://github.com/NilavoBoral/Therapeutics-Data-Commons",
                "https://www.biorxiv.org/content/10.1101/2022.06.29.115436v1", "N/A", 9.185
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://ieeexplore.ieee.org/document/9412489", "480,193", 9.292
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://pubmed.ncbi.nlm.nih.gov/31408336/",
                "300,806", 9.373
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 9.445
            ]
        ],
        [
            [
                7.526,
                0.106
            ],
            [
                7.660,
                0.058
            ],
            [
                7.788,
                0.210
            ],
            [
                7.914,
                0.096
            ],
            [
                7.99,
                0.104
            ],
            [
                8.288,
                0.173
            ],
            [
                8.582,
                0.036
            ],
            [
                8.680,
                0.262
            ],
            [
                9.185,
                0.000
            ],
            [
                9.292,
                0.384
            ],
            [
                9.373,
                0.335
            ],
            [
                9.445,
                0.224
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.PPBR_AZ ", "%", "1,797", "Regression", "MAE", "Scaffold"]
    ],
    "VDss_Lombardo": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "Spearman"],
        "desc",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.713
            ],
            [
                "Innoplexus ADME", "Rohit Yadav", "rohit.yadav@ics.innoplexus.com", 
                "https://github.com/Innoplexus-opensource/ics-therapeutics-data-commons/tree/main", 
                "https://github.com/Innoplexus-opensource/ics-therapeutics-data-commons/blob/main/Innoplexus_ADME_Model_report.pdf",
                "N/A", 0.707
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.707
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.628
            ],
            [
                "Basic ML", "Nilavo Boral", "nilavoboral@gmail.com", "https://github.com/NilavoBoral/Therapeutics-Data-Commons",
                "https://www.biorxiv.org/content/10.1101/2022.06.29.115436v1", "N/A", 0.627
            ],
            [
                "Euclia ML model", "Euclia", "euclia@euclia.io", "https://github.com/euclia/public-models", 
                "https://github.com/euclia/public-models", "50", 0.609
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC", 
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.582
            ],
            [
                "RDKit2D + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "633,409", 0.561
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.559
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.497
            ],
            [
                "Morgan + MLP (DeepPurpose)", "Kexin Huang", "kexinhuang@hsph.harvard.edu", 
                "https://github.com/mims-harvard/TDC/tree/master/examples/single_pred/admet", 
                "https://doi.org/10.1093/bioinformatics/btaa1005", "1,477,185", 0.493
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.491
            ],
        ],
        [
            [
                0.713,
                0.007
            ],
            [
                0.707,
                0.006
            ],
            [
                0.707,
                0.009
            ],
            [
                0.628,
                0.023
            ],
            [
                0.627,
                0.010
            ],
            [
                0.609,
                0.014
            ],
            [
                0.582,
                0.031
            ],
            [
                0.561,
                0.025
            ],
            [
                0.559,
                0.019
            ],
            [
                0.497,
                0.011
            ],
            [
                0.493,
                0.011
            ],
            [
                0.491,
                0.046
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.VDss_Lombardo ", "L/kg", "1,130", "Regression", "Spearman", "Scaffold"]
    ],
    "CYP2C9_Veith": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUPRC"],
        "desc",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.859
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.839
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.829
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark",
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.786
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.783
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.777
            ],
            [
                "ColorRefinement + Weighted Ensemble LGBM", "Parker Burchett", "parkerburchett@gmail.com", 
                "https://github.com/parkerburchett/TDC-DeepLearning/blob/main/modeling/CYP%20Weighted%20Model.ipynb",
                "https://tdcommons.ai/benchmark/admet_group/10cyp2c9i/No%20paper", "68", 0.767
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.758
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.754
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.751
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://pubmed.ncbi.nlm.nih.gov/31408336/", "300,806", 0.749
            ],
        ],
        [
            [
                0.859,
                0.001
            ],
            [
                0.839,
                0.003
            ],
            [
                0.829,
                0.003
            ],
            [
                0.786,
                0.004
            ],
            [
                0.783,
                0.002
            ],
            [
                0.777,
                0.003
            ],
            [
                0.767,
                0.003
            ],
            [
                0.758,
                0.002
            ],
            [
                0.754,
                0.002
            ],
            [
                0.751,
                0.006
            ],
            [
                0.749,
                0.004
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.CYP2C9_Veith ", "%", "12,092", "Binary", "AUPRC", "Scaffold"]
    ],
    "CYP2D6_Veith": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUPRC"],
        "desc",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.790
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.739
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.723
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://doi.org/10.1101/2024.05.27.595849",
                "2,067,053", 0.721
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.685
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.673
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.664
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.649
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://pubmed.ncbi.nlm.nih.gov/31408336/",
                "300,806", 0.646
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.644
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://ieeexplore.ieee.org/document/9412489",
                "480,193", 0.627
            ],
        ],
        [
            [
                0.790,
                0.001
            ],
            [
                0.739,
                0.005
            ],
            [
                0.723,
                0.003
            ],
            [
                0.721,
                0.009
            ],
            [
                0.685,
                0.000
            ],
            [
                0.673,
                0.007
            ],
            [
                0.664,
                0.012
            ],
            [
                0.649,
                0.016
            ],
            [
                0.646,
                0.014
            ],
            [
                0.644,
                0.085
            ],
            [
                0.627,
                0.009
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.CYP2D6_Veith ", "%", "13,130", "Binary", "AUPRC", "Scaffold"]
    ],
    "CYP3A4_Veith": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUPRC"],
        "desc",
        [
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.916
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.904
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.902
            ],
            [
                "MapLight", "Jim Notwell", "https://github.com/maplightrx/MapLight-TDC", "https://arxiv.org/abs/2310.00174",
                "N/A", 0.881
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.876
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.875
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.862
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.855
            ],
            [
                "AttentiveFP", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://pubmed.ncbi.nlm.nih.gov/31408336/",
                "300,806", 0.851
            ],
            [
                "NeuralFP", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://ieeexplore.ieee.org/document/9412489", "480,193", 0.849
            ],
        ],
        [
            [
                0.916,
                0.000
            ],
            [
                0.904,
                0.002
            ],
            [
                0.902,
                0.002
            ],
            [
                0.881,
                0.001
            ],
            [
                0.876,
                0.003
            ],
            [
                0.875,
                0.002
            ],
            [
                0.862,
                0.003
            ],
            [
                0.855,
                0.004
            ],
            [
                0.851,
                0.006
            ],
            [
                0.849,
                0.004
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.CYP3A4_Veith ", "%", "12,328", "Binary", "AUPRC", "Scaffold"]
    ]
    "CYP2C9_Substrate_CarbonMangels": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUPRC"],
        "desc",
        [
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.441
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.437
            ],
            [
                "Random Forest", "Andrew Li", "andrew@oloren.ai", "https://github.com/Oloren-AI/OCE-TDC", 
                "https://github.com/Oloren-AI/OCE-TDC/blob/main/Report.pdf", "9", 0.437
            ],
            [
                "SimGCN", "Suman Kalyan Bera", "suman@katanagraph.com", "https://github.com/KatanaGraph/SimGCN-TDC", 
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf",
                "https://github.com/KatanaGraph/SimGCN-TDC/blob/main/Report_SimGCN_for_TDC_Benchmarks.pdf", "1,103,000", 0.433
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.417
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.417
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.415
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.400
            ],
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", 
                "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet", "https://arxiv.org/abs/1905.12265",
                "2,067,053", 0.392
            ],
            [
                "Chemprop", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.382
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.381
            ]
        ],
        [
            [
                0.441,
                0.033
            ],
            [
                0.437,
                0.008
            ],
            [
                0.437,
                0.022
            ],
            [
                0.433,
                0.017
            ],
            [
                0.417,
                0.010
            ],
            [
                0.417,
                0.005
            ],
            [
                0.415,
                0.008
            ],
            [
                0.400,
                0.008
            ],
            [
                0.392,
                0.026
            ],
            [
                0.382,
                0.019
            ],
            [
                0.381,
                0.045
            ]
        ],
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset Split"],
        ["TDC.CYP2C9_Substrate_CarbonMangels ", "%", "666", "Binary", "AUPRC", "Scaffold"]
    ],
    "CYP2D6_Substrate_CarbonMangels": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "AUPRC"],
        "desc",
        [
            [
                "ContextPred", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.736
            ],
            [
                "DeepMol (AutoML)", "DeepMol Team", "jcapels96@gmail.com", "https://github.com/BioSystemsUM/deepmol_case_studies",
                "https://doi.org/10.1101/2024.05.27.595849", "N/A", 0.731
            ],
            [
                "MapLight + GNN", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC",
                "https://arxiv.org/abs/2310.00174", "N/A", 0.720
            ],
            [
                "MapLight", "Jim Notwell", "jnotwell@maplightrx.com", "https://github.com/maplightrx/MapLight-TDC", 
                "https://arxiv.org/abs/2310.00174", "N/A", 0.713
            ],
            [
                "CFA", "Nan Jiang", "njiang3@fordham.edu", "https://github.com/F-LIDM/CFA4DD", 
                "https://chemrxiv.org/engage/chemrxiv/article-details/6563ec17cf8b3c3cd73212b3", "N/A", 0.704
            ],
            [
                "AttrMasking", "Kexin Huang", "kexinh@stanford.edu", "https://github.com/mims-harvard/TDC/tree/main/examples/single_pred/admet",
                "https://arxiv.org/abs/1905.12265", "2,067,053", 0.704
            ],
            [
                "Chemprop-RDKit", "Kyle Swanson", "swansonk@stanford.edu", "https://github.com/chemprop/chemprop", 
                "https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b00237", "N/A", 0.686
            ],
            [
                "ZairaChem", "Gemma Turon", "gemma@ersilia.io", "https://github.com/ersilia-os/zaira-chem-tdc-benchmark", 
                "https://www.biorxiv.org/content/10.1101/2022.12.13.520154v1", "N/A", 0.685
            ],
            [
                
            ]
        ]
    ]
}