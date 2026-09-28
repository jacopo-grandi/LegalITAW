from legalitaw.agentic.coverage import generic_document_coverage

SOURCES = ["02_reference_pack.md", "03_legal_sources.md", "documents/01_contratto.pdf", "documents/02_email.eml"]


def ev(seq, tool, **args):
    return {"sequence": seq, "tool": tool, "arguments": args, "status": "ok"}


def test_read_e_shell_con_pattern_contano_come_aperti():
    trace = [ev(1, "read", path="documents/02_reference_pack.md"),
             ev(2, "bash", command='for f in documents/documents/*.pdf; do pdftotext "$f" scratch/x.txt; done')]
    cov = generic_document_coverage(SOURCES, trace)
    assert cov["opened_count"] == 2
    assert set(cov["unopened"]) == {"03_legal_sources.md", "documents/02_email.eml"}
    assert cov["reference_pack_opened"] is True and cov["legal_sources_opened"] is False


def test_glob_non_conta_e_grep_solo_su_testo():
    trace = [ev(1, "glob", pattern="documents/**/*"), ev(2, "grep", pattern="x", path="documents")]
    cov = generic_document_coverage(SOURCES, trace)
    assert cov["opened_count"] == 0
    assert set(cov["grep_only"]) == {"02_reference_pack.md", "03_legal_sources.md"}
