<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0692.txt",
      "sha256": "da5c448d2758d5063c5fafc62da2355acd589dbe90b7a22e1c3dbbe8535c9fb3",
      "bytes": 12894
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ca3544e91ceaf80403955b66882c1824b6f6ab62de99b3d00ec6453f7bc9b286",
      "bytes": 1416
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6d2b052efe343506924742eb2029c0e6f94361eed2cb3e85dd4bce7d49e6aa08",
      "bytes": 204495
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "ceb5e08fde980358b7fc80a5e4f6d7bd3a39e52337a676f3dfae1ad93194d33e",
      "bytes": 781
    },
    {
      "path": "characters/Black Hand.md",
      "sha256": "10d11d4150ed4a128e6157a24b429478e2d6185845185bfb336398ab6fcc0610",
      "bytes": 788
    },
    {
      "path": "characters/Black Tiger.md",
      "sha256": "255c41e83ce19701b3d1d165ed7f085cd86ad46546beaa8a8aa9ae058f358111",
      "bytes": 812
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8754b7be45df4c2bcbcc56f364253d4a1361c7e028b587720c48cb20d2c3a59c",
      "bytes": 553
    },
    {
      "path": "characters/Great Snow Fiend.md",
      "sha256": "cab5c11dbd3793ccfe5e637e75804dc23718473337bdee251019bd65dd1c2e12",
      "bytes": 898
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "cf931d3815d98002cc1d3273d6051ed2902ef8b426774461b2178e34ccf10691",
      "bytes": 784
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "81e4912e8bf9bcda8644825e0d88e35fd4f01241a6a8ed851663a6e5bded3c8d",
      "bytes": 667
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "dc33459dfd5cc757993bfb0de4170370f1b06f10ee14cf4e732ab28cec46fa4c",
      "bytes": 687
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "46f8905d9456d7c5ad1d2a0c41778d9436f8958f5be8f589abd971ca43c693c3",
      "bytes": 770
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "92d10844cb67833efe330cd8724e8fed3e16324d0f75001c5f0df758b5b06cf6",
      "bytes": 213075
    }
  ],
  "estimated_tokens": 10100
}
-->

# Durable State Update — Chapter 692

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 692. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 692. Profile updates may replace only one
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
  "chapter": 692,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 692,
    "continuity_sources": [692],
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
    "Jin Taekyung, Yohi, and Muyaho remain in an unknown enclosed realm containing a pond that heals severe injuries.",
    "The healing pond saved Muyaho from the brink of death and restored Jin's severe injuries.",
    "Yohi confirms that Heugung was a Dark Heaven spy who threatened her life; she believes he is probably dead.",
    "The Black Tiger known as the apparition of Ailao Mountain saved them and communicates through telepathy.",
    "The Black Tiger claims not to know what it is, has been called by many names over centuries, and possesses the Water God Dragon's Origin Essence.",
    "Jin's System has produced unresolved ??? discovery and pending sudden Quest notifications."
  ],
  "continuity_sources": [
    691
  ],
  "open_questions": [
    "What is the Black Tiger, and whose existence did it confirm through Jin?",
    "Why did the Black Tiger save Jin, Yohi, and Muyaho?",
    "How did the Black Tiger obtain the Water God Dragon's Origin Essence?",
    "Is Heugung truly dead?",
    "What are the unidentified discovery and pending sudden Quest?"
  ],
  "safe_through": 691,
  "temporary_decisions": [
    "Keep 흑호 distinct from 백호 as Black Tiger and White Tiger.",
    "Render 애뇌산의 망령 as the apparition of Ailao Mountain.",
    "Render 흑호's 의념 as telepathic dialogue with em dashes and a calm, detached voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 암천     | **Dark Heaven**                  |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 지능               | **Intelligence**               |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 흑수 | **Black Hand** | Sadistic Dark Heaven agent and Supreme Peak master. |
| 흑수권마 | **Black Hand Fist Demon** | Sobriquet revealed by Black Hand. |
| 흑호 | **Black Tiger** | A colossal black tiger that appears at the Ailao Mountain massacre site. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대설귀 | **Great Snow Fiend** | Fiend who ruled Great Snow Mountain and killed Baekhwi and Venerable Wusang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 평화 | **Peace Guild** | Guild name. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 산군 | **mountain lord** | Traditional epithet for a tiger; retain an explanatory footnote on first use. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 기문진 | **Mystic Gate Formation** | Formation concealing Dong Feng's clinic in Sichuan. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 원정 | **Origin Essence** | The Water God Dragon's purified energy core, which humans call an inner core. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 야수묘왕 | 흑호 | hostile pursuer to unknown supernatural beast | you | blunt and furious | Directly challenges the Black Tiger over the massacre. |
| 흑수권마 | 대설귀 | junior hostile subordinate to senior ally | Senior | deferential but urgent and protesting | Black Hand protests the Great Snow Fiend's order to capture Jin. |
| 대설귀 | 흑수권마 | senior hostile commander to junior subordinate | you | blunt, commanding, and threatening | The Great Snow Fiend orders Black Hand to stop questioning him. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 691
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace and a Supreme Peak master who secretly lived for decades under Heugung's identity through the Bone-Shrinking Technique.
- **Personality:** The Beast Miao King is calculating, patient, ruthless, and willing to endanger Nanman's people to advance Dark Heaven's grand plan.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He maintained his public bond with Baeksang while secretly monitoring Baeksang and Yohi for the Southern Heaven Demon Empress, but he has now been branded a traitor, fled the Nanman Beast Palace, and disappeared.

### Black Hand.md

# Black Hand (흑수)

- **Safe through:** Chapter 688
- **Aliases:** Black Hand Fist Demon (흑수권마)
- **Role:** Black Hand was a sadistic Dark Heaven agent and Supreme Peak master who acted under orders associated with the Southern Heaven Demon Empress before his death.
- **Personality:** Black Hand is cruel, gleeful, predatory, and fascinated by the despair of his victims.
- **Voice:** Black Hand speaks in archaic first person with drunken mockery, humiliating insults, and casual threats.
- **Relationships:** Black Hand was the captor and torturer of Yohi and Heugung and an enemy of Jin Taekyung; the Great Snow Fiend was his senior and could overrule him under the Southern Heaven Demon Empress's orders.

### Black Tiger.md

# Black Tiger (흑호)

- **Safe through:** Chapter 691
- **Aliases:** Apparition of Ailao Mountain
- **Role:** The Black Tiger is an ancient, colossal supernatural beast that saved Jin Taekyung, Yohi, and Muyaho in an unknown healing realm and possesses the Water God Dragon's Origin Essence.
- **Personality:** The Black Tiger is enigmatic, detached, and inscrutable, claiming not to know its own identity after centuries of existence.
- **Voice:** The Black Tiger communicates through calm, measured telepathic thoughts with an ancient and commanding tone.
- **Relationships:** The Black Tiger saved Jin Taekyung, Yohi, and Muyaho, summoned Jin for a private discussion, and claims to have confirmed an unknown being's existence through him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 691
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Great Snow Fiend.md

# Great Snow Fiend (대설귀)

- **Safe through:** Chapter 685
- **Aliases:** Hanbaek (한백)
- **Role:** The Great Snow Fiend was the former ruler of Great Snow Mountain and a Supreme Peak fiend who killed Baekhwi and Venerable Wusang during the Great Faction War before Jin Taekyung killed him.
- **Personality:** The Great Snow Fiend is cold, pragmatic, controlled, proud, and unwilling to risk his life foolishly when outnumbered.
- **Voice:** The Great Snow Fiend speaks in measured, archaic, calm, and authoritative language that becomes frost-cold when challenged.
- **Relationships:** The Great Snow Fiend was an enemy of Baeksang, Baekhwi, Venerable Wusang, the Beast Miao King, and the allied Southern Army; he was senior to Black Hand and served under the Southern Heaven Demon Empress before Jin Taekyung killed him.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 691
- **Aliases:** Beast Miao King
- **Role:** Heugung is the secret identity of the Beast Miao King, a Supreme Peak master and long-term Dark Heaven contingency who concealed himself through the Bone-Shrinking Technique.
- **Personality:** Heugung is calculating, patient, ruthless, and obsessive, masking coercion and strategic intent behind warmth and romantic devotion toward Yohi.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung is obsessed with Yohi and is willing to threaten her and the Yao people to force her compliance while secretly serving the Southern Heaven Demon Empress.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 679
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 691
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature currently sharing an unexplained healing realm with Yohi and Jin Taekyung.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and returned to Jin with Heugung and Yohi after carrying them through the darkness.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 691
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is the strategist directing Baeksang's defense of Nanman's Inner and Outer Palaces while advancing a grand plan scheduled to begin within three days.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and regards Jin's destruction of her trap with amused surprise.

## Korean source

```text
＃692화



가끔은 본능이 이성을 이길 때가 있다.

예를 들자면, 흑호의 입안에 예쁘게 자리 잡은 수신룡의 원정을 본 순간처럼.

“너 이 새끼. 그건 또 언제 훔쳐 갔어?”

- …….

나도 모르게 튀어 나간 한마디.

짜게 식은 눈빛으로 나를 바라보던 흑호가 의념을 흘려보냈다.

- 훔쳤다니. 말이 과하군.

사실 좀 말이 과하긴 했다.

설령 저놈이 수신룡의 원정을 훔쳐 간 것이 사실이라 해도, 마음만 먹으면 언제든 꿀꺽 삼킬 수 있는 상황에서는 무조건 내가 잘못한 거다.

“좋아, 사과할게. 미안.”

깔끔하게 사과한 내가 공손히 두 손을 내밀었다.

“그러니까 이제 뱉자. 내 손바닥 보이지? 여기에 퉤, 뱉자. 응?”

- 놀라웠다.

“어, 그래. 나도 지금 엄청 놀라긴 했어. 일단 다 알겠으니까 우선 그것부터…….”

- 이것에 담긴 힘을 느꼈고, 그다음으로는 아득한 시간을 보았다.

멈칫한 내가 되물었다.

“시간이라고?”

- 그래. 그것은 같은 동류(同類)만이 엿볼 수 있는 수백여 년의 시간이자 기억이었다. 용이 되지 못한 어느 이무기의 모든 것이 담긴.

“……!”

- 유구한 기억의 끄트머리에 한 인간이 나오더군. 젊고 거칠며, 한없이 무모한 어느 인간이.

무야호를 닮은 청백색의 눈동자가 물끄러미 나를 응시한다. 뒤이어 담담한 사내의 목소리와도 같은 의념이 뇌리에 울려 퍼진다.

- 그 이무기에게 감사하거라. 만약 내가 그의 기억을 보지 못했다면…… 너희 역시 그 불쾌한 인간과 같은 최후를 맞이했을 테니.

이 세상에 불쾌한 인간은 쌔고 쌨다. 당장 천하를 뒤집어서 탈탈 털면 장강을 가득 채우고도 남겠지만, 적어도 흑호가 가리키는 것이 누구인지는 알 것 같았다.

“설마, 흑웅?”

- 이름 따위는 모른다. 다만 너와 달리 그자는 앞발이 하나뿐이었지.

일단 앞발이 아니라 손이긴 한데. 지금은 그게 중요한 게 아니다.

나는 새삼스러운 눈빛으로 흑호를 바라보았다.

“음. 우선 살려 줘서 고맙다고 해야 하나?”

- 상관없다. 내 선택이었으니.

“그럼 고맙다고 해 두지. 진심이야.”

힐끔 나를 바라본 흑호가 돌아서서 천천히 걷기 시작했다. 자연스럽게 녀석의 뒤를 따르게 된 내가 입을 열었다.

“몇 가지 궁금한 게 있는데.”

- 귀찮군.

“뭐? 귀찮아도 성심성의껏 대답해 준다고?”

- 안 된다.

“오. 흔쾌히 허락해 줘서 고마워.”

- ……인간의 소통 방법은 참으로 희한하군. 세월이 너무 많이 흐른 탓인가?

흑호의 의념을 가볍게 씹어 버린 나는 가장 중요한 것부터 물었다.

“시간이 얼마나 흘렀지?”

빳빳하게 내려간 꼬리만 봐도 불편한 기색이 역력했지만, 얼마 지나지 않아 대답이 돌아왔다.

- 너는 이곳에서 인간의 시간으로 하루를 머물렀다.

“하루?”

평범한 기준에서 생각해 보면 턱없이 짧은 시간.

하지만 지금 같은 상황이라면 이야기가 달라진다.

대설귀와 흑수권마는 곧 남만에 불어닥칠 혈풍(血風)을 예고했고, 야수묘왕마저 행적이 묘연해진 지금 남천마후를 막을 수 있는 것은 아무도 없으니까.

‘빌어먹을.’

어쩔 수 없던 상황이었지만 내가 의식을 잃은 하루 동안 수천, 혹은 수만이 죽어 나갔다 해도 이상하지 않다.

이를 악물며 욕설을 삼킨 나는 가까스로 말을 이었다.

“출구. 이곳을 빠져나갈 출구를 알려 줘.”

- 떠날 생각인가?

“그래. 구해 준 건 고맙지만 더 머뭇거릴 시간이 없어.”

- 위기에 처한 동족들을 구할 생각이군. 지난번처럼 무모하게.

“너, 혹시?”

- 안심해라. 인간의 기억까지 읽지는 못하니까. 그저 이무기의 기억 속에 남은 네 모습을 보며 짐작했을 뿐이다. 그토록 치열하게 싸운 이유 역시 비슷한 이유였을 테고.

“……보고 있었다고?”

- 그래. 처음부터 끝까지. 언제나처럼 이곳에서 벌어지는 모든 것을 지켜보고 있었지.

자연스럽게 고개를 돌려 나를 바라본 흑호가 담담하게 의념을 이어 갔다.

- 하지만 굳이 인간들의 일에 끼어들 이유를 찾지 못했다. 적어도 네가 ‘그것’을 꺼내기 전까지는.

“……!”

나는 눈을 크게 떴다. 흑호가 말하는 ‘그것’이 수신룡의 원정을 뜻하는 것임을 알았기 때문이 아니다.

살고자 하는 마지막 발악으로 원정을 취하려던 그때, 어디선가 불어온 스산한 바람에 멈칫했던 기억이 떠올라서였다.

그와 동시에 무언가 이상한 낌새를 느낀 나는 원정을 내려놓았고, 그 직후 도착한 무야호 덕분에 목숨을 건졌다.

“그럼 그 바람이…….”

흐려지는 말꼬리. 뒤이어 흑호가 흘려보낸 의념이 머릿속에 울려 퍼졌다.

- 바보 같은 짓을 하더군. 정해진 이치를 거스른다면 그것이야말로 역천(逆天). 가만히 놔두었다면 넌 이무기가 남긴 힘을 이기지 못하고 죽었겠지.

끝없이 이어진 절벽 위를 걷는 흑호의 뒷모습을 말없이 바라보던 나는 문득 중얼거렸다.

“한 번이 아니라, 두 번이었군.”

- 무엇을 말하는 것이냐.

“네가 날 살린 거.”

흑호가 작게 코웃음 쳤다.

- 멍청한 인간에게 자신의 모든 것을 넘겨 준 누군가가 안타까웠을 뿐이다. 그 이유만 아니었다면 네놈은 죽어 마땅해.

“그건 좀 억울하네. 뭐 때문에 인간을 적대하는지는 모르겠지만, 살면서 그 정도로 큰 잘못을 저지른 적은 없는데.”

- 죄 없는 목숨을 빼앗으려 하고, 평화롭게 살아가던 터전을 불태웠는데도 말이냐?

“뭐?”

흑호가 대답 대신 고갯짓으로 절벽 아래를 가리킨다.

몸 군데군데가 검게 그을린 수많은 짐승들이 이름 모를 개울가에서 목을 축이고 있었다. 그 머릿수가 어림잡아도 수천.

도무지 끝이 보이지 않는 이 공간에 머무르고 있을 다른 짐승들까지 더한다면, 도무지 그 숫자를 짐작하기 어렵다.

‘도대체…….’

절벽 위에 우뚝 선 채. 멍하니 그 광경을 바라보던 그때였다.

- 네가 불러일으킨 화마(火魔)가 지금도 산 전체를 집어삼키고 있다. 그대로 불길이 번졌다면 진즉 모든 것이 불타 없어졌겠지.

“…….”

- 그래, 내가 저들을 이곳으로 인도했다. 일곱 밤 전과 같이.

칠주야(七晝夜) 전이라면 바로 그날이다. 나와 야수묘왕이 급보를 접하고 애뇌산으로 향했던 바로 그 날.

빠르게 기억을 되짚은 내 머릿속에 섬광과도 같은 깨달음이 스쳐 지나갔다.

‘맹수들.’

똑똑히 기억난다.

애뇌산에 배치되어 있던 삼백여 명의 전사들 중 이백여 명은 살아서 귀환했지만, 맹수들은 아니었다.

그 어디에도 녀석들의 모습을 보지 못했다. 애뇌산에서도, 독혈지에서도.

“그것도 너였군. 네가 맹수들을 구한 거야.”

- 있어서는 안 될 마물들이 풀려났다. 지난 수백여 년간 인간의 일에는 관여하지 않았으나, 그때만큼은 나서지 않을 수 없었지.

평소였다면 무심코 지나쳤을지도 모른다. 하지만 흑호의 의념에 한껏 귀 기울이고 있던 나는 곧장 이상함을 알아차렸다.

“풀려났다고?”

- 몰랐더냐?

은은한 경멸이 떠오른 청백색의 눈동자가 나를 응시한다.

- 모두 인간의 짓이었다. 아주 오래전부터 너희는 그러했고, 나는 이곳에 머무르며 그 모든 것을 지켜보고 있었지.

빌어먹을.

끝내 짐작에 그쳤던 애뇌산에서의 일. 하지만 흑호의 말에 의해 확실해졌다.

결국 그것 역시 암천의 소행이었다는 것을.

‘조금만. 조금만 더 빨리 이 사실이 밝혀졌다면.’

때 지난 후회와 함께, 나는 흑호를 응시했다. 이제야 그날 보았던 녀석이 왜 그런 행동을 했는지 어렴풋이 알 것 같았다.

충분히 벗어날 수 있음에도, 자꾸만 나타나고 사라지기를 반복하던 흑호의 뒷모습이 떠오른다.

“그날 넌 우리를 공격한 게 아니었어.”

- 그래. 그건 내게 주어진 사명이 아니니까.

“단지…… 알려 주려던 거였지. 천년지주가 있는 곳을.”

- 삿된 마물이 이 산을 어지럽히는 것을 지켜만 볼 수 없었다. 인간이 심은 씨앗이니, 인간이 거두어야 하는 것이 순리(順理)지.

조용히 대답한 흑호의 걸음은 계속해서 이어졌다.

절벽 위의 길은 점점 좁고 가팔라졌고, 구름 사이 우뚝 솟은 험준한 봉우리에 둥지를 튼 새들이 호기심 어린 눈빛으로 우리를 바라보고 있었다.

대화를 나누는 동안 얼마나 걸었던 것일까. 사방이 운무(雲霧)로 가득한 그곳에서 내려다보이는 지상은 실로 까마득했다.

‘분명 이 정도 면적은 아니었던 것 같은데.’

처음 눈을 떴을 때는 작은 연못을 낀 숲이라 생각했다.

하지만 주위를 둘러보니 이제는 거대한 산맥과 계곡, 초록빛 목초지로 가득했다.

‘도대체.’

이제는 도무지 감도 잡히지 않는다. 불가사의에 둘러싸인 듯한 기분으로 눈앞에 벌어진 광경을 바라보던 나는 가까스로 입술을 뗐다.

“이곳은…… 어디지?”

- 생명이 깃든 땅. 모든 것이 조화 속에서 살아가는 곳.

무슨 귀신 씻나락 까먹는 소리일까.

그 순간 문득 내가 꼬꼬마였던 시절, 떡볶이를 주며 예수 천국 불신 지옥을 부르짖던 교회 집사님이 생각났다.

“아무리 그래도 천국은 아닐 텐데.”

- 하늘의 나라? 제법 그럴듯한 표현이로군. 하지만 이곳은 내 허락이 없다면 누구도 들어올 수 없는 땅 깊숙한 곳이다. 너희가 있던 곳과도 매우 가깝지.

“그럼 설마…… 여기가 독혈지(毒血地)라고?”

내 중얼거림에, 몇 걸음 앞서가던 흑호의 커다란 머리가 작게 끄덕여졌다.

- 그렇다.

“하지만 이곳은…….”

문득 말문이 막혔다. 독혈지라니.

설령 이곳이 애뇌산이라고 해도 믿을 수 없었을 것이다.

지금 이곳에는 맹렬하게 타오르는 불길도 없고, 애뇌산에 감돌던 특유의 스산한 기운도 없었으니까.

- 그만두어라. 이곳은 너희 인간들이 침범할 수도, 이해할 수도 없는 장소이니.

말 그대로다. 무림에는 온갖 기기묘묘한 것들이 존재하며 기문진법(奇門陣法)도 그중 하나지만, 지금 눈 앞에 펼쳐진 광경은 그 한계를 아득히 초월해 버렸다.

“하. 독혈지. 여기가 독혈지라니.”

나는 헛웃음 섞인 혼잣말을 흘리며 흑호를 따라 봉우리를 올랐다.

어느덧 정상에 가까워지는 발걸음과 함께, 흑호의 의념이 들려왔다.

- 독혈지는 현재의 이름이다. 내가 그러했듯, 인간들은 시간의 흐름에 따라 많은 것을 바꾸었지.

“그럼 전에는 뭐라 불렸지?”

- 성지(聖地).

“뭐?”

- 이무기의 기억만큼이나 오래된, 실로 까마득한 과거의 이야기다. 그 시절 이 땅의 주인은 인간이 아닌 짐승이었고, 각자의 영역에서 무리 지어 살아가던 소수의 인간은 우리를 숭배했다.

“허.”

나도 모르게 말문이 막혔다.

그 누구도 접근할 수 없는 금역(禁域)이 한때는 성지라 불렸었다니. 게다가 남만인들이 몇 안 되던 시절이라면…… 도대체 얼마나 오래전의 일인지 감도 잘 안 잡혔다.

오백 년? 아니면 천 년?

‘미치겠네.’

처음부터 지능 스탯에 몰빵을 했어도 지금 이 순간만큼은 바보가 되어 버렸을 거다.

고개를 절레절레 흔든 나는 어느새 발걸음을 멈춘 흑호를 향해 입을 열었다.

“그럼 넌. 도대체 너는 뭐지?”

- 일전에 네 입으로 말하지 않았더냐. 망령이라고.

“내가 궁금한 건, 이곳이 성지였을 때의 네 이름이야.”

잠시 침묵하던 흑호가 거대한 신형을 움직였다. 청백색의 눈동자에 아련한 무언가가 스쳐 지나갔다.

- 수호령.

“뭐?”

- 머나먼 옛날, 사람들은 나를 그렇게 불렀다. 애뇌산을 지키는 산군. 신석(神石)과 함께 태어난 수호령이라고.
```

## Final English reading copy

```markdown
# Chapter 692

Sometimes instinct beats reason.

Like the moment I saw the Water God Dragon’s Origin Essence sitting prettily inside the Black Tiger’s mouth.

“You bastard. When did you steal that?”

—…….

The words slipped out before I could stop them.

The Black Tiger stared at me with a frigid look before sending a thought my way.

—“Steal” is an excessive word.

It was a little excessive.

Even if he had actually stolen the Water God Dragon’s Origin Essence, he could swallow it whenever he wanted. In that situation, I was unquestionably in the wrong.

“Fine. I’ll apologize. I’m sorry.”

After apologizing cleanly, I politely held out both hands.

“So spit it out now. You can see my palm, right? Spit it out here. Come on.”

—It was astonishing.

“Yeah, I was pretty shocked too. Now that I understand everything, let’s start with that….”

—I felt the power contained within it. Then I saw an immeasurably distant span of time.

I paused and asked,

“Time?”

—Yes. It was several hundred years of time and memory, visible only to beings of the same kind. Everything belonging to an imugi who had failed to become a dragon was contained within it.

“……!”

—At the end of that ancient memory, a human appeared. A young, rough, infinitely reckless human.

The Black Tiger’s blue-white eyes, so much like Muyaho’s, gazed at me. Then a thought resembling the calm voice of a man echoed inside my mind.

—Be grateful to that imugi. If I had not seen his memories, all of you would have met the same end as that unpleasant human.

This world was full of unpleasant humans. If you turned the whole land upside down and shook it out, there would probably be enough to fill the Yangtze and then some. But I had a pretty good idea who the Black Tiger meant.

“Don’t tell me… Heugung?”

—I do not know his name. But unlike you, he had only one forepaw.

Technically, it had been a hand, not a forepaw. But that wasn’t important right now.

I looked at the Black Tiger with renewed interest.

“Hmm. Should I start by thanking you for saving me?”

—It does not matter. It was my choice.

“Then I’ll thank you anyway. I mean it.”

The Black Tiger gave me a brief look, then turned and began walking slowly. I naturally followed behind him and opened my mouth.

“There are a few things I’m curious about.”

—You are bothersome.

“What? You mean you’ll answer all my questions in good faith even though I’m bothering you?”

—No.

“Oh. Thanks for granting permission so readily.”

—……Human communication is truly strange. Is it because too much time has passed?

I let the Black Tiger’s thought wash past me and asked about the most important thing first.

“How much time has passed?”

His tail hung stiffly downward, making his discomfort obvious. Even so, an answer came before long.

—You spent one day here, by human reckoning.

“One day?”

By ordinary standards, that was an absurdly short time.

But under the circumstances, it was a different story.

The Great Snow Fiend and the Black Hand Fist Demon had foretold the bloody storm that would soon sweep across Nanman. With even the Beast Miao King’s whereabouts unknown, there was no one left who could stop the Southern Heaven Demon Empress.

*Damn it.*

The situation had been unavoidable, but it wouldn’t have been strange if thousands—or tens of thousands—had died during the one day I was unconscious.

I clenched my teeth and swallowed the curse before forcing out my next words.

“An exit. Tell me how to get out of here.”

—You intend to leave?

“Yeah. I’m grateful that you saved me, but I don’t have time to hesitate.”

—You intend to save your own kind from danger. Recklessly, as you did last time.

“You…?”

—Be at ease. I cannot read human memories. I merely inferred it from the sight of you remaining in the imugi’s memories. You must have fought so fiercely for a similar reason.

“……You were watching?”

—Yes. From beginning to end. As always, I was watching everything that happened here.

The Black Tiger naturally turned his head to look at me and continued sending his calm thoughts.

—But I found no reason to involve myself in human affairs. At least, not until you pulled out “that.”

“……!”

My eyes widened. Not because I realized that “that” meant the Water God Dragon’s Origin Essence.

I had remembered the moment when, in one last desperate struggle to stay alive, I had reached for the Origin Essence—only to hesitate when a chill wind blew in from somewhere.

At the same time, I had sensed something strange, so I let go of the Origin Essence. Muyaho arrived immediately afterward and saved my life.

“Then that wind…”

My voice trailed off. The Black Tiger’s thought echoed through my head.

—You were about to do something foolish. If you defy what is ordained, that is defying Heaven. Had I done nothing, you would have died, unable to overcome the power left behind by the imugi.

I silently watched the Black Tiger’s back as he walked along the endless cliff.

“Not once, but twice.”

—What are you talking about?

“You saving me.”

The Black Tiger gave a small snort.

—I merely felt sorry for someone who had handed everything they possessed to a foolish human. Without that reason, you deserved to die.

“That’s a little unfair. I don’t know why you’re hostile toward humans, but I’ve never committed a crime that serious in my life.”

—Even after trying to take innocent lives and burning down the home of those who lived in peace?

“What?”

Instead of answering, the Black Tiger pointed his head toward the bottom of the cliff.

Countless beasts, their bodies blackened in places, were drinking from an unnamed stream. There were thousands of them, even by a rough estimate.

If I added all the other beasts that might be living in this boundless space, there was no way to guess the total number.

*What the hell…?*

I stood rigidly atop the cliff, staring blankly at the sight.

—The inferno you unleashed is still devouring the entire mountain. If the flames had spread unchecked, everything would have burned away long ago.

“…….”

—Yes, I led them here. Just as I did seven days and nights ago.

Seven days and nights ago.

That had been the very day the Beast Miao King and I received the emergency report and headed for Ailao Mountain.

I quickly retraced my memories, and a flash of realization passed through my mind.

*The wild beasts.*

I remembered it clearly.

Of the more than three hundred warriors stationed at Ailao Mountain, more than two hundred had returned alive.

But the wild beasts hadn’t.

I hadn’t seen them anywhere—not at Ailao Mountain, and not in the Poisonblood Grounds.

“You were the one who did that too. You saved the wild beasts.”

—Monsters that should never have existed were released. I had not involved myself in human affairs for the past several hundred years, but that time, I could not remain uninvolved.

“Released?”

—You did not know?

A faint contempt appeared in the Black Tiger’s blue-white eyes as he stared at me.

—It was all the work of humans. You have been doing this for a very long time, and I remained here, watching all of it.

*Damn it.*

What had happened at Ailao Mountain had ultimately remained speculation. But the Black Tiger’s words confirmed it.

That, too, had been the work of Dark Heaven.

*If only… If only this had come to light a little sooner.*

With belated regret, I stared at the Black Tiger. I thought I finally understood, at least vaguely, why he had acted as he did that day.

I remembered the Black Tiger’s back as he repeatedly appeared and disappeared, even though he could have escaped at any time.

“You weren’t attacking us that day.”

—Yes. That was not my mission.

“You were just trying to tell us where the Thousand-Year Spider was.”

—I could not simply watch while a foul monster disturbed this mountain. Humans planted the seed, so humans should reap it. That is the natural order.

The Black Tiger continued walking as he answered quietly.

The path along the cliff grew narrower and steeper. Birds nesting on rugged peaks that rose among the clouds watched us with curious eyes.

How long had we walked while talking? The ground below, visible through the clouds and mist surrounding us on every side, looked unimaginably far away.

*I’m pretty sure this place wasn’t this large.*

When I first opened my eyes, I had thought it was a forest surrounding a small pond.

But when I looked around now, I saw enormous mountain ranges, valleys, and green pastures stretching in every direction.

*What the hell?*

I couldn’t even begin to guess anymore. Feeling as though I were surrounded by mysteries, I managed to part my lips.

“Where is this place…?”

—A land where life dwells. A place where everything lives in harmony.

*What kind of nonsense was that?*

At that moment, I suddenly remembered the church deacon who used to hand me spicy rice cakes when I was little and shout, “Jesus, heaven! Unbelievers, hell!”

“Even so, this can’t be heaven.”

—The kingdom of heaven? That is a fairly fitting expression. But this is a place deep within the land that no one can enter without my permission. It is also very close to where you were.

“Then… could this be the Poisonblood Grounds?”

At my muttered words, the Black Tiger’s massive head, several paces ahead of me, gave a small nod.

—It is.

“But this place….”

The words caught in my throat.

The Poisonblood Grounds?

Even if this had been Ailao Mountain, I wouldn’t have been able to believe it.

There were no fierce flames burning here, nor the distinctive eerie atmosphere that had lingered over Ailao Mountain.

—Enough. This is a place that you humans can neither invade nor understand.

He was right.

The Murim contained all kinds of strange and mysterious things, and Mystic Gate Formations were one of them. But the scene spread before my eyes had far surpassed their limits.

“Ha. The Poisonblood Grounds. This is the Poisonblood Grounds.”

I let out a hollow laugh and followed the Black Tiger up the mountain.

As our steps drew us closer to the summit, the Black Tiger’s thought reached me.

—Poisonblood Grounds is its current name. As I did, humans changed many things over the passage of time.

“What was it called before?”

—The Sacred Land.

“What?”

—It is a story from a distant past, as old as the imugi’s memories. In those days, beasts—not humans—were the masters of this land. The few humans who lived in groups within their own territories worshiped us.

“Wow.”

I was rendered speechless.

A forbidden land that no one could approach had once been called the Sacred Land. And if this had been back when the Nanman people were still few in number…

I couldn’t even begin to comprehend how long ago that must have been.

Five hundred years? Or a thousand?

*This is driving me crazy.*

Even if I had dumped every point into Intelligence from the beginning, I would have become an idiot at this very moment.

I shook my head and opened my mouth toward the Black Tiger, who had stopped walking before I noticed.

“Then what about you? What are you, anyway?”

—Did you not say it yourself before? An apparition.

“What I’m asking is what you were called when this place was the Sacred Land.”

The Black Tiger was silent for a moment before moving his massive body. Something wistful passed through his blue-white eyes.

—A guardian spirit.

“What?”

—Long ago, people called me that. The mountain lord[^1] who guarded Ailao Mountain. A guardian spirit born alongside a sacred stone.

[^1]: “Mountain lord” is a traditional epithet for a tiger.
```
