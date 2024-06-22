# Shiny Invoice

This tool is meant as a simple and naive way to manage invoices locally.
It is not meant to be published online and used as an enterprise tool.


## Run

To run shiny invoice you need to clone this repository and install the dependencies with (it is suggested to use a venv)

```bash
pip install -e .
```

Once `shiny-invoice` is installed you need to create configuration file. 
A suitable example looks like this:

```yaml
paths:
  invoices_root_dir: /home/user/invoices/  # must be an absolute path, and it needs to end with /
  invoices_dir_paid: paid
  invoices_dir_unpaid: open
  html_template: shiny_invoice/default_invoice_template.html
company:  # here you can specify details of your company
  name: Company Name
  skills:
    - Primary Skill
    - Secondary Skill
  address:
    - Address line 1
    - 4234 Addresline2
  contact:
    - contact@shinyinvoice.de
    - +49 123 456789
    - shinyinvoice.de
  bank:
    name: SomeBank
    iban: DE12 1234 5678 9100 00
    bic: BICCCCCCC
    tax_number: 11/2222/3333
  tax_rate: 0.19
  payment_terms_days: 14
invoice_defaults:  # here you can set defaults, which will be used to prefill the invoice formular
  recipient: |-
    Comp 2
    Compstreet Comp
    1335 Compvill
  items: |
    Services, Hours, Rate, Price
    Service 1, 40h, 100 €, 4.000 €
```

Once everything is set up you can run `shiny-invoice` with:

```bash
shiny-invoice run --config config.yaml 
```

## Workflow

This application manages the invoices as plain html files, which then can be turned into pdfs via the 
browsers print functionality. 
According to the configuration invoices can be separated into paid/unpaid directories.
Based on that they will be also categorised inside the ui.
The application does not offer ways to move or change files, this has to be done manually. 
The filename also needs to follow a specific pattern which is 
`<CREATED_AT_DATE>-<INVOICE_NUMBER>-<CUSTOMERNAME>.html`
