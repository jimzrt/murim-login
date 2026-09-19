<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0432.txt",
      "sha256": "112b8037ca895cff83acfec662baee794c86438ff55c177924ac32d0b7d43422",
      "bytes": 13664
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "cba02a7766ad90454a936979a8332b1cafd99c81e7c5886ed716a286c569435c",
      "bytes": 2917
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "63a23715f5ad9b22a0a45f09af5ba17eb049e72f3afcc18c03f938db719596ab",
      "bytes": 142400
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "761c4e90611152429f124e468df2c2d5c4a7f759f8cde16ff962ec431718550f",
      "bytes": 590
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "3beae0f29113ee709286cd33bd87f4d4f543ce8bfdca69e44b16467bc46fd093",
      "bytes": 800
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "cae6591952f10c5d5e266d2b51fd9bd2271c52057a1f53da92db702e50d754b4",
      "bytes": 1182
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "018d88cf08075ae25c728a10fef8854bb4932dbaab4b20a0bb90fcc72b2f5180",
      "bytes": 795
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4bfbc0882d252b2473237ab7defa1a1cd251e79d271f548777bb003141fc7f96",
      "bytes": 133895
    }
  ],
  "estimated_tokens": 10179
}
-->

# Durable State Update — Chapter 432

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 432. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 432. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 432,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 432,
    "continuity_sources": [432],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The Arch Lich's magic-circle fragments match the patterns and symbols of the Moving Formation Jin saw in Murim, and can be assembled into one enormous circle.",
    "The circle appears to have absorbed human life force to accumulate mana, but this remains the Skeleton King's inference rather than a confirmed decipherment.",
    "The circle at the Arch Lich's ruined base is inactive and retains traces of the deaths it once caused; Jin gains no interpretation from it and the System remains silent.",
    "Jin suspects that the Murim formation, the modern world's magic circle, the battle phenomena involving the Blood Lord and Western Heaven Demon Lord, and his junk capsule are connected.",
    "Magic Johnson is researching the circle on behalf of the coalition forces and now knows that Jin killed Lee Jungryong and Wu Heixing.",
    "The Skeleton King remains hidden in Jin's Inventory or an extradimensional pocket when necessary and continues pursuing a human-world identity as Stone-King.",
    "Chairman Shao is preparing a political reckoning against the Crown Prince Party after its persecution and forced-labor campaign.",
    "Jin's mother and Hayeon remain in China under Chairman Shao's protection.",
    "Lee Jungryong and Wu Heixing were killed by Jin, while the public remains unaware of the full truth.",
    "Go Jun remains alive after Jin grievously mutilated him and demanded that the conflict end with Lee Jungryong.",
    "Jin chose not to kill Go Jun because his disappearance would make suspicion surrounding Jin's earlier killings harder to dismiss.",
    "Magic Johnson expects a detailed discussion with Jin about what happened at the ruins."
  ],
  "continuity_sources": [
    431,
    430
  ],
  "open_questions": [
    "What do the shared patterns and symbols represent, and why did the Arch Lich possess a circle matching the Moving Formation?",
    "What connection links the two worlds, the battle phenomena, and the junk capsule?",
    "What will Magic Johnson do after learning the truth about the confrontation and Jin's killings?",
    "What final punishment will be imposed on Wu Heixing's father and the Crown Prince Party leadership?",
    "How will the Skeleton King's human identity and Stone-King name be formalized in the human world?"
  ],
  "safe_through": 431,
  "temporary_decisions": [
    "Render 샤오 쉔 as “Xiao Shen” and preserve “hyung” for his address to Jin.",
    "Render 매직 존슨 as “Magic Johnson,” 스켈레톤 킹 as “Skeleton King,” and 스톤-킹 as “Stone-King.”",
    "Render the suspected function of the circle as “life-force absorption” while preserving the uncertainty of the inference.",
    "Preserve Jin's dry, profane voice and the Skeleton King's grandiose, Internet-influenced insults.",
    "Render 아공간 포켓 as “extradimensional pocket.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 암천     | **Dark Heaven**                  |
| 살기     | **killing intent**                               |                                                       |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 귀가      | **your family**                                                 |
| 대사      | **Master** for a senior Buddhist monk                           |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 선장 | **Zen staffs** | Staff weapons carried by the Hundred and Eight Arhats. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 420
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 431
- **Aliases:** Team Leader Seok
- **Role:** Leader of Lee Jungryong's security team, an Ares Guild combatant, and Lee's disciple and right-hand man who remains alive after Jin Taekyung grievously mutilated him.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and capable of suppressing his anger and killing intent under provocation.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of the late Lee Jungryong, Go Jun confronted Jin Taekyung over Lee's death and was forced to accept Jin's demand that the conflict end with Lee.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 431
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 431
- **Aliases:** None
- **Role:** Wu Heixing was a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practiced martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts, before Jin Taekyung killed him.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger and protects himself even while his allies die.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃432화



매직 존슨은 좋은 사람이다.

전장에서도, 사회에서도 마찬가지다.

그는 어떤 상황에서도 늘 유쾌하고 웃음을 잃지 않는다. 특히 나와 최 팀장에게는 각별한 호의를 갖고 있기에 스켈레톤 킹에 관한 문제를 비밀리에 해결해 주기도 했다.

하지만 지금 나를 바라보는 매직 존슨의 눈빛에는 어떤 장난기나 웃음도 찾아볼 수 없었다.

여러 감정이 뒤섞인 복잡한 눈빛으로 말없이 나를 응시하던 그가 불현듯 입을 열었다.

「어디부터 어디까지가 진실이지?」

“처음부터 끝까지. 보고 들으신 전부요.”

나는 전부라는 두 글자에 유난히 힘을 주었다. 그리고 매직 존슨은 이 말에 담긴 뜻을 알아차리지 못할 만큼 둔한 사람이 아니었다.

「……처음부터 알고 있었던 거군.」

“아시다시피 제가 좀 예민해서.”

「그런데도 상관없었다?」

“제 뒤를 따라오실 줄은 몰랐어요. 하지만 이것도 나쁘지 않겠다는 생각이 들었죠.”

「궁금했어. 한편으로는 걱정도 됐고. 저 수수께끼의 문양에 관해 뭔가 알고 있는 것이 분명한데 숨기는 모습이 너무 뻔히 보였으니까.」

헤어지기 전, 마법진에 관해 묻는 매직 존슨에게 나는 꿈에서 본 것 같다며 변명했었다.

당연히 믿으라고 한 소리가 아니라, 지금 당장은 묻지 말라는 완곡한 표현이었다.

「그래서 혹시나 하는 마음에 뒤따라 온 건데…….」

말꼬리를 흐린 매직 존슨이 온통 핏물로 뒤덮인 주위를 둘러보며 말을 이었다.

「괜한 짓을 한 모양이야.」

한 나라의 얼굴이나 다름없는 S급 헌터가 둘이나 죽은 대사건, 심지어 그중 한 사람은 한때 매직 존슨과 같은 전장에서 싸웠던 전우이기도 했다.

간혹 어떤 종류의 진실은 불편하게 느껴지기도 한다. 바로 지금 이 자리가 매직 존슨에게는 그럴 것이다.

“후회되십니까?”

「조금은. 차라리 모르는 게 나았을지도 모르지.」

나직하게 한숨을 내쉰 매직 존슨이 나를 똑바로 응시했다.

「진. 내게 이런 사실을 알려 주는 의도가 뭐지?」

“글쎄요.”

「어차피 진실을 아는 건 너 혼자였어. 마음만 먹는다면 이대로 은폐시킬 수 있었다고. 저 자에게도 마찬가지지.」

정신을 잃은 석고준을 힐끗 바라본 나는 고개를 저었다.

“숨긴다고 해서 숨길 수 있는 종류의 것이 아니었어요. 제가 아무리 부정한다고 해도 어차피 저놈은 믿지 않았을 겁니다. 이정룡도, 저 녀석도 언제 터질지 모르는 시한폭탄이었죠. 제 사람들을 위협할 만큼.”

「진. 너는…… 저들과 적이었구나. 이미 예전부터.」

“네. 적을 제거할 수 없는 상황이라면, 저를 두 번 다시 쳐다보지도 못할 만큼 두려워하게 만들어야 합니다. 뇌관이 제거된 폭탄은 터지지 않을 테니까.”

「그렇다면 나는? 내게는 왜 이 사실을 알려 준 거지?」

“알고 계시잖아요. 지금 같은 상황에서 선택할 수 있는 사람은 두 종류뿐이라는 거.”

나는 또박또박, 천천히 말을 이었다.

“적. 아니면 친구.”

「……!」

“존슨이라면 절 믿을 거라 생각했습니다. 제 친구니까.”

낮은 침음성을 흘린 매직 존슨이 온갖 감정이 뒤섞인 복잡한 눈빛으로 나를 응시했다.

「친구라고 해서 모든 걸 믿어 주지는 않아, 진.」

“하지만 믿어 주셨죠. 대화를 나누는 내내 단 한 번도 절 의심하지 않으셨어요.”

「…….」

“절 도와주세요. 제 사람들을 지키고, 힘을 키울 수 있도록.”

어느 순간부터, 나를 둘러싼 모든 것들이 변화하고 있는 것이 느껴진다.

무림에서는 암천이 준동했으며 현대에서는 아크 리치라는 전대미문의 네임드 몬스터가 수백만의 인명을 학살하고 재앙을 초래했다.

그리고 두 세계에서 나타난 알 수 없는 문양과 기호들. 아니, 어쩌면 ‘흑마법’이라 부르는 것일지도 모르는 무언가.

‘이 모든 것이 우연일까.’

세상에서 벌어지는 모든 일은 보이지 않는 고리로 연결되어 있다. 도미노처럼 줄줄이 쓰러지지 않으려면 준비해야 한다.

그러기 위해서는 한 사람의 아군이 절실하다.

“존슨.”

「……빌어먹을.」

잠시 말이 없던 매직 존슨이 깊은 한숨을 내쉬었다.

「그거 알아?」

“……?”

「그날. 네가 몬스터 군단이 기다리는 그곳으로 텔레포트를 시켜 달라고 하지 않았다면, 난 널 의심했을지도 몰라.」

승낙을 뜻하는 한마디.

환하게 밝아진 내 얼굴에, 매직 존슨도 어쩔 수 없이 풀썩 웃어 버렸다.

「젠장. 이렇게 된 이상 어쩔 수 없군. 우선 순찰이 오기 전에 주위부터 치우자고.」

그가 손을 내젓자 사방에 튀어있던 핏물이 흔적도 없이 지워졌다.

클린 마법으로 단번에 주변을 정리한 매직 존슨이 쓰러진 석고준을 보며 미간을 좁혔다.

「이자가 문제인데…… 아예 기억을 지워 버리고 싶어도 상황이 애매하니, 거 참.」

“어?”

귀가 번쩍 뜨이는 말이다.

문득 과거 명동 길드에 쳐들어갔을 당시, 아레스 길드의 마법사들이 현장에 있던 명동 길드원들에게 기억 조작 마법을 사용한 것이 생각났다.

“할 수 있어요?”

「당연히 어렵겠지만 불가능하지는 않아. 다만 대상이 강한 정신력을 지니고 있고, 조작해야 하는 기억의 정도에 따라 더 어려워지겠지.」

“아.”

「이자는 상당히 강해 보이는데, 최악의 경우에는 실패하고 정신 조작을 시도한 흔적까지 남을지도 몰라.」

저래 봬도 S급 헌터의 반열에 들기에는 충분한 석고준이다.

우헤이싱과는 달리 제법 심지가 굳센 놈이기도 하니 괜한 시도는 모험일 수도 있었다.

“흔적이 남으면 곤란한데.”

「응. 만약에 발각되면 처벌을 피할 수 없을걸? 정신 조작 마법은 심각한 중범죄니까.」

그런 일을 이정룡과 아레스 길드는 아무렇지 않게 해냈다.

알아차린 사람이 있다 하더라도 감히 의문을 제시하지 못한다. 그들이 가진 힘과 권력을 알기 때문이다.

“그래도 만약 시도해서 성공한다면…….”

「연방법 기준으로는 최소 가석방 없는 징역 100년 이상. 할래?」

나는 숨도 쉬지 않고 대답했다.

“아뇨.”

「굿 보이. 좋은 생각이야.」

최소가 가석방 없는 징역 100년이라니.

걸렸다가는 얄짤 없이 감옥에서 썩게 생겼다. 도망친다고 해도 국제적 지명 수배자로 평생을 살게 될 것이다.

만화에서처럼 현상금 100억 베리쯤 걸린 다음 소말리아의 위대한 항로에서 해적질이나 하며 살지도 모른다.

생각만 해도 끔찍한 일이지…….

“아쉽네요. 한국이면 시도해 볼 만한데.”

「코리아? 왜?」

“여기저기 돈 뿌리고, 전관예우 받는 전직 검사장 출신 변호사 고용하면 형량 얼마 안 나올걸요.”

「전콴예후? 그게 뭔데.」

“그런 게 있어요. 아, 소주 다섯 병쯤 원샷 하고 취중에 저지른 일이라고 하면 집행유예 받을 수도.”

매직 존슨은 대단한 농담이라도 들은 것처럼 껄껄 웃었다.

「말도 안 되는 소리 하지 마, 진. 그런 나라가 어디 있어?」

“…….”

「진짜야? 맙소사.」

어쨌건 기억 조작 마법은 물 건너갔다.

나는 쓰러진 석고준을 놔둔 채 걸음을 옮겼다. 석고준이 은신시켜 둔 A급 헌터 세 명은 내가 쏘아 보낸 지풍에 마혈(痲穴)이 점혈 당한 채 석상처럼 굳어 있었다.

“다 봤지?”

세 놈은 공포에 젖은 눈빛으로 나를 올려다봤다.

직접 당하는 것보다 지켜보는 것이 오히려 더 큰 공포를 심어 줄 때가 있다.

석고준이 잔인하고 철저하게 짓밟히는 모습을 손가락 하나 까딱하지 못하는 상태로 지켜본 놈들은 반쯤 혼이 빠져 있었다.

“너희 얼굴 전부 기억했고, 신상 정보 입수하는 건 시간 문제야.”

힘 있는 자들이 늘 해 왔던 방식이다.

놈들을 죽이지 못한다면 그 방식 그대로 공포를 심어 주어야 한다. 다시는 이빨을 들이대지 못하도록.

“다시 이런 식으로 마주친다면…… 그때는 죽인다.”

콰아아아아!

순간적으로 내뿜어진 살기가 사방을 베고 짓눌렀다.

기운을 갈무리한 나는 시체처럼 창백해진 세 놈의 얼굴을 천천히 쓸어보다 불쑥 손을 뻗었다.

투두둑!

“크헉!”

“훅, 후욱.”

마침내 점혈에서 풀려난 놈들이 참았던 숨을 토해 냈다. 충혈된 눈가에는 물기가 고여 있고, 벌어진 입가에서 침과 토사물이 줄줄 흘러나왔다.

“10초 준다. 저 새끼 데리고 꺼져.”

저 새끼가 누굴 가리키는 말인지는 명백하다.

말이 끝나기도 전에 허우적거리며 일어난 세 사람이 석고준을 향해 달려갔다.

번개 같은 속도로 아직 정신을 차리지 못한 상관을 업고 사라지는 놈들을 향해, 나는 마지막 한마디를 던졌다.

“오늘 있었던 일, 전부 기억에서 지워. 그리고 잘 생각해라. 어느 배에 타고 있어야 목숨을 보전할지.”

“……!”

“……!”

“……!”

아레스 길드는 거대하면서도 견고한 배다.

하지만 위대한 선장이었던 천태민은 이미 자취를 감춘 지 오래였고, 뒤를 이어 방향키를 잡은 이정룡마저 죽음을 맞이했다.

영원히 바다를 누빌 것 같던 배가 기울어지기 시작하는 상황.

선장은 배를 버릴 수 없으나 배에 고용된 선원들은 다르다.

그들은 자신이 원한다면 새로운 배와 선주(船主)를 찾을 수 있다.

‘이만하면 충분히 알아들었겠지.’

내 말을 듣고 잠시 주춤거리던 세 사람은 이내 어둠 너머로 파묻혔다.

아무런 대답도, 별다른 반응도 없이 사라졌지만 나는 알고 있다. 놈들은 내 말을 결코 잊지 못하리라는 걸.

수십, 수백 번을 곱씹다가 주위의 다른 동료들에게 전해 줄 테고, 그렇게 아레스 길드라는 거대한 배의 밑창에는 서서히 물이 차오르기 시작할 것이다.

- 오오, 간악한 인간. 오오오.

“이게 다 계략이라는 거다, 인마.”

- 머리는 나쁜데, 어찌 이리도 음습하고 교활할 수가!

“……아니, 이 새끼가.”

맞는 말이긴 한데 개빡치네.

헌터 생활 몇 년 하다 보니 경험으로 이것저것 체득하게 되었다고 해 두자.

현재의 마정석은 최첨단 문명의 필수 원동력. 그러다 보니 자연스럽게 큰 자본이 모였고, 자본이 있으니 사람이 모였으며 사람들 사이에서는 온갖 별의별 일들이 벌어지기 마련이다.

‘우선 아는 대로 던져 놓긴 했는데…… 기다리고 있으면 입질이 오겠지.’

마치 무림에서의 문파처럼, 현대 길드의 위상은 얼마나 대단한 헌터를 보유하느냐로 결정된다.

그리고 석고준은 결코 이정룡의 빈자리를 메울 수 없다. 과거 이정룡이 천태민의 공백을 채울 수 없었듯이.

텅 빈 공백 너머로 또 다른 먹음직스러운 미끼를 본 물고기들이 빠져나가는 건 시간문제다.

「거침없군. 아레스 길드와 전쟁이라도 할 셈이야?」

나는 매직 존슨의 말에 어깨를 으쓱했다.

“못 할 것도 없지만, 모양새 좋게 가야죠.”

「모양새라.」

“평화 길드는 앞으로 엄청나게 성장할 겁니다. 저도 있고, 최 팀장님도 매스컴의 주목을 받고 있죠.”

「아, 나도 소식 들었어. 요즘 최가 대단하다던데.」

세계 언론의 스포트라이트가 향하는 곳은 나지만, 내가 언론과의 접촉을 피할수록 최 팀장을 향한 관심도 높아졌다.

같은 평화 길드 소속이며 내 병실을 드나들 수 있었던 극소수의 인물.

거기에 더해 이번 몬스터 웨이브에서 세운 훌륭한 전공과 연예인 뺨치는 외모까지.

‘가장 큰 비밀은 아직 밝혀지지 않았지만.’

바로 그 천태민의 핏줄이라는 것까지 공개된다면 언론은 한바탕 난리를 피울 것이 분명하다.

“뭐 어쨌든. 평화 길드가 날아오르는 건 시간문제라는 거죠. 아레스 길드의 영향력은 나날이 줄어들 테고.”

「으음. 충분히 그럴 수 있지.」

고개를 끄덕인 매직 존슨이 문득 입을 열었다.

「그런데, 진.」

“네?”

「마법진에 대해 도대체 뭘 알고 있는…….」

“아, 맞다. 클럽!”

「응?」

“스켈레톤 킹이랑 클럽 가기로 하셨다면서요.”

「잠깐, 잠깐만, 진!」

“골골아. 클럽 가자!”

- 예에! 갈비뼈 들고 소리 질러!

나는 스켈레톤 킹의 헛소리를 들으며 황급히 걸음을 옮겼다. 그리고 희미한 달빛을 바라보며 문득 생각했다.

‘슬슬 돌아가야겠어.’

때가 다가오고 있었다. 또 다른 세상, 무림으로 돌아갈 시기가.
```

## Final English reading copy

```markdown
# Chapter 432

Magic Johnson was a good man.

He was the same way both on the battlefield and in society.

No matter the situation, he was always cheerful and never lost his smile. He had shown particular kindness to Team Leader Choi and me, even secretly resolving the matter concerning the Skeleton King for us.

But there was no trace of playfulness or laughter in the way Magic Johnson was looking at me now.

He silently stared at me with a complicated gaze filled with mixed emotions before suddenly opening his mouth.

“Which parts were true?”

“Everything. From beginning to end. Everything you saw and heard.”

I put particular emphasis on the word *everything*. And Magic Johnson was not dull enough to miss what I meant.

“…So you knew from the beginning.”

“As you know, I’m a little sensitive.”

“And that didn’t matter?”

“I didn’t expect you to follow me. But I thought it might not be such a bad thing.”

“I was curious. And part of me was worried, too. It was obvious that you knew something about that mysterious pattern, but you were trying to hide it.”

Before we parted, when Magic Johnson had asked about the magic circle, I had made the excuse that I had seen something like it in a dream.

Of course, I hadn’t said that to make him believe me. It had been a roundabout way of telling him not to ask for now.

“So I followed you, just in case…”

Magic Johnson let his voice trail off as he looked around at the surroundings, which were covered entirely in blood.

“Looks like I shouldn’t have followed you.”

It was a major incident in which two S-rank Hunters—each practically the face of his own country—had died. One of them had even been a comrade who had once fought alongside Magic Johnson on the same battlefield.

Sometimes, certain kinds of truth were uncomfortable.

For Magic Johnson, this must have been one of those uncomfortable truths.

“Do you regret it?”

“A little. Maybe it would have been better if I hadn’t known.”

Magic Johnson let out a quiet sigh and looked straight at me.

“Jin. Why are you telling me all this?”

“I wonder.”

“You were the only one who knew the truth. If you wanted to, you could have covered it up. The same goes for him.”

I glanced at Go Jun, who had lost consciousness, and shook my head.

“This wasn’t the kind of thing I could hide simply by keeping quiet. No matter how much I denied it, that bastard wouldn’t have believed me anyway. Lee Jungryong and that guy were both ticking time bombs. They were dangerous enough to threaten my people.”

“Jin. You… were enemies with them. You had been enemies for a long time.”

“Yes. If you’re in a situation where you can’t eliminate an enemy, you have to make them afraid of you—afraid enough that they’ll never dare look at you again. A bomb with its detonator removed won’t explode.”

“Then what about me? Why did you tell me this?”

“You already know. In a situation like this, there are only two kinds of people you can choose.”

I continued slowly, enunciating each word.

“An enemy. Or a friend.”

“……!”

“I thought Johnson would believe me. Because you’re my friend.”

Magic Johnson let out a low groan and stared at me with a complicated gaze filled with every kind of emotion.

“Just because someone’s your friend doesn’t mean you believe everything they say, Jin.”

“But you believed me. You didn’t doubt me even once during our entire conversation.”

“……”

“Help me. Help me protect my people and grow stronger.”

At some point, I had begun to feel everything around me changing.

In Murim, Dark Heaven had begun to stir. In the modern world, the Arch Lich—a Named Monster unlike any that had come before it—had slaughtered millions and brought about a catastrophe.

And then there were the mysterious patterns and symbols that had appeared in both worlds.

Or perhaps they were something that could be called *dark magic*.

*Could all of this really be a coincidence?*

Everything that happened in the world was connected by invisible links. To keep everything from toppling one after another like dominoes, I had to prepare.

And to do that, I desperately needed one ally.

“Johnson.”

“…Damn it.”

Magic Johnson was silent for a moment before letting out a deep sigh.

“Do you know something?”

“…?”

“That day. If you hadn’t asked me to teleport you to the place where the monster army was waiting, I might have suspected you.”

That single remark signaled his acceptance.

My face brightened, and Magic Johnson let out a helpless laugh.

“Damn it. Now that things have turned out this way, I can’t help it. Let’s clean up the area before the patrol gets here.”

He waved his hand, and the blood splattered in every direction vanished without a trace.

After clearing the surroundings in an instant with Clean magic, Magic Johnson looked at Go Jun on the ground and furrowed his brow.

“This man is a problem… I’d like to erase his memories entirely, but the situation is complicated. What a pain.”

“Huh?”

My ears perked right up.

I suddenly remembered how, when I had stormed into the Myeongdong Guild in the past, the mages from the Ares Guild had used memory-manipulation magic on the Myeongdong Guild members at the scene.

“You can do that?”

“It would obviously be difficult, but it isn’t impossible. Still, the stronger the target’s mental fortitude and the more extensive the memories you have to alter, the harder it becomes.”

“Oh.”

“He seems quite strong. In the worst case, we could fail and even leave traces that someone attempted to manipulate his mind.”

Go Jun was strong enough to qualify as an S-rank Hunter, despite his current condition.

Unlike Wu Heixing, he also had a fairly strong will, so attempting something like that could be a needless gamble.

“Leaving traces would be a problem.”

“Indeed. If we were discovered, we couldn’t avoid punishment. Mental-manipulation magic is a serious felony.”

Lee Jungryong and the Ares Guild had carried out such things without the slightest hesitation.

Even if someone noticed, they wouldn’t dare question it. Everyone knew how much power and influence they possessed.

“Still, if we tried it and succeeded…”

“Under federal law, the minimum sentence would be one hundred years in prison without parole. Want to try?”

I answered without even taking a breath.

“No.”

“Good boy. That’s a wise decision.”

A minimum sentence of one hundred years without parole?

If I got caught, I’d rot in prison without a chance. Even if I escaped, I’d spend the rest of my life as an internationally wanted fugitive.

I might even end up with a ten-billion-beri bounty on my head, living as a pirate on Somalia’s Grand Line, just like in a manga.

Just thinking about it was horrifying…

“It’s a shame. If this were Korea, it might be worth trying.”

“Korea? Why?”

“If you spread money around, hired a lawyer who used to be a chief prosecutor, and took advantage of *jeongwan yewu*,[^1] you probably wouldn’t get much of a sentence.”

“Jeongwan yewu? What’s that?”

“It’s a thing. Ah, if you said you’d done it while drunk after downing about five bottles of soju,[^2] you might even get a suspended sentence.”

Magic Johnson laughed loudly as if he had heard an incredible joke.

“Don’t say ridiculous things, Jin. What kind of country is that?”

“……”

“You’re serious? My God.”

In any case, memory-manipulation magic was out of the question.

I left Go Jun where he lay and began walking.

The three A-rank Hunters Go Jun had hidden away were frozen like stone statues, their Paralysis Acupoints struck by the Finger Qi I had fired at them.

“You saw everything, right?”

The three men looked up at me with eyes filled with terror.

Sometimes, watching someone else suffer could instill more fear than suffering yourself.

They had been unable to move even a finger as they watched Go Jun get brutally and thoroughly crushed. Their souls had almost left their bodies.

“I remember all three of your faces. Getting your personal information is only a matter of time.”

That was how powerful people had always operated.

If you couldn’t kill someone, you had to instill fear in them the same way. You had to make sure they could never bare their teeth at you again.

“If we meet like this again… I’ll kill you.”

Whoosh!

The killing intent that erupted in an instant sliced through and pressed down on everything around us.

After reining in my qi, I slowly swept my gaze across their corpse-pale faces before suddenly thrusting out a hand.

Crack!

“Ghk!”

“Hah, huff…”

At last, the men were released from the pressure points and exhaled the breaths they had been holding.

Their bloodshot eyes were wet, and saliva and vomit dribbled from their open mouths.

“I’ll give you ten seconds. Get that bastard out of here.”

It was obvious who *that bastard* referred to.

Before I had even finished speaking, the three men struggled to their feet and rushed toward Go Jun.

They hoisted their still-unconscious superior onto one of their backs and vanished at lightning speed.

I threw one final word after them.

“Erase everything that happened today from your memories. And think carefully. Which ship do you need to be aboard to keep yourselves alive?”

“……!”

“……!”

“……!”

The Ares Guild was a massive, sturdy ship.

But Cheon Taemin, its great captain, had vanished without a trace long ago, and Lee Jungryong—the man who had taken the helm after him—had also met his death.

The ship that had seemed destined to sail the seas forever had begun to list.

A captain couldn’t abandon his ship, but the sailors hired to work aboard it were different.

If they wanted to, they could find a new ship and a new shipowner.

*That should have been enough for them to understand.*

The three men hesitated for a moment after hearing my words before disappearing into the darkness.

They gave me no answer and showed no particular reaction, but I knew.

They would never forget what I had said.

They would turn it over in their minds dozens and hundreds of times before passing it on to their other companions. And little by little, water would begin filling the bottom of the enormous ship called the Ares Guild.

“Ooh, vile human. Ooooooh.”

“This is what you call strategy, you idiot.”

“You’re an idiot, so how are you this devious and cunning?!”

“……You son of a bitch.”

He wasn’t wrong, but it pissed me the fuck off.

Let’s just say that after several years of Hunter life, I had learned various things through experience.

Magic Gems were now an essential power source for cutting-edge civilization. As a result, enormous amounts of capital had naturally gathered. And where there was capital, people gathered as well—and all kinds of things were bound to happen among them.

*I’ve thrown out what I know for now… If I wait, someone will bite.*

Just as a sect’s standing in Murim was determined by the martial artists it possessed, the standing of a modern Guild was determined by how impressive its Hunters were.

And Go Jun could never fill the void left by Lee Jungryong.

Just as Lee Jungryong had never been able to fill the gap left by Cheon Taemin.

It was only a matter of time before the fish that had spotted another tasty bait beyond that empty space began swimming away.

“You’re not holding back. Are you planning to go to war with the Ares Guild?”

I shrugged at Magic Johnson’s words.

“It’s not something I can’t do, but we need to make it look good.”

“Make it look good?”

“The Peace Guild is going to grow enormously from now on. I’m here, and Team Leader Choi is attracting attention from the media.”

“Oh, I heard about that, too. Apparently Choi’s been incredible lately.”

The spotlight from the world’s media was aimed at me, but the more I avoided contact with the press, the more attention was directed toward Team Leader Choi.

He belonged to the same Peace Guild as me and was one of the very few people allowed to visit my hospital room.

On top of that, he had achieved remarkable results during this monster wave and possessed looks that could rival a celebrity’s.

*The greatest secret still hasn’t been revealed.*

If the truth—that he was Cheon Taemin’s own flesh and blood—were made public as well, the media would undoubtedly go into a frenzy.

“Anyway, it’s only a matter of time before the Peace Guild takes off. The Ares Guild’s influence will shrink day by day.”

“Hmm. That’s certainly possible.”

Magic Johnson nodded before suddenly opening his mouth.

“But, Jin.”

“Yes?”

“What exactly do you know about the magic circle—”

“Oh, right. The club!”

“Huh?”

“You said you were going to a club with the Skeleton King.”

“Wait, wait, Jin!”

“Golgoli. Let’s go to the club!”

“Yes! Raise your ribs and scream!”

I hurried away while listening to the Skeleton King’s nonsense.

Then, as I looked up at the faint moonlight, a thought suddenly crossed my mind.

*I should head back soon.*

The time was approaching.

The time to return to another world—to Murim.

[^1]: *Jeongwan yewu* is the unofficial preferential treatment often afforded to lawyers who formerly served as judges or prosecutors, particularly through their old professional connections.

[^2]: Soju is a clear Korean distilled liquor, commonly served in small glasses.
```
