(function () {
  'use strict';

  const $ = (id) => document.getElementById(id);
  const AI_URL = 'https://chatgpt.com/';

  function addStyles() {
    const style = document.createElement('style');
    style.id = 'tt-smart-tools-style';
    style.textContent = `
      .tt-smart-tools{margin:16px 0 4px;padding:18px;border:1px solid #ead1bf;border-radius:16px;background:linear-gradient(135deg,#fffaf5,#fff);box-shadow:0 7px 20px rgba(105,24,15,.08)}
      .tt-smart-head{margin-bottom:12px}.tt-smart-head h3{margin:3px 0 0;color:#8f1d15;font-size:21px}.tt-smart-head p{margin:4px 0 0;color:#6b625e;font-size:13px}
      .tt-smart-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.tt-smart-card{border:1px solid #ead3c3;border-radius:14px;padding:16px;background:#fff;cursor:pointer;transition:.2s;display:flex;gap:13px;align-items:flex-start}.tt-smart-card:hover{transform:translateY(-2px);box-shadow:0 9px 22px rgba(120,30,20,.12);border-color:#c64232}.tt-smart-icon{width:48px;height:48px;min-width:48px;border-radius:13px;background:#a82017;color:#ffe56c;display:flex;align-items:center;justify-content:center;font-size:24px}.tt-smart-card b{display:block;color:#8f1d15;font-size:16px;margin-bottom:6px}.tt-smart-card p{margin:0;color:#615956;line-height:1.45;font-size:13px}.tt-smart-card span{display:inline-block;margin-top:8px;color:#a82017;font-weight:700;font-size:13px}
      .tt-reserve-area{border:2px dashed #a82017!important;background:linear-gradient(135deg,#fff8e8,#fff)!important}.tt-reserve-area b{color:#8f1d15!important}.tt-reserve-area small{color:#765f54!important}
      .tt-tool-overlay{position:fixed;inset:0;background:rgba(35,8,6,.68);z-index:2147482500;display:none;align-items:center;justify-content:center;padding:18px}.tt-tool-modal{width:min(720px,96vw);max-height:90vh;overflow:auto;background:#fff;border-radius:16px;border:2px solid #d8aa39;box-shadow:0 24px 70px rgba(0,0,0,.32);color:#302724}.tt-tool-title{padding:16px 18px;background:linear-gradient(135deg,#981b15,#c42b20);color:#fff;display:flex;justify-content:space-between;align-items:center}.tt-tool-title h3{margin:0;font-size:20px}.tt-tool-close{border:0;background:rgba(255,255,255,.16);color:#fff;border-radius:8px;width:34px;height:34px;font-size:20px;cursor:pointer}.tt-tool-body{padding:18px}.tt-tool-note{background:#fff7e8;border-left:4px solid #d6a325;padding:10px 12px;margin-bottom:14px;border-radius:7px;font-size:13px;line-height:1.45}.tt-tool-form{display:grid;grid-template-columns:1fr 1fr;gap:12px}.tt-tool-form label{display:block;font-weight:700;color:#6f1a15;font-size:13px}.tt-tool-form input,.tt-tool-form select,.tt-tool-form textarea{box-sizing:border-box;width:100%;margin-top:5px;padding:10px;border:1px solid #d9c8bd;border-radius:8px;font:14px Segoe UI,Arial;background:#fff}.tt-tool-form .full{grid-column:1/-1}.tt-tool-files{font-size:12px;color:#6d625d;margin-top:5px}.tt-tool-actions{display:flex;gap:9px;justify-content:flex-end;margin-top:16px;flex-wrap:wrap}.tt-tool-actions button{border:0;border-radius:9px;padding:11px 15px;font-weight:700;cursor:pointer}.tt-tool-secondary{background:#f0e5dd;color:#7c2018}.tt-tool-primary{background:#a82017;color:#fff}
      @media(max-width:720px){.tt-smart-grid,.tt-tool-form{grid-template-columns:1fr}.tt-tool-form .full{grid-column:auto}}
    `;
    document.head.appendChild(style);
  }

  function addPanel() {
    const ai = $('aiwork');
    if (!ai || document.querySelector('.tt-smart-tools')) return;
    const panel = document.createElement('div');
    panel.className = 'tt-smart-tools';
    panel.innerHTML = `
      <div class="tt-smart-head"><div class="tt-kicker">TIỆN ÍCH AI CHUYÊN SÂU</div><h3>ĐỌC - HỢP NHẤT - TRUYỀN THÔNG VĂN BẢN</h3><p>Hai quy trình hỗ trợ tham mưu và chuyển nội dung văn bản thành sản phẩm dễ sử dụng.</p></div>
      <div class="tt-smart-grid">
        <div class="tt-smart-card" data-tool="merge"><div class="tt-smart-icon">📚</div><div><b>Tham mưu hợp nhất nhiều văn bản</b><p>Đọc nhiều văn bản cùng lĩnh vực, loại trùng lặp và dự thảo một văn bản triển khai chung của xã.</p><span>Mở quy trình →</span></div></div>
        <div class="tt-smart-card" data-tool="image"><div class="tt-smart-icon">🎨</div><div><b>Tạo ảnh tuyên truyền từ văn bản</b><p>Rút nội dung cốt lõi và tạo infographic phục vụ tuyên truyền hoặc trình bày.</p><span>Mở quy trình →</span></div></div>
      </div>`;
    const head = ai.querySelector('.tt-ai-big');
    if (head) head.insertAdjacentElement('afterend', panel); else ai.prepend(panel);
    panel.querySelector('[data-tool="merge"]').onclick = () => openTool('merge');
    panel.querySelector('[data-tool="image"]').onclick = () => openTool('image');
  }

  function addReserveArea() {
    const areas = $('areas');
    if (!areas || areas.querySelector('.tt-reserve-area')) return;
    const card = document.createElement('div');
    card.className = 'area tt-reserve-area';
    card.innerHTML = '<b>🧭 Lĩnh vực dự phòng – Tham mưu theo tác vụ</b><small>Dùng cho nhiệm vụ phát sinh theo yêu cầu lãnh đạo</small>';
    card.onclick = () => openTool('reserve');
    areas.appendChild(card);
  }

  function watchReserveArea() {
    const areas = $('areas');
    if (!areas) return;
    addReserveArea();
    new MutationObserver(addReserveArea).observe(areas, { childList: true });
  }

  function addModal() {
    if ($('ttToolOverlay')) return;
    const overlay = document.createElement('div');
    overlay.id = 'ttToolOverlay';
    overlay.className = 'tt-tool-overlay';
    overlay.innerHTML = '<div class="tt-tool-modal"><div class="tt-tool-title"><h3 id="ttToolTitle">Tiện ích AI</h3><button id="ttToolClose" class="tt-tool-close">×</button></div><div id="ttToolBody" class="tt-tool-body"></div></div>';
    overlay.onclick = (e) => { if (e.target === overlay) closeTool(); };
    document.body.appendChild(overlay);
    $('ttToolClose').onclick = closeTool;
  }

  function fileNames(input, outputId) {
    const names = Array.from(input.files || []).map((f) => f.name);
    $(outputId).textContent = names.length ? names.join(' • ') : 'Chưa chọn tệp.';
  }

  function openTool(type) {
    addModal();
    $('ttToolOverlay').style.display = 'flex';
    if (type === 'reserve') {
      $('ttToolTitle').textContent = '🧭 Lĩnh vực dự phòng – Tham mưu theo tác vụ';
      $('ttToolBody').innerHTML = `
        <div class="tt-tool-note"><b>Khi nào sử dụng:</b> Dùng cho công việc phát sinh chưa thuộc các lĩnh vực hoặc công việc mẫu hiện có. Hãy nhập yêu cầu cụ thể của lãnh đạo; hệ thống sẽ tạo câu lệnh để AI phân tích nhiệm vụ, đề xuất quy trình và chỉ rõ thông tin cần bổ sung.</div>
        <div class="tt-tool-form">
          <label class="full">Tác vụ cụ thể cần thực hiện<input id="ttReserveTask" placeholder="Ví dụ: Rà soát hồ sơ và tham mưu văn bản trả lời..." /></label>
          <label class="full">Nội dung chỉ đạo hoặc yêu cầu của lãnh đạo<textarea id="ttReserveDirection" rows="4" placeholder="Ghi đúng nội dung lãnh đạo giao, mục tiêu và yêu cầu cần đạt..."></textarea></label>
          <label>Sản phẩm dự kiến<select id="ttReserveOutput"><option>Đề xuất quy trình thực hiện</option><option>Công văn</option><option>Kế hoạch</option><option>Báo cáo</option><option>Tờ trình</option><option>Quyết định</option><option>Danh sách hoặc biểu tổng hợp</option><option>Chưa xác định – đề nghị AI gợi ý</option></select></label>
          <label>Thời hạn/đối tượng thực hiện<input id="ttReserveDeadline" placeholder="Có thể để trống nếu chưa được giao" /></label>
          <label class="full">Tài liệu liên quan (không bắt buộc)<input id="ttReserveFiles" type="file" multiple accept=".pdf,.doc,.docx,.xls,.xlsx,.png,.jpg,.jpeg"><div id="ttReserveNames" class="tt-tool-files">Chưa chọn tệp.</div></label>
          <label class="full">Thông tin khác cần lưu ý (nếu có)<textarea id="ttReserveNote" rows="3" placeholder="Ví dụ: thẩm quyền ký, đơn vị phối hợp, mẫu văn bản phải sử dụng..."></textarea></label>
        </div><div class="tt-tool-actions"><button id="ttCancel" class="tt-tool-secondary">Đóng</button><button id="ttRun" class="tt-tool-primary">📋 Tạo câu lệnh & mở ChatGPT</button></div>`;
      $('ttReserveFiles').onchange = (e) => fileNames(e.target, 'ttReserveNames');
      $('ttRun').onclick = runReserve;
    } else if (type === 'merge') {
      $('ttToolTitle').textContent = '📚 Tham mưu hợp nhất nhiều văn bản';
      $('ttToolBody').innerHTML = `
        <div class="tt-tool-note"><b>Cách sử dụng:</b> Chọn các văn bản cùng một lĩnh vực. Trung tâm sẽ chuẩn bị câu lệnh chuẩn; sau khi ChatGPT mở, tải đúng các tệp đã chọn rồi dán câu lệnh. AI chỉ dự thảo, cán bộ kiểm tra trước khi trình ký.</div>
        <div class="tt-tool-form">
          <label>Lĩnh vực<select id="ttMergeArea"><option>Công tác tổ chức cán bộ</option><option>Đánh giá, xếp loại cán bộ</option><option>Quy hoạch cán bộ</option><option>Phân cấp quản lý cán bộ</option><option>Công tác đảng viên</option><option>Tuyên giáo, dân vận</option><option>Khác</option></select></label>
          <label>Văn bản xã dự kiến ban hành<select id="ttMergeType"><option>Kế hoạch</option><option>Công văn triển khai</option><option>Hướng dẫn</option><option>Quyết định</option><option>Báo cáo</option><option>Văn bản khác</option></select></label>
          <label class="full">Chọn ít nhất 02 văn bản cùng lĩnh vực<input id="ttMergeFiles" type="file" multiple accept=".pdf,.doc,.docx,.xls,.xlsx"><div id="ttMergeNames" class="tt-tool-files">Chưa chọn tệp.</div></label>
          <label class="full">Yêu cầu của lãnh đạo (nếu có)<textarea id="ttMergeNote" rows="3" placeholder="Ví dụ: Chỉ ban hành 01 kế hoạch chung; phân rõ nhiệm vụ từng cơ quan..."></textarea></label>
        </div><div class="tt-tool-actions"><button id="ttCancel" class="tt-tool-secondary">Đóng</button><button id="ttRun" class="tt-tool-primary">📋 Sao chép câu lệnh & mở ChatGPT</button></div>`;
      $('ttMergeFiles').onchange = (e) => fileNames(e.target, 'ttMergeNames');
      $('ttRun').onclick = runMerge;
    } else {
      $('ttToolTitle').textContent = '🎨 Tạo ảnh tuyên truyền từ văn bản';
      $('ttToolBody').innerHTML = `
        <div class="tt-tool-note"><b>Cách sử dụng:</b> Chọn văn bản nguồn. AI tóm tắt nội dung để cán bộ duyệt trước, sau đó mới tạo ảnh; không tự thêm số liệu, thời gian hoặc căn cứ.</div>
        <div class="tt-tool-form">
          <label>Mục đích<select id="ttImgPurpose"><option>Infographic tuyên truyền</option><option>Ảnh trình bày tại hội nghị</option><option>Ảnh thông báo nội bộ</option><option>Ảnh đăng mạng xã hội</option></select></label>
          <label>Đối tượng<select id="ttImgAudience"><option>Cán bộ, đảng viên</option><option>Cấp ủy, tổ chức đảng</option><option>Nhân dân</option><option>Cán bộ chuyên môn</option></select></label>
          <label class="full">Chọn văn bản mới<input id="ttImgFile" type="file" accept=".pdf,.doc,.docx"><div id="ttImgName" class="tt-tool-files">Chưa chọn tệp.</div></label>
          <label>Khổ ảnh<select id="ttImgSize"><option>Dọc - infographic</option><option>Ngang - màn hình trình chiếu</option><option>Vuông - mạng xã hội</option></select></label>
          <label>Phong cách<select id="ttImgStyle"><option>Trang trọng, hiện đại, màu đỏ - vàng</option><option>Hành chính, rõ ràng, ít trang trí</option><option>Trực quan, dễ đọc, nhiều biểu tượng</option></select></label>
          <label class="full">Nội dung cần nhấn mạnh (nếu có)<textarea id="ttImgNote" rows="3" placeholder="Ví dụ: thời gian, đối tượng, nhiệm vụ trọng tâm..."></textarea></label>
        </div><div class="tt-tool-actions"><button id="ttCancel" class="tt-tool-secondary">Đóng</button><button id="ttRun" class="tt-tool-primary">🎨 Sao chép câu lệnh & mở ChatGPT</button></div>`;
      $('ttImgFile').onchange = (e) => fileNames(e.target, 'ttImgName');
      $('ttRun').onclick = runImage;
    }
    $('ttCancel').onclick = closeTool;
  }

  function closeTool() { $('ttToolOverlay').style.display = 'none'; }

  function copyAndOpen(text) {
    if (navigator.clipboard) navigator.clipboard.writeText(text).catch(() => {});
    window.open(AI_URL, '_blank');
    setTimeout(() => alert('Đã sao chép câu lệnh. Hãy tải văn bản đã chọn lên ChatGPT, sau đó dán câu lệnh để thực hiện.'), 150);
  }

  function runMerge() {
    const files = Array.from($('ttMergeFiles').files || []);
    if (files.length < 2) return alert('Hãy chọn ít nhất 02 văn bản cùng lĩnh vực.');
    const area = $('ttMergeArea').value;
    const type = $('ttMergeType').value;
    const note = $('ttMergeNote').value.trim();
    const names = files.map((f, i) => `${i + 1}. ${f.name}`).join('\n');
    copyAndOpen(`Bạn đang hỗ trợ Đảng ủy xã Thư Lâm tham mưu xử lý nhiều văn bản cùng lĩnh vực.

LĨNH VỰC: ${area}
VĂN BẢN XÃ DỰ KIẾN BAN HÀNH: ${type}
CÁC TỆP NGUỒN:
${names}
${note ? `YÊU CẦU CỦA LÃNH ĐẠO: ${note}\n` : ''}
NHIỆM VỤ:
1. Đọc toàn bộ văn bản và lập bảng đối chiếu: cơ quan ban hành, số ký hiệu, ngày, phạm vi, nhiệm vụ, thời hạn, đối tượng thực hiện.
2. Xác định nội dung trùng lặp, nội dung bổ sung và điểm chưa thống nhất; không tự suy đoán.
3. Đề xuất phương án ban hành 01 văn bản chung của xã để triển khai đồng bộ, tránh nhiều văn bản rời.
4. Soạn dự thảo ${type} ngắn gọn, đúng thẩm quyền; phân rõ chủ trì, phối hợp, sản phẩm và thời hạn khi nguồn có quy định.
5. Chỉ sử dụng thông tin trong tài liệu. Thiếu ghi [CẦN BỔ SUNG], mâu thuẫn ghi [CẦN KIỂM TRA]. Không tự tạo căn cứ, số liệu, tên người hoặc thời hạn.
6. Cuối dự thảo lập mục NỘI DUNG CẦN CÁN BỘ KIỂM TRA TRƯỚC KHI TRÌNH KÝ.

AI chỉ hỗ trợ tham mưu; cán bộ chịu trách nhiệm kiểm tra và quyết định văn bản chính thức.`);
  }

  function runReserve() {
    const task = $('ttReserveTask').value.trim();
    const direction = $('ttReserveDirection').value.trim();
    if (!task) return alert('Hãy nhập tác vụ cụ thể cần thực hiện.');
    if (!direction) return alert('Hãy nhập nội dung chỉ đạo hoặc yêu cầu của lãnh đạo.');
    const output = $('ttReserveOutput').value;
    const deadline = $('ttReserveDeadline').value.trim();
    const note = $('ttReserveNote').value.trim();
    const files = Array.from($('ttReserveFiles').files || []);
    const names = files.length ? files.map((f, i) => `${i + 1}. ${f.name}`).join('\n') : 'Không có tài liệu đính kèm.';
    copyAndOpen(`Bạn đang hỗ trợ cán bộ Ban Xây dựng Đảng xã Thư Lâm xử lý một nhiệm vụ phát sinh theo chỉ đạo của lãnh đạo.

TÁC VỤ CỤ THỂ: ${task}
CHỈ ĐẠO/YÊU CẦU CỦA LÃNH ĐẠO: ${direction}
SẢN PHẨM DỰ KIẾN: ${output}
${deadline ? `THỜI HẠN/ĐỐI TƯỢNG: ${deadline}\n` : ''}${note ? `LƯU Ý KHÁC: ${note}\n` : ''}TÀI LIỆU LIÊN QUAN:
${names}

HÃY THỰC HIỆN THEO TRÌNH TỰ:
1. Tóm tắt chính xác yêu cầu và xác định mục tiêu cuối cùng của tác vụ.
2. Xác định tác vụ thuộc hoặc gần với lĩnh vực nghiệp vụ nào; nêu cơ quan, người chủ trì/phối hợp nếu thông tin nguồn đã có.
3. Đề xuất các bước thực hiện theo thứ tự, hồ sơ/tài liệu cần chuẩn bị và sản phẩm của từng bước.
4. Liệt kê riêng những thông tin còn thiếu, điểm chưa rõ hoặc nội dung cần xin ý kiến lãnh đạo trước khi làm tiếp.
5. Gợi ý câu hỏi ngắn gọn để cán bộ bổ sung thông tin cần thiết. Không hỏi lại những nội dung đã có.
6. Khi đủ thông tin, đề xuất cấu trúc hoặc soạn dự thảo sản phẩm phù hợp; trước khi soạn phải để cán bộ xác nhận phương án.

NGUYÊN TẮC:
- Chỉ sử dụng nội dung tôi cung cấp và tài liệu tải lên; không tự tạo căn cứ, số liệu, tên người, chức vụ, thời hạn hoặc kết quả.
- Nội dung thiếu ghi [CẦN BỔ SUNG]; nội dung mâu thuẫn ghi [CẦN KIỂM TRA].
- Phân biệt rõ: thông tin từ tài liệu, nhận định của AI và đề xuất để cán bộ lựa chọn.
- AI chỉ hỗ trợ tham mưu; cán bộ kiểm tra trước khi sử dụng hoặc trình lãnh đạo.`);
  }

  function runImage() {
    const file = $('ttImgFile').files && $('ttImgFile').files[0];
    if (!file) return alert('Hãy chọn văn bản nguồn.');
    const purpose = $('ttImgPurpose').value;
    const audience = $('ttImgAudience').value;
    const size = $('ttImgSize').value;
    const style = $('ttImgStyle').value;
    const note = $('ttImgNote').value.trim();
    copyAndOpen(`Đọc kỹ văn bản tôi tải lên: ${file.name}. Hãy tạo 01 ${purpose} phục vụ ${audience}.

YÊU CẦU NỘI DUNG:
- Chỉ lấy thông tin trong văn bản; không tự thêm số liệu, căn cứ, thời gian, địa điểm hoặc tên người.
- Chọn tiêu đề ngắn gọn; rút 4-6 nội dung quan trọng nhất, ưu tiên đối tượng, nhiệm vụ, thời gian, cách thực hiện và yêu cầu cần nhớ.
- Trước khi tạo ảnh, đưa bản tóm tắt chữ để tôi kiểm tra. Chỉ tạo ảnh sau khi tôi xác nhận.

YÊU CẦU THIẾT KẾ:
- Khổ ảnh: ${size}.
- Phong cách: ${style}.
- Tiêu đề lớn, các khối nội dung rõ, màu sắc trang trọng; chữ tiếng Việt đầy đủ dấu, dễ đọc.
- Không dùng logo, hình chân dung hoặc biểu tượng cơ quan nếu văn bản không yêu cầu; không chèn nội dung ngoài nguồn.
${note ? `- Nội dung cần nhấn mạnh: ${note}.\n` : ''}
Sau khi tôi duyệt phần chữ, hãy dùng công cụ tạo ảnh để xuất hình hoàn chỉnh, không watermark.`);
  }

  function normalizedTaskText(value) {
    return String(value || '').toLowerCase().replace(/\s+/g, ' ').trim();
  }

  function detailedProductForCommune(task) {
    const t = normalizedTaskText(task);
    const explicit = (label, detail) => `${label}: ${detail}`;
    if (/(báo cáo).*(rà soát)|(rà soát).*(báo cáo)/i.test(t))
      return explicit('Báo cáo kết quả rà soát', 'kèm bảng tổng hợp/danh sách hoặc phụ lục theo đúng yêu cầu của văn bản nguồn (nếu có)');
    if (/rà soát|thống kê|tổng hợp danh sách/i.test(t))
      return '[ĐỀ XUẤT ĐỂ LÃNH ĐẠO DUYỆT] Bảng tổng hợp hoặc danh sách kết quả rà soát; kèm báo cáo/công văn gửi cơ quan yêu cầu nếu văn bản nguồn yêu cầu báo cáo';
    if (/xây dựng|ban hành/.test(t) && /kế hoạch/.test(t))
      return explicit('Dự thảo Kế hoạch của cấp xã', 'nêu mục đích, nhiệm vụ, phân công đơn vị chủ trì/phối hợp, tiến độ và chế độ báo cáo theo văn bản nguồn');
    if (/kế hoạch/.test(t))
      return explicit('Kế hoạch triển khai của cấp xã', 'kèm phân công nhiệm vụ và tiến độ thực hiện theo nội dung văn bản nguồn');
    if (/công văn/.test(t) && /triển khai|thực hiện|hướng dẫn/.test(t))
      return explicit('Dự thảo Công văn triển khai', 'xác định rõ đối tượng thực hiện, nhiệm vụ, sản phẩm và thời hạn theo văn bản nguồn');
    if (/báo cáo/.test(t))
      return explicit('Báo cáo của cấp xã', 'kèm biểu mẫu/phụ lục/danh sách theo văn bản nguồn; nêu kết quả, tồn tại và kiến nghị nếu được yêu cầu');
    if (/đăng ký|đề xuất danh sách/.test(t))
      return explicit('Công văn đăng ký/đề xuất', 'kèm danh sách và phụ lục theo mẫu của cơ quan yêu cầu (nếu có)');
    if (/xin ý kiến|lấy ý kiến|góp ý/.test(t))
      return explicit('Văn bản tham gia ý kiến', 'kèm bảng tổng hợp ý kiến hoặc nội dung thống nhất/đề nghị sửa đổi theo yêu cầu');
    if (/quyết định|kiện toàn|thành lập/.test(t))
      return explicit('Dự thảo Quyết định', 'kèm tờ trình, danh sách hoặc hồ sơ liên quan theo quy trình và thẩm quyền');
    if (/hội nghị|tập huấn|quán triệt/.test(t))
      return '[ĐỀ XUẤT ĐỂ LÃNH ĐẠO DUYỆT] Kế hoạch/tài liệu tổ chức; danh sách đại biểu; biên bản hoặc báo cáo kết quả sau khi hoàn thành';
    if (/kiểm tra|giám sát/.test(t))
      return '[ĐỀ XUẤT ĐỂ LÃNH ĐẠO DUYỆT] Kế hoạch hoặc nội dung kiểm tra; biên bản làm việc; báo cáo kết quả và kiến nghị xử lý';
    if (/tuyên truyền|phổ biến|quán triệt/.test(t))
      return '[ĐỀ XUẤT ĐỂ LÃNH ĐẠO DUYỆT] Nội dung/kế hoạch tuyên truyền; tài liệu hoặc sản phẩm truyền thông; báo cáo kết quả nếu được yêu cầu';
    if (/tham mưu/.test(t))
      return '[ĐỀ XUẤT ĐỂ LÃNH ĐẠO DUYỆT] Dự thảo văn bản tham mưu phù hợp thẩm quyền; kèm tài liệu, bảng tổng hợp hoặc hồ sơ làm căn cứ';
    return '[CẦN LÃNH ĐẠO XÁC ĐỊNH] Chốt rõ loại sản phẩm chính, tài liệu kèm theo, đơn vị nhận và thời hạn hoàn thành';
  }

  function communeImplementationFor(task) {
    const t = normalizedTaskText(task);
    const steps = ['Đối chiếu yêu cầu và xác định đơn vị/cá nhân thuộc phạm vi cấp xã'];
    if (/rà soát|thống kê|danh sách/.test(t)) steps.push('Tổ chức rà soát, thu thập số liệu và lập danh sách/bảng tổng hợp');
    if (/kế hoạch|triển khai|thực hiện/.test(t)) steps.push('Tham mưu văn bản triển khai, phân rõ chủ trì, phối hợp và tiến độ');
    if (/báo cáo/.test(t)) steps.push('Tổng hợp kết quả theo đề cương/biểu mẫu và kiểm tra số liệu trước khi trình');
    if (/xin ý kiến|lấy ý kiến|góp ý/.test(t)) steps.push('Lấy ý kiến đơn vị liên quan và tổng hợp nội dung tiếp thu/giải trình');
    if (/hội nghị|tập huấn|quán triệt/.test(t)) steps.push('Chuẩn bị nội dung, thành phần, điều kiện tổ chức và tài liệu phục vụ');
    steps.push('Trình lãnh đạo duyệt; ban hành/gửi đúng nơi nhận và cập nhật kết quả hoàn thành');
    return steps.map((s, i) => `${i + 1}. ${s}`).join(' ');
  }

  function installAIAssignEnhancement() {
    if (window.__ttCommuneAdviceInstalled || typeof window.analyzeAIDocument !== 'function' || typeof window.renderAIProposals !== 'function') return;
    window.__ttCommuneAdviceInstalled = true;
    const baseAnalyze = window.analyzeAIDocument;
    const baseRender = window.renderAIProposals;

    window.analyzeAIDocument = function () {
      baseAnalyze();
      if (typeof AI_PROPOSALS !== 'undefined') {
        AI_PROPOSALS.forEach((x) => {
          x.communeImplementation = communeImplementationFor(x.task);
          x.product = detailedProductForCommune(x.task);
        });
        window.renderAIProposals();
      }
    };

    window.renderAIProposals = function () {
      baseRender();
      if (typeof AI_PROPOSALS === 'undefined') return;
      const rows = document.querySelectorAll('#aiAssignRows tr');
      rows.forEach((row, i) => {
        const x = AI_PROPOSALS[i];
        if (!x) return;
        const taskCell = row.cells[1];
        if (taskCell && !taskCell.querySelector('.tt-commune-advice')) {
          const box = document.createElement('div');
          box.className = 'tt-commune-advice';
          const label = document.createElement('b');
          label.textContent = 'Cấp xã cần triển khai: ';
          box.appendChild(label);
          box.appendChild(document.createTextNode(x.communeImplementation || communeImplementationFor(x.task)));
          taskCell.appendChild(box);
        }
        const productCell = row.cells[5];
        const oldInput = productCell && productCell.querySelector('input.ai-inline-input');
        if (oldInput) {
          const area = document.createElement('textarea');
          area.className = 'ai-inline-input tt-product-detail';
          area.rows = 5;
          area.value = x.product || '';
          area.onchange = () => { AI_PROPOSALS[i].product = area.value; };
          oldInput.replaceWith(area);
          const hint = document.createElement('small');
          hint.className = 'tt-product-hint';
          hint.textContent = 'Lãnh đạo rà soát và chỉnh lại trước khi duyệt giao việc.';
          productCell.appendChild(hint);
        }
      });
    };

    const pane = $('c-aiassign');
    const note = pane && pane.querySelector('.ctrl-note');
    if (note) note.innerHTML = '<b>Quy trình chuẩn:</b> Chọn văn bản đã lưu trong <b>Văn bản chỉ đạo</b> → hệ thống đọc nội dung → xác định yêu cầu đối với cấp xã → đề xuất <b>cấp xã cần triển khai thế nào</b>, người chủ trì/phối hợp, <b>kết quả/sản phẩm cụ thể</b> và thời hạn. Nội dung AI suy ra được gắn nhãn để lãnh đạo kiểm tra. <b>Chỉ sau khi lãnh đạo bấm “Duyệt & giao việc” thì nhiệm vụ mới vào Dashboard.</b>';
  }

  function init() {
    addStyles(); addPanel(); addModal(); watchReserveArea(); installAIAssignEnhancement();
    const extra = document.createElement('style');
    extra.textContent = '.tt-commune-advice{margin-top:8px;padding:8px;border-left:3px solid #a82017;background:#fff7e8;color:#594b43;font-size:12px;line-height:1.45}.tt-commune-advice b{color:#8f1d15}.tt-product-detail{min-width:240px;line-height:1.35;resize:vertical}.tt-product-hint{display:block;margin-top:4px;color:#8a5b22;line-height:1.3}';
    document.head.appendChild(extra);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
