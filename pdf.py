import os
import base64
from datetime import datetime
from fpdf import FPDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.lib.utils import simpleSplit

def gerar_com_reportlab(caminho, destinatario, plano_estudos):
    largura, altura = A4
    c = canvas.Canvas(caminho, pagesize=A4)

    c.setFillColor(Color(0.05, 0.02, 0.15))
    c.rect(0, 0, largura, altura, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(Color(1, 0.85, 0.2))
    c.drawCentredString(largura / 2, altura - 70, "🔮 PLANO DE ESTUDOS MÁGICO 🔮")

    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(Color(0.9, 0.9, 1))
    c.drawCentredString(largura / 2, altura - 100, f"Para: {destinatario}")

    c.setFont("Helvetica", 10)
    c.setFillColor(Color(0.7, 0.7, 0.9))
    c.drawCentredString(largura / 2, altura - 120, f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    c.setFont("Helvetica-Oblique", 11)
    c.setFillColor(Color(0.8, 0.9, 1))
    c.drawCentredString(largura / 2, altura - 140, "Que a sabedoria da nuvem te guie nesta jornada...")

    c.setFont("Helvetica", 12)
    c.setFillColor(Color(1, 1, 1, alpha=0.4))
    for x in [80, 150, largura - 150, largura - 80]:
        c.drawString(x, altura - 160, "✦")

    c.setFont("Helvetica", 10)
    c.setFillColor(Color(0.9, 0.95, 1))

    y_atual = altura - 180
    max_largura = largura - 100

    for paragrafo in plano_estudos.strip().split("\n"):
        paragrafo = paragrafo.strip()
        if not paragrafo:
            y_atual -= 10
            continue

        is_title = any(marker in paragrafo for marker in ["Missão", "Trilha", "Certificação"])
        if is_title:
            c.setFont("Helvetica-Bold", 11)
            c.setFillColor(Color(1, 0.8, 0.4))
        else:
            c.setFont("Helvetica", 10)
            c.setFillColor(Color(0.9, 0.95, 1))

        linhas = simpleSplit(paragrafo, "Helvetica", 10, max_largura)
        for linha in linhas:
            c.drawString(60, y_atual, linha)
            y_atual -= 14

        if is_title:
            c.setFillColor(Color(1, 0.8, 0.4))
            c.rect(60, y_atual + 5, len(linha) * 5, 1, fill=1, stroke=0)
            y_atual -= 5

        if y_atual < 100:
            c.showPage()
            c.setFillColor(Color(0.05, 0.02, 0.15))
            c.rect(0, 0, largura, altura, fill=1, stroke=0)
            y_atual = altura - 100
            c.setFont("Helvetica", 10)
            c.setFillColor(Color(0.9, 0.95, 1))

    c.setStrokeColor(Color(0.5, 0.7, 1))
    c.setLineWidth(1)
    c.setFillColor(Color(0.2, 0.3, 0.5, alpha=0.8))
    c.roundRect(60, 60, 140, 50, 15, stroke=1, fill=1)

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(Color(1, 1, 1))
    c.drawCentredString(130, 95, "📜 Certificado")
    c.setFont("Helvetica", 8)
    c.drawCentredString(130, 80, "Pela Mentora Mágica")
    c.drawCentredString(130, 70, "do Agent-Career-Quest")

    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(Color(0.7, 0.7, 1))
    c.drawString(60, 40, "— Que sua carreira floresça como um feitiço bem lançado!")

    c.save()

class PDFMagico(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(255, 220, 100)
        self.cell(0, 10, '🔮 PLANO DE ESTUDOS MÁGICO 🔮', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-30)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(150, 150, 200)
        self.cell(0, 10, f'Gerado em: {datetime.now().strftime("%d/%m/%Y %H:%M")}', 0, 0, 'C')
        self.ln(5)
        self.set_font('Arial', '', 8)
        self.cell(0, 10, '📜 Certificado pela Mentora Mágica do Agent-Career-Quest', 0, 0, 'C')

def gerar_com_fpdf(caminho, destinatario, plano_estudos):
    pdf = PDFMagico()
    pdf.add_page()

    pdf.set_fill_color(30, 20, 60)
    pdf.rect(0, 0, 210, 297, 'F')

    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(255, 220, 100)
    pdf.cell(0, 10, '🔮 PLANO DE ESTUDOS MÁGICO 🔮', 0, 1, 'C')

    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(200, 200, 255)
    pdf.cell(0, 8, f'Para: {destinatario}', 0, 1, 'C')

    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(150, 150, 200)
    pdf.cell(0, 8, f'Gerado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}', 0, 1, 'C')

    pdf.set_font('Arial', 'I', 10)
    pdf.set_text_color(200, 220, 255)
    pdf.cell(0, 8, 'Que a sabedoria da nuvem te guie nesta jornada...', 0, 1, 'C')
    pdf.ln(5)

    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(230, 240, 255)

    for paragrafo in plano_estudos.strip().split("\n"):
        paragrafo = paragrafo.strip()
        if not paragrafo:
            pdf.ln(2)
            continue

        is_title = any(marker in paragrafo for marker in ["Missão", "Trilha", "Certificação"])
        if is_title:
            pdf.set_font('Arial', 'B', 11)
            pdf.set_text_color(255, 200, 100)
        else:
            pdf.set_font('Arial', '', 10)
            pdf.set_text_color(230, 240, 255)

        # Quebra de linha automática
        pdf.multi_cell(0, 6, paragrafo)
        pdf.ln(1)

    pdf.ln(10)
    pdf.set_draw_color(100, 150, 255)
    pdf.set_line_width(0.5)
    pdf.rect(20, pdf.get_y(), 60, 20)

    pdf.set_font('Arial', 'B', 9)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(25, pdf.get_y() + 5)
    pdf.cell(0, 5, '📜 Certificado', 0, 1)
    pdf.set_font('Arial', '', 7)
    pdf.cell(0, 4, 'Pela Mentora Mágica', 0, 1)
    pdf.cell(0, 4, 'do Agent-Career-Quest', 0, 1)

    pdf.ln(5)
    pdf.set_font('Arial', 'I', 9)
    pdf.set_text_color(200, 200, 255)
    pdf.cell(0, 5, '— Que sua carreira floresça como um feitiço bem lançado!', 0, 1, 'C')

    pdf.output(caminho)

def main(destinatario: str = "Usuário", plano_estudos: str = "Plano de estudos vazio"):
    """
    Gera um PDF e retorna:
      - caminho absoluto do arquivo salvo
      - conteúdo base64 do PDF (string)
      - mensagens de log
    """
    logs = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"plano_estudos_{timestamp}.pdf"
    pasta = "/mnt/data"
    os.makedirs(pasta, exist_ok=True)
    caminho_arquivo = os.path.join(pasta, nome_arquivo)

    try:
        logs.append("Tentando gerar PDF com reportlab...")
        gerar_com_reportlab(caminho_arquivo, destinatario, plano_estudos)
        logs.append("PDF gerado com reportlab com sucesso.")
    except ImportError as e:
        logs.append(f"reportlab indisponível: {e}. Tentando fpdf...")
        try:
            gerar_com_fpdf(caminho_arquivo, destinatario, plano_estudos)
            logs.append("PDF gerado com fpdf com sucesso.")
        except ImportError as e2:
            logs.append(f"fpdf também indisponível: {e2}. Não foi possível gerar PDF.")
            return {
                "success": False,
                "error": "Nenhuma biblioteca de PDF disponível (reportlab ou fpdf).",
                "logs": logs
            }
        except Exception as e2:
            logs.append(f"Erro ao gerar com fpdf: {e2}")
            return {"success": False, "error": str(e2), "logs": logs}
    except Exception as e:
        logs.append(f"Erro ao gerar com reportlab: {e}")
        return {"success": False, "error": str(e), "logs": logs}

    try:
        with open(caminho_arquivo, "rb") as f:
            conteudo = f.read()
        conteudo_b64 = base64.b64encode(conteudo).decode("utf-8")
        logs.append(f"Tamanho do PDF gerado: {len(conteudo)} bytes.")
    except Exception as e:
        logs.append(f"Erro ao ler/encodar o PDF: {e}")
        return {"success": False, "error": str(e), "logs": logs}

    return {
        "success": True,
        "pdf_path": caminho_arquivo,
        "pdf_base64": conteudo_b64,
        "logs": logs
    }