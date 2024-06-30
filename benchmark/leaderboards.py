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
        ["Dataset", "Unit", "Size", "Task", "Metric", "Dataset", "Split"],
        ["TDC.Lipophilicity_AstraZeneca", "log-ratio", "4,200", "Regression", "MAE", "Scaffold"]
    ],
    "Solubility_AqSolDB": [
        "old",
        ["Rank", "Model", "Contact", "Link", "#Params", "MAE" ],
        "incr",
        [
            [
                "Chemprop-RDKit",
            ]
        ],
    ]
}