import asyncio
import yfinance as yf
from telegram import Bot
from config import TOKEN, CHAT_ID
from strategy import signal
from stocks import stocks
