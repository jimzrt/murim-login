<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0672.txt",
      "sha256": "0cafbff2bce1f7034e6a2ea8eeccb36a1ed6385ffd4fd881e8570e4e9f064063",
      "bytes": 15028
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1205623ce3f09bfec520b6a375e465554209b821de855841afb524530afe4ab5",
      "bytes": 1823
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "20240b3c73f403375624ae660702bf64c519e1d89049394ddc015fc50f02c400",
      "bytes": 202564
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "ef265c60def219cc71400fee8f8b57606fc1249337aa38729815b4fb018522f0",
      "bytes": 1006
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "eb3cfdb0bd7b1089c130419cb7804180cbbaafe19c652fa580548341b4ccc089",
      "bytes": 1702
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "7ad9d554eec8d24a4be766f9e59c7c574e6f5f3bdd0f7f73faa3cc3f4cb726e4",
      "bytes": 699
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "7dc1fbc489594b2fbf758d0cd7b494eed205c6d9c4a0da306ffbf6fb9ec56d04",
      "bytes": 787
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "512349270bbf439f9c140c9c604cd30792d9c4edcf93b94142ba0e94c5cfb2bb",
      "bytes": 962
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "4a83f9855ab2ad0e00cc5a668c9cbe1d76f8fc8860eac52ec923df0e5f68e171",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4045b33709c85492f6e5a040817a29f9f908e64bbead101e589c38cbc6fe4ca0",
      "bytes": 208612
    }
  ],
  "estimated_tokens": 11235
}
-->

# Durable State Update — Chapter 672

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 672. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 672. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 672,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 672,
    "continuity_sources": [672],
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
    "The System has generated the Supreme Peak-grade Sudden Quest Yohi's Tracking Scent, requiring Jin to choose a direction; its reward and failure conditions remain unknown.",
    "Yohi's damaged scent pouch contained a nearly odorless high-grade tracking scent that Muyaho can detect.",
    "Muyaho identifies two possible directions: northwest toward the reconnaissance squad and southeast toward Yohi.",
    "Jin is torn between escaping Nanman and pursuing Yohi's scent because returning later could take seven days and nights.",
    "Jin believes the people who stayed behind to protect his escape may die before he can return.",
    "Baeksang's net over heaven and earth remains an imminent threat.",
    "The Beast Miao King's fate and the fate of the rescuers who stayed behind remain unresolved.",
    "Namho has awakened on a large beast after Yayul Mok's plan succeeded and discovered that Jin is absent from the group."
  ],
  "continuity_sources": [
    671
  ],
  "open_questions": [
    "Which direction will Jin choose for Yohi's Tracking Scent?",
    "What will Yohi's tracking scent lead Jin to, and where are Yohi and Heugung?",
    "Did the Beast Miao King survive Baeksang's Sword Force?",
    "Will Wonhu and the remaining Miao warriors survive Baeksang's Bai forces?",
    "Can the reconnaissance squad and the other rescuers survive until Jin can return?"
  ],
  "safe_through": 671,
  "temporary_decisions": [
    "Use Great Chieftain for 대족장 and Palace Lord for 궁주.",
    "Use Sword Force for 검강 and half a shichen for 반 시진.",
    "Use Outer Palace for 외궁 and Yohi's Tracking Scent for 요희의 추종향.",
    "Use Thousand-Li Tracking Scent for 천리추종향 and Ten-Thousand-Li Tracking Scent for 만리추종향."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 열화문    | **Fire Gate Clan**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 신법     | **movement technique**                           |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 상태               | **Status**                     |
| 로그아웃             | **Logout**                     |
| 체력               | **Stamina**                    |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 671
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi, whom the Great Snow Fiend killed during the Great Faction War; despite his bond with Yayul Cheok, he has chosen to oppose the Beast Miao King's escape and has surrounded Wonhu's remaining force with Bai warriors.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 662
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 635
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 671
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 671
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese; he is currently unconscious on White Tiger while Jin carries him away from the Outer Palace.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and his father, Baeksang is his father's sworn younger brother, and Yayul Mok has risked his position and life to rescue Jin Taekyung, entrusting Muyaho to Jin while he remains behind with the Seven Miao Tigers.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 671
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, manipulates Heugung alongside Baeksang, and has disappeared from the Inner Palace alongside Heugung after the assault on the Fire Dragon Pavilion.

## Korean source

```text
＃672화



쉬쉬쉬쉭!

세차게 몰아치는 바람에 새하얀 터럭이 출렁인다. 나는 백호의 목덜미를 움켜쥔 채, 스쳐 지나가는 주위 풍경을 바라보았다.

사방을 무성하게 채운 수풀과 거인처럼 우뚝 서 있는 나무들.

이끼 낀 바위틈 사이에 숨어 있던 뱀은 샛노란 눈으로 우리를 노려보고, 풀숲 사이에 납작 엎드린 채 사냥감을 물색하던 표범은 백호를 발견하고 슬그머니 뒷걸음질 쳤다.

그리고 이 모든 것의 위에, 서서히 밝아 오는 하늘이 있었다.

‘벌써?’

내심 중얼거린 나는, 얼마 지나지 않아 상당한 시간이 흘렀음을 깨달았다.

뇌옥을 탈출했을 때가 자정이 넘은 직후였으니, 얼추 계산해 보면 못해도 세 시진 정도의 시간을 정신없이 달려온 셈이다.

그르릉.

그래서일까. 지금 나를 등에 태우고 있는 백호, 무야호의 숨결은 처음보다 훨씬 거칠었고 내딛는 발걸음에서는 피로가 느껴졌다.

‘그럴 만도 하겠지.’

지금까지의 무림 짬밥으로 장담하는데, 경신법 좀 익혔다는 절정 고수라 해도 이 지랄 맞은 동네에서 세 시진이나 전력으로 달리면 하지정맥류에 걸릴 거다.

하물며 무야호는 평범한 호랑이보다도 더 커다란 체구를 지닌 대호(大虎).

김정호도 지도 제작을 때려치울 만한 험지를 오가느라 체력도, 근육도 빠르게 소모되었을 것이다.

거기에 더해 등에는 나름 한 덩치 하는 나까지.

비록 내가 수의사는 아니지만 지금 무야호의 상태는 눈 감고도 알 수 있을 정도였다.

‘그나마 이 녀석 정도 되는 영물이라 지금까지 버틴 거지.’

남만에서도 내로라하는 영물답게 기본적인 운동 능력이 훌륭한 것은 사실이지만, 지금처럼 이동한다면 정작 중요할 때 힘을 발휘하지 못한다.

나는 녀석의 목덜미를 쓰다듬으며 속삭였다.

“근처에서 잠시 쉬었다가 가자.”

- 그르릉.

어렵지 않게 내 말을 알아들은 녀석이 작게 고개를 끄덕인다.

때마침 그리 멀지 않은 곳에서 물 흐르는 소리가 들려오고 있었고, 걸음을 늦춘 우리는 잠시 후 작은 개울가를 발견할 수 있었다.

일찍 일어나 물을 마시러 온 산짐승 몇 마리도 함께.

꾸이익?

멧돼지라. 좋지.

나는 지체하지 않고 순간 머릿속에 떠오른 생각을 즉각 실행에 옮겼다.

‘인벤토리 오픈. 소환.’

살기 위해서 닥치는 대로 이것저것 인벤토리에 쑤셔 넣다 보니, 이제는 걸어 다니는 무기 창고나 다름없다.

언제 보관해 두었는지 모를 싸구려 철창을 꺼내어 던지자, 커다란 덩치의 멧돼지 두 마리가 비명도 못 지르고 쓰러진다.

쉭, 푸푹!

꾸이이익!

방금 쓰러진 것이 저 녀석들의 부모였던 모양이다.

울음소리와 함께 쏜살같이 도망치는 멧돼지 새끼들의 모습을 보니 마음이 무거워졌다.

“후우.”

- 크르르.

무야호가 숙연한 눈빛으로 고개를 끄덕인 그때, 내가 슬픈 얼굴로 말을 이었다.

“새끼가 살이 더 연한데. 쟤들부터 잡을걸.”

- ……크릉?

뭐, 인마.

저게 진짜 사람 새끼인가, 하는 눈빛으로 바라보는 무야호를 무시하고 멧돼지 가죽을 벗겨 철창에 끼웠다.

화륵. 타다닥.

거기에 더해 열양지기를 이용해 모닥불까지. 모락모락 피어오르는 연기와 함께 익어 가는 멧돼지 고기를 보자 피식 실소가 흘러나왔다.

이유는 별거 없다. 그냥, 지금 이 행동이 스스로 생각해도 어이가 없어서 웃음이 나온 거다.

‘남만 전체를 적으로 돌렸는데, 그 와중에 버젓이 바비큐 파티라.’

나도 안다. 이게 미친 짓이라는 걸.

아니, 애초에 남만의 중심부로 향하는 남동쪽 길을 따라 왔던 길을 되돌아온 것부터가 정신 나간 짓이었다.

하지만 몇 번을 다시 생각해 봐도 결론은 늘 같았다.

요희의 추종향을 따라 움직이기로 마음먹은 이상, 이것이 내가 할 수 있는 최선의 방법이라는 것.

굳이 외궁(外宮)에서 백 리 남짓 떨어진 이곳에서 불을 피우는 미친 짓을 벌이는 것도 그런 이유에서다.

‘이쪽에서 이목을 끌수록, 다른 사람들이 살아남을 확률이 높아질 테니까.’

나는 떠나기 전, 태산에게 신신당부했다.

뒤도 돌아보지 말고 달리라고. 야율목을 통해 척후대의 부족장들을 설득하고, 수룡채의 쾌조선을 이용해 남만을 빠져나가라고.

그러자 태산은 평소와 달리 한참 침묵하더니, 이렇게 말했다.



‘각주.’

‘왜.’

‘태산이도 함께 가겠다. 각주 혼자 보낼 수는 없다.’



새벽이라 그랬는지, 아니면 예상치 못했던 말이라 그랬는지. 그 순간만큼은 나도 퍽 감성적이었던 것 같다.

하지만 뭉클해진 마음과는 달리 차갑게 식은 머리는 알고 있었다.

이들 중 누구 하나라도 나와 함께 한다면, 양쪽 다 무사할 수 없음을.



‘다른 사람들이랑 같이 기다리고 있어. 금방 돌아올 테니까.’

‘언제? 태산이 몇 밤이나 기다려야 하나?’

‘글쎄다. 한 열 밤 정도?’

‘태산이 싫다. 열 밤은 너무 길다.’

‘그럼 다섯 밤.’

‘좋다. 약속이다.’

‘그래, 약속.’



그렇게 나는 떠났다. 스스로도 확신할 수 없는 약속을 남긴 채.

다섯 밤이라.

내가 그 안에 돌아갈 수 있을까. 아니, 돌아갈 수 있기는 한 걸까. 사실 나도 잘 모르겠다.

뇌옥을 탈출한 뒤에도 로그아웃 기능은 여전히 막혀 있고, 적이 되어 버린 수많은 남만인들은 지금쯤 나를 찾기 위해 사방을 조여 오고 있을 것이다.

어쩌면…….

바스락.

그래, 지금 이 순간조차도.

- 크르릉.

노릇노릇 익어 가는 멧돼지 고기를 보며 침을 흘리던 무야호가 문득 낮은 울음소리를 흘린다.

하지만 나는 적의를 드러내는 녀석을 진정시키는 한편, 감각을 더욱 끌어올렸다.

동시에 더욱 예리해진 오감(五感)을 통해 속속들이 전해지는 새로운 정보들.

‘머릿수는 오십 남짓. 아직 부족은 모르겠지만 모두 전사고…… 함께하는 맹수는 없군. 발각될 우려가 있어서 뒤에 남겨 두고 왔나?’

설령 맹수를 한 트럭 끌고 왔다 해도 달라질 건 없지만, 덕분에 일이 더 편해진 건 사실이다.

대강의 상황 파악을 끝낸 나는 멧돼지를 꿴 철창을 천천히 돌리기 시작했다.

치이이익.

노릇노릇 익어 가는 먹음직스러운 소리 너머, 한껏 숨죽인 불청객들의 대화가 희미하게 귓가를 간지럽혔다.

- 저놈이다. 야율목, 그놈이 아끼던 백호를 곁에 두고 있는 것으로 보면 확실해.

- 그게, 저는 잘 모르겠습니다. 여기서는 뒷모습밖에 안 보여요. 이러지 말고 차라리 이쯤에서 돌아가서 지원을 요청하는 것이…….

- 한심한 놈. 하늘이 우리에게 기회를 주었거늘 다른 부족에게 전공(戰功)을 넘기자니. 여기까지 왔는데도 그따위 나약한 소리를 지껄일 셈이더냐.

- 하, 하지만 형님. 만약 저자의 정체가 우리가 아는 그 한족이 맞다 해도, 당장 저희가 어찌 저런 괴물을 감당할 수 있겠습니까.

- 그래 봤자 저놈도 결국 한낱 피륙으로 이루어진 인간. 이런 상황에서 거지꼴로 고기를 굽는 걸 보아하니 홀로 떨어져 정신이 나간 모양인데, 우리가 이 자리에서 놈을 잡는다면 만금(萬金)은 물론 아버님께서 새로운 대족장이 될 수도 있다.

음. 그렇단 말이지.

귓가로 흘러 들어오는 대화를 유심히 듣고 있던 나는 엉덩이를 툭툭 털며 일어났다. 그리고 돌아섬과 동시에 불쑥 물었다.

“그래? 지금 내 꼴이 그렇게 별로야?”

“……!”

“……!”

삼십여 장이나 떨어져 있음에도 느낄 수 있었다. 파르르 떨리는 공기와 최대한 은밀히 접근해 오던 적들을 휘감은 여러 감정을.

충격. 경악. 그리고…….

“쳐라!”

멍청함과 헛된 공명심(功名心)이 낳은 섣부른 결단.

하지만 놈들은 몰랐다. 엉망이 된 의복과 달리 지금의 내 몸 상태는 최상이며, 이미 그들을 향해 쏘아지고 있었음을.

쐐애애애액!

빛살 같은 속도로 쇄도하는 신형. 돌풍과도 같이 휘몰아친 바람에 무성한 풀숲이 터져 나간다.

산산이 부서져 흩날리는 나뭇잎 사이, 경악으로 가득 찬 눈동자들이 보인다.

“다들 뭐 하냐. 마저 안 뽑고.”

내 친절한 조언에도, 채 반도 뽑지도 못한 병장기를 쥔 손들은 얼어붙은 듯 움직이지 않았다.

그리고 그것은 이들을 이끄는 선두의 사내 역시 마찬가지였다.

“네, 네놈…….”

이 얼굴 어디서 본 것 같은데.

뭐, 지금 당장은 별 상관없지만.

“넌 왜 안 치냐.”

“뭐, 뭐라고?”

“치라며. 여기까지 와 줬는데 안 쳐?”

“그, 그것이…….”

“안 해? 그럼 내가 하고.”

나는 조용하게 한마디를 툭 내뱉었다.

“쳐라.”

그리고 다음 순간. 땅에 드리워지는 커다란 그림자.

- 크아아아아앙!

포효와 함께 내 머리 위를 뛰어넘은 거대한 동체가, 사내를 덮쳤다.

우득, 콰드드득!



* * *



누가 그랬다. 무력과 억압은 대화의 수단이 될 수 없다고. 닫힌 입을 열게 하는 것은 온화한 표정과 친절한 말투라고.

사실 아주 틀린 말은 아니다. 닫힌 입을 열게 하기 위해서는 그냥 무력과 억압이 아니라, 존나 무자비한 무력과 억압이 필요한 법이니까.

그리고 새삼 느끼는 사실이지만, 나는 이 분야에 제법 탁월한 소질이 있었다.

“지금 남만야수궁의 내부 사정은?”

“놈! 차라리 날 죽여라!”

“좋아. 무야호?”

콰득!

“끄아아아악!”

“잘했어. 이제 뱉어.”

퉤.

“끄흑. 끄흐흐흑.”

“뭘 청승맞게 질질 짜고 있어, 사내새끼가.”

“끄흐흐흡.”

“이번엔 다리였지만, 계속 울면 다음은 불알이다. 알아들었니. 이 씨부랄 새끼야?”

“끕. 끄으으읍……!”

“좋아. 그럼 다시 묻는다. 현재 남만야수궁의 내부 사정은?”

심문은 빠르고 순조롭게 진행됐다.

물론 심문을 위한 사전 작업도 완벽했다.

뒤늦게 덤벼들었던 놈들은 양팔을 부러트리고, 도망치던 놈들은 다리를 부러트렸으니까.

한 이십 명 정도를 병신으로 만든 다음 무야호의 한입만 찬스를 사용했더니 하나같이 골든 리트리버처럼 유순해졌다.

‘이 정도면 얼추 끝났나.’

이 와중에 놈들이 거짓말을 쳤을 가능성도 있지만, 일단은 충분한 근거와 신빙성이 있기에 사실로 치부해도 괜찮을 듯싶었다.

더군다나 죽음 앞에서는 모두가 솔직해지는 법이다. 특히 불알 앞에서는 더더욱.

그리고 모든 심문을 끝낸 나는, 가장 먼저 무야호에게 당했던 사내를 힐끗 바라보았다.

전신이 으스러진 그는 간신히 숨만 붙은 채 거친 호흡을 내쉬다가, 나와 눈이 마주치자 신음을 흘렸다.

‘어디서 봤나 했더니.’

핏줄은 못 속인다고, 부족장인 아비의 얼굴을 그대로 빼다 박았다.

물론 이 녀석의 아비가 되는 그자도 내게는 그리 중요한 인물은 아니었다.

대회의 첫날과 요서부의 참극이 있던 날. 그저 어떻게든 백상의 뒤에 서고 싶어 안달 난 아부꾼에 불과했으니까.

하지만 그것이 내가 놈을 포함한 다른 이들을 살려 주는 이유이기도 했다.

“돌아가서 전해.”

내 나직한 한 마디에, 놈이 두려움 가득한 눈빛으로 입술을 달싹였다.

“무, 무엇을?”

“내가 여기 있다고. 멀리 떨어지지 않은 어딘가에서, 너희를 지켜보고 있다고.”

“……!”

“오늘 들은 모든 것을 잊지 마라. 나 역시 잊지 않을 테니.”

놈은 물론이고, 주위에서 내 일거수일투족에 촉각을 곤두세우고 있던 남만인들이 몸을 부르르 떨었다.

아마 그들은 오늘 일을 죽을 때까지 기억할 것이다.

내 표정과 말투. 목소리와 행동.

그리고 앞서 심문하는 과정에서, 전날 밤 뇌옥을 습격한 묘족 전사들이 아직 살아 있다는 것을 알았을 때 내가 남긴 경고를.



‘만약 그들을 건드리면, 너희도 모조리 죽는다. 당장 오늘이 아니더라도 내일. 혹은 내년. 어쩌면 모든 것이 끝났다고 생각하여 안심하던 그때에.’



사람이 누군가의 협박에 두려움을 느끼는 것은, 그 협박이 정말 현실로 이루어진다는 불안에 기반한다.

그리고 그들의 눈에 비친 나는 충분히 그러고도 남을 위인이었다.

열화문의 명맥을 이은 계승자. 화왕 적천강의 후인이자. 불과 약관 어림의 나이에 천하를 격동시킨 전대미문(前代未聞)의 괴물.

그것으로 충분하다.

오늘 나는 이들의 뼛속 깊이 지워지지 않을 두려움을 새겨넣었고, 이제 이들이 품은 두려움은 백상의 편에 선 남만인들 사이로 퍼져나갈 것이다.

빠르게. 더 멀리.

감히 어느 부족도 그들을 해할 수 없을 만큼.

아직 백상이 있기에 완벽한 안전을 논하기에는 부족하지만, 이것이 지금의 내가 그들에게 해 줄 수 있는 최선이다.

“당장 떠나라. 이 자리에서 죽고 싶지 않다면.”

“……!”

“……!”

잠시 후, 나는 어느 거목의 가지에 앉아 하얗게 질린 얼굴로 숲을 빠져나가는 오십여 명의 인영을 확인했다.

그리고 마치 귀신에 홀린 듯, 혼비백산하여 도망치는 그들의 뒷모습을 끝까지 바라본 뒤 천천히 삼 갑자의 열양지기를 끌어올렸다.

화아악.

양손에 깃든 화염.

이제, 천라지망이라는 거대한 그물을 내게로 끌어당길 봉화(烽火)를 피울 차례다. 한 숲을 장작으로 삼아 타오르는 선명한 봉화를.

화륵. 콰아아아!

사방으로 번지며 숲을 집어삼키는 끔찍한 열기와 불길을 보며, 문득 그런 생각이 들었다.

‘노야가 보면 쌍욕 좀 하시겠는데.’

피식 웃은 나는 활활 타오르는 숲을 뒤로하고 걸음을 옮겼다.

앞에는 이미 반쯤 탄 멧돼지 고기를 입에 문 무야호가 힘차게 달려가는 중이었다.
```

## Final English reading copy

```markdown
# Chapter 672

Whoosh, whoosh, whoosh!

The fierce wind sent white fur rippling. Clinging to the nape of the White Tiger, I watched the scenery rushing past.

Dense undergrowth filled every direction, and trees stood tall like giants.

A snake hiding between moss-covered rocks glared at us with bright yellow eyes, while a leopard lying flat in the grass and searching for prey spotted the White Tiger and slowly began backing away.

And above all of it, the sky was gradually growing brighter.

*Already?*

I muttered inwardly, then realized that quite a lot of time had passed.

We had escaped the underground prison just after midnight, so by a rough calculation, we had been running nonstop for at least three shichen.

Growl.

Perhaps that was why the breathing of the White Tiger carrying me—Muyaho—was much rougher than before, and fatigue could be felt in every step he took.

*It’s only natural.*

I could say this with confidence after all my time in the Murim: even a Peak master who had learned a movement technique would develop varicose veins if he ran at full speed for three shichen in this godforsaken place.

And Muyaho was a great tiger—a spiritual creature even larger than an ordinary tiger.

Running across terrain so rugged that even Kim Jeong-ho[^1] would have given up on mapmaking must have rapidly drained his stamina and worn down his muscles.

[^1]: Kim Jeong-ho was a nineteenth-century Korean cartographer famous for producing detailed maps of Korea.

And on top of that, he had to carry me, a fairly large man, on his back.

I might not be a veterinarian, but even with my eyes closed, I could tell what condition Muyaho was in.

*He’s lasted this long only because he’s a spiritual creature of Muyaho’s caliber.*

As befitted one of the most renowned spiritual creatures in Nanman, his basic physical abilities were excellent. But if he kept traveling like this, he would be unable to show his strength when it truly mattered.

I stroked his nape and whispered,

“Let’s rest for a little while nearby before we go on.”

—Growl.

Understanding me without difficulty, he gave a small nod.

As luck would have it, the sound of running water was coming from not far away. We slowed down and soon found a small stream.

A few mountain animals had also come out early to drink.

Squeal?

Wild boars. Excellent.

Without hesitation, I immediately put the thought that had popped into my head into action.

*Open Inventory. Summon.*

After shoving all kinds of things into my Inventory in a desperate effort to survive, I had practically become a walking armory.

I pulled out a cheap iron spear I couldn’t even remember storing and hurled it.

Two large wild boars collapsed without even having time to scream.

Whoosh—thunk!

Squeeeeeal!

Those two must have been the piglets’ parents.

Seeing the young wild boars flee at top speed, squealing as they went, I felt a weight settle over my heart.

“Hoo.”

—Grrr.

Just as Muyaho solemnly nodded, I continued speaking with a sorrowful expression.

“The young ones have more tender meat. I should’ve caught them first.”

—……Grr?

What, you little punk?

Ignoring the look Muyaho gave me—as if wondering whether that bastard was really human—I skinned the wild boars and skewered them on the iron spear.

Fwoosh. Crackle.

Then I used Scorching Yang Qi to make a campfire. As I watched the wild boar meat cook amid the curling smoke, a quiet laugh escaped me.

There was no special reason. I simply found my own actions so absurd that I started laughing.

*I’ve made all of Nanman my enemy, and I’m throwing a barbecue party in the middle of it.*

I knew this was insane.

No, the fact that I had retraced the southeastern road toward the heart of Nanman was already insane.

But no matter how many times I thought it over, I always reached the same conclusion.

Once I had decided to follow Yohi’s Tracking Scent, this was the best method available to me.

That was also why I had committed the madness of lighting a fire here, barely a hundred li from the Outer Palace.

*The more attention I draw over here, the greater the chance that the others will survive.*

Before leaving, I had repeatedly impressed one thing upon Taishan.

Run without looking back. Persuade the chieftains of the reconnaissance squad’s tribes through Yayul Mok, then use the swift ships of the Water Dragon Stronghold to escape Nanman.

Taishan had been silent for a long while, unlike his usual self. Then he had said,

*Pavilion Master.*

*What?*

*Taishan will go too. Taishan cannot let Pavilion Master go alone.*

Maybe it was because it had been dawn, or maybe because his words had been so unexpected. For that moment, at least, I think I had been rather sentimental too.

But while my heart had been moved, my cold head had known the truth.

If even one of them came with me, neither side could remain safe.

*Wait here with the others. I’ll be back soon.*

*When? How many nights does Taishan have to wait?*

*Who knows? About ten nights?*

*Taishan doesn’t like that. Ten nights is too long.*

*Then five nights.*

*Good. It’s a promise.*

*Yeah. A promise.*

And so I had left, leaving behind a promise even I could not be certain I could keep.

Five nights.

Could I return within that time? No. Would I even be able to return at all? To be honest, I had no idea.

Even after escaping the underground prison, the Logout function remained blocked, and the countless Nanman people who had become my enemies were probably tightening the net from every direction as they searched for me.

Maybe…

Rustle.

Yes. Even now.

—Grrr.

Muyaho, who had been drooling while watching the wild boar meat turn golden brown, suddenly let out a low growl.

While calming the creature that had revealed its hostility, I sharpened my senses even further.

New information flowed in through my heightened five senses.

*About fifty people. I don’t know their tribe yet, but they’re all warriors… and there are no beasts with them. Did they leave them behind because they were worried about being discovered?*

Even if they had brought a truckload of beasts, nothing would have changed. Still, this did make things easier.

After roughly assessing the situation, I slowly began turning the iron spear on which the wild boars were skewered.

Sizzle.

Beyond the appetizing sound of meat roasting, the conversation of the uninvited guests holding their breaths faintly tickled my ears.

—That’s him. He must be, since he has that White Tiger Yayul Mok cherished at his side.

—I’m not sure. All I can see from here is his back. Instead of doing this, shouldn’t we turn back and request support?

—Pathetic. Heaven has given us this opportunity, and you want to hand the battle merit to another tribe? We’ve come this far, and you still intend to spout such cowardly nonsense?

—B-but, hyung. Even if that man really is the Han Chinese we know about, how are we supposed to deal with a monster like him?

—Even so, he’s still just a human made of flesh and blood. Judging by the fact that he’s cooking meat here dressed like a beggar, he must have been separated from the others and lost his mind. If we capture him here, we’ll gain not only ten thousand gold, but our father might even become the new Great Chieftain.

Hm. So that was it.

Listening carefully to the conversation drifting into my ears, I brushed off my backside and stood.

Then I turned around and abruptly asked,

“Really? Do I look that bad right now?”

“……!”

“……!”

Even from more than thirty zhang away, I could feel it: the trembling air and the many emotions wrapping around the enemies who had been approaching as stealthily as possible.

Shock. Astonishment. And…

“Attack!”

A rash decision born from stupidity and a vain thirst for glory.

But they did not know that, despite my ruined clothes, my body was in peak condition—and that I was already shooting toward them.

Whoooosh!

My body surged forward like a streak of light. Wind whipped up like a gale, and the thick grass burst apart.

Through the leaves shattering and scattering in every direction, I saw eyes filled with terror.

“What’s everyone doing? Aren’t you going to finish drawing your weapons?”

Despite my friendly advice, the hands gripping weapons that were not even halfway drawn remained frozen in place.

The same was true of the man leading them.

“Y-you…….”

*I feel like I’ve seen this face somewhere.*

It did not matter right now.

“Why aren’t you attacking?”

“W-what did you say?”

“You said to attack. You came all the way here, and you’re not going to?”

“Th-that is…….”

“You won’t? Then I will.”

I quietly tossed out a single word.

“Attack.”

And the next moment, a huge shadow fell across the ground.

—Raaaaar!

With a roar, the massive body that leaped over my head crashed down upon the man.

Crack. Craaack!

* * *

Someone once said that force and oppression could never be tools of communication. That to make a closed mouth open, you needed a gentle expression and a kind tone of voice.

That was not entirely wrong.

To make a closed mouth open, you did not merely need force and oppression. You needed fucking merciless force and oppression.

And I had to admit, I seemed to possess a remarkable talent in this field.

“What’s the current internal situation of the Nanman Beast Palace?”

“You bastard! Just kill me!”

“Good. Muyaho?”

Crunch!

“Gyaaaah!”

“Good job. Now spit it out.”

Ptooey.

“Urgh. Hic—hiiic.”

“Why are you bawling so pathetically? You’re a grown-ass man.”

“Hic.”

“That was your leg this time, but if you keep crying, I’ll go for your balls next. Do you understand, you fucking bastard?”

“Ghk. Gnnng……!”

“Good. Then I’ll ask again. What’s the current internal situation of the Nanman Beast Palace?”

The interrogation proceeded quickly and smoothly.

Of course, the preparations for the interrogation had also been flawless.

I had broken both arms of the men who attacked me late, and the legs of those who tried to run away.

After leaving about twenty men crippled, I used Muyaho’s one-bite-only chance. Every one of them became docile as a golden retriever.

*Is that about it?*

There was a possibility they had lied, but they had given me enough grounds and credible information that I could treat their answers as fact for now.

Besides, everyone became honest in the face of death.

Especially in the face of losing their balls.

After finishing all the interrogations, I glanced at the man Muyaho had attacked first.

His entire body had been crushed. He was barely breathing, and when our eyes met, he let out a groan.

*So that’s where I’d seen him.*

Blood ties told the truth. He was the spitting image of his father, the chieftain.

Of course, his father was not particularly important to me either.

On the first day of the Tribal Grand Council and the day of the tragedy at Yoseo Manor, he had been nothing more than a sycophant desperate to stand behind Baeksang somehow.

But that was also why I was sparing him and the others.

“Go back and tell them.”

At my quiet words, the man’s lips trembled as he looked at me with terrified eyes.

“T-tell them what?”

“That I’m here. That I’m watching you from somewhere not far away.”

“……!”

“Don’t forget everything you heard today. I won’t forget it either.”

The man—and the other Nanman people nearby, who had been watching my every move with all their senses alert—shuddered.

They would probably remember what happened today until the day they died.

My expression and tone. My voice and actions.

And the warning I had left during the interrogation, after learning that the Miao warriors who had attacked the underground prison the night before were still alive.

*If you touch them, I’ll kill every one of you. Maybe not today, but tomorrow. Or next year. Perhaps at the very moment you think everything is over and finally let your guard down.*

People feared someone’s threats because they were afraid those threats might truly become reality.

And in their eyes, I was more than capable of making mine real.

The inheritor of the Fire Gate Clan’s legacy. The successor of Jeok Cheongang, the Fire King. An unprecedented monster who had shaken the entire world at only around twenty years of age.

That was enough.

Today, I had carved an indelible fear deep into their bones. Now, that fear would spread among the Nanman people who stood on Baeksang’s side.

Quickly. Farther and farther.

Until no tribe dared harm them.

Baeksang still existed, so it was too early to call them completely safe. But this was the best I could do for them right now.

“Leave at once. Unless you want to die here.”

“……!”

“……!”

A short while later, seated on the branch of a giant tree, I watched around fifty pale-faced figures make their way out of the forest.

Like ghosts had possessed them, they fled in panic. I watched their backs until they disappeared, then slowly drew up the Scorching Yang Qi of three jiazi.

Fwoosh.

Flames gathered in both my hands.

Now it was time to light the beacon that would draw the net over heaven and earth toward me—a vivid beacon burning with an entire forest as its kindling.

Fwoosh. Whooom!

As I watched the horrifying heat and flames spread in every direction and devour the forest, a thought suddenly occurred to me.

*Old Master would swear a blue streak if he saw this.*

I let out a quiet laugh and turned away from the blazing forest.

Ahead of me, Muyaho was already running energetically with a half-charred piece of wild boar meat clenched in his mouth.
```
