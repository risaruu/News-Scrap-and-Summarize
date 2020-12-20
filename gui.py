import tkinter as tk

app = tk.Tk()

def setup_ui():
    # General settings of the window
    app.title("Summarized News")
    app.geometry('1200x600')
    app.configure(bg='#222831')

    #Title label and textbox setup
    tlabel = tk.Label(app, text = "Title")
    tlabel.config(bg='#393e46', fg='#ffd369')
    tlabel.pack()
    title = tk.Text(app, height=1, width=140)
    title.config(state='disabled', bg='#393e46', fg='#eeeeee')
    title.pack()

    #Author label and textbox setup
    alabel = tk.Label(app, text = "Author")
    alabel.config(bg='#393e46', fg='#ffd369')
    alabel.pack()
    author = tk.Text(app, height=1, width=140)
    author.config(state='disabled', bg='#393e46', fg='#eeeeee')
    author.pack()

    #Publication label and textbox setup
    plabel = tk.Label(app, text = "Publication Date")
    plabel.config(bg='#393e46', fg='#ffd369')
    plabel.pack()
    publication = tk.Text(app, height=1, width=140)
    publication.config(state='disabled', bg='#393e46', fg='#eeeeee')
    publication.pack()

    #Summary label and textbox setup
    slabel = tk.Label(app, text = "Summary")
    slabel.config(bg='#393e46', fg='#ffd369')
    slabel.pack()
    summary = tk.Text(app, height=20, width=140)
    summary.config(state='disabled', bg='#393e46', fg='#eeeeee')
    summary.pack()

    #Sentiment label and textbox setup
    selabel = tk.Label(app, text = "Sentiment Analysis")
    selabel.config(bg='#393e46', fg='#ffd369')
    selabel.pack()
    sentiment = tk.Text(app, height=1, width=140)
    sentiment.config(state='disabled', bg='#393e46', fg='#eeeeee')
    sentiment.pack()

    #URL label and textbox setup
    ulabel = tk.Label(app, text = "URL")
    ulabel.config(bg='#393e46', fg='#ffd369')
    ulabel.pack()
    utext = tk.Text(app, height=1, width=140)
    utext.config(bg='#393e46', fg='#eeeeee')
    utext.pack()

    app.mainloop()