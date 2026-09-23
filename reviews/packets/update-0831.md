<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0831.txt",
      "sha256": "bde8ce5a45c74f5ae3f311f05c230a31fd6c6999d7dffa7ca1a4d048b27ac077",
      "bytes": 13219
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b056b9e76b2226ec9361cb0af6bc8e03de9f28a7e008dceeac71f3548eacae6c",
      "bytes": 1626
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3c3b9627e7353c69a66f8e10657ef055c79a30700111295e071d564e07f7e0ae",
      "bytes": 226707
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "b580259234dfd50ffa04ba91ca8b453bbff39e76f54f0989ddbe305774c9f9e5",
      "bytes": 900
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "21ea24cc51928413a96b86c8b4e996d0785e54dc7b9ded76e65166e79527e68b",
      "bytes": 251052
    }
  ],
  "estimated_tokens": 8591
}
-->

# Durable State Update — Chapter 831

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
1 and safe_through 831. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 831. Profile updates may replace only one
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
  "chapter": 831,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 831,
    "continuity_sources": [831],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate the Doppelganger known as the Prophet.",
    "The Doppelganger is the last surviving member of its species and can absorb appearances, abilities, and memories; it is now a Level 10 shadow.",
    "The Doppelganger claims to have served Demon King Asmodeus and received his order to infiltrate humanity before Asmodeus fell.",
    "The Doppelganger claims Asmodeus overcame the gods’ curse and will return to claim the earth and water.",
    "Jin believes Asmodeus died on Victory Day, the day Jin was born, but cannot determine whether the Doppelganger’s claims are true.",
    "Jin’s vision depicts a future devastated by monsters, a memorial and final stand led in his name, and Asmodeus appearing before the Hunters; its reliability is unknown."
  ],
  "continuity_sources": [
    829,
    830
  ],
  "open_questions": [
    "Is Demon King Asmodeus truly dead, and will he return?",
    "Are the Doppelganger’s claims about Asmodeus true?",
    "What caused Jin’s vision, and does it depict a future that can be prevented?"
  ],
  "safe_through": 830,
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

| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 헌터      | **Hunter**            |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 평화 | **Peace Guild** | Guild name. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 830
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a Demon Realm being that can regenerate in new bodies by consuming its stored lives and is now reduced to a Level 10 shadow.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

## Korean source

```text
＃831화



분명, 그런 소리를 들었던 것 같다.

콰창.

마치 유리창이 깨지는 듯한 소리.

그것은 내 주위를 둘러싼 허상을 벗어나 현실로 돌아갈 때가 되었다는 신호였고, 깊이 잠들어 있던 정신을 일깨우는 알람이었다.

화아악.

주위의 풍경이 아이스크림처럼 빠르게 녹아내린다. 또렷하게 들리던 함성이 메아리처럼 멀게만 느껴졌다.

- 돌겨억!

이 대전쟁의 마지막, 어쩌면 인류의 운명이 걸렸을 최후의 전투.

영웅의 검을 높게 치켜든 채 앞으로 나선 최 팀장과 그 뒤를 따르는 무수한 헌터들이 물결처럼 나아가고 있었다.

달빛조차 닿지 않는 저 어딘가를 향해.

그곳에 홀로 우뚝 선, 짙은 어둠을 망토처럼 두른 한 존재를 향해.

‘안 돼.’

아직은. 아직은 안 된다.

나는 안간힘을 다해 손을 뻗었다. 뿌옇게 흐려지는 시야 속에서, 오롯이 내 것이 된 몸뚱어리를 움직여 놈을 향해 걸음을 뗐다.

마왕 아스모데우스.

거대하지도, 흉측하지도 않은 재앙의 뒷모습이 보인다.

비록 이 모든 것이 이루어지지 않을 허상이라 해도, 누구에게도 듣지 못했던 그 실체를 두 눈으로 똑똑히 확인하고 싶었다.

짙은 어둠에 파묻혀 보이지 않는 놈의 모습을, 그 안에 웅크린 힘을 잠시나마 느끼고 싶었다.

‘더. 조금만 더!’

모르겠다.

마음속에서 울려 퍼지는 내 간절한 외침이 닿았던 것인지. 아니면 지금 내가 보고 느낀 이 모든 게 허상이 아닌 또 다른 무언가인지.

다만 한 가지 확신할 수 있는 것은, 어떤 소리도 없었던 내 외침에 어떤 존재가 반응했다는 것뿐이었다.

스륵.

천천히 돌아서는 신형. 넘실거리는 어둠.

“……!”

가슴이 덜컥 내려앉는다. 얼음장처럼 차가운 한기가 등골을 타고 흘렀다.

말도 안 된다. 있을 수 없는 일이다.

하지만 마왕은 분명 나를 향해 돌아서고 있었고, 그것이 곧 내가 본 마지막 장면이 되었다.

파앗.

주위를 둘러싼 모든 것이 사라졌다. 최 팀장과 샤오 쉔, 수많은 헌터들. 그리고 마왕 아스모데우스까지.

그러나 어둠은 사라지지 않았다.

아니, 오히려 심연(深淵)과도 같은 기운이 사방을 옥죄며 다가오고 있었다.

‘이게 도대체…….’

혼란스러웠다. 분간할 수조차 없었다.

지금 내가 보고 있는 광경이 또 다른 허상인지. 아니면 이미 한계에 달해 있던 내가 의식을 잃고 꿈을 꾸고 있는 것인지.

그리고 의문에 사로잡힌 그 순간.

띠링.



- 당신은 선택받은 자. 방주의 주인.

- [시스템]이 자동으로 방화벽을 실행합니다.

- [시스템]이 새롭게 감지된 바이러스를 차단합니다.

- [심연의 늪]이 해제되었습니다.

- [심연의 힘]이 흩어집니다.

- [Lv.10 “최후의 심연” 도플갱어]가 차단되었습니다.



띠링. 띠링. 띠링.

맑은 종소리가 귓가에 닿았다. 사방으로 울려 퍼졌다.

그와 동시에 마치 살아 있는 뱀처럼 꿈틀거리며 나를 향해 다가오던 어둠이 빠르게 흩어졌다.

두려운 무언가를 마주한 듯이, 거칠게 몸서리치며.

그리고 나는 이 심연의 정체를 깨달았다.

갑작스럽게 내게 들이닥친 그 수많은 허상을 불러온 존재도.

‘도플갱어.’

문득 어디선가 읽었던 글귀가 떠오른다.

당신이 심연을 바라볼 때, 심연도 당신을 바라본다.

그 짧은 문장이 말하고자 하는 바는 달랐으나 내게 벌어진 일이 그와 같았다.

나는 도플갱어를 바라보았고, 도플갱어는 나를 바라보았다. 그렇게 나는 놈이 만들어 낸 심연 속으로 끌려 들어갔다.

아니, 그랬었다.

하지만 이제는 안다.

이것이 현실 속의 또 다른 허상이라는 것을. 도플갱어가 지닌 권능 그 자체라는 것을.

그리고 내가 무엇을 해야 하는지도.

화륵.

텅 비어 있던 두 손에서 솟구치는 열기. 눈부시게 타오르는 청백색의 화염에 어둠이 몸부림친다.

나는 아주 오래전부터 그렇게 하기로 마음먹었던 사람처럼, 열양지기로 타오르는 손을 뻗어 어둠을 움켜쥐었다.

콰득.

동시에 힘주어 찢어발긴 순간.

촤아아악!

나는 보았다.

화염에 의해 잿더미가 된 어둠이 힘없이 스러지는 모습을. 그 너머로 내가 기억하는 세상이 나타나는 광경을.

후욱.

먼지가 뒤섞인 공기가 코와 입을 통해 흘러들어 온다.

허공에서 잠시 멈춰 있던 돌 부스러기가 다시 떨어져 내리고, 눈을 부릅뜬 채 나를 바라보는 스켈레톤 킹이 시야에 들어왔다.

‘모든 것이 찰나였어.’

현실에서는 1초 남짓한 시간이나 흘렀을까.

하지만 나는 최소 몇 시간 동안, 수년간의 허상을 경험하고 돌아왔다.

아마도 나와 같은 일을 겪은 이들 중 살아남은 자는 없을 것이다. 모두 도플갱어에 의해 흡수당했을 테니까.

“이게 무슨…….”

말로는 쉽게 설명할 수도 없는 일이고, 설명할 시간도 없다.

나는 혼란스러워하는 스켈레톤 킹에게 대답 대신 고개를 저어 보였다.

그리고 녀석을 뒤로 한 채, 넋 나간 시선으로 나를 올려다보는 도플갱어와 마주했다.

- 넌, 너는 도대체…….

스르륵.

그림자처럼 일렁이는 몸뚱어리가 조금씩, 동시에 계속해서 흩어진다.

앞서 내가 화염이 깃든 두 손으로 찢어 낸 것은 단순한 허상이 아닌 놈의 몸뚱어리였고, 생명 그 자체였다.

“마지막 발악, 잘 봤다.”

- ……!

“그래, 아까부터 왕왕거리면서 열심히 짖어 대던 개새끼가 너무 쉽게 협조한다 싶었지.”

툭 던지듯 건넨 한마디에 도플갱어가 부르르 몸을 떨었다.

마치 핏물처럼 울컥거리며 샘솟는 어둠이 잿가루처럼 흩어질 때마다, 놈의 육신이라 할 수 있는 그림자가 줄어들고 있었다.

“솔직히 시도는 괜찮았어. 평소 몸 상태 같았으면 애초에 어림도 없었겠지만…… 어떤 시벌놈이 깜빡이도 안 켜고 훅 들어올 줄은 몰랐거든.”

- 이럴 수는, 이럴 수는 없어.

“너 같은 새끼도 있는데, 나 같은 새끼라고 없을 건 또 뭐냐.”

도플갱어가 신음처럼 뇌까렸다.

- 선택받은 자…….

선택받은 자. 방주의 주인.

왜 도플갱어와 시스템이 나를 이렇게 부르는지는 모르겠다.

누가 나를 선택했는지도, 방주가 무엇인지도 지금 당장은 알 수 없다.

하지만 나를 지칭하는 저 두 개의 단어가 단순한 헛소리가 아니라면, 도플갱어가 보여 준 그 좆 같은 광경을 막는 것이 내게 주어진 사명이리라는 것쯤은 안다.

- 각오해라. 네가 본 그 모든 광경이 곧 미래이자 현실이 될 테니.

“확실해? 내가 천재는 맞지만, 딱히 요절할 생각은 없어서.”

내 대답을 들은 도플갱어가 소리 내어 웃었다. 이미 완전한 소멸을 받아들인 놈에게서 숨길 수 없는 허탈함과 광기가 묻어났다.

- 왕께서 돌아오신다면, 그때에도 네놈이 같은 말을 할 수 있을까.

나는 문득 허상에서 봤던 그 짙은 어둠을 떠올렸다.

끝끝내 확인하지 못한 채로 떠나보내야 했던 마왕 아스모데우스의 마지막 모습을, 단지 멀리서 보는 것만으로도 전해지던 강대함을 떠올렸다.

‘만약 놈과 맞붙는다면, 과연 내가 승리할 수 있을까.’

공허한 질문이다.

그 물음에 대한 답은 이미 스스로도 알고 있으니까.

마왕 아스모데우스는 강하다. 아니, 강함을 논하는 것 자체가 무의미한 존재다.

허상이 아닌 현실이었다면, 내가 느낀 그 힘이 진정 사실이라면 시선이 마주치는 것만으로도 손발이 굳고 얼어붙었을 것이다.

그러나 때로는 어떤 문제에 대한 답이, 하나가 아닌 여러 개가 되고는 한다.

그 문제를 푸는 사람이 바로 나라면 더더욱.

“지금의 나라면 틀림없이 죽겠지. 제대로 된 상처도 못 입히고 처참하게.”

내 대답을 들은 도플갱어의 웃음소리가 커졌다. 이미 절반도 넘게 사라진 제 몸뚱어리 따위는 신경도 쓰지 않는다는 듯이.

- 그래, 그것이 진실이다. 왕께서 내리신 죽음을 받아들이는 것만이 네놈이 할 수 있는 전부…….

“전제(前提)를 빼먹으면 안 되지.”

- 뭐?

말을 멈춘 도플갱어를 바라보며, 나는 천천히 말을 이었다.

“지금의 나라면. 그게 가장 중요한 전제야.”

어느 날부터인가 나는 바뀌었다. 살아남기 위해, 지키기 위해 바뀔 수밖에 없었다.

F급 헌터로 살아오며 간직했던 조심성을 내던졌고, 때로는 과감하고 그 이상으로 무모하게 적과 맞섰다.

그리고 내가 목숨을 건 싸움을 치를 때마다 위험에 대한 대가를 톡톡히 얻어 냈다.

‘지금까지 그래 왔고, 앞으로도 마찬가지겠지.’

지금의 나와 훗날의 나는 다르다.

그러니 미래 역시 바뀔 수밖에 없다. 어떤 위험을 치르더라도, 설령 죽는 한이 있더라도 반드시 내 힘으로 변화시킬 것이다.

그것이 내가 할 수 있는 전부이며, 알 수 없는 누군가가 나를 선택한 이유일 테니까.

“허상은 그저 허상일 뿐이야. 미래가 어떻게 바뀔지는 두고 봐야 알겠지만…… 당장 뒈질 것 같은 어떤 새끼는 이미 세상에 없을 테니 알 바 아니고.”

중단전을 움직이는 것은 심력(心力)이며, 심력은 곧 마음의 굳건함.

나는 끔찍한 허상 따위에, 도플갱어가 지껄이는 말 몇 마디 정도로 흔들리지 않는다.

“그리고 중요한 걸 잊었나 본데.”

피곤하다. 당장이라도 쓰러질 것 같다.

하지만 어느새 딱딱하게 굳어 있는 도플갱어를 얼굴을 내려다보며 이 말은 꼭 해 주고 싶었다.

“그 미래는 이미 바뀌었어.”

나는 핏물에 굳은 입꼬리를 끌어당겼다. 쏟아지는 졸음을 견뎌 내며 말을 이었다.

“네가 세웠던 계획을, 내 손으로 끝장냈으니까.”

도플갱어가 정확히 어떤 방식으로 어떤 결과를 얻고자 했는지는 모른다.

놈을 통해 직접 전해 듣고 싶었지만, 불과 몇 초 후면 완전히 소멸할 테니 이제 와서 물어봤자 헛수고일 것이다.

그러나 전부 알아내면 그만이다.

전 세계를 샅샅이 뒤져서라도 도플갱어의 흔적을 좇고, 놈이 어딘가에 남겨두었을 잔뿌리들을 뽑아내면 허상은 허상으로 남을 것이다.

끔찍한 재앙으로 가득하던 미래에는 평화가 깃들 것이다.

‘할 수 있다.’

이건 단순한 바람이 아닌, 확신이다.

마침내 세계가 하나로 모였다. 나는 평화에 취해 방심하고 있던 이들에게 경종(警鐘) 울렸고, 현실을 외면하고 있던 권력자들의 면전에 찬물을 쏟아부었다.

그리고 인류의 검과 방패라 불리는 이들을, 수많은 헌터들을 하나의 깃발 아래에 세웠다.

세계 헌터 연맹.

성별과 인종. 나이와 국경을 초월한 집단.

나는 그 거대한 연맹의 정점에 선 맹주(盟主)다.

모두가 나를 추대했고, 모두가 나를 믿고 따른다. 그렇기에 불가능이라는 단어는 마음속 어디에도 존재하지 않는다.

“그러니까…….”

힘을 잃은 말꼬리가 길게 늘어진다.

의지와는 반대로 천천히 기울어지는 시야 속, 아무런 말도 없이 불현듯 다가온 스켈레톤 킹이 팔을 뻗어 나를 부축했다.

아직 끝맺지 못한 말을 이어 나가도록 도왔다.

“더 이상 개지랄 떨지 말고, 먼저 떠난 네 친구 새끼랑 어깨동무하고 구경이나 해.”

후웅.

묵직한 파공성과 함께 힘차게 내리찍은 발끝.

그리고 그 순간. 문득 흐릿한 시야에 잡힌 알 수 없는 광경.

‘웃……어?’

나로서는 도무지 알 수 없었다.

놈이 웃었다고 느낀 것이 피로가 불러온 허상이었는지. 아니면 이해할 수 없는 현실이었는지.

그리고 그 찰나의 의문을 미처 되짚어 보기도 전에, 이미 미약한 화염이 깃든 발끝이 그림자를 짓밟았다. 아득한 세월을 살아왔던 괴물을 소멸로 이끌었다.

쾅!

굉음과 함께 산산이 부서져 흩어지는 그림자. 그 사이로 울려 퍼지는, 도플갱어의 소멸을 알리는 맑은 종소리.

띠링.

끝났다. 마침내.

적어도 그 순간만큼은, 분명 그렇게 생각했다.

곧이어 귓가를 파고든, 불쾌한 소음을 듣기 전까지는.

삐빅.



- 메인 퀘스트, [격변]이 실패했습니다!



……뭐라고?
```

## Final English reading copy

```markdown
# Chapter 831

I could’ve sworn I heard something like that.

*CRASH.*

The sound of a window shattering.

It was a signal that it was time to shed the illusion surrounding me and return to reality. An alarm waking my mind from its deep slumber.

*Fwoosh.*

The scenery around me melted away like ice cream. The cheers that had sounded so clear now seemed distant, like echoes.

“Chaaaarge!”

The final battle of this Great War. Perhaps the final battle on which humanity’s fate would rest.

Team Leader Choi strode forward, Hero’s Sword held high, and countless Hunters followed behind him like a surging wave.

Toward somewhere the moonlight couldn’t reach.

Toward a being standing alone, cloaked in darkness.

*No.*

Not yet. Not yet.

I reached out with all my strength. Through my blurring vision, I moved the body that had become entirely my own and took a step toward him.

Demon King Asmodeus.

I could see the back of the calamity. It wasn’t enormous or grotesque.

Even if all of this was an illusion that would never come to pass, I wanted to see his true form with my own eyes—the form no one had ever told me about.

I wanted to catch even a glimpse of him buried in the deep darkness, to feel the power coiled within him, if only for a moment.

*More. Just a little more!*

I didn’t know.

Maybe my desperate cry had echoed in my heart and reached him. Or maybe everything I was seeing and feeling wasn’t an illusion after all, but something else.

There was only one thing I could be sure of: something had reacted to my silent cry.

*Rustle.*

A figure slowly turning around. Darkness rippling.

“……!”

My heart lurched. An icy chill ran down my spine.

It made no sense. It was impossible.

But the Demon King was definitely turning toward me—and that was the last thing I saw.

*Flash.*

Everything around me disappeared. Team Leader Choi and Xiao Shen, the countless Hunters. And even Demon King Asmodeus.

But the darkness did not disappear.

No—an abyss-like presence was closing in, pressing in on me from every direction.

*What the hell is this…*

I was confused. I couldn’t make sense of anything.

Was what I was seeing another illusion? Or had I finally reached my limit, lost consciousness, and started dreaming?

And just as I was gripped by those questions—

*Ding.*

> **System**
> You are the Chosen One. The Master of the Ark.
>
> The System automatically activates its firewall.
>
> The System blocks a newly detected virus.
>
> Abyssal Swamp has been dispelled.
>
> Power of the Abyss dissipates.
>
> Level 10 “Final Abyss” Doppelganger has been blocked.

*Ding. Ding. Ding.*

Clear chimes reached my ears. Their sound rang out in every direction.

At the same time, the darkness that had writhed toward me like a living snake scattered rapidly.

It thrashed violently, as if confronted by something it feared.

And then I realized what this abyss was.

The being that had conjured all those countless illusions that came crashing down on me, too.

*Doppelganger.*

A line I’d read somewhere suddenly came to mind.

When you look into the abyss, the abyss looks back at you.

The short sentence meant something else, but what had happened to me was the same.

I looked at the Doppelganger, and the Doppelganger looked at me. And so I was dragged into the abyss it had created.

No. I had been.

But now I knew.

This was another illusion within reality. The Doppelganger’s power itself.

And I knew what I had to do.

*Fwoosh.*

Heat surged from my empty hands. Darkness writhed against the dazzling blue-white flames.

As if I’d made up my mind to do this long ago, I reached out with hands blazing with Scorching Yang Qi and seized the darkness.

*CRUNCH.*

And the instant I gathered my strength and tore it apart—

*SHRAAAK!*

I saw it.

The darkness, reduced to ash by the flames, crumbled away without a fight. Beyond it, the world I remembered came into view.

*Huff.*

Air mixed with dust flowed through my nose and mouth.

The chunks of stone that had hung in midair began to fall again. The Skeleton King came into view, staring at me with wide eyes.

*It all happened in an instant.*

Had even a second passed in reality?

But I’d experienced at least several hours—years’ worth of illusions—and returned.

There probably wasn’t a single survivor among those who’d gone through what I had. They must all have been absorbed by the Doppelganger.

“What the…”

It was impossible to explain in a few words, and there was no time to explain.

Instead of answering the confused Skeleton King, I shook my head.

Then I turned away from him and faced the Doppelganger, who was staring up at me, dazed.

“You—you… What are you…?”

*Rustle.*

Its body, wavering like a shadow, was slowly scattering—bit by bit, without pause.

What I’d torn apart with my flame-filled hands wasn’t just an illusion. It was the Doppelganger’s body, its very life.

“I got a good look at your last-ditch effort.”

“……!”

“Yeah. I figured there had to be some reason that dog barking its head off this whole time was cooperating so easily.”

At my offhand remark, the Doppelganger shuddered.

Whenever darkness welled up from it in bursts, like spurting blood, and scattered like ash, the shadow that was its body shrank.

“Honestly, it wasn’t a bad attempt. If I’d been in my usual shape, you wouldn’t have stood a chance, but… I didn’t expect some bastard to come flying in without even signaling.”

“This can’t… This can’t be happening.”

“If a bastard like you can exist, why can’t a bastard like me?”

The Doppelganger muttered as if groaning.

“The Chosen One…”

The Chosen One. The Master of the Ark.

I didn’t know why the Doppelganger and the System called me that.

I didn’t know who had chosen me, or what the Ark was. I couldn’t know that right now.

But if those two words referring to me weren’t just nonsense, then I knew at least this much: stopping that fucked-up scene the Doppelganger had shown me must be the mission I’d been given.

“Be prepared. Everything you saw will soon become the future—and reality.”

“Are you sure? I may be a genius, but I’m not exactly planning to die young.”

The Doppelganger laughed out loud at my reply. Its helplessness and madness were impossible to hide now that it had accepted its complete Erasure.

“If the King returns, will you still be able to say the same thing?”

I thought of the deep darkness I’d seen in the illusion.

I thought of that last glimpse of Demon King Asmodeus, whose appearance I’d never managed to make out clearly. I thought of the overwhelming strength I’d felt from him, even from a distance.

*If I fought him, could I really win?*

An empty question.

I already knew the answer.

Demon King Asmodeus was strong. No—there was no point even talking about how strong he was.

If that had been reality, and the power I’d felt was real, just meeting his gaze would’ve frozen my hands and feet.

But sometimes, a question can have more than one answer.

Especially when I’m the one solving it.

“If it were me right now, I’d definitely die. Miserably, without even managing to hurt him properly.”

At my answer, the Doppelganger’s laughter grew louder. It didn’t seem to care that more than half of its body had already disappeared.

“Yes. That is the truth. Accepting the death our King has decreed is all you can do…”

“You’re leaving out a premise.”

“What?”

I looked at the Doppelganger as it fell silent and continued slowly.

“If it were me right now. That’s the most important premise.”

At some point, I’d changed. I’d had no choice but to change in order to survive, in order to protect what mattered.

I’d thrown away the caution I’d held on to as an F-rank Hunter. Sometimes I’d faced my enemies with courage—and with even more recklessness.

And every time I risked my life in a fight, I’d reaped the rewards of that risk.

*That’s how it’s been so far, and that’s how it’ll keep being.*

The me of now and the me of the future are different.

So the future has to change, too. Whatever risks I have to take—even if it costs me my life—I’ll change it with my own power.

That’s all I can do. And it must be why some unknown someone chose me.

“An illusion is just an illusion. We’ll have to wait and see how the future changes… but some bastard who’s about to drop dead won’t be around to find out, so it’s none of his business.”

The Middle Dantian is moved by mental strength, and mental strength comes from the firmness of one’s heart.

I won’t be shaken by a horrible illusion, or by a few words from the Doppelganger.

“And you seem to have forgotten something important.”

I was tired. I felt like I could collapse at any moment.

But as I looked down at the Doppelganger, which had stiffened, I wanted to make sure I said this.

“The future’s already changed.”

I tugged at the corner of my mouth, stiff with dried blood. Then I forced the words out, fighting the sleepiness washing over me.

“I put an end to the plan you came up with. With my own hands.”

I didn’t know exactly how the Doppelganger had planned to get the results it wanted.

I’d wanted to hear it directly from the thing itself, but it would be completely gone in a few seconds. There was no point asking now.

I could find everything out.

Even if I had to scour the whole world, I’d track down every trace of the Doppelganger and pull up every root it had left behind somewhere. Then the illusion would remain an illusion.

The future, once filled with horrible calamities, would be filled with peace.

*I can do it.*

This wasn’t just a wish. I was certain.

At long last, the world had come together as one. I’d sounded the alarm for those who’d been complacent in their peace, and doused the powerful—who’d been turning their backs on reality—with a bucket of cold water.

And I’d brought those known as humanity’s sword and shield, the countless Hunters, together under one flag.

The World Hunter Federation.

A group that transcended gender, race, age, and national borders.

I was the Alliance Leader at the head of that vast federation.

Everyone had chosen me. Everyone trusted and followed me. So there was no room in my heart for the word *impossible*.

“So…”

My voice trailed off, growing weak.

My vision slowly tilted against my will. Without a word, the Skeleton King suddenly came up beside me and reached out to support me.

He helped me finish what I hadn’t yet managed to say.

“Quit your bullshit and go link arms with your friend who went ahead of you. You can watch from there.”

*Whoosh.*

My toe came down hard, with a heavy rush of air.

And in that moment, an inexplicable sight flickered into my hazy vision.

*Was it… smiling?*

I couldn’t possibly know.

Was it a phantom brought on by exhaustion, or an incomprehensible reality?

Before I could even think back over that fleeting question, the toe, still wreathed in a faint flame, had already stamped down on the shadow. It led a monster that had lived through ages beyond imagining to Erasure.

*BOOM!*

The shadow shattered and scattered with a deafening crash. Through it rang the clear chime announcing the Doppelganger’s Erasure.

*Ding.*

It was over. At last.

At least in that moment, I was sure it was.

Until an unpleasant noise pierced my ears.

*Beep.*

> **System**
> Main Quest Cataclysm has failed!

…What did it say?
```
