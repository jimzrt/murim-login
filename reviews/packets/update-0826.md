<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0826.txt",
      "sha256": "46ea22990cfee0fe6220e4d98353e068fb9740956435f4891436a736ac652929",
      "bytes": 12682
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9a91b4e9f766f31db12315585e1b043f336a37bfc2274865236ec137560b2402",
      "bytes": 2239
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3c3b9627e7353c69a66f8e10657ef055c79a30700111295e071d564e07f7e0ae",
      "bytes": 226707
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "233ead5d4e51433b2203e70270141ff2ec38e6dcd173856e33c662ec3451ea9f",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "2f723d0e7c1069aba4249a148509d82663f803ccc4e669dfdc55b62f6763f90a",
      "bytes": 831
    },
    {
      "path": "characters/Michael.md",
      "sha256": "689c79d93ec32bafd48ac7c1412b3fc776ae53392cab140cd789e89e7775b5ab",
      "bytes": 820
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "67c773e1faecc341a7cfdee91a1ed0aa8d8bc470d8ce806fc6749e013e6e32b8",
      "bytes": 250673
    }
  ],
  "estimated_tokens": 8779
}
-->

# Durable State Update — Chapter 826

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
1 and safe_through 826. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 826. Profile updates may replace only one
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
  "chapter": 826,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 826,
    "continuity_sources": [826],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” who concealed itself for decades, including under the name Muninn.",
    "The Doppelganger can resurrect by consuming absorbed lives and reproduce absorbed people’s appearances, abilities, and memories; it has taken Siegfried Bassman’s face and Grand Mage abilities.",
    "The Doppelganger’s absorbed lives were dwindling after it forced Blink beyond its normal range; it has since killed twenty followers and absorbed their vitality and souls.",
    "The Doppelganger confirmed Jin is the Chosen One and believes its master will be pleased.",
    "The Doppelganger has lost an arm but remains alive and retains the Grand Mage’s soul, which it says it needs for what comes next.",
    "Jin’s White Flame spear produces blue-white flames.",
    "Jin and the Skeleton King have engaged the Doppelganger after Teleporting hundreds of kilometers; their attacks are coordinated.",
    "The long-range Teleport left Jin physically injured, and his mental strength is depleted; he cannot move.",
    "A tremendous force is pulsing through the ruins where Jin, the Skeleton King, and the Doppelganger are fighting.",
    "Magic Johnson stayed behind to guard the battlefield."
  ],
  "continuity_sources": [
    824,
    825
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, what is the plan, and why must the target be avoided until it is complete?",
    "What does the Chosen One designation mean?",
    "What is the force pulsing through the ruins, and what will it do?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 825,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword.”",
    "Render 에어 슬래시 as “Air Slash” and 실드 마법 as “Shield magic.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 일류     | **First Rate**    |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 몬스터     | **monster**           |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 825
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 825
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a powerful being from the Demon Realm that spent decades manipulating events in the human world.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** Not established
- **Relationships:** It served an unnamed master who sent it to this world and ordered it to avoid the target until the master’s plan was complete; it regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 825
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

## Korean source

```text
＃826화



인간이라는 동물은 그렇다.

수십억 명에 달하는 인류가 있지만 그들은 저마다의 기준으로, 저마다의 상식으로 세상을 인식하고 바라본다.

그리고 자신의 잣대로 쉽게 받아들일 수 없는 현상을 목격했을 때, 비로소 경악이라는 감정을 품게 된다.

물론 나 역시 예외는 아니다.

어느 날부터 갑작스럽게 두 세상을 오가게 되었어도, 시스템이라는 믿지 못할 힘으로 지금 이 자리까지 오르게 되었어도 그 사실은 달라지지 않았다.

나는 언제나 감정에 솔직한 사람이었고, 때로는 감정에 사로잡혀 무슨 일을 해야 하는지조차 잊고는 했다.

바로 지금 이 순간처럼.

‘저게…… 뭐지?’

모든 사고 회로를 정지시킨 한 가지 의문.

나는 아연한 눈빛으로 눈앞에서 펼쳐지는 광경을 바라보았다.

아니, 비단 나 혼자만이 아니다.

“이게 무슨.”

도플갱어를 향해 재차 쏘아지려던 스켈레톤 킹조차 멍하니 뇌까렸다.

[영웅의 검]을 찬란하게 물들였던 황금빛 마력은 어느새 사그라진 지 오래.

우리는 도플갱어를 중심으로 흘러나오는 거대한 기운을 느꼈고, 동시에 발아래의 폐허 깊숙한 곳으로부터 흘러나오는 울림을 들었다.

구궁, 구구궁.

‘이건.’

익숙한 느낌이다. 그러나 이 울림은 그저 시끄럽기만 한 굉음 따위가 아닌, 보다 깊고 본질적인 무언가였다.

마땅한 단어를 찾자면, 그래.

‘감응(感應).’

내가 떠올렸으면서도 순간 미친 소리라고 느껴졌다.

비록 무림에서는 일류에 이른 검객이 검명(劍鳴)을 이끌어 낼 수 있다지만, 이건 그저 땅이다.

나무 한 그루, 잡초 하나 자라나지 않는 황무지였고, 이제는 그 누구도 찾지 않는 폐허였다.

그런 죽음의 땅이, 그것도 온 사방의 폐허 전체가 감응하듯 떨리고 있다니.

다시 생각해 봐도 미친 소리가 아닐 수 없었다.

만약 섬광처럼 뇌리를 스쳐 지나가는 어떤 생각이 아니었다면, 나는 한참이나 이 해결되지 않는 의문 앞에서 머뭇거렸을 것이다.

하지만 언제나 늘 그래 왔듯이, 해답은 생각보다 가까이에 있었다.

“마법.”

신음과도 같은 한 단어가 입술 사이로 흘러나온 그 순간.

쿠웅!

마치 심장 박동처럼 깊은 울림을 토해 내던 폐허가 물결친다. 동시에 지금껏 본 적 없는 휘황한 빛 무리가 사방을 물들이며 터져 나왔다.

화아아아악!

앞서 겪었던 텔레포트 마법과는 비교도 할 수 없을 만큼 눈부신 섬광.

나는 망설임 없이 눈을 감으며 몸을 비스듬히 굽혔다. 자연스럽게 힘이 들어간 창대가 파르르 떨렸다.

‘온다. 분명히.’

이미 오래전부터 뼛속 깊이 각인된 본능이 지친 몸을 움직인다.

나는 곧 들이닥칠 도플갱어의 공격을 회피하기 위해, 더불어 놈의 기습에 대응하기 위해 만반의 준비를 끝마쳤다.

몸과 마음이 물먹은 솜처럼 무겁다.

그러나 이 격돌에서 죽음을 맞이하는 것이 나라고 해도, 도플갱어 역시 무사하지 못하리라는 확신이 있었다.

일격(一擊).

누가 쓰러지건, 단 한 수에 승부가 결정될 것이다.

지금 당장은 보이지 않지만, 아마도 스켈레톤 킹 역시 나와 같은 마음으로 놈을 기다리고 있겠지.

‘와라.’

호흡을 가다듬으며 최대한 감각을 끌어 올렸다.

지그시 감은 두 눈. 그러나 날 선 오감을 통해 부르르 떨리는 공기와 죽어 버린 폐허의 흙내음이 전해진다.

얇은 눈꺼풀을 비집고 들어온 눈부신 섬광이, 망막을 어루만지다가 조금씩 사그라지는 것 또한 예외는 아니었다.

‘빛이…… 사그라졌다고?’

어째서, 라는 의문이 가장 먼저 떠오른 것은 당연했다.

그만큼 조금 전의 상황은 도플갱어에게 있어서 완벽한 타이밍이었고, 절호의 기회였으니까.

하지만 예상했던 기습은 기미조차 보이지 않았다. 다만 어느덧 익숙해진 목소리가 귓가로 날아들었을 뿐이었다.

“보기보다 겁이 많군, 선택받은 자여.”

나는 입술을 깨물었다.

지금 저 말의 의도는 함정일까, 아니면 단순한 방심일까.

그러나 고민은 찰나였고 내게 남은 선택지는 명확했다.

천천히 눈을 뜨자, 선명해진 시야 속에서 나를 응시하는 도플갱어의 모습이 보였다.

아니, 완전히 달라진 주위의 모든 것이.

“……!”

“……!”

도플갱어의 어깨너머, 두 눈을 부릅뜬 스켈레톤 킹의 얼굴이 시야에 들어온다.

아니, 어쩌면 나 역시 녀석과 같은 표정을 짓고 있을지도 모른다.

그만큼 생각해 본 적 없는 광경이었으니까.

“이건…….”

“어때, 멋지지 않나?”

스켈레톤 킹의 말꼬리를 잡아챈 도플갱어가 과장된 동작으로 두 팔을 떨쳤다.

놈의 손끝을 따라 두둥실 솟아오른 빛의 구(球)가 폐허를, 정확히는 조금 전까지만 해도 ‘폐허였던’ 공간을 비추었다.

“영광으로 알아라. 이 경이로운 신전의 첫 손님이 된 것을.”

도플갱어의 말에는 거짓과 진실이 절반씩 섞여 있었다.

이곳은 분명 신전(神殿)이라 부를 만한 구색을 갖추었으나, 경이롭다기보다는 기괴하다는 표현이 훨씬 어울렸다.

당연한 일이다.

눈에 보이는 모든 것이 신화 속 신전의 모습을 본뜬 것처럼 웅장하고 거대했지만, 웅대한 기둥은 썩은 식물의 뿌리로 감겨 있었고 하늘을 가로막은 천장은 햇빛 한 점도 새어 들어오지 않았으니.

문득 이 신전이 마치 도플갱어를 닮았다는 생각이 들었다.

신화의 겉가죽을 그럴듯하게 베껴 왔을 뿐, 그 안은 온통 썩고 죽어 있었으니.

그나마 신화와 흡사하다고 생각하는 부분은, 직경만 수백 미터에 이르는 이 드넓은 공간을 빼곡히 채운 괴물들의 거대한 석상뿐이었다.

“걸작이지, 안 그래?”

나는 대답 대신 담담한 눈빛으로 도플갱어를 응시했다.

지금 놈이 보이는 태도는 조금 전과는 확연히 달랐다.

그리고 수많은 적들과 마주하며 자연스럽게 체득한 본능은, 저 느긋한 태도가 방심 따위가 아니라는 것을 알려 주었다.

‘여유.’

틀림없다. 현재의 도플갱어는 잠시 잃어버렸던 여유를 되찾았다.

하지만 그것은 단지 텅 비었던 한쪽 어깻죽지에 새로운 팔이 생겨서, 혹은 괴물들의 석상으로 가득한 신전이 세워져서만은 아닐 것이다.

‘처음부터 이곳으로 온 이유가 있었어.’

내심 중얼거린 나는 조용히 감각을 퍼트렸다.

보이지 않는 기운이 사방에 꿈틀거리는 것이 느껴진다. 동시에 언젠가 매직 존슨이 지크프리트 바스만에 대해 지나가듯 언급했던 말이 문득 뇌리를 스쳤다.



‘바스만은 훌륭한 대마도사였어. 비록 나 정도의 워 메이지는 아니었지만, 누구보다 학구열이 뛰어났고 특히 마법진을 잘 활용했지.’



나 역시도 알고 있던 사실이다.

긴 세월 동안 수많은 영혼을 흡수하며 경험을 쌓은 도플갱어가, 생전의 대마도사보다 더욱 강력하게 거듭났으리라는 확신도 함께.

‘삼 년.’

길다면 길고, 짧다면 짧은 애매한 시간.

그러나 대마도사의 힘과 영혼을 취한 도플갱어가 여러 안배를 끝마치기에는 충분한 시간이기도 하다.

“이봐.”

나를 물끄러미 바라보던 도플갱어가 문득 혀를 찼다.

“사람이 물어보면, 대답을 해야지.”

우웅.

힘주어 내뱉은 한 마디와 함께, 나직하게 울려 퍼지는 공명음(共鳴音).

찰나의 순간 스켈레톤 킹과 시선을 교환한 내가 입을 열었다.

“병신이냐? 사람도 아닌 새끼가 물어보니까 대답을 안 하지.”

“흠. 위아래가 없군. 지크프리트 바스만이면 이 세상에선 제법 존경받는 영웅일 텐데.”

“그렇지. 내가 아는 그 대마도사라면. 하지만……”

나는 창날을 아래로 늘어트리며 말을 이었다.

“너 같은 몬스터 새끼는 예외로 쳐야지.”

지크프리트 바스만이 생전에 어떤 사람이었는지는 모른다. 본 적도, 직접 겪어 본 적도 없다. 교과서와 주위 사람들의 증언으로만 알고 있을 뿐이다.

하지만 한낱 껍데기를 뒤집어쓴 놈의 조롱을 듣고 있자니 기분이 더러운 것도 사실이다.

물론 지금 내가 노골적으로 적의를 드러내는 이유는, 그것이 도플갱어가 생각하는 자연스러운 반응 중 하나이기 때문이었다.

‘조금만. 조금만 더.’

비록 도플갱어를 겨누고 있던 창날은 내렸지만, 마음속에 품은 또 다른 창은 아직도 놈을 향하고 있다.

나는 대기의 기운을 서서히 끌어모았다.

상대가 눈치채지 못할 정도로 은밀하게. 그리고 조용히.

그것은 이번에 중단전(中丹田)의 효용을 일부 깨달으며 얻게 된 묘리 중 하나였다.

‘텔레포트 마법의 여파를 수습하기도 전에 너무 큰 힘을 소모했다. 약간의 시간이 필요해.’

이건 스켈레톤 킹도 마찬가지다. 다만 녀석은 이미 죽어 있는 몸이었기에 오히려 나보다도 상황이 나았고, 대기에 분포된 마력을 조금씩 흡수하고 있었다.

만약 내 신호가 떨어진다면, 지금 이 순간에도 지껄이고 있는 도플갱어의 목을 쳐 날릴 수 있도록.

“몬스터라. 그래, 그랬지. 근 수십 년 동안은 하도 인간들이랑 어울려서 그런지, 가끔 헷갈릴 때가 있었단 말이야.”

턱을 긁적이던 도플갱어가 말을 이었다.

“하지만 어떤 상황에서도 한 가지는 잊지 않았지. 바로 이곳. 이곳에서 들었던 주인님의 명령.”

나도 모르게 잠시 멈칫했다.

도플갱어의 주인.

놈이 미카엘 실베르트를 허수아비로 내세웠듯이, 도플갱어를 이 세상에 뿌리내리게 한 바로 그 존재.

“설마…….”

흐려지는 말꼬리.

문득 차오른 의문에 가슴이 울렁였다.

그리고 그런 내 마음을 단번에 눈치챈 것처럼, 도플갱어의 입꼬리가 부드럽게 올라갔다.

“지금 누굴 생각하고 있는지, 내가 한번 맞춰 볼까?”

그 미소에, 가슴 한구석이 덜컥 가라앉는 것은 어째서일까.

나는 애써 담담하게 대답했다.

“아가리 닥쳐.”

“왜, 궁금해하지 않았나?”

“누구든 상관없어. 만에 하나…….”

마치 모래알을 한 움큼 집어삼킨 것처럼, 입 안이 꺼끌거린다.

호흡을 가다듬은 나는 갈라진 목소리로 말을 이었다.

“네 주인이 마왕 아스모데우스라고 해도.”

“……!”

공기가 흔들린다. 스켈레톤 킹의 동요가 여기까지 느껴진다.

마왕(魔王).

인간 중 누구도 닿지 못한 죽음의 땅, 마계의 주인이자 몬스터들의 군주.

마왕 아스모데우스는 인류에게 있어 화인(禍因)과도 같은 존재인 동시에, 재앙 그 자체로 각인된 존재다.

놈의 등장으로 인류의 역사가 바뀌었고, 문명이 뒤집혔으며, 수많은 이들이 소중한 사람을 잃어야 했다.

바로 나처럼.

‘아버지.’

그리운 얼굴이 눈앞을 스친다. 우리 가족에게 들이닥친 불행은 찰나였지만, 슬픔과 그리움은 영원했다.

어쩌면 그 때문일지도 모른다.

어느 때보다 냉정해야 할 지금, 가슴 깊숙한 곳에서 뜨거운 무언가가 끓어오르는 이유는.

눈앞에서 웃고 있는 저놈의 아가리를 찢어 버리고 싶으면서도, 동시에 대답을 원하는 이율배반적인 이 충동은.

우득.

어느새 한껏 힘이 들어간 손아귀가 새하얗게 물들었다.

나는 도플갱어를 노려보며 입을 열었다. 아니, 스스로 다짐하듯 중얼거렸다.

“놈은, 마왕은 이미 죽었어.”

그리고 그 순간.

똑똑히 볼 수 있었다.

더욱 짙어지는 도플갱어의 미소를. 뒤이어 되묻는 목소리에 담긴, 받아들일 수 없는 진실을.

“정말 그렇게 생각하나?”

“……!”
```

## Final English reading copy

```markdown
# Chapter 826

That’s how humans are.

There are billions of people, and each one sees and understands the world by their own standards, by their own common sense.

And it’s only when they witness something they can’t easily accept by their own measure that they feel shock.

Of course, I’m no exception.

Even after I suddenly began moving between two worlds one day, even after I made it this far with the unbelievable power called the System, that hadn’t changed.

I’d always been honest about my feelings, and sometimes I got so caught up in them that I even forgot what I was supposed to do.

Like right now.

*What… is that?*

One question brought every thought in my mind to a halt.

I stared, stunned, at the sight unfolding before me.

No. I wasn’t the only one.

“What the hell is this?”

Even the Skeleton King, who’d been about to attack the Doppelganger again, muttered blankly.

The golden magical power that had brilliantly colored the Hero’s Sword had long since faded.

We felt the tremendous force flowing out from the Doppelganger, and at the same time, heard a rumbling rise from deep beneath the ruins at our feet.

*Rumble. Rumble-rumble.*

*This is…*

The sensation was familiar. But this rumbling wasn’t just some noisy roar. It was something deeper, more fundamental.

If I had to find the right word, then…

*Resonance.*

Even as the thought occurred to me, I felt like I was talking crazy.

In Murim, a First Rate swordsman could draw out the ringing of a sword. But this was just the earth.

A barren wasteland where not a single tree or weed grew, now a ruin no one visited anymore.

And this land of death, these ruins stretching in every direction, were trembling as if in resonance.

Even after thinking it over, it still sounded crazy.

If not for a thought that flashed through my mind like lightning, I might have stood there for a long time, stalled by this unanswered question.

But, as always, the answer was closer than I thought.

“Magic.”

The moment that one word slipped from my lips, almost like a groan—

*Boom!*

The ruins, which had been giving off a deep rumble like a heartbeat, rippled. At the same time, a dazzling mass of light burst out, coloring everything around us.

*Fwoooosh!*

A flash brighter than anything I’d ever seen—not even the Teleport spell I’d experienced earlier came close.

I closed my eyes without hesitation and bent my body at an angle. The spear shaft, gripped tightly in my hand, quivered.

*It’s coming. It has to be.*

An instinct carved deep into my bones long ago moved my exhausted body.

I was fully prepared to evade the Doppelganger’s imminent attack and counter its ambush.

My body and mind felt as heavy as waterlogged cotton.

But even if I was the one who died in this clash, I was certain the Doppelganger wouldn’t get away unscathed.

*One Strike.*

Whoever fell, it would be decided in a single move.

I couldn’t see him right now, but the Skeleton King was probably waiting for it with the same resolve.

*Come on.*

I steadied my breathing and drew my senses up as high as I could.

My eyes were shut tight. But through my sharp five senses, I could feel the air trembling and smell the earth of the dead ruins.

The dazzling flash seeping through my thin eyelids, brushing against my retinas before slowly fading, was no exception.

*The light… faded?*

It was only natural that the first question to come to mind was why.

That moment had been perfect for the Doppelganger. The ideal chance.

But there wasn’t even a hint of the ambush I’d expected. All that reached my ears was a voice I’d grown familiar with.

“You’re more timid than you look, Chosen One.”

I bit my lip.

Was that meant to be a trap, or had it simply let its guard down?

But I only hesitated for an instant. The choice left to me was clear.

I slowly opened my eyes. In my sharpened vision, I saw the Doppelganger staring at me.

No—the whole world around me had changed completely.

“……!”

“……!”

Over the Doppelganger’s shoulder, I saw the Skeleton King, eyes wide open.

Or maybe I had the same expression on my face.

That’s how unthinkable the sight before me was.

“This is…”

“What do you think? Impressive, isn’t it?”

The Doppelganger snatched the end of the Skeleton King’s sentence and swept both arms out in an exaggerated gesture.

A ball of light rose and floated at the Doppelganger’s fingertips, illuminating the ruins—or rather, the space that had been “ruins” only moments ago.

“Consider it an honor. You’re the first guests in this marvelous temple.”

The Doppelganger’s words were half lie and half truth.

This place certainly had enough to it to be called a temple, but “grotesque” suited it far better than “marvelous.”

Naturally.

Everything in sight was grand and immense, as if modeled after a temple from mythology. But rotten plant roots coiled around its towering pillars, and the ceiling blocking the sky let in not a single ray of sunlight.

For a moment, I thought this temple resembled the Doppelganger.

It had copied mythology’s outer shell convincingly enough, but inside, everything was rotten and dead.

The only thing that seemed remotely like the myths was the enormous stone statues of monsters, packed tightly into this vast space, hundreds of meters across.

“It’s a masterpiece, don’t you think?”

Instead of answering, I stared calmly at the Doppelganger.

Its attitude was unmistakably different from a moment ago.

And the instinct I’d developed from facing countless enemies told me that its relaxed demeanor wasn’t carelessness.

*Composure.*

No doubt about it. The Doppelganger had regained the composure it had briefly lost.

But that wasn’t just because a new arm had grown where one shoulder had been empty, or because a temple filled with monster statues had appeared.

*There was a reason it came here in the first place.*

I thought to myself and quietly spread out my senses.

I could feel an unseen force writhing all around us. At the same time, something Magic Johnson had once mentioned about Siegfried Bassman casually drifted into my mind.

*“Bassman was a great Grand Mage. He wasn’t a War Mage on my level, but he was more scholarly than anyone, and especially skilled at using magic circles.”*

I already knew that.

And I was certain the Doppelganger, which had spent a long time absorbing countless souls and gaining experience, had become even stronger than the Grand Mage had been in life.

*Three years.*

A strange amount of time—long if you thought of it as long, short if you thought of it as short.

But it had been enough for the Doppelganger, after taking the Grand Mage’s power and soul, to complete various preparations.

“Hey.”

The Doppelganger, staring at me, suddenly clicked its tongue.

“When someone asks you a question, you should answer.”

*Vwoom.*

A low hum reverberated with its emphatic words.

I exchanged a glance with the Skeleton King for an instant, then spoke.

“Are you an idiot? I’m not answering because you’re not a person—you’re a piece of shit.”

“Hmm. You have no respect for your elders. Siegfried Bassman would be a well-respected hero in this world.”

“That’s right. If you mean the Grand Mage I know. But…”

I lowered the spearhead and continued:

“A monster like you doesn’t count, you bastard.”

I had no idea what Siegfried Bassman had been like in life. I’d never seen him or met him. I only knew him from textbooks and what people around me had said.

But it still pissed me off to listen to the taunts of a bastard wearing someone else’s shell.

Of course, I was openly showing my hostility now because it was one of the reactions the Doppelganger would consider natural.

*Just a little longer. Just a little.*

I’d lowered the spearhead I’d been aiming at the Doppelganger, but the other spear I held in my heart was still pointed at it.

I slowly gathered the energy in the air.

Quietly and carefully, so my opponent wouldn’t notice.

It was one of the principles I’d learned this time, after gaining some understanding of the Middle Dantian’s uses.

*I used too much power before I could recover from the effects of the Teleport spell. I need a little time.*

The same was true of the Skeleton King. But since he was already dead, he was actually in a better state than I was, and was slowly absorbing the magical power scattered through the air.

So that when my signal came, he could strike off the Doppelganger’s head—even as it kept running its mouth.

“Monster. Right, that’s what I am. I’ve spent so many decades among humans that I sometimes forget.”

The Doppelganger scratched its chin and continued.

“But there was one thing I never forgot, no matter the circumstances. This place. The command I heard from my master here.”

I paused without meaning to.

The Doppelganger’s master.

The very being who had sunk the Doppelganger’s roots into this world, just as it had used Michael Silbert as a puppet.

“Don’t tell me…”

My voice trailed off.

A question that had suddenly risen in my mind made my chest churn.

And as if it had seen right through me, the Doppelganger’s lips curved into a gentle smile.

“Want me to guess who you’re thinking of?”

Why did my heart sink at the sight of that smile?

I answered as calmly as I could.

“Shut your mouth.”

“What? Weren’t you curious?”

“It doesn’t matter who it is. Even if…”

It felt like I’d swallowed a handful of sand. My mouth was gritty.

I steadied my breathing and continued in a hoarse voice.

“Even if your master is the Demon King Asmodeus.”

“……!”

The air trembled. I could feel the Skeleton King’s agitation from here.

The Demon King.

The master of the Demon Realm, the land of death no human had ever reached, and the ruler of monsters.

To humanity, the Demon King Asmodeus was both a source of calamity and calamity itself.

His appearance changed human history. Civilization was overturned, and countless people lost those they held dear.

Just like me.

*Father.*

A beloved face flashed before my eyes. The misfortune that struck my family had lasted only an instant, but the sorrow and longing lasted forever.

Maybe that was why.

Maybe that was why something hot was boiling deep in my chest, even now, when I had to be calmer than ever.

This contradictory urge—to tear apart the mouth of the bastard grinning in front of me, and at the same time demand an answer.

*Crack.*

My hand had clenched so hard that it had turned stark white.

I glared at the Doppelganger and opened my mouth. No—muttered as if making a vow to myself.

“He—the Demon King—is already dead.”

And at that very moment,

I saw it clearly.

The Doppelganger’s smile deepening. Then the truth I couldn’t accept, in the voice that asked me:

“Do you really think so?”

“……!”
```
