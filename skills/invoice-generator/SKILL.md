---
name: invoice-generator
description: Use when someone asks to create an invoice for PT Swiss Hospitality Consulting, generate an invoice for a client, or bill a client for services.
---

# Invoice Generator

Creates a professional HTML invoice from PT Swiss Hospitality Consulting. Always asks for the current exchange rate before calculating. Saves to the relevant project folder.

---

## Step 1 — Collect Required Inputs

Ask the user for any missing information:

| Field | Required | Notes |
|---|---|---|
| Client name | Yes | Full company name |
| Client contact | Optional | e.g. "Attn: Toby" |
| Invoice date | Yes | DD.MM.YYYY |
| Concerns | Yes | Short description, e.g. "Sales Training" |
| Line items | Yes | Description + USD price for each |
| Invoice number | Yes | Format: INV-YYYY-NNN (auto-increment from last) |
| Payment split | Optional | e.g. "50% today, 50% before start" |
| Save location | Yes | Default: `Projects/Sales-Training/` |

**Always ask:** "What is the current USD/IDR exchange rate?"
Never use a cached rate. Always ask fresh at the moment of invoice creation.

---

## Step 2 — Calculate IDR Amounts

For each line item and totals:
- IDR amount = USD amount × exchange rate
- Format: `X XXX XXX,00` (spaces as thousands separator, comma as decimal)
- Include exchange rate note in the invoice footer

---

## Step 3 — Generate the HTML Invoice

Use the template at `Projects/Sales-Training/invoice-nirvana-001.html` as the visual reference (it is the canonical design).

Key design rules:
- Header: Company name (left) + INVOICE label + number (right)
- Meta row: Date, Location (Bali), Concerns
- Bill To block: Client name + contact
- Items table: Description with subtitle | USD | IDR columns. Header row = light blue (#c8dce8). Body rows alternate #eef4f8 / #e4edf3.
- Totals block: Right-aligned, grand total row in black (#1a1a1a) with white text
- Payment schedule table (if split): Show each installment, badge "Due Now" on the first one in amber (#e8a820)
- FX note: Italic, small, below payment table: "Exchange rate: 1 USD = IDR X,XX on [Dth of Month, YYYY]" (spell out the date in full, e.g. "5th of June, 2026")
- Bank details grid: Mandiri, 175-00-0313369-0, PT Swiss Hospitality Consulting, IDR, Bali

PT Swiss Hospitality Consulting address:
```
Jalan Sunset Road No. 28
Seminyak, Kuta
Kabupaten Badung, Bali 80361
Indonesia
```

---

## Step 4 — Save the File

File naming: `invoice-[client-slug]-[NNN].html`
- Example: `invoice-nirvana-001.html`, `invoice-nirvana-002.html`
- Save to the project folder specified, or ask if unclear.

---

## Step 5 — Confirm

Report back:
- File saved at: `[path]`
- Amount due now: $X,XXX = IDR X XXX XXX,00
- Exchange rate used: 1 USD = IDR X,XX
