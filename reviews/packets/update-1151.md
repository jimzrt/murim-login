<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1151.txt",
      "sha256": "a2c0ade846c68e6cc78a735db7b9a7e327c256da71c54a194c1c9fc66e5a7e93",
      "bytes": 11442
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "db7cb0ef3b5ef8562fb7b883e834daaecc9b5a1acfcccb7352d2504f588e3908",
      "bytes": 969
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2b8eaa77ee80729eb8250b7ede77d8e7ec834c0781cdde2940ecd1483e65494c",
      "bytes": 246400
    },
    {
      "path": "characters/Carus.md",
      "sha256": "c63a8949a00aa49d836b0fe63e8d54db84d77089ec1c0919168c98242cd0e34f",
      "bytes": 572
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "bb84133cedf2d53fb1d9bcc15b2ed0d60e04e69e221373795fa0d4836562f0b2",
      "bytes": 760
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "eef02e291e5f6e743e292aeac3cead39935281790b926097781c3f67a302d5ea",
      "bytes": 554
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "086dd0005e1c1a65a8c9b775bfb0a1e4fc134619a76bb15f40ddb6e22d4198e5",
      "bytes": 292572
    }
  ],
  "estimated_tokens": 7686
}
-->

# Durable State Update — Chapter 1151

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
1 and safe_through 1151. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1151. Profile updates may replace only one
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
  "chapter": 1151,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1151,
    "continuity_sources": [1151],
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
    "Morgoth says he once stayed in another world, left for the Demon Realm, and entered another’s service there.",
    "Morgoth describes his devastation and subjugation of humanity as punishment and demands Furin’s surrender.",
    "Furin estimates 50 million casualties from the past ten days; North Africa and West Asia are devastated, resisters are rotting or undead, and survivors are enslaved.",
    "Furin presses a concealed button, triggering a deep rumble beneath the Kremlin."
  ],
  "continuity_sources": [
    1150
  ],
  "open_questions": [
    "What caused the rumble beneath the Kremlin when Furin pressed the concealed button?",
    "Is Morgoth afraid of someone he has not yet found, as Furin suggests?"
  ],
  "safe_through": 1150,
  "temporary_decisions": [
    "Render 크렘린 궁 as “the Kremlin.”",
    "Render 사상자 as “casualties,” without specifying deaths versus injuries."
  ],
  "version": 1
}
```

## Exact glossary matches

| 대주     | **Squad Leader** / **Commander**             |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 대사      | **Master** for a senior Buddhist monk                           |
| 카루스 | **Carus** | Name of the Black Wyvern. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 계인 | **Buddhist precept seals** | Seals carved into the foreheads of Shaolin martial monks. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 브레스 | **Breath** | Dragonkin power used by the Wyverns. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 모스크바 | **Moscow** | Russian city used in Taekyung's modern-world comparison. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Carus.md

# Carus (카루스)

- **Safe through:** Chapter 297
- **Aliases:** One-Eyed
- **Role:** The Black Wyvern's name; a Level 115 Named Monster and lesser branch of the dragonkin with one eye, killed by Jin Taekyung.
- **Personality:** Predatory, vengeful, patient, and increasingly intelligent.
- **Voice:** Initially nonverbal; now halting, hostile speech accompanied by spellcasting.
- **Relationships:** Sought revenge against the human who took his eye and fought Jin Taekyung until Taekyung killed him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1150
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1144
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

## Korean source

```text
＃1151화



이 세상에서 오직 한 사람에게만 허락된 비밀 장치를 작동시킨 그 순간, 블라디미르 푸린은 마음속으로 뇌까렸다.

‘여기까지군.’

삶에 대한 미련이나 두려움?

왜 없겠나.

손에 쥔 것이 많을수록 내려놓기 싫어하는 것이 인간의 본질일 진대, 무려 반세기에 달하는 긴 세월 동안 독재자로 군림해온 그라면 두말할 필요도 없었다.

살고 싶었다.

살아야 했다.

블라디미르 푸린이라는 한 인간의 이름을, 신과 같은 반열에 올려놓아야 했다.

고귀한 혈통으로 대를 이어 이 땅을 지배했던 차르(Tsar)도, 혹은 그 누구도 감히 반항할 엄두를 내지 못했던 강철의 대원수도 따라올 수 없을 만큼 위대하게.

하지만 그것이 불가능하다면.

만약 다른 누군가가 나타나 그가 지금껏 쌓아 올린 모든 것을 빼앗으려 한다면-

‘불태워 버릴 것이다. 내 손으로 직접, 그 누구도 가질 수 없게.’

영원불멸을 꿈꾸던 늙은 독재자는 흐릿하게 웃었다.

정확히는, 웃으려 했다.

주마등처럼 느리게 흘러가는 시간 속, 선명한 미소를 머금고 있는 약탈자의 모습을 발견하기 전까지는.

“역시, 자네는 흥미로운 인간이야.”

“……!”

노회한 눈동자가 부릅떠진 그 순간.

구구구궁.

크렘린 궁을, 아니 모스크바 전체를 집어삼킬 것만 같던 거대한 울림이 가까워졌다.

느리면서도 신중하게.

마치 누군가의 의지에 따라 움직이는 것처럼.

그리고 마침내, 블라디미르 푸린은 이 예상치 못한 현상의 실체를 두 눈으로 직접 확인하게 되었다.

우우우우웅.

수천, 수만 마리의 벌떼가 한데 뒤엉킨다면 이런 소리가 날까.

집무실 바닥을 녹이며 솟아오른 화염의 소용돌이를, 그는 그저 멍하니 바라보았다.

모든 것이 붉었다. 뜨거웠다.

칠흑처럼 어두운 기운에 둘러싸인 채, 커다란 구체(毬體)로 압축된 그것은 마치 작은 태양처럼 이글거리고 있었다.

그리고 이 광경을 아연히 바라보던 늙은 독재자는, 작은 태양이라는 표현이 결코 과장된 것이 아님을 누구보다 잘 알고 있었다.

한때 전 세계를 공포로 몰아넣었을 만큼 거대한 힘이, 자신을 향해 빙긋 웃고 있는 저 괴물의 손아귀에 들어갔다는 사실도.

‘차르 봄바(Tsar Bomba).’

인류 역사상 가장 강력한 무기.

모든 폭탄의 어머니이자 제왕.

냉전 시대 당시, 오대양 육대주를 얼어붙게 만들었던 최강의 수소 폭탄이 크렘린 궁의 지하 깊숙이 잠들어 있었던 것은 극소수의 관련자만이 아는 사실이었다.

독재자의 명령으로 수십년 간 계속된 비밀 실험을 통해, 과거를 아득히 초월하는 파괴력과 새로운 명칭을 갖게 되었다는 것 역시도.

“놀랍군. 정말 놀라워. 이 정도로 강력한 힘을 만들어 내다니. 너희 인간들은 이 무기를 뭐라고 부르지?”

진심으로 경탄하는 모르고스의 물음에, 모든 것이 끝났음을 직감한 푸린이 공허한 목소리로 대답했다.

“블라디미르(Vladimir).”

“뭐?”

이미 몰락한 것이나 다름없는 늙은 독재자와, 그의 성을 딴 재앙의 힘을 번갈아 바라보던 모르고스가 이내 소리 내어 웃었다.

“그것참, 걸작이군. 아니, 자네답다고 해야 하나.”

모르고스에게는 실로 우스운 일이었다.

고작 일백 년 남짓한 시간을 허락받은 인간 주제에 이 정도로 거대한 욕망을 품고 있다는 것도.

그리고 필멸자에 불과한 그들이 만들어 낸 무기로, 불멸에 가까운 권능을 지닌 자신을 죽이려 했다는 것도.

“고작 이 정도로 나를 쓰러트릴 수 있을 거라 생각했나? 하등한 몬스터로부터 얻은 마정석 따위로, 감히 나를?”

이미 모든 것을 간파한 듯한 모르고스의 말에, 푸린은 조용히 숨을 삼켰다.

맞다. 차르 봄바, 아니 블라디미르라는 새로운 이름을 부여받은 저것은 단순한 과학의 산물이 아니었다.

대격변.

전 세계의 상식과 질서를 송두리째 뒤흔들어 버린 대사건 이후, 가까스로 살아남은 독재자의 머릿속에는 한 가지 생각이 자리 잡았다.

‘더욱 강해져야 한다. 두 번 다시 이와 같은 일이 일어나지 않도록. 어떤 전쟁에서도 승리할 수 있도록.’

그리고 방법은 매우 가까운 곳에 있었다.

마법과 마정석. 이를 토대로 탄생한 새로운 지식, 마도 공학.

그렇게 차르 봄바는 블라디미르가 되었다.

전 세계에서 손꼽히는 강대국, 그것도 독재 국가였기에 실험에 쓰일 마정석을 구할 방법은 무궁무진했다.

물론 그 과정에서 헤아릴 수조차 없을 만큼 수많은 국제 조약을 어기고, 기밀 유지를 위해 자국의 과학자와 마법사들마저 죽여야 했지만…… 그게 무슨 상관이란 말인가.

마더 러시아(Mother Russia).

러시아는, 아니 그는 더욱더 위대해져야 했다.

설령 제2의 마왕이 강림한다 하더라도, 그와 러시아만큼은 살아남아 세계의 질서를 새로 써야 했다.

‘혹은, 함께 죽든지.’

그래.

분명, 그래야 했다.

투둑.

덩어리 채로 떨어져 내리는 잿가루.

수십 년간의 금연이 무색하게도, 고작 몇 모금밖에 피우지 못한 시가를 멍하니 바라보던 푸린이 문득 입을 열었다.

“이제 어쩔 셈이지?”

모르고스는 대답하지 않았다.

그러나 부드럽게 올라간 그의 입꼬리에 담긴 뜻을, 푸린은 즉각 알아차렸다.

“그래, 어차피 나와는 상관없는 일이겠군.”

시가가 파르르 떨렸다.

아니, 떨고 있는 것은 푸린 그 자신이었다.

“마지막으로 남길 말이라도 있나?”

모르고스의 친절한 제안에, 푸린은 사시나무처럼 떨리는 손을 들어 시가를 물었다.

그리고 그 어느 때보다 깊게 빨아들인 뒤, 눈앞의 괴물을 향해 뱉어냈다.

“아니, 없다. 하지만 이 말은 꼭 해 줘야겠군.”

자신의 성을 딴 폭탄을 작동시키기 직전, 뇌리에 스쳤던 한 사람의 이름과 함께.

“진(Jin)이 돌아온다면, 네놈도 끝장이야.”

그 순간.

“기대되는군. 진심으로.”

스아아아아.

모르고스의 담담한 대답과 함께, 재앙과도 같은 거대한 힘을 속박하고 있던 칠흑빛 기운이 천천히 흩어져 주인의 몸을 감싸 안았다.

마치, 이 땅의 종말을 고하는 죽음의 손길처럼.

화악.

아득한 섬광이, 늙고 추악한 독재자의 마지막 시야를 뒤덮었다.

따뜻했다.



* * *



길이 8미터. 지름 2미터에 무게는 27톤.

대형 트럭 한 대에 가득 차는 부피에 담긴 위력은, 50Mt(TNT 5천만 톤).

그것이 세간에 알려진 차르 봄바의 수치였다.

세계 2차대전 당시, 히로시마를 죽음의 땅으로 변모시킨 리틀보이(Little Boy)를 이름 그대로 작은 소년으로 만들어 버릴 만큼의 파괴력.

하지만 누구도 예상치 못했다.

냉전 시대의 과시 체제가 낳은 이 구시대의 괴물이, 무려 80여 년이 지난 지금 다시 깨어날 것이라고는.

그리고 오랜 잠에서 깨어난 괴물의 첫 울음소리가, 크렘린궁에서 울려 퍼질 것이라고는.

고오오옹.

일순간, 공기가 떨렸다.

크렘린 궁의, 아니 모스크바의 모두가 그 깊고도 불길한 울림을 느낄 수 있었다.

두려움을 억누른 채 각자의 위치를 지키던 군인과 헌터들도, 붉은 광장이 무너짐과 동시에 방공호와 거리 곳곳으로 뛰쳐나간 시민들도.

그 누구도 예외는 없었다.

모두가 느꼈고, 동시에 본능적으로 깨달았다.

바로 지금이, 그들이 살아 숨 쉴 수 있는 마지막 순간이라는 사실을.

그리고.

화아아악.

빛이 있었다.

인간의 감각으로는 인식조차 할 수 없는 끔찍한 열기가, 무수한 마정석을 바탕으로 한 강력한 기운과 뒤섞인 원자력이 온 사방을 집어삼키며 뻗어 나갔다.

끝없이, 탐욕스럽게.

콰아아아아-!

휘몰아친 힘의 폭풍 속, 모든 것이 녹아내린다.

살아 있는 것은 죽었고 살아 있지 않은 것은 형체를 잃었다.

지하, 지상. 어디에 있건, 어떤 삶을 살았건, 그것은 중요하지 않았다.

크렘린 궁에서부터 뿜어져 나온 아득한 섬광은 모두를 평등하게 만들었다.

태양에 너무 가까이 다가간 이카루스가 날개를 잃고 추락했듯이, 어느 독재자의 욕망과 불안감이 만들어 낸 작은 태양은 그 자신은 물론 무수한 생명을 집어삼켰다.

단 한 존재를 제외한 그들 모두를.

구구구구궁.

온 사방을 뒤흔드는 울림의 중심에서, 모르고스는 고개를 들어 자신이 만들어 낸 풍경을 바라보았다.

없다.

불과 몇 분 전까지만 해도 주위에 존재했던 모든 것이 사라졌다.

녹아내린 쇳물은 강이 되어 흐르고, 그 위로 거대한 버섯구름이 우뚝 솟아올라 죽음의 땅으로 변모한 지상을 굽어보고 있었다.

실로, 장관이었다.

“이 정도의 위력이라니, 브레스(Breath)는 쓸 필요도 없었군.”

모르고스는 감탄과 동시에 안타까움을 느꼈다.

필멸자란 어찌 이리도 탐욕스러우면서도 어리석은 존재란 말인가.

그 덕분에 상당한 수고를 덜었지만, 이미 재앙이 드리워진 그곳은 황량하기 그지없었다.

유구한 역사는 물론 천만이 넘는 인구를 품고 있던 대도시가, 향후 수백 년간 생명이 살아갈 수 없는 죽음의 땅으로 변모한 것이다.

“하지만, 탄생은 죽음 속에서 깨어나는 법이지.”

모르고스가 나직한 음성과 함께 두 손을 펼친 그 순간.

팟.

공기가, 바람이 멈췄다. 

그리고 방사능보다 더한 살상력을 발휘하며 도시를 휩쓸었던 마정석의 기운이 그의 의지를 따라 변화했다.

전보다도 어둡고, 더욱 순수하게.

우우우웅.

드래곤(Dragon).

탄생과 동시에 마나의 축복을 받은 위대한 이들.

그중에서도 가장 강력한 존재로 추앙받았던, 그러나 끝끝내 스스로 타락을 택한 모르고스의 손끝을 따라 공간이 뒤흔들렸다.

뭉치고, 다져지고, 솟아오르고.

그리고 마침내.

쿠구구궁.

세워졌다.

지금껏 이 세상에서 찾아볼 수 없었던 거대한 성이. 

그만의 왕국이.

콘크리트와 대리석 대신 짙은 마력으로 점칠 된 공기와 칠흑빛 땅 위에 우뚝 선 그것은 압도적이면서도 아름다웠고, 모르고스는 구름을 뚫고 솟구친 첨탑(尖塔)을 바라보며 웃었다.

아니, 정확히는 자욱한 먹구름 속에 숨어 그를 바라보던 드론의 카메라 렌즈를 향해.

“보았느냐, 인간들이여.”

그날, 전 세계인은 보았다.

모스크바가 사라지고, 드래곤 레어(Dragon Lair)가 탄생하는 과정을.

코앞까지 닥친 재앙을.
```

## Final English reading copy

```markdown
# Chapter 1151

The moment he activated the secret device that only one person in the world was permitted to use, Vladimir Furin muttered to himself.

*This is as far as I go.*

Was he reluctant to let go of life? Afraid of death?

Of course he was.

The more a person had, the harder it was to let go. That was human nature. And for a man who had ruled as a dictator for nearly half a century, there was no need to ask.

He wanted to live.

He had to live.

He had to raise the name Vladimir Furin to the level of a god.

He had to become greater than the tsars, who had ruled this land for generations through their noble blood, and greater even than the Iron Marshal, against whom no one had dared rebel.

But if that proved impossible—

If someone else appeared and tried to take everything he had built—

*I’ll burn it all down. With my own hands, so no one else can have it.*

The old dictator, who had dreamed of immortality, smiled faintly.

Or rather, he tried to.

Time slowed, stretching out like a passing life flashing before his eyes. Then he saw the looter wearing a vivid smile.

“You really are an interesting human.”

“……!”

The moment his shrewd eyes flew open—

Rrrrrumble.

The enormous rumble, as if it would swallow the Kremlin—or Moscow itself—drew closer.

Slowly. Deliberately.

As though it moved at someone’s will.

At last, Vladimir Furin saw the source of this unexpected phenomenon with his own eyes.

Wooooom.

Would a swarm of thousands, tens of thousands of bees tangled together sound like this?

Furin could only stare blankly at the vortex of flames as it rose from the melting floor of his office.

Everything was red. Everything was hot.

Surrounded by an aura as dark as pitch, it had been compressed into a great sphere, blazing like a tiny sun.

And the old dictator staring at the sight in shock knew better than anyone that “tiny sun” was no exaggeration.

He also knew that a power once great enough to terrify the entire world was now in the grasp of the monster smiling at him.

*Tsar Bomba.*

The most powerful weapon in human history.

The mother and emperor of all bombs.

Only a handful of people involved knew that the most powerful hydrogen bomb of the Cold War—the one that had frozen the five oceans and six continents with fear—lay sleeping deep beneath the Kremlin.

They also knew that decades of secret experiments, carried out on the dictator’s orders, had given it a new name and destructive power far beyond anything it had possessed before.

“Remarkable. Truly remarkable. To create such powerful force. What do you humans call this weapon?”

At Morgoth’s genuinely awestruck question, Furin—sensing that everything was over—answered in a hollow voice.

“Vladimir.”

“What?”

Morgoth looked from the old dictator, already all but fallen, to the catastrophic power named after him, then burst out laughing.

“That’s a masterpiece. Or should I say, very like you?”

Morgoth found it truly amusing.

A human granted barely a hundred years could harbor such enormous ambitions.

And that these mere mortals had tried to kill him, a being with power close to immortality, using a weapon they had made.

“Did you think this alone could bring me down? With Magic Gems taken from lowly monsters, you dare challenge me?”

At Morgoth’s words, which seemed to reveal he had already seen through everything, Furin quietly swallowed.

He was right. Tsar Bomba—or rather, the weapon now given the new name Vladimir—was not merely a product of science.

The Great Cataclysm.

After that world-shaking event had overturned all the laws and common sense of the world, one thought had taken root in the mind of the dictator who had barely survived.

*I have to become stronger. So this can never happen again. So we can win any war.*

And the means were close at hand.

Magic and Magic Gems. The new knowledge born from them: magical engineering.

And so Tsar Bomba became Vladimir.

As one of the world’s great powers—and a dictatorship at that—the country had countless ways to obtain Magic Gems for experiments.

Of course, that meant violating more international treaties than anyone could count and killing even his own scientists and mages to keep everything secret…but what did that matter?

Mother Russia.

Russia—or rather, he—had to become greater still.

Even if a second Demon King descended, he and Russia alone had to survive and rewrite the world order.

*Or die together.*

Yes.

That was how it had to be.

Plop.

Ash fell away in clumps.

The decades he’d spent avoiding cigarettes counted for nothing. Furin had barely taken a few drags from the cigar. He stared at it, then suddenly spoke.

“What are you going to do now?”

Morgoth didn’t answer.

But Furin immediately understood the meaning behind the gentle curve of his lips.

“Right. It has nothing to do with me anymore.”

The cigar trembled.

No—it was Furin himself who was shaking.

“Any last words?”

At Morgoth’s kind offer, Furin raised his trembling hand and brought the cigar to his lips.

Then, after taking the deepest drag of his life, he blew the smoke toward the monster before him.

“No. But there’s one thing I have to tell you.”

Along with the name of the man who had crossed his mind just before he activated the bomb named after himself.

“If Jin comes back, you’re finished.”

At that moment—

“I look forward to it. Truly.”

Swoooosh.

With Morgoth’s calm reply, the pitch-black aura restraining the catastrophic power slowly dispersed, then enveloped its master.

Like the touch of death announcing the end of this land.

Whoosh.

A blinding flash swallowed the old, wretched dictator’s final sight.

It was warm.

* * *

Eight meters long. Two meters in diameter. Twenty-seven tons.

Its destructive power packed into a volume that could fill a large truck: 50 Mt—fifty million tons of TNT.

Those were the figures publicly known for the Tsar Bomba.

Its power could make the Little Boy that had turned Hiroshima into a land of death during World War II seem like a little boy indeed.

But no one had expected it.

No one had expected this monster from a bygone era, born of the Cold War’s arms race, to awaken again more than eighty years later.

And no one had expected the monster’s first cry after its long sleep to ring out from the Kremlin.

Gooooom.

The air trembled in an instant.

Everyone in the Kremlin—or rather, everyone in Moscow—felt that deep, ominous rumble.

The soldiers and Hunters holding their posts as they suppressed their fear. The citizens who had fled into bomb shelters and out onto the streets as Red Square collapsed.

No one was spared.

Everyone felt it and instinctively understood.

This was the last moment they would ever draw breath.

And then—

Whoooosh.

There was light.

A terrible heat beyond human perception, atomic power mingled with potent energy drawn from countless Magic Gems—it all spread out, devouring everything in its path.

Without end. Without restraint.

Kraaaaaash!

In the storm of power, everything melted.

The living died. The lifeless lost their shape.

Underground or aboveground, whatever life they had lived—it didn’t matter.

The blinding light that burst from the Kremlin made everyone equal.

Just as Icarus, who had flown too close to the sun, lost his wings and fell, the tiny sun born of a dictator’s ambition and fear swallowed countless lives, including its creator.

All of them, save one.

Rrrrrumble.

At the heart of the rumbling that shook everything around him, Morgoth lifted his head and surveyed the scene he had created.

Nothing remained.

Everything that had surrounded him just minutes earlier was gone.

Melted metal flowed like rivers, and above it rose a massive mushroom cloud, looming over the surface now transformed into a land of death.

It was quite a sight.

“Such power. I didn’t even need to use Breath.”

Morgoth felt both admiration and regret.

How could mortals be so greedy and yet so foolish?

They had saved him a great deal of trouble, but the place now shadowed by calamity was desolate beyond measure.

A city with a long history and a population of over ten million had become a land where nothing could live for hundreds of years.

“But birth awakens from within death.”

The moment Morgoth spread both hands with those quiet words—

Pop.

The air stopped. The wind stopped.

And the Magic Gem energy that had swept across the city with a deadliness greater than radiation changed in response to his will.

Darker than before. Purer still.

Wooooom.

Dragon.

Great beings blessed by mana from the moment of their birth.

Space trembled at Morgoth’s fingertips. He had been revered as the greatest of them, yet in the end he had chosen corruption of his own accord.

Gathering. Packing together. Rising up.

And at last—

Rrrrrumble.

It was built.

A gigantic castle, unlike anything ever seen in this world.

His own kingdom.

In place of concrete and marble, it stood upon pitch-black earth amid air saturated with dense magical power. It was overwhelming, yet beautiful. Morgoth smiled as he gazed at its spire piercing the clouds.

Or, more precisely, at the camera lens of the drone hidden in the thick black clouds, watching him.

“Have you seen it, humans?”

That day, people all over the world saw it.

They watched Moscow disappear and a Dragon Lair come into being.

The calamity that had reached their doorstep.
```
