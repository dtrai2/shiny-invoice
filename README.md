# Shiny Invoice

This tool is meant as a simple and naive way to manage invoices locally.
It is not meant to be published online and used as an enterprise tool.


## Run

To run `shiny-invoice` you need install it with:

```bash
pip install shiny-invoice
```

Once `shiny-invoice` is installed you need to create configuration file.
A suitable example looks like this:

```yaml
paths:
  invoices_dir: /home/user/invoices/  # must be an absolute path, and it needs to end with /
  html_template: shiny_invoice/templates/default_en.html
  datastore: datastore.json
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
  introduction: Dear Sir or Madam,
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

More information you can find with

```bash
shiny-invoice --help
shiny-invoice run --help
```

## Workflow

This application manages the invoices as plain html files, named by the invoice id.
To turn the html file into a pdf just use the browsers print functionality.
All the data corresponding to the invoices is stored inside a json file, which is configured with the key
`paths.datastore`.
The json you can edit as you like, via the gui it is only possible to change the 'Paid At' value.
This value is also used to determine if in invoice is indeed 'Paid' or 'Unpaid'.

## Impressions

### View of creating a new invoice
![new-invoice.png](docs/new-invoice.png)

### View of existing invoices
![existing-invoices.png](docs/existing-invoices.png)
