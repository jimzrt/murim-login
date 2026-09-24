<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0984.txt",
      "sha256": "621d18779da1cf41fcebe5954d4d8ff605f244b0a5b82798f4b8fe2a5fb5fa77",
      "bytes": 14345
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2a170543e308b8116d1fab90383e4f50357f61f49802afe4a57a8d1bc1f17aac",
      "bytes": 504
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2f94b4dbac7a01179a44f1931f0c573499c7caf58da15bcdaf401ece1fceb82b",
      "bytes": 236158
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0c32568ef2780e68d2a886f92ac49bf814a6ff7ce46285dfc6e62a4c57eefe71",
      "bytes": 759
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "73b99c64775e18ba9220f0c24d7169fd87bb4e8498fe8cf22db2a7335714b145",
      "bytes": 1479
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "97409f4fdce64d650542957f4c92f57ccb652c78ed671fd934fb44c5087a78b2",
      "bytes": 1178
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0f68c20e1ff1e0840326f3491018bc20180bd9f7f204ae58e500397d19db36ac",
      "bytes": 622
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "5b43845a1f694733982261401e3e7bcab85ae2e2a20c6c04778f773792ce9fc1",
      "bytes": 1071
    },
    {
      "path": "characters/Murong Baek.md",
      "sha256": "bc69d1f7defe3c54a44ecfa3108ceec850990ee948a8fb13f2e96086a269404f",
      "bytes": 660
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0383ccfd72d4fbc4b38d48993234603f14d1f5c66c449dca8bf366ced2819cb9",
      "bytes": 272663
    }
  ],
  "estimated_tokens": 11382
}
-->

# Durable State Update — Chapter 984

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 984. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 984. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 984,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 984,
    "continuity_sources": [984],
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
    "The Murong Family has been dissolved. About a hundred survivors, including Murong Su, are to be interrogated; if proven innocent, they may rebuild as the Murong household under a new Family Head."
  ],
  "continuity_sources": [
    983
  ],
  "open_questions": [
    "Will the survivors’ innocence be established, allowing the Murong household to rebuild under Murong Su or another Family Head?"
  ],
  "safe_through": 983,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 이소월    | **Lee Seowol**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 하오문    | **Lower District Sect**          |
| 화산파    | **Huashan**                      |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 장강수로맹  | **Yangtze River Channel League** |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 명성               | **Fame**                       |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 팔천협    | **Eight Spring Gorge** |
| 정마대전   | **Great Faction War**         |
| 도사      | **Daoist**                                                      |
| 방장      | **Abbot**                                                       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모용백 | **Murong Baek** | Former northern rival and later comrade of Peng Cheolhu. |
| 평화 | **Peace Guild** | Guild name. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 요녕 | **Liaoning** | Northeastern region from which the Murong Family arrives. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 한국 | **Korea** | Destination of the international Hunters and Guild Masters. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 중양절 | **Double Ninth Festival** | Festival used as the expected date for the invasion of the Central Plains. |
| 이룡신창 | **Divine Spear of the Imugi** | Murong Baek’s sobriquet. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 전령 | 진위경 | military messenger to Lesser Family Head | Lesser Family Head | formal-polite and deferential | Uses 소가주님 when confirming Wikyung's identity. |
| 유생 | 진위경 | scholar_to_lesser_family_head | Lesser Family Head | formal-deferential | The scholar reports matters to Jin Wikyung and apologizes for his inadequate proposal. |
| 진위경 | 유생 | lesser_family_head_to_scholar | you | formal-but-familiar | Jin Wikyung uses 자네 while correcting and instructing the inexperienced scholar. |
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 모용백 | adversaries | you | informal and confrontational | Directly asks whether Murong Baek beat up his older brother. |
| 모용백 | 진태경 | adversaries | you | informal | Addresses Taekyung directly during their confrontation. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 983
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 983
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 982
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he uses calculated leverage to keep dangerous allies in line and commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 983
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 964
- **Aliases:** None
- **Role:** Lee Seowol is the eighteen-year-old Sect Leader of the reconstructed and rapidly growing Mount Heng Sword Sect, a vassal of the Jin Family of Taiyuan who still awaits Taekyung’s answer to her marriage proposal.
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge, to whom he entrusted the Shura Annihilating Fist manual; has proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist; during her farewell with Taekyung, she asked him to address her as Young Lady rather than Sect Leader.

### Murong Baek.md

# Murong Baek (모용백)

- **Safe through:** Chapter 983
- **Aliases:** North Heaven Demon Lord, Divine Spear of the Imugi
- **Role:** Murong Baek was the North Heaven Demon Lord, known as the Divine Spear of the Imugi; Jin Taekyung killed him after he burned his life to gain power.
- **Personality:** He coveted the dragon pearl and the chance to become a dragon, rationalizing his pursuit while choosing to seize what belonged to others.
- **Voice:** Not established
- **Relationships:** Jeok Cheongang and the Bow Saint fought him alongside Jin Taekyung, who delivered the killing blow.

## Korean source

```text
＃984화



발 없는 말이 천 리를 간다는 속담은 틀렸다. 만 리, 아니 더 멀리도 눈 깜짝할 사이에 갈 수 있다.

북방을 중심으로 벌어진 일련의 사건들은 놀라울 정도로 빠르게, 더불어 끝없이 퍼져 나갔다.

사람들의 입에서 입으로, 전서응의 날갯짓으로, 전령(傳令)들의 바쁜 채찍질을 따라 힘차게 내달리는 말발굽으로.

그리고 밝혀진 진실에 대한 여파는, 이내 중원 전체를 뒤흔들기에 충분했다.

“모용세가가 어찌……!”

“말도 안 돼. 그럴 리가 없소!”

처음 소식을 접한 무림인들이 드러낸 감정은 바로 불신이었다.

당연한 일이었다.

만천하에 드러난 배신자들의 정체는 장강수로맹이나 녹림맹처럼 사마외도(邪魔外道)에 뿌리를 둔 집단이 아닌, 무려 모용세가였으니까.

천하 오대 세가의 일원.

비록 북방의 끝자락이라고는 하나, 광활한 면적을 지닌 요녕땅을 넘어 중원에 이르기까지 그 명성을 모르는 이가 없는 말 그대로의 세가(世家).

그런데 바로 그 모용세가가 암천과 손을 잡았다고 했다.

심지어 몇몇 불순분자의 소행도 아닌, 가주인 모용백을 포함한 가문원 대부분이.

그렇기에 이 믿을 수 없는 소식을 접한 사람들이 받은 충격은 말로 형용할 수 없을 정도였다.

“가주인 이룡신창(螭龍神槍)은 정마대전에서도 혁혁한 공을 세웠던 인물이오. 그런 그가, 모용세가가 도대체 무슨 연유로…….”

하지만 그들이 느낀 불신은 찰나에 불과했다.

개방이, 하오문이, 화산파와 하북팽가가.

그리고 천하 무림의 중심이라 할 수 있는 무림맹이 공식적으로 모든 것이 한 치의 거짓도 없는 사실을 밝혔기 때문이었다.

심지어는, 존재하되 존재하지 않는 것과 같았던 무림 밖의 거인까지도.

“길을 여시오!”

적게는 수십, 많게는 수백에 달하는 관병들이 무리 지어 곳곳을 누볐다.

길어진 평화 속 나른한 얼굴로 창에 기대어 하루를 보내던 그들은, 철저한 무장을 갖춘 채 투구 사이로 한껏 날카로워진 눈매로 사방을 주시하며 자신들에게 떨어진 명령을 수행했다.

“여보게, 무슨 일인가?”

“글쎄. 난들 알 턱이 있나. 다만 분위기가 흉흉한 걸 보니 근래에 황도(皇都)에서 벌어졌다는 모종의 사건에 관한 문제가 아닐까 싶은데.”

“어, 나도 그 소식 들었네. 암천인지 뭔지 그 쳐죽일 놈들 말하는 거 맞나? 아는 무림인한테 듣기로는 놈들이 또 한 번 난동을 피웠다는데…….”

그것은 비단 어느 한 곳에서만 벌어지는 일이 아니었다.

갑작스럽게 돌변한 관병들의 모습을 본 사람들은 당혹스러움과 긴장감을 동시에 느끼며 모여들었다.

그리고 머지않아 관병들이 사방에 붙이고 떠난 방(榜)의 내용을 확인할 수 있었다.



만천하, 만백성에게 고하노라.



각 성부에 속한 문장가들이 일필휘지(一筆揮之)로 써내려 간 포고문의 첫 문장은 그렇게 시작되었고, 수많은 군중들의 시선을 받아 떠밀리듯 앞으로 나선 유생들의 목소리는 시간이 흐를수록 잘게 떨렸다.

“……하, 하여 관에 속하지 않은 무부(武夫)들을 아울러 암천(暗天)이라 불리는 역적의 무리를 일벌백계하고자 하니, 이는 곧 짐의 뜻이자 하늘의 계시로다.”

제법 긴 낭송을 끝마친 후에도 장내는 쥐죽은 듯이 조용했다.

이 갑작스러운 포고문에 대한 뜻을 이해한 이들은 유생들과 같이 눈을 부릅떴고, 이해하지 못한 촌부들은 눈동자를 이리저리 굴리며 작은 목소리로 소곤거렸다.

“대관절 저게 뭔 뜻이여?”

“나도 잘 몰러. 관에 속하지 않은 무부는 무림인들을 말하는 것 같긴 한디…… 알아먹기 쉽게 전하면 되지 무슨 말을 저리 거창하게 써 놨대.”

하루 벌어 하루 먹고 사는 인생.

태어나 보니 배울 수 있던 것은 몸 쓰는 것과 우직함뿐이라, 늘 가벼운 주머니와 달리 어깨는 천근만근 무거운 그들이 글줄이나 제대로 읽어 보았겠는가.

하지만 침묵과 무지를 견디지 못하는 이들은 어느 곳에서나 존재하기 마련이었다.

“폐하께서 친히 내리신 황명이오. 암천의 무리를 역적으로 규정짓는 동시에, 강호의 무림인들과 힘을 합쳐 놈들을 벌할 것을 만백성에게 천명(天命)하신 게지.”

그제야 사람들의 시선이 밑을 향했다.

깨알처럼 적힌 글자 아래, 선명하게 찍힌 직인(職印)이 보였다.

그것은 이 광활한 구주 천하에서 오직 한 존재에게만 허락된, 수많은 이들이 지금껏 본 적도 없었던 옥새의 흔적이었다.

까막눈들조차 한눈에 범상치 않음을 알아볼 수 있는.

“예상했던 것보다 사안이 중대하군. 강호인들의 창칼까지 빌려 쓸 정도라니.”

젊은 유생이 불쑥 꺼낸 그 말에, 또 다른 누군가가 탄식하듯 뇌까렸다.

“암천에 관한 무성한 소문은 들었지만…… 아무리 그렇다 하여도 이 정도일 줄이야.”

천하 각지에서 전해지는 정보를 가장 먼저 듣는 이들은 무림인들과 상계(商界)다.

그 밖의 영역에 속한 이들은 따로 연줄이 있지 않고서야 이목이 밝지 않았고, 설령 무슨 일이 터졌다 한들 별다른 걱정을 품지 않았던 것이 현실이었다.

단단한 반석 위에 세워진 대국이다.

건국 직후 이어졌던 무수한 숙청과 지방 군벌의 반란도 이미 끝난 지 오래.

흐르는 시간 속에서 천하는 안정되었고, 무림인들이 정마대전이라 부르는 오십여 년 전의 환란 속에서도 양민들의 피해는 거의 없었다.

이유?

간단했다.

마교(魔敎)라는 섬뜩한 명칭을 지닌, 저 서쪽 너머의 광신도들조차 대국의 참전을 두려워했으니까.

단지 강호인들만의 세력 다툼으로 여겨지기를 원했으니까.

하지만…….

“이번에는 다를 것이오. 그 어느 때와도.”

활불(活佛)과도 비견되었던 소림사의 방장이 열반에 들고, 평화로운 목탁 소리만 울려 퍼지던 경내가 피로 물들었을 때만 해도 이중 누구도 안타까움 그 이상의 감정을 느끼지는 않았다.

신선과도 같았던 청성과 아미의 도사들이 쓰러지고, 세간에도 독한 놈들이라고 소문난 사천당문이 극심한 피해를 입었다는 소식을 들었어도 마찬가지였다.

그것이 모두가 알고 있던 무림(武林)이니까.

푸르른 초목 대신 창칼이 난무하는 저 잔인한 숲에서는, 고승도 도사도 언제든지 죽어 나갈 수 있었으니까.

아니, 그들이 별다른 걱정 없이 상황을 지켜본 가장 큰 이유는 따로 있었다.

‘아무리 그래도 그렇지, 설마하니 우리한테까지 무슨 일이라도 있으려고.’

사는 세상이, 울타리가 달랐다.

백성들은 대국의 울타리에 몸을 의탁한 채, 자신들만의 영역에서 치열한 전투를 벌이는 무림인들을 지켜보았을 따름이었다.

간혹 무림의 일에 휘말려 희생당하는 운 없는 양민들을 안타까워하면서도, 고작 그 정도였다.

수백 리 밖에서 불길이 일어나도 그 열기는 모두에게 닿지 않는 법.

백성들의 느끼는 감정과 관심은 일순간 뜨겁게 불타올랐다가 빠르게 식었다.

전체에 비하면 한 줌에 불과한 극소수의 피해일 뿐, 그들은 멀쩡히 내일을 맞이할 수 있기에.

그들에게는 대국이라는 크고 단단한 울타리가 있었기에.

그러나 그 굳건한 믿음은, 바로 이 순간 산산이 허물어지고 있었다.

“자, 잠깐. 나으리들. 그렇다면 지금 하시는 말씀이 혹시…….”

꿀꺽.

차마 말을 잇지 못하고 마른침만 삼키는 촌로를 대신하여, 늙은 유생이 입을 열었다.

누구도 믿고 싶지도, 듣고 싶지도 않았던.

하지만 마주할 수밖에 없는 현실을.

“그래. 자네가 생각하는 그것이 맞네.”

나직하게 흘러나오는 한숨.

늙은 유생은 문득, 세월의 흔적이 아로새겨진 자신의 주름진 손을 내려다보았다.

한때는 희고 매끄러웠던, 과거의 모습을 떠올리며.

수많은 가능성이 있었음에도 끝나지 않은 난세의 시대에 가로막혀 더는 나아가지 못했던 젊은 날의 자신을, 그 혼란했던 시기를 떠올리며.

그는 천천히 말을 이었다.

“전란(戰亂)은, 이미 시작되었네.”

“……!”

“……!”

누군가는 이를 악물고 주먹을 쥐었다. 또 다른 눈을 질끈 감았다.

소리 없는 경악이 파도가 되어 군중을 휩쓸었다.

전란이라는 두 글자가 부릅떠진 눈과 멍하니 벌어진 입술을 통해 사방으로 전해졌다.

넓은 대로변에서, 좁고 어두컴컴한 골목길에서, 이 믿을 수 없는 소식을 전하기 위해 바쁘게 움직이는 누군가의 발걸음을 따라서.

전쟁.

모든 것을 불태울 거대한 대전쟁의 불길.

그 순간, 늙은 유생은 보았다.

마침내 오랜 세월 잠자고 있던 어둠이 깨어나, 모두의 낯빛을 암담하게 물들이는 것을.

그리고 불현듯, 하늘 같은 황명이 적힌 포고문에 등장한 낯선 이름을 조용히 마음속으로 뇌까렸다.

태원진가의 진태경.

아니, 상산후(上山侯) 진태경.

이번의 역모를 막은 일등 공신이자, 젊다 못해 새파란 나이와 무림인이라는 신분임에도 열후(列侯)의 자리에 오른 자.

‘비록 강호의 사정에는 밝지 않으나…… 한 가지는 확실하군.’

한때 관직에 몸담았던 늙은 유생은 충분히 짐작할 수 있었다.

전례(前例)가 없는, 아니 앞으로도 없을 전무후무(前無後無)한 일을 이뤄 낸 저 젊은 무림인을 기다리고 있는 미래를.

‘뉘신지는 모르겠으나, 부디 온 힘을 다해 나아가게. 본래 그대가 살아가던 무림을 넘어 이 나라를 위해서라도.’

닿지 않을 말과 함께, 늙은 유생은 포고문을 향해 절을 올렸다.

첫 번째로는 머나먼 황도에서 모든 것을 굽어보고 있을 천자를 향해.

두 번째로는 이 천하를 지키기 위해 피를 흘리며 쓰러질 수많은 영령(英靈)들을 위해.

마지막으로, 지엄한 황명으로 무림의 중심에 우뚝 선 새로운 열후를 향해.

늙은 유생은 계속해서 절을 올렸다.

사람들의 시선 앞에서도 그저 묵묵히, 지금 당장 자신이 할 수 있는 최대한의 예의와 진심을 다하여.

그리고 그로부터 수천 리 떨어진 어느 비좁은 협곡에서는, 샛노란 국화꽃이 사방을 물들이고 있었다.



* * *



나는 중양절(重陽節)에 대해 스치듯 몇 번 들어 보기만 했을 뿐, 그 이상은 알지 못한다.

토종 한국인답게 설날과 추석 같은 민족 대표 명절은 꼬박꼬박 챙겼다지만, 대륙 놈들 풍습까지 관심을 가질 정도로 시간이 남아돌지는 않았으니까.

그러나 오늘만큼은 나도 중양절의 풍습에 따라 국화꽃을 들었다.

샛노란 그것을 넘치도록 한 아름 안고, 산수유가 든 주머니를 어색하게나마 옆구리에 찼다.

그것이 중양절을 맞이하지 못하고 떠난 자들에 대한 예의였으므로.

그들의 희생을 뒤로한 채, 계속해서 앞으로 나아가야 했으므로.

솨아아아.

저 멀리서 불어온 바람이 품 안의 국화를 흔들었다.

불현듯 찾아와 손을 잡아끄는 그 거센 보챔에, 크고 작은 꽃잎 여러 개가 못 이기는 척 바람을 따라나섰다.

그리고 이내, 꽃비가 되어 휘날렸다.

아득한 과거, 이 땅에 살아가던 이들이 팔천협(八天峽)이라 이름 붙인 그곳을 따라 바람을 타고 굽이굽이 헤엄쳤다.

‘아.’

나도 모르게 흘러나오려는 탄성을 삼켰다.

그것은 아름다운 동시에, 한편으로는 더없이 서글픈 광경이었기에.

비단 나뿐만이 아니라, 팔천협을 가득 메운 수만여 명의 사람들이 함께 느끼고 있을 감정이었기에.

샛노란 꽃비를 바라보며, 나는 문득 생각했다.

지금 이 순간에도 바람을 따라 멀리, 저 멀리 떠나는 것은 꽃잎인지. 아니면 소중한 것을 지키기 위해 기꺼이 목숨을 내던진 그들의 영혼인지.

정해진 정답은 없었다.

답을 찾을 이유도 없었다.

그저 믿고자 하는 대로 믿을 뿐이다. 언제고 오늘 이 자리에 돌아와 그들을 기억할 뿐이다.

각자의 방식으로.

웃음으로. 국화꽃과 산수유로.

혹은…….

눈물로.

투둑. 투두둑.

인간의 한계를 아득히 넘어선 감각은, 때때로 알고 싶지 않은 정보를 전해 주고는 한다.

이를테면, 고개를 숙인 채 잘게 몸을 떨고 있는 한 사내의 가죽신을 적시는 눈물처럼.

아니, 빗물처럼.

‘그래, 그런 거지.’

나는 조용히 하늘을 올려다보았다.

그런 진위경의 모습을, 가장 든든한 버팀목이 되어 주었던 백부의 죽음에 소리 없이 눈물을 흘리는 이소월과 또 다른 수많은 이들의 모습을 차마 볼 자신이 없어서.

솨아아아.

다시금 바람이 분다.

높게 솟아오른 꽃비가 모두를 위로하듯 감싸며 떨어져 내린다.

그러나 그 어느 때보다 맑은 하늘 아래, 수많은 빗방울은 계속해서 떨어져 내리고 있었다.

중양절은 지났으나, 국화는 시들지 않았다.

떠난 이도, 남은 이도.

모두 이곳에 함께하고 있다는 것을 나는 알고 있다.

앞으로 나아가야 할 길이, 이들로 인해 더욱 넓고 환해졌다는 사실도 함께.

띠링.

꽃비와 함께 어우러진 하늘 위로, 맑은 종소리가 울려 퍼졌다.
```

## Final English reading copy

```markdown
# Chapter 984

The saying that words without feet can travel a thousand *ri* was wrong. They could travel ten thousand—or even farther—in the blink of an eye.

The chain of events in the north spread with astonishing speed, and without end.

From person to person, on the beating wings of messenger eagles, and with the pounding hooves of horses galloping behind messengers’ hurried whips.

Before long, the fallout from the truth that had come to light was enough to shake the entire Central Plains.

“How could the Murong Family…!”

“That’s impossible. It can’t be true!”

Disbelief was the first emotion martial artists felt when they heard the news.

Of course it was.

The traitors exposed before the whole world weren’t groups rooted in demonic, heterodox arts, like the Yangtze River Channel League or the Green Forest Alliance. They were none other than the Murong Family.

One of the Five Great Families of the world.

Though based at the very edge of the north, it was a true great family, renowned from the vast lands of Liaoning all the way to the Central Plains.

And yet that very Murong Family had supposedly joined forces with Dark Heaven.

Worse, it wasn’t the work of a few disloyal members. Most of the family, including its Family Head, Murong Baek, had been involved.

The shock this unbelievable news dealt to those who heard it was beyond words.

“The Family Head, the Divine Spear of the Imugi, was a man who distinguished himself in the Great Faction War. Why would he—or the Murong Family—do such a thing…?”

But their disbelief lasted only a moment.

The Beggars’ Sect, the Lower District Sect, Huashan, and the Hebei Peng Family—

and the Murim Alliance, the heart of the martial world—

all officially confirmed that every word of it was true, without the slightest falsehood.

Even the giant beyond the martial world—who existed, yet might as well not have—confirmed it.

“Clear the way!”

Groups of government soldiers, some with dozens of men and others with hundreds, swept through the land.

They had once leaned against their spears, spending their days with languid faces in a peace that had lasted so long. Now, fully armed, they carried out their orders with eyes sharp beneath their helmets, watching every direction.

“Hey, what’s going on?”

“How should I know? But with things this tense, I’d guess it has something to do with whatever happened in the Imperial Capital recently.”

“Oh, I heard about that too. You mean those bastards called Dark Heaven? I heard from a martial artist I know that they went on another rampage…”

This wasn’t happening in just one place.

Seeing the soldiers’ sudden change in demeanor, people gathered, feeling both alarmed and on edge.

Before long, they were able to read the proclamations the soldiers had posted all around before leaving.



Let it be known to all under Heaven, to all the people:



That was how the proclamation began. It had been written in a single flowing hand by the finest men of letters in each province. Pressed forward beneath the gazes of the crowd, the scholars who stepped up to read it aloud found their voices trembling more and more as time went on.

“…Th-therefore, I shall join forces with the martial men outside government service to make an example of the traitorous band known as Dark Heaven. This is my will and Heaven’s decree.”

Even after the lengthy recitation ended, the gathering remained silent as the grave.

Those who understood the proclamation stared wide-eyed, like the scholars reading it. The country folk who didn’t understand shifted their eyes from side to side and whispered under their breath.

“What in the world does that mean?”

“I don’t rightly know. Seems like ‘martial men who don’t belong to the government’ means martial artists, though… Couldn’t they just say it plain? Why’d they have to write it so fancy?”

They were people who lived one day at a time, earning what they ate.

They had been born with nothing to learn but hard work and how to use their bodies. Their pockets were always light, but their shoulders weighed a thousand *geun*. How likely was it that they could read a line of writing properly?

But there were always people who couldn’t stand silence and ignorance.

“It is an imperial decree personally issued by His Majesty. He has declared Dark Heaven a band of traitors and announced to all his people that he will join forces with the martial artists of the world to punish them.”

Only then did people look down.

Beneath the tiny letters, a clear seal had been stamped.

It was the mark of the imperial seal, an object reserved for only one person in all the vast Nine Provinces—one that countless people had never even seen.

Even the illiterate could tell at a glance that it was no ordinary seal.

“This is more serious than I expected. They’re even calling on the martial world to lend its blades and spears.”

At the young scholar’s sudden remark, someone else murmured with a sigh.

“I’ve heard all the rumors about Dark Heaven, but… I never thought it was this bad.”

The first to hear news from every corner of the world were martial artists and merchants.

People outside those circles rarely had their ear to the ground unless they had special connections. And even when something happened, in truth, they didn’t give it much thought.

The Great Nation stood on a firm foundation.

The countless purges and provincial warlord rebellions that had followed its founding were long over.

With the passage of time, the world had settled into peace. Even during the calamity more than fifty years ago that martial artists called the Great Faction War, the common people had suffered almost no harm.

Why?

It was simple.

Even the fanatics from far to the west, who bore the chilling name of the Demonic Cult, had feared the Great Nation joining the war.

They had wanted it to be seen as nothing more than a struggle between martial-world factions.

But…

“This time will be different. Unlike any other.”

Even when Shaolin Temple’s Abbot, once considered the equal of a living Buddha, entered nirvana and the grounds where only peaceful wooden fish once sounded ran red with blood, no one there had felt anything beyond sorrow.

It was the same when they heard that the Daoists of Qingcheng and Emei, who seemed like immortals, had fallen, and that the Sichuan Tang Clan—whose people were known even among ordinary folk as a fearsome bunch—had suffered terrible losses.

That was the Murim everyone knew.

In that cruel forest, where spears and swords ran wild in place of green trees, even venerable monks and Daoists could die at any moment.

No, there was another reason they had watched everything without much concern.

*Come on. Whatever happens, surely it won’t reach us.*

They lived in different worlds, behind different walls.

The people had entrusted their safety to the Great Nation’s walls. All they had done was watch the martial artists fight their fierce battles in their own domain.

Now and then, they pitied the unlucky common folk caught up in Murim affairs and killed. But that was all.

A fire blazing hundreds of *ri* away couldn’t warm everyone.

The people’s feelings and attention burned hot for a moment, then quickly cooled.

Compared to the whole, the victims were only a handful, a tiny minority. The rest could wake up tomorrow just fine.

They had the Great Nation, a great and sturdy wall.

But that unshakable faith was crumbling to pieces at that very moment.

“W-wait, sirs. Then what you’re saying is…”

Gulp.

The old scholar spoke for the village elder, who couldn’t continue and could only swallow dryly.

The truth no one wanted to believe, or even hear.

The truth they had no choice but to face.

“That’s right. It’s exactly what you think.”

A quiet sigh escaped him.

The old scholar looked down at his wrinkled hands, etched with the marks of time.

He thought of how they had once been white and smooth.

He thought of his younger self, who had been unable to go any farther, blocked by an age of chaos that refused to end despite all the possibilities that had once lain before him. He thought of those turbulent years.

Slowly, he continued.

“The war has already begun.”

“……!”

“……!”

Some clenched their teeth and fists. Others squeezed their eyes shut.

Soundless shock surged through the crowd like a wave.

The two characters for *war* spread in every direction, carried on wide-open eyes and slackened lips.

Along broad avenues, through narrow, dark alleys, and in the hurried footsteps of those rushing to carry the unbelievable news onward.

War.

The flames of a great war that would burn everything to ash.

At that moment, the old scholar saw it.

The darkness that had slumbered for so many years had finally awoken, painting everyone’s faces with despair.

And suddenly, he silently mouthed the unfamiliar name that appeared in the proclamation, beneath the imperial decree as lofty as the heavens.

Jin Taekyung of the Jin Family of Taiyuan.

No—the Marquis of Shangshan, Jin Taekyung.

The foremost contributor to stopping this rebellion, a martial artist so young he was barely more than a boy, and yet raised to the rank of marquis.

*I don’t know much about the affairs of the martial world… but one thing is certain.*

The old scholar had once served in government. He could guess well enough what future awaited that young martial artist, who had achieved something without precedent—and something that would never be repeated.

*I don’t know who you are, but please, give it everything you have and keep moving forward. Not only for the martial world you’ve always known, but for this country as well.*

Along with words that would never reach him, the old scholar bowed toward the proclamation.

First, to the Son of Heaven, who watched over all things from the distant Imperial Capital.

Second, to the countless departed spirits who would shed their blood and fall to protect this world.

And lastly, to the new marquis who stood at the heart of the martial world by virtue of the solemn imperial decree.

The old scholar continued to bow.

In full view of the crowd, he did so quietly and without complaint, giving everything he could in the way of sincerity and respect.

And thousands of *ri* away, in a narrow gorge, bright yellow chrysanthemums were coloring the landscape in every direction.



* * *



I’d heard of the Double Ninth Festival a few times in passing, but that was about all I knew.

As a Korean born and raised, I’d always observed the big holidays like Lunar New Year and Chuseok. But I didn’t have so much time on my hands that I could take an interest in the customs of those guys on the continent.

But today, I, too, followed the customs of the Double Ninth Festival.

I held an armful of bright yellow chrysanthemums, more than enough to overflow my arms, and awkwardly wore a pouch of cornelian berries at my side.

It was a way to honor those who had passed before they could celebrate the Double Ninth Festival themselves.[^1]

We had to keep moving forward, leaving their sacrifice behind us.

*Whoosh.*

Wind from far away stirred the chrysanthemums in my arms.

The wind came out of nowhere, insistently tugging the petals by the hand. Several, large and small, gave in and went along with it.

Before long, they fluttered through the air like a rain of flowers.

They swept along the Eight Spring Gorge, winding through it on the breeze. Long ago, the people who had lived in this land had given the place that name.

*Ah.*

I swallowed the exclamation that almost escaped me.

It was beautiful, and at the same time, unbearably sad.

And I wasn’t the only one who felt that way. Tens of thousands of people filled the Eight Spring Gorge, and I knew they felt it too.

Watching the yellow petals fall, I found myself wondering: Even now, as they drifted farther and farther away with the wind, were they only petals? Or were they the souls of those who had willingly thrown away their lives to protect what they cherished?

There was no single right answer.

There was no need to find one.

We could believe whatever we wanted to believe. Whenever this day came around, we would return here and remember them.

Each in our own way.

With laughter. With chrysanthemums and cornelian berries.

Or…

With tears.

Drip. Drip, drip.

My senses, far beyond the limits of human beings, sometimes gave me information I didn’t want.

Like the tears wetting the leather shoes of a man whose head was bowed and whose body was trembling slightly.

No, like raindrops.

*Yeah. That’s how it is.*

I quietly looked up at the sky.

I couldn’t bring myself to look at Jin Wikyung like that, or at Lee Seowol silently mourning the death of her uncle, who had been her strongest support, or at the countless others in tears.

*Whoosh.*

The wind blew again.

A shower of flowers rose high, then fell, wrapping around everyone as if to comfort them.

Yet beneath the clearest sky imaginable, countless raindrops kept falling.

The Double Ninth Festival had passed, but the chrysanthemums hadn’t withered.

I knew that those who had left and those who remained were all here together.

And I knew, too, that because of them, the road we had to walk from here had grown wider and brighter.

*Ding.*

A clear chime rang out in the sky, mingling with the shower of flowers.

[^1]: On the Double Ninth Festival, people traditionally wore cornelian berries and admired chrysanthemums.
```
