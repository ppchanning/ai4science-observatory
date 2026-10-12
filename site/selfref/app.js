(() => {
  const form = document.querySelector('[data-search]');
  if (form) {
    const input = form.querySelector('input');
    const cards = [...document.querySelectorAll('[data-entry]')];
    const count = document.querySelector('[data-count]');
    const buttons = [...document.querySelectorAll('[data-filter]')];
    const params = new URLSearchParams(location.search);
    let filter = params.get('type') || 'all';
    if (!buttons.some(button => button.dataset.filter === filter)) filter = 'all';
    input.value = params.get('q') || '';
    const refresh = () => {
      const terms = input.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
      let visible = 0;
      for (const card of cards) {
        const text = card.dataset.search.toLocaleLowerCase();
        const match = (filter === 'all' || card.dataset.kind === filter) && terms.every(term => text.includes(term));
        card.hidden = !match;
        visible += Number(match);
      }
      for (const button of buttons) button.setAttribute('aria-pressed', String(button.dataset.filter === filter));
      count.textContent = document.documentElement.lang === 'zh-CN' ? `${visible} 条结果` : `${visible} results`;
      document.querySelector('[data-empty]').hidden = visible !== 0;
      const url = new URL(location.href);
      input.value.trim() ? url.searchParams.set('q', input.value.trim()) : url.searchParams.delete('q');
      filter !== 'all' ? url.searchParams.set('type', filter) : url.searchParams.delete('type');
      history.replaceState(null, '', url);
    };
    form.addEventListener('submit', event => { event.preventDefault(); refresh(); });
    input.addEventListener('input', refresh);
    buttons.forEach(button => button.addEventListener('click', () => { filter = button.dataset.filter; refresh(); }));
    refresh();
  }
  document.querySelectorAll('[data-copy]').forEach(button => {
    button.addEventListener('click', async () => {
      const status = button.parentElement.querySelector('[role="status"]');
      try {
        await navigator.clipboard.writeText(button.dataset.copy);
        status.textContent = document.documentElement.lang === 'zh-CN' ? '已复制' : 'Copied';
      } catch {
        status.textContent = document.documentElement.lang === 'zh-CN' ? '请选择上方命令复制' : 'Select the command above to copy';
      }
    });
  });
})();
