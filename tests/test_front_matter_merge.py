GLOBAL_SCHEMA = {
    "author": {
        "@type": "Person",
        "@id": "https://example.com/",
        "name": "John Doe",
        "url": "https://example.com/",
        "alternateName": [
            "Jonny Doe",
        ],
        "sameAs": ["https://example.com"],
    },
    "@graph": [
        {
            "@type": "DefinedTermSet",
            "@id": "http://entitygarden.com/glossary/#definedTermSet",
            "name": "Knowledge Graph Optimization Glossary",
            "alternateName": ["KGO Glossary"],
            "description": "A glossary for knowledge graph optimization. The glossary extends to terms in the fields of search engine optimization, marketing, and branding.",
            "url": "http://entitygarden.com/glossary/",
        }
    ],
}

LOCAL_SCHEMA = {
    "@type": "WebPage",
    "@id": "https://entitygarden.com/glossary/knowledge_graph_optimization/",
    "name": "Glossary for Knowledge Graph Optimization",
    "abstract": "Knowledge Graph Optimization is a process of publishing information about an entity optimal for the creation of a knowledge graph",
    "datePublished": "2024-03-08T07:52:13+02:00",
    "dateModified": "2024-03-08T14:54:13+02:00",
    "url": "https://entitygarden.com/glossary/knowledge_graph_optimization/",
    "author": {
        "@type": "Person",
        "@id": "https://kajkandler.com/",
        "name": "Kaj Kandler",
    },
    "@graph": [
        {
            "@type": "DefinedTerm",
            "@id": "http://entitygarden.com/glossary/knowledge_graph_optimization/",
            "name": "Knowledge Graph Optimization",
            "description": "Knowledge Graph Optimization is the process of publishing Information about an entity in such a way that search engine algorithms can understand it.",
            "inDefinedTermSet": "http://entitygarden.com/glossary/",
        }
    ],
}


def test_get_data():
    pass
    # front_matter = merge_schema(GLOBAL_SCHEMA, LOCAL_SCHEMA)
    # assert front_matter.startswith("# Blurry: ")
    # assert len(front_matter) == 4
    # assert front_matter.get("@context")
    # assert front_matter.get("@graph")
    # assert front_matter.get("@type") == "WebPage"
